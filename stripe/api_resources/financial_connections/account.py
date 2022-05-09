# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.abstract import custom_method


@custom_method("disconnect", http_verb="post")
@custom_method("refresh_account", http_verb="post", http_path="refresh")
class Account(APIResource):
    OBJECT_NAME = "financial_connections.account"

    def disconnect(self, idempotency_key=None, **params):
        url = self.instance_url() + "/disconnect"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def refresh_account(self, idempotency_key=None, **params):
        url = self.instance_url() + "/refresh"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
