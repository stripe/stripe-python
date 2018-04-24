from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_SUBSCRIPTION_ITEM_ID = 'si_123'


class UsageRecordTest(StripeTestCase):
    def test_is_creatable(self):
        resource = stripe.UsageRecord.create(
            subscription_item=TEST_SUBSCRIPTION_ITEM_ID,
            quantity=5000,
            timestamp=1524182400,
            action='increment',
        )
        self.assert_requested(
            'post',
            '/v1/subscription_items/%s/usage_records' % (
                TEST_SUBSCRIPTION_ITEM_ID
            )
        )
        self.assertIsInstance(resource, stripe.UsageRecord)

    def test_raises_when_creating_without_subscription_item(self):
        with self.assertRaises(ValueError):
            stripe.UsageRecord.create(
                quantity=5000,
                timestamp=1524182400,
                action='increment',
            )
