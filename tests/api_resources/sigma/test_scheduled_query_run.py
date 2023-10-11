import stripe


TEST_RESOURCE_ID = "sqr_123"


class TestTransaction(object):
    def test_is_listable(self, request_mock):
        resources = stripe.sigma.ScheduledQueryRun.list()
        request_mock.assert_requested("get", "/v1/sigma/scheduled_query_runs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.sigma.ScheduledQueryRun)

    def test_is_retrievable(self, request_mock):
        resource = stripe.sigma.ScheduledQueryRun.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/sigma/scheduled_query_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.sigma.ScheduledQueryRun)
