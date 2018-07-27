from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'sqr_123'


class TestTransaction(object):
    FIXTURE = {
        'id': TEST_RESOURCE_ID,
        'object': 'scheduled_query_run'
    }

    def test_is_listable(self, request_mock):
        request_mock.stub_request(
            'get',
            '/v1/sigma/scheduled_query_runs',
            {
                'object': 'list',
                'data': [self.FIXTURE],
            }
        )
        resources = stripe.sigma.ScheduledQueryRun.list()
        request_mock.assert_requested(
            'get',
            '/v1/sigma/scheduled_query_runs'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.sigma.ScheduledQueryRun)

    def test_is_retrievable(self, request_mock):
        request_mock.stub_request(
            'get',
            '/v1/sigma/scheduled_query_runs/%s' % TEST_RESOURCE_ID,
            {
                'id': '%s' % TEST_RESOURCE_ID,
                'object': 'scheduled_query_run'
            }
        )
        resource = stripe.sigma.ScheduledQueryRun.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/sigma/scheduled_query_runs/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.sigma.ScheduledQueryRun)
