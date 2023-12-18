import stripe


TEST_RESOURCE_ID = "ich_123"


class TestCardholder(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.issuing.Cardholder.create(
            billing={
                "address": {
                    "city": "city",
                    "country": "US",
                    "line1": "line1",
                    "postal_code": "postal_code",
                }
            },
            name="Jenny Rosen",
            type="individual",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cardholders",
            post_data="billing[address][city]=city&billing[address][country]=US&billing[address][line1]=line1&billing[address][postal_code]=postal_code&name=Jenny+Rosen&type=individual",
        )
        assert isinstance(resource, stripe.issuing.Cardholder)

    def test_is_listable(self, http_client_mock):
        resources = stripe.issuing.Cardholder.list()
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/cardholders"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Cardholder)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.issuing.Cardholder.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Cardholder)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Cardholder)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        cardholder = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Cardholder)
        assert resource is cardholder
