import stripe


TEST_RESOURCE_ID = "tu_123"


class TestTopup(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Topup.list()
        http_client_mock.assert_requested("get", path="/v1/topups")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Topup)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/topups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Topup.create(
            amount=100,
            currency="usd",
            source="src_123",
            description="description",
            statement_descriptor="statement descriptor",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups",
            post_data="amount=100&currency=usd&description=description&source=src_123&statement_descriptor=statement+descriptor",
        )
        assert isinstance(resource, stripe.Topup)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Topup.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Topup)

    def test_can_cancel(self, http_client_mock):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource = resource.cancel()
        http_client_mock.assert_requested(
            "post", path="/v1/topups/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.Topup.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/topups/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)
