# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer_balance_transaction import (
        CustomerBalanceTransaction,
    )
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.credit_note_line_item import CreditNoteLineItem
    from stripe.api_resources.refund import Refund


@nested_resource_class_methods(
    "line",
    operations=["list"],
)
class CreditNote(
    CreateableAPIResource["CreditNote"],
    ListableAPIResource["CreditNote"],
    UpdateableAPIResource["CreditNote"],
):
    """
    Issue a credit note to adjust an invoice's amount after the invoice is finalized.

    Related guide: [Credit notes](https://stripe.com/docs/billing/invoices/credit-notes)
    """

    OBJECT_NAME = "credit_note"
    amount: int
    amount_shipping: int
    created: str
    currency: str
    customer: ExpandableField[Any]
    customer_balance_transaction: Optional[
        ExpandableField["CustomerBalanceTransaction"]
    ]
    discount_amount: int
    discount_amounts: List[StripeObject]
    effective_at: Optional[str]
    id: str
    invoice: ExpandableField["Invoice"]
    lines: ListObject["CreditNoteLineItem"]
    livemode: bool
    memo: Optional[str]
    metadata: Optional[Dict[str, str]]
    number: str
    object: Literal["credit_note"]
    out_of_band_amount: Optional[int]
    pdf: str
    reason: Optional[str]
    refund: Optional[ExpandableField["Refund"]]
    shipping_cost: Optional[StripeObject]
    status: str
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax_amounts: List[StripeObject]
    total: int
    total_excluding_tax: Optional[int]
    type: str
    voided_at: Optional[str]

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
    def preview_lines(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "get",
            "/v1/credit_notes/preview/lines",
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
