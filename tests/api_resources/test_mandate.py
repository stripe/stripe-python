from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "mandate_123"


class TestMandateSchedule(object):
    def test_is_retrievable(self, request_mock):
        resource = stripe.Mandate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/mandates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Mandate)
