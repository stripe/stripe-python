from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class BalanceTransactionTest(StripeResourceTest):

    def test_list_balance_transactions(self):
        stripe.BalanceTransaction.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/balance/history',
            {}
        )

    def test_convert_to_stripe_object(self):
        transaction = stripe.util.convert_to_stripe_object({
            'id': 'txn_foo',
            'object': 'balance_transaction',
        })
        self.assertIsInstance(transaction, stripe.BalanceTransaction)
