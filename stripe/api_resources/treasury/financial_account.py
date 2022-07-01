# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("retrieve_features", http_verb="get", http_path="features")
@custom_method("update_features", http_verb="post", http_path="features")
class FinancialAccount(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "treasury.financial_account"

    def retrieve_features(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def update_features(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
