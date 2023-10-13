# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            credit_amount: NotRequired["int|None"]
            effective_at: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            invoice: str
            lines: NotRequired["List[CreditNote.CreateParamsLine]|None"]
            memo: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            out_of_band_amount: NotRequired["int|None"]
            reason: NotRequired[
                "Literal['duplicate', 'fraudulent', 'order_change', 'product_unsatisfactory']|None"
            ]
            refund: NotRequired["str|None"]
            refund_amount: NotRequired["int|None"]
            shipping_cost: NotRequired[
                "CreditNote.CreateParamsShippingCost|None"
            ]

        class CreateParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]

        class CreateParamsLine(TypedDict):
            amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            invoice_line_item: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            type: Literal["custom_line_item", "invoice_line_item"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            invoice: NotRequired["str|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            memo: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]

        class PreviewParams(RequestOptions):
            amount: NotRequired["int|None"]
            credit_amount: NotRequired["int|None"]
            effective_at: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            invoice: str
            lines: NotRequired["List[CreditNote.PreviewParamsLine]|None"]
            memo: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            out_of_band_amount: NotRequired["int|None"]
            reason: NotRequired[
                "Literal['duplicate', 'fraudulent', 'order_change', 'product_unsatisfactory']|None"
            ]
            refund: NotRequired["str|None"]
            refund_amount: NotRequired["int|None"]
            shipping_cost: NotRequired[
                "CreditNote.PreviewParamsShippingCost|None"
            ]

        class PreviewParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]

        class PreviewParamsLine(TypedDict):
            amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            invoice_line_item: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            type: Literal["custom_line_item", "invoice_line_item"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class PreviewLinesParams(RequestOptions):
            amount: NotRequired["int|None"]
            credit_amount: NotRequired["int|None"]
            effective_at: NotRequired["int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            invoice: str
            limit: NotRequired["int|None"]
            lines: NotRequired["List[CreditNote.PreviewLinesParamsLine]|None"]
            memo: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            out_of_band_amount: NotRequired["int|None"]
            reason: NotRequired[
                "Literal['duplicate', 'fraudulent', 'order_change', 'product_unsatisfactory']|None"
            ]
            refund: NotRequired["str|None"]
            refund_amount: NotRequired["int|None"]
            shipping_cost: NotRequired[
                "CreditNote.PreviewLinesParamsShippingCost|None"
            ]
            starting_after: NotRequired["str|None"]

        class PreviewLinesParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]

        class PreviewLinesParamsLine(TypedDict):
            amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            invoice_line_item: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            type: Literal["custom_line_item", "invoice_line_item"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class VoidCreditNoteParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListLinesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

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
