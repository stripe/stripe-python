import stripe
from stripe.test.helper import (
    StripeApiTestCase, MyCreatable
)


class CreateableAPIResourceTests(StripeApiTestCase):

    def test_create(self):
        self.mock_response({
            'object': 'charge',
            'foo': 'bar',
        })

        res = MyCreatable.create()

        self.requestor_mock.request.assert_called_with(
            'post', '/v1/mycreatables', {}, None)

        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)

    def test_idempotent_create(self):
        self.mock_response({
            'object': 'charge',
            'foo': 'bar',
        })

        res = MyCreatable.create(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post', '/v1/mycreatables', {}, {'Idempotency-Key': 'foo'})

        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)
