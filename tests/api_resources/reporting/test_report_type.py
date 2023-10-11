import stripe


TEST_RESOURCE_ID = "activity.summary.1"


class TestReportType(object):
    def test_is_listable(self, request_mock):
        resources = stripe.reporting.ReportType.list()
        request_mock.assert_requested("get", "/v1/reporting/report_types")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.reporting.ReportType)

    def test_is_retrievable(self, request_mock):
        resource = stripe.reporting.ReportType.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/reporting/report_types/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.reporting.ReportType)
