# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource


class Account(ListableAPIResource):
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
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/financial_connections/accounts/{account}/disconnect".format(
            account=util.sanitize_id(account)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_disconnect")
    def disconnect(self, idempotency_key=None, **params):
        url = "/v1/financial_connections/accounts/{account}/disconnect".format(
            account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def _cls_list_owners(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/financial_connections/accounts/{account}/owners".format(
            account=util.sanitize_id(account)
        )
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        stripe_object._retrieve_params = params
        return stripe_object

    @util.class_method_variant("_cls_list_owners")
    def list_owners(self, idempotency_key=None, **params):
        url = "/v1/financial_connections/accounts/{account}/owners".format(
            account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    @classmethod
    def _cls_refresh_account(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/financial_connections/accounts/{account}/refresh".format(
            account=util.sanitize_id(account)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_refresh_account")
    def refresh_account(self, idempotency_key=None, **params):
        url = "/v1/financial_connections/accounts/{account}/refresh".format(
            account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
