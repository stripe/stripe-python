import stripe
from stripe.test.helper import StripeResourceTest


class BalanceTest(StripeResourceTest):

    def test_retrieve_balance(self):
        stripe.Balance.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/balance',
            {},
            None
        )


class BalanceTransactionTest(StripeResourceTest):

    def test_list_balance_transactions(self):
        stripe.BalanceTransaction.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/balance/history',
            {}
        )
