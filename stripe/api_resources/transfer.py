# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import nested_resource_class_methods


@custom_method("cancel", http_verb="post")
@nested_resource_class_methods(
    "reversal",
    operations=["create", "retrieve", "update", "list"],
)
class Transfer(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "transfer"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/transfers/{transfer}/cancel".format(
            transfer=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
