# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.tax_rate import TaxRate


class CreditNoteLineItem(ListableAPIResource["CreditNoteLineItem"]):
    """
    The credit note line item object
    """

    OBJECT_NAME = "credit_note_line_item"

    class DiscountAmount(StripeObject):
        amount: int
        discount: ExpandableField["Discount"]

    class TaxAmount(StripeObject):
        amount: int
        inclusive: bool
        tax_rate: ExpandableField["TaxRate"]
        taxability_reason: Optional[
            Literal[
                "customer_exempt",
                "not_collecting",
                "not_subject_to_tax",
                "not_supported",
                "portion_product_exempt",
                "portion_reduced_rated",
                "portion_standard_rated",
                "product_exempt",
                "product_exempt_holiday",
                "proportionally_rated",
                "reduced_rated",
                "reverse_charge",
                "standard_rated",
                "taxable_basis_reduced",
                "zero_rated",
            ]
        ]
        taxable_amount: Optional[int]

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

    amount: int
    amount_excluding_tax: Optional[int]
    description: Optional[str]
    discount_amount: int
    discount_amounts: List[DiscountAmount]
    id: str
    invoice_line_item: Optional[str]
    livemode: bool
    object: Literal["credit_note_line_item"]
    quantity: Optional[int]
    tax_amounts: List[TaxAmount]
    tax_rates: List["TaxRate"]
    type: Literal["custom_line_item", "invoice_line_item"]
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[float]
    unit_amount_excluding_tax: Optional[float]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditNoteLineItem.ListParams"]
    ) -> ListObject["CreditNoteLineItem"]:
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

    _inner_class_types = {
        "discount_amounts": DiscountAmount,
        "tax_amounts": TaxAmount,
    }
