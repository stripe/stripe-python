import stripe


TEST_RESOURCE_ID = "ipi_123"


class TestTransaction(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.issuing.Transaction.list()
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/transactions"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Transaction)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.issuing.Transaction.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/transactions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Transaction)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Transaction)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        transaction = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/transactions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Transaction)
        assert resource is transaction
