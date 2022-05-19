# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import nested_resource_class_methods


@custom_method("expire", http_verb="post")
@nested_resource_class_methods("line_item", operations=["list"])
class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "checkout.session"

    def expire(self, idempotency_key=None, **params):
        url = self.instance_url() + "/expire"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
