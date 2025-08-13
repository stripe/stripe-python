import stripe


TEST_RESOURCE_ID = "link_123"


class TestFileLink(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.FileLink.list()
        http_client_mock.assert_requested("get", path="/v1/file_links")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.FileLink)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.FileLink.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/file_links/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileLink)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.FileLink.create(file="file_123")
        http_client_mock.assert_requested("post", path="/v1/file_links")
        assert isinstance(resource, stripe.FileLink)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.FileLink.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/file_links/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.FileLink.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/file_links/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.FileLink)
