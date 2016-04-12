import stripe
from stripe.test.helper import StripeResourceTest


class TransferTest(StripeResourceTest):

    def test_list_transfers(self):
        stripe.Transfer.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers',
            {}
        )

    def test_cancel_transfer(self):
        transfer = stripe.Transfer(id='tr_cancel')
        transfer.cancel()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_cancel/cancel',
            {},
            None
        )
