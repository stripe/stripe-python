# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("cancel", http_verb="post")
@custom_method("reverse", http_verb="post")
class Payout(
    CreateableAPIResource, ListableAPIResource, UpdateableAPIResource
):
    OBJECT_NAME = "payout"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/payouts/{payout}/cancel".format(
            payout=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def reverse(self, idempotency_key=None, **params):
        url = "/v1/payouts/{payout}/reverse".format(
            payout=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
