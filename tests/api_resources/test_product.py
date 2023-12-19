import stripe


TEST_RESOURCE_ID = "prod_123"


class TestProduct(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Product.list()
        http_client_mock.assert_requested("get", path="/v1/products")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Product)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Product)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Product.create(name="NAME")
        http_client_mock.assert_requested(
            "post", path="/v1/products", post_data="name=NAME"
        )
        assert isinstance(resource, stripe.Product)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/products/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Product.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/products/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Product)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Product.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/products/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
