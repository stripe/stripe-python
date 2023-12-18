import pytest

import stripe


TEST_SUBSCRIPTION_ITEM_ID = "si_123"


class TestUsageRecord(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.UsageRecord.create(
            subscription_item=TEST_SUBSCRIPTION_ITEM_ID,
            quantity=5000,
            timestamp=1524182400,
            action="increment",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/%s/usage_records"
            % (TEST_SUBSCRIPTION_ITEM_ID),
        )
        assert isinstance(resource, stripe.UsageRecord)

    def test_raises_when_creating_without_subscription_item(self):
        with pytest.raises(ValueError):
            stripe.UsageRecord.create(
                quantity=5000, timestamp=1524182400, action="increment"
            )
