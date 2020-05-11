from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("line_item", operations=["list"])
class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "checkout.session"
