from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = '250FG'


class UsageRecordTest(StripeTestCase):
    def test_is_creatable(self):
        resource = stripe.UsageRecord.create(
            subscription_item='si_123',
            quantity=123,
            timestamp=123123,
            action='increment',
        )
        self.assert_requested(
            'post',
            '/v1/subscription_items/si_123/usage_records'
        )
        self.assertIsInstance(resource, stripe.UsageRecord)
