import stripe


TEST_RESOURCE_ID = "sub_123"


class TestSubscription(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Subscription.list()
        http_client_mock.assert_requested("get", path="/v1/subscriptions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Subscription)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Subscription.create(customer="cus_123")
        http_client_mock.assert_requested(
            "post", path="/v1/subscriptions", post_data="customer=cus_123"
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscriptions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Subscription.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscriptions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    def test_can_delete(self, http_client_mock):
        resource = stripe.Subscription.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    def test_can_delete_discount(self, http_client_mock):
        sub = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        sub.delete_discount()
        http_client_mock.assert_requested(
            "delete", path="/v1/subscriptions/%s/discount" % sub.id
        )

    def test_can_delete_discount_classmethod(self, http_client_mock):
        stripe.Subscription.delete_discount(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/subscriptions/%s/discount" % TEST_RESOURCE_ID
        )
