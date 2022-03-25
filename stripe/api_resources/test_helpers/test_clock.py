# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("advance", http_verb="post")
class TestClock(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
):
    OBJECT_NAME = "test_helpers.test_clock"

    def advance(self, idempotency_key=None, **params):
        url = self.instance_url() + "/advance"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
