# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@test_helpers
@custom_method("cancel", http_verb="post")
class OutboundTransfer(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "treasury.outbound_transfer"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
            outbound_transfer=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_fail(
            cls,
            outbound_transfer,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                outbound_transfer=util.sanitize_id(outbound_transfer)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_fail")
        def fail(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                outbound_transfer=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        @classmethod
        def _cls_post(
            cls,
            outbound_transfer,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                outbound_transfer=util.sanitize_id(outbound_transfer)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_post")
        def post(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                outbound_transfer=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        @classmethod
        def _cls_return_outbound_transfer(
            cls,
            outbound_transfer,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                outbound_transfer=util.sanitize_id(outbound_transfer)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_return_outbound_transfer")
        def return_outbound_transfer(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                outbound_transfer=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
