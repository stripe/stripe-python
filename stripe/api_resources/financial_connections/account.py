# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    "inferred_balance",
    operations=["list"],
)
class Account(ListableAPIResource):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    OBJECT_NAME = "financial_connections.account"

    @classmethod
    def _cls_disconnect(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/disconnect".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_disconnect")
    def disconnect(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/disconnect".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_owners(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/financial_connections/accounts/{account}/owners".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_owners")
    def list_owners(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/financial_connections/accounts/{account}/owners".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_refresh_account(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/refresh".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_refresh_account")
    def refresh_account(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/refresh".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_subscribe(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/subscribe".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_subscribe")
    def subscribe(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/subscribe".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_unsubscribe(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/unsubscribe".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_unsubscribe")
    def unsubscribe(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/unsubscribe".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
