import stripe


TEST_RESOURCE_ID = "vs_123"


class TestVerificationReport(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.identity.VerificationReport.list()
        http_client_mock.assert_requested(
            "get", path="/v1/identity/verification_reports"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], stripe.identity.VerificationReport
        )

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.identity.VerificationReport.retrieve(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_reports/%s" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.identity.VerificationReport)
