import stripe


TEST_RESOURCE_ID = "re_123"


class TestRefund(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Refund.list()
        http_client_mock.assert_requested("get", path="/v1/refunds")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Refund)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/refunds/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Refund.create(charge="ch_123")
        http_client_mock.assert_requested(
            "post", path="/v1/refunds", post_data="charge=ch_123"
        )
        assert isinstance(resource, stripe.Refund)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/refunds/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Refund.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/refunds/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Refund)
