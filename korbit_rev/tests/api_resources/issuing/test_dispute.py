import stripe


TEST_RESOURCE_ID = "idp_123"


class TestDispute(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.issuing.Dispute.create(transaction="ipi_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/disputes",
            post_data="transaction=ipi_123",
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_listable(self, http_client_mock):
        resources = stripe.issuing.Dispute.list()
        http_client_mock.assert_requested("get", path="/v1/issuing/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Dispute)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.issuing.Dispute.modify(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/disputes/%s" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.issuing.Dispute.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_submittable(self, http_client_mock):
        resource = stripe.issuing.Dispute.submit(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/disputes/%s/submit" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Dispute)
