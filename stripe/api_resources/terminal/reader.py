# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
        url = self.instance_url() + "/cancel_action"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def process_payment_intent(self, idempotency_key=None, **params):
        url = self.instance_url() + "/process_payment_intent"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def process_setup_intent(self, idempotency_key=None, **params):
        url = self.instance_url() + "/process_setup_intent"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def set_reader_display(self, idempotency_key=None, **params):
        url = self.instance_url() + "/set_reader_display"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @custom_method("present_payment_method", http_verb="post")
    class TestHelpers(APIResourceTestHelpers):
        def present_payment_method(self, idempotency_key=None, **params):
            url = self.instance_url() + "/present_payment_method"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
