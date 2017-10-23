import stripe
from stripe.test.helper import StripeResourceTest


class PayoutTest(StripeResourceTest):

    def test_list_payouts(self):
        stripe.Payout.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/payouts',
            {}
        )

    def test_cancel_payout(self):
        payout = stripe.Payout(id='po_cancel')
        payout.cancel()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/payouts/po_cancel/cancel',
            {},
            None
        )
