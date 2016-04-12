import stripe
from stripe.test.helper import StripeResourceTest


class ReversalTest(StripeResourceTest):

    def test_fetch_reversal(self):
        transfer = stripe.Charge.construct_from({
            'id': 'tr_get',
            'reversals': {
                'object': 'list',
                'url': '/v1/transfers/tr_get/reversals',
            }
        }, 'api_key')

        transfer.reversals.retrieve("foo")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_get/reversals/foo',
            {},
            None
        )

    def test_list_reversals(self):
        transfer = stripe.Charge.construct_from({
            'id': 'tr_list',
            'reversals': {
                'object': 'list',
                'url': '/v1/transfers/tr_list/reversals',
            }
        }, 'api_key')

        transfer.reversals.list()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_list/reversals',
            {},
            None
        )

    def test_update_transfer(self):
        reversal = stripe.resource.Reversal.construct_from({
            'id': "rev_update",
            'transfer': "tr_update",
            'metadata': {},
        }, 'api_key')
        reversal.metadata["key"] = "value"
        reversal.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_update/reversals/rev_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )
