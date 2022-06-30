# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Charge(
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "charge"

    @classmethod
    def _cls_capture(
        cls,
        charge,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/charges/{charge}/capture".format(
            charge=util.sanitize_id(charge)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_capture")
    def capture(self, idempotency_key=None, **params):
        url = "/v1/charges/{charge}/capture".format(
            charge=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/charges/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def refund(self, idempotency_key=None, **params):
        url = self.instance_url() + "/refund"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def update_dispute(self, idempotency_key=None, **params):
        requestor = api_requestor.APIRequestor(
            self.api_key,
            api_version=self.stripe_version,
            account=self.stripe_account,
        )
        url = self.instance_url() + "/dispute"
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)
        self.refresh_from({"dispute": response}, api_key, True)
        return self.dispute

    def close_dispute(self, idempotency_key=None, **params):
        requestor = api_requestor.APIRequestor(
            self.api_key,
            api_version=self.stripe_version,
            account=self.stripe_account,
        )
        url = self.instance_url() + "/dispute/close"
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)
        self.refresh_from({"dispute": response}, api_key, True)
        return self.dispute

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "fraudulent"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "safe"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
