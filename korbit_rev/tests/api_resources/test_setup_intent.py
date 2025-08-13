import stripe


TEST_RESOURCE_ID = "seti_123"


class TestSetupIntent(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.SetupIntent.list()
        http_client_mock.assert_requested("get", path="/v1/setup_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SetupIntent)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/setup_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.SetupIntent.create(payment_method_types=["card"])
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents",
            post_data="payment_method_types[0]=card",
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.SetupIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_can_cancel(self, http_client_mock):
        resource = stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        resource.cancel()
        http_client_mock.assert_requested(
            "post", path="/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.SetupIntent.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/setup_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_can_confirm(self, http_client_mock):
        resource = stripe.SetupIntent.retrieve(TEST_RESOURCE_ID)
        resource.confirm()
        http_client_mock.assert_requested(
            "post", path="/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)

    def test_can_confirm_classmethod(self, http_client_mock):
        resource = stripe.SetupIntent.confirm(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/setup_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SetupIntent)
