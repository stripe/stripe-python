# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("cancel", http_verb="post")
@custom_method("list_line_items", http_verb="get", http_path="line_items")
@custom_method("reopen", http_verb="post")
@custom_method("submit", http_verb="post")
class Order(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "order"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/orders/{id}/cancel".format(
            id=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/orders/{id}/line_items".format(
            id=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    def reopen(self, idempotency_key=None, **params):
        url = "/v1/orders/{id}/reopen".format(
            id=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def submit(self, idempotency_key=None, **params):
        url = "/v1/orders/{id}/submit".format(
            id=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
