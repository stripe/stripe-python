from __future__ import absolute_import, division, print_function

import pytest

import stripe


TEST_RESOURCE_ID = "sub_sched_rev_123"


class TestSubscriptionScheduleRevision(object):
    def construct_resource(self):
        revision_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "subscription_schedule_revision",
            "schedule": "sub_sched_123",
        }
        return stripe.SubscriptionScheduleRevision.construct_from(
            revision_dict, stripe.api_key
        )

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/subscription_schedules/sub_sched_123/revisions/%s"
            % TEST_RESOURCE_ID
        )

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            stripe.SubscriptionScheduleRevision.retrieve(TEST_RESOURCE_ID)
