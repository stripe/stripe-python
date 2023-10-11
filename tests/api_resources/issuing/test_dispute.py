import stripe


TEST_RESOURCE_ID = "idp_123"


class TestDispute(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.issuing.Dispute.create(transaction="ipi_123")
        request_mock.assert_requested("post", "/v1/issuing/disputes")
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_listable(self, request_mock):
        resources = stripe.issuing.Dispute.list()
        request_mock.assert_requested("get", "/v1/issuing/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Dispute)

    def test_is_modifiable(self, request_mock):
        resource = stripe.issuing.Dispute.modify(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/issuing/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = stripe.issuing.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_submittable(self, request_mock):
        resource = stripe.issuing.Dispute.submit(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/issuing/disputes/%s/submit" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)
