# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class FinancialAccount(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
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
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
            financial_account=util.sanitize_id(financial_account)
        )
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_retrieve_features")
    def retrieve_features(self, idempotency_key=None, **params):
        url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
            financial_account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        return stripe_object

    @classmethod
    def _cls_update_features(
        cls,
        financial_account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
            financial_account=util.sanitize_id(financial_account)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_update_features")
    def update_features(self, idempotency_key=None, **params):
        url = "/v1/treasury/financial_accounts/{financial_account}/features".format(
            financial_account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("post", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        return stripe_object
