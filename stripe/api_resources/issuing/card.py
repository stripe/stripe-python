# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@custom_method("details", http_verb="get")
@test_helpers
class Card(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "issuing.card"

    def details(self, idempotency_key=None, **params):
        return self.request("get", self.instance_url() + "/details", params)

    @custom_method("deliver_card", http_verb="post", http_path="deliver")
    @custom_method("fail_card", http_verb="post", http_path="fail")
    @custom_method("return_card", http_verb="post", http_path="return")
    @custom_method("ship_card", http_verb="post", http_path="ship")
    class TestHelpers(APIResourceTestHelpers):
        def deliver_card(self, idempotency_key=None, **params):
            url = self.instance_url() + "/deliver"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        def fail_card(self, idempotency_key=None, **params):
            url = self.instance_url() + "/fail"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        def return_card(self, idempotency_key=None, **params):
            url = self.instance_url() + "/return"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        def ship_card(self, idempotency_key=None, **params):
            url = self.instance_url() + "/ship"
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
