import stripe
from stripe.test.helper import (
    StripeApiTestCase, MyListable
)


class ListableAPIResourceTests(StripeApiTestCase):

    def test_all(self):
        self.mock_response([
            {
                'object': 'charge',
                'name': 'jose',
            },
            {
                'object': 'charge',
                'name': 'curly',
            }
        ])

        res = MyListable.all()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mylistables', {})

        self.assertEqual(2, len(res))
        self.assertTrue(all(isinstance(obj, stripe.Charge) for obj in res))
        self.assertEqual('jose', res[0].name)
        self.assertEqual('curly', res[1].name)
