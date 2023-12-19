import stripe


TEST_RESOURCE_ID = "dp_123"


class TestDispute(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Dispute.list()
        http_client_mock.assert_requested("get", path="/v1/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Dispute)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/disputes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Dispute.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/disputes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Dispute)

    def test_can_close(self, http_client_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.close()
        http_client_mock.assert_requested(
            "post", path="/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    def test_can_close_classmethod(self, http_client_mock):
        resource = stripe.Dispute.close(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)
