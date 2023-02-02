# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class FinancialAccount(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.
    FinancialAccounts serve as the source and destination of Treasury's money movement APIs.
    """

    OBJECT_NAME = "treasury.financial_account"

    @classmethod
    def _cls_retrieve_features(
        cls,
        financial_account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(financial_account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_retrieve_features")
    def retrieve_features(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_update_features(
        cls,
        financial_account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(financial_account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_update_features")
    def update_features(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
