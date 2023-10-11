import stripe


TEST_RESOURCE_ID = "vs_123"


class TestVerificationReport(object):
    def test_is_listable(self, request_mock):
        resources = stripe.identity.VerificationReport.list()
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], stripe.identity.VerificationReport
        )

    def test_is_retrievable(self, request_mock):
        resource = stripe.identity.VerificationReport.retrieve(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get", "/v1/identity/verification_reports/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.identity.VerificationReport)
