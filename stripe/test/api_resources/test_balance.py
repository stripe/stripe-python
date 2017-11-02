from __future__ import absolute_import, division, print_function

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
