from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("accept", http_verb="post")
@custom_method("cancel", http_verb="post")
@custom_method("finalize_quote", http_verb="post", http_path="finalize")
@custom_method("list_line_items", http_verb="get", http_path="line_items")
@custom_method("pdf", http_verb="get", is_streaming=True)
class Quote(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "quote"

    def accept(self, idempotency_key=None, **params):
        url = self.instance_url() + "/accept"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def cancel(self, idempotency_key=None, **params):
        url = self.instance_url() + "/cancel"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def finalize_quote(self, idempotency_key=None, **params):
        url = self.instance_url() + "/finalize"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def list_line_items(self, idempotency_key=None, **params):
        url = self.instance_url() + "/line_items"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("get", url, params, headers))
        return self

    def pdf(self, idempotency_key=None, **params):
        url = self.instance_url() + "/pdf"
        headers = util.populate_headers(idempotency_key)
        return self.request_stream("get", url, params, headers)
