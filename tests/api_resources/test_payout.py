from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeResourceTest


class PayoutTest(StripeResourceTest):

    def test_list_payouts(self):
        stripe.Payout.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/payouts',
            {}
        )

    def test_cancel_payout(self):
        self.mock_response({
            'id': 'po_cancel',
            'status': 'canceled',
        })

        payout = stripe.Payout(id='po_cancel')

        self.assertTrue(payout is payout.cancel(idempotency_key='idem-foo'))
        self.assertEquals('canceled', payout.status)
        self.assertEquals('po_cancel', payout.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/payouts/po_cancel/cancel',
            {},
            {'Idempotency-Key': 'idem-foo'}
        )
