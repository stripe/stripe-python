from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "evt_123"


class TestEvent(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Event.list()
        request_mock.assert_requested("get", "/v1/events")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Event)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Event.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/events/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Event)
