# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@test_helpers
@custom_method("cancel", http_verb="post")
class Refund(
    CreateableAPIResource, ListableAPIResource, UpdateableAPIResource
):
    OBJECT_NAME = "refund"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/refunds/{refund}/cancel".format(
            refund=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_expire(
            cls,
            refund,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/refunds/{refund}/expire".format(
                refund=util.sanitize_id(refund)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_expire")
        def expire(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/refunds/{refund}/expire".format(
                refund=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
