import stripe


TEST_RESOURCE_ID = "we_123"


class TestWebhookEndpoint(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.WebhookEndpoint.list()
        http_client_mock.assert_requested("get", path="/v1/webhook_endpoints")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.WebhookEndpoint)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.WebhookEndpoint)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.WebhookEndpoint.create(
            enabled_events=["charge.succeeded"], url="https://stripe.com"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/webhook_endpoints",
            post_data="enabled_events[0]=charge.succeeded&url=https://stripe.com",
        )
        assert isinstance(resource, stripe.WebhookEndpoint)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        resource.enabled_events = ["charge.succeeded"]
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID,
            post_data="enabled_events[0]=charge.succeeded",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.WebhookEndpoint.modify(
            TEST_RESOURCE_ID,
            enabled_events=["charge.succeeded"],
            url="https://stripe.com",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID,
            post_data="enabled_events[0]=charge.succeeded&url=https://stripe.com",
        )
        assert isinstance(resource, stripe.WebhookEndpoint)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.WebhookEndpoint.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.WebhookEndpoint.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/webhook_endpoints/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
