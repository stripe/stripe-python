# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("line_item", operations=["list"])
class Session(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "checkout.session"

    @classmethod
    def _cls_expire(
        cls,
        session,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/checkout/sessions/{session}/expire".format(
            session=util.sanitize_id(session)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_expire")
    def expire(self, idempotency_key=None, **params):
        url = "/v1/checkout/sessions/{session}/expire".format(
            session=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
