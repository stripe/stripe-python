# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("void_credit_note", http_verb="post", http_path="void")
class CreditNote(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "credit_note"

    @classmethod
    def preview(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/credit_notes/preview"
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    def void_credit_note(self, idempotency_key=None, **params):
        url = "/v1/credit_notes/{id}/void".format(
            id=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
