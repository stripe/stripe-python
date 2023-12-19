import stripe


TEST_RESOURCE_ID = "price_123"


class TestPrice(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Price.list()
        http_client_mock.assert_requested("get", path="/v1/prices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Price)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Price.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Price)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Price.create(
            unit_amount=1000,
            currency="usd",
            recurring={"interval": "month"},
            product_data={"name": "price_nickname"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices",
            post_data="unit_amount=1000&currency=usd&recurring[interval]=month&product_data[name]=price_nickname",
        )
        assert isinstance(resource, stripe.Price)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Price.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Price.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Price)
