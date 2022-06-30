# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class PaymentLink(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_link"

    @classmethod
    def _cls_list_line_items(
        cls,
        payment_link,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/payment_links/{payment_link}/line_items".format(
            payment_link=util.sanitize_id(payment_link)
        )
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        stripe_object._retrieve_params = params
        return stripe_object

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/payment_links/{payment_link}/line_items".format(
            payment_link=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object
