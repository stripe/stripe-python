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
        return self._request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
