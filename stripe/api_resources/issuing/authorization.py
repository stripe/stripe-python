# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("approve", http_verb="post")
@custom_method("decline", http_verb="post")
class Authorization(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "issuing.authorization"

    def approve(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def decline(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
