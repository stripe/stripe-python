import stripe


TEST_RESOURCE_ID = "si_123"


class TestSubscriptionItem(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.SubscriptionItem.list(subscription="sub_123")
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_items",
            query_string="subscription=sub_123",
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SubscriptionItem)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.SubscriptionItem.create(
            price="price_123", subscription="sub_123"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items",
            post_data="price=price_123&subscription=sub_123",
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.price = "price_123"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/%s" % TEST_RESOURCE_ID,
            post_data="price=price_123",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.SubscriptionItem.modify(
            TEST_RESOURCE_ID, price="price_123"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/%s" % TEST_RESOURCE_ID,
            post_data="price=price_123",
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.SubscriptionItem.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/subscription_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True


class TestUsageRecords(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.SubscriptionItem.create_usage_record(
            TEST_RESOURCE_ID,
            quantity=5000,
            timestamp=1524182400,
            action="increment",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/%s/usage_records" % TEST_RESOURCE_ID,
            post_data="action=increment&quantity=5000&timestamp=1524182400",
        )
        assert isinstance(resource, stripe.UsageRecord)


class TestUsageRecordSummaries(object):
    def test_is_listable(self, http_client_mock):
        resource = stripe.SubscriptionItem.list_usage_record_summaries(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_items/%s/usage_record_summaries"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resource.data, list)
        assert isinstance(resource.data[0], stripe.UsageRecordSummary)
