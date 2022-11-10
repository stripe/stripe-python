# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class CreditNote(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Issue a credit note to adjust an invoice's amount after the invoice is finalized.

    Related guide: [Credit Notes](https://stripe.com/docs/billing/invoices/credit-notes).
    """

    OBJECT_NAME = "credit_note"

    @classmethod
    def preview(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "get",
            "/v1/credit_notes/preview",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def _cls_void_credit_note(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/credit_notes/{id}/void".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_void_credit_note")
    def void_credit_note(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/credit_notes/{id}/void".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
