import stripe


TEST_RESOURCE_ID = "frr_123"


class TestReportRun(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.reporting.ReportRun.create(
            parameters={"connected_account": "acct_123"},
            report_type="activity.summary.1",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/reporting/report_runs",
            post_data="parameters[connected_account]=acct_123&report_type=activity.summary.1",
        )
        assert isinstance(resource, stripe.reporting.ReportRun)

    def test_is_listable(self, http_client_mock):
        resources = stripe.reporting.ReportRun.list()
        http_client_mock.assert_requested(
            "get", path="/v1/reporting/report_runs"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.reporting.ReportRun)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.reporting.ReportRun.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/reporting/report_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.reporting.ReportRun)
