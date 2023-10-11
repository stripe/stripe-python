# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.credit_note_line_item import CreditNoteLineItem
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.customer_balance_transaction import (
        CustomerBalanceTransaction,
    )
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.refund import Refund


@nested_resource_class_methods("line")
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

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        credit_amount: NotRequired[Optional[int]]
        effective_at: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        invoice: str
        lines: NotRequired[Optional[List["CreditNote.CreateParamsLine"]]]
        memo: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        out_of_band_amount: NotRequired[Optional[int]]
        reason: NotRequired[
            Optional[
                Literal[
                    "duplicate",
                    "fraudulent",
                    "order_change",
                    "product_unsatisfactory",
                ]
            ]
        ]
        refund: NotRequired[Optional[str]]
        refund_amount: NotRequired[Optional[int]]
        shipping_cost: NotRequired[
            Optional["CreditNote.CreateParamsShippingCost"]
        ]

    class CreateParamsShippingCost(TypedDict):
        shipping_rate: NotRequired[Optional[str]]

    class CreateParamsLine(TypedDict):
        amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        invoice_line_item: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        type: Literal["custom_line_item", "invoice_line_item"]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ListParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice: NotRequired[Optional[str]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        memo: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]

    class PreviewParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        credit_amount: NotRequired[Optional[int]]
        effective_at: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        invoice: str
        lines: NotRequired[Optional[List["CreditNote.PreviewParamsLine"]]]
        memo: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        out_of_band_amount: NotRequired[Optional[int]]
        reason: NotRequired[
            Optional[
                Literal[
                    "duplicate",
                    "fraudulent",
                    "order_change",
                    "product_unsatisfactory",
                ]
            ]
        ]
        refund: NotRequired[Optional[str]]
        refund_amount: NotRequired[Optional[int]]
        shipping_cost: NotRequired[
            Optional["CreditNote.PreviewParamsShippingCost"]
        ]

    class PreviewParamsShippingCost(TypedDict):
        shipping_rate: NotRequired[Optional[str]]

    class PreviewParamsLine(TypedDict):
        amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        invoice_line_item: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        type: Literal["custom_line_item", "invoice_line_item"]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class PreviewLinesParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        credit_amount: NotRequired[Optional[int]]
        effective_at: NotRequired[Optional[int]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice: str
        limit: NotRequired[Optional[int]]
        lines: NotRequired[Optional[List["CreditNote.PreviewLinesParamsLine"]]]
        memo: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        out_of_band_amount: NotRequired[Optional[int]]
        reason: NotRequired[
            Optional[
                Literal[
                    "duplicate",
                    "fraudulent",
                    "order_change",
                    "product_unsatisfactory",
                ]
            ]
        ]
        refund: NotRequired[Optional[str]]
        refund_amount: NotRequired[Optional[int]]
        shipping_cost: NotRequired[
            Optional["CreditNote.PreviewLinesParamsShippingCost"]
        ]
        starting_after: NotRequired[Optional[str]]

    class PreviewLinesParamsShippingCost(TypedDict):
        shipping_rate: NotRequired[Optional[str]]

    class PreviewLinesParamsLine(TypedDict):
        amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        invoice_line_item: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        type: Literal["custom_line_item", "invoice_line_item"]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class VoidCreditNoteParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListLinesParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    amount: int
    amount_shipping: int
    created: int
    currency: str
    customer: ExpandableField["Customer"]
    customer_balance_transaction: Optional[
        ExpandableField["CustomerBalanceTransaction"]
    ]
    discount_amount: int
    discount_amounts: List[StripeObject]
    effective_at: Optional[int]
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
    reason: Optional[
        Literal[
            "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
        ]
    ]
    refund: Optional[ExpandableField["Refund"]]
    shipping_cost: Optional[StripeObject]
    status: Literal["issued", "void"]
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax_amounts: List[StripeObject]
    total: int
    total_excluding_tax: Optional[int]
    type: Literal["post_payment", "pre_payment"]
    voided_at: Optional[int]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.CreateParams"]
    ) -> "CreditNote":
        return cast(
            "CreditNote",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.ListParams"]
    ) -> ListObject["CreditNote"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id, **params: Unpack["CreditNote.ModifyParams"]
    ) -> "CreditNote":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "CreditNote",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def preview(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.PreviewParams"]
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
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.PreviewLinesParams"]
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
    def retrieve(
        cls, id: str, **params: Unpack["CreditNote.RetrieveParams"]
    ) -> "CreditNote":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_void_credit_note(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.VoidCreditNoteParams"]
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
    def void_credit_note(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["CreditNote.VoidCreditNoteParams"]
    ):
        return self._request(
            "post",
            "/v1/credit_notes/{id}/void".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list_lines(
        cls,
        credit_note: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNote.ListLinesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/credit_notes/{credit_note}/lines".format(
                credit_note=util.sanitize_id(credit_note)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
