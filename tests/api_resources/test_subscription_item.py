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
