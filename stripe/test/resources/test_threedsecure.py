import stripe
from stripe.test.helper import StripeResourceTest


class ThreeDSecureTest(StripeResourceTest):

    def test_threedsecure_create(self):
        stripe.ThreeDSecure.create(
            card="tok_test",
            amount=1500,
            currency="usd",
            return_url="https://example.org/3d-secure-result"
        )

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/3d_secure',
            {
                'card': 'tok_test',
                'amount': 1500,
                'currency': 'usd',
                'return_url': 'https://example.org/3d-secure-result'
            },
            None
        )

    def test_threedsecure_retrieve(self):
        stripe.ThreeDSecure.retrieve('tdsrc_id')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/3d_secure/tdsrc_id',
            {},
            None
        )
