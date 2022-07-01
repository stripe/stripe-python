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
        return self._request(
            "post",
            "/v1/orders/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/orders/{id}/line_items".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def reopen(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/orders/{id}/reopen".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def submit(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/orders/{id}/submit".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
