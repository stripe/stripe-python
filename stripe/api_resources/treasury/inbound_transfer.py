# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@test_helpers
@custom_method("cancel", http_verb="post")
class InboundTransfer(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "treasury.inbound_transfer"

    def cancel(self, idempotency_key=None, **params):
        url = self.instance_url() + "/cancel"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    @custom_method("fail", http_verb="post")
    @custom_method(
        "return_inbound_transfer",
        http_verb="post",
        http_path="return",
    )
    @custom_method("succeed", http_verb="post")
    class TestHelpers(APIResourceTestHelpers):
        def fail(self, idempotency_key=None, **params):
            url = self.instance_url() + "/fail"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        def return_inbound_transfer(self, idempotency_key=None, **params):
            url = self.instance_url() + "/return"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        def succeed(self, idempotency_key=None, **params):
            url = self.instance_url() + "/succeed"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
