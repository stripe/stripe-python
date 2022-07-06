# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("approve", http_verb="post")
class Review(ListableAPIResource):
    OBJECT_NAME = "review"

    def approve(self, idempotency_key=None, **params):
        url = "/v1/reviews/{review}/approve".format(
            review=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
