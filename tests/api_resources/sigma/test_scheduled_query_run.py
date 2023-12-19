import stripe


TEST_RESOURCE_ID = "sqr_123"


class TestTransaction(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.sigma.ScheduledQueryRun.list()
        http_client_mock.assert_requested(
            "get", path="/v1/sigma/scheduled_query_runs"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.sigma.ScheduledQueryRun)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.sigma.ScheduledQueryRun.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/sigma/scheduled_query_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.sigma.ScheduledQueryRun)
