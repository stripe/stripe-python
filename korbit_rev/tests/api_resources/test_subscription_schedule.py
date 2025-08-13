import stripe


TEST_RESOURCE_ID = "sub_sched_123"


class TestSubscriptionScheduleSchedule(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.SubscriptionSchedule.list()
        http_client_mock.assert_requested(
            "get", path="/v1/subscription_schedules"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SubscriptionSchedule)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/subscription_schedules/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.create(customer="cus_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules",
            post_data="customer=cus_123",
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_can_cancel(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource = resource.cancel()
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s/cancel" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s/cancel" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_can_release(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.retrieve(TEST_RESOURCE_ID)
        resource = resource.release()
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s/release" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)

    def test_can_release_classmethod(self, http_client_mock):
        resource = stripe.SubscriptionSchedule.release(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/%s/release" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.SubscriptionSchedule)
