import stripe


TEST_RESOURCE_ID = "ic_123"


class TestCard(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.issuing.Card.create(currency="usd", type="physical")
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cards",
            post_data="currency=usd&type=physical",
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_listable(self, http_client_mock):
        resources = stripe.issuing.Card.list()
        http_client_mock.assert_requested("get", path="/v1/issuing/cards")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Card)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.issuing.Card.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cards/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        card = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cards/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Card)
        assert resource is card
