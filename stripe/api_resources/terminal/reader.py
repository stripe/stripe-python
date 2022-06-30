# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@test_helpers
@custom_method("cancel_action", http_verb="post")
@custom_method("process_payment_intent", http_verb="post")
@custom_method("process_setup_intent", http_verb="post")
@custom_method("set_reader_display", http_verb="post")
class Reader(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "terminal.reader"

    def cancel_action(self, idempotency_key=None, **params):
        url = "/v1/terminal/readers/{reader}/cancel_action".format(
            reader=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def process_payment_intent(self, idempotency_key=None, **params):
        url = "/v1/terminal/readers/{reader}/process_payment_intent".format(
            reader=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def process_setup_intent(self, idempotency_key=None, **params):
        url = "/v1/terminal/readers/{reader}/process_setup_intent".format(
            reader=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def set_reader_display(self, idempotency_key=None, **params):
        url = "/v1/terminal/readers/{reader}/set_reader_display".format(
            reader=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_present_payment_method(
            cls,
            reader,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                reader=util.sanitize_id(reader)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_present_payment_method")
        def present_payment_method(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                reader=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
