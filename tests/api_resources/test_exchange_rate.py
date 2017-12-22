from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'usd'


class ExchangeRateTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.ExchangeRate.list()
        self.assert_requested(
            'get',
            '/v1/exchange_rates'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.ExchangeRate)

    def test_is_retrievable(self):
        resource = stripe.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/exchange_rates/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.ExchangeRate)
