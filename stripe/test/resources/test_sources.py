import stripe
from stripe.test.helper import StripeResourceTest


class SourceTest(StripeResourceTest):

    def test_retrieve_resource(self):
        stripe.Source.retrieve("src_foo")
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/sources/src_foo',
            {},
            None
        )

    def test_create_source(self):
        stripe.Source.create(type="bitcoin", amount=1000, currency="usd",
                             owner={"email": "jenny.rosen@example.com"})
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/sources',
            {
                'type': 'bitcoin',
                'amount': 1000,
                'currency': 'usd',
                'owner': {'email': 'jenny.rosen@example.com'}
            },
            None
        )
