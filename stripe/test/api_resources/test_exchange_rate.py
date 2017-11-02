from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class ExchangeRateTest(StripeResourceTest):

    def test_is_listable(self):
        stripe.ExchangeRate.list()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/exchange_rates',
            {}
        )

    def test_is_retrievable(self):
        stripe.ExchangeRate.retrieve('usd')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/exchange_rates/usd',
            {},
            None
        )
