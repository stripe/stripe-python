# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("expire", http_verb="post")
@custom_method("list_line_items", http_verb="get", http_path="line_items")
class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "checkout.session"

    def expire(self, idempotency_key=None, **params):
        url = "/v1/checkout/sessions/{session}/expire".format(
            session=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/checkout/sessions/{session}/line_items".format(
            session=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object
