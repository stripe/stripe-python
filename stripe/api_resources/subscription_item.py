from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("usage_record", operations=["create"])
class SubscriptionItem(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "subscription_item"

    def usage_record_summaries(self, **params):
        return self.request(
            "get", self.instance_url() + "/usage_record_summaries", params
        )
