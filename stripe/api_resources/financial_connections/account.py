# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("disconnect", http_verb="post")
@custom_method("list_owners", http_verb="get", http_path="owners")
@custom_method("refresh_account", http_verb="post", http_path="refresh")
class Account(ListableAPIResource):
    OBJECT_NAME = "financial_connections.account"

    def disconnect(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/disconnect".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def list_owners(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/financial_connections/accounts/{account}/owners".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def refresh_account(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/refresh".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
