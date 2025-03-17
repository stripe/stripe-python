# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._discount import Discount
    from stripe._tax_rate import TaxRate
    from stripe.billing._credit_balance_transaction import (
        CreditBalanceTransaction,
    )


class CreditNoteLineItem(StripeObject):
    """
    The credit note line item object
    """

    OBJECT_NAME: ClassVar[Literal["credit_note_line_item"]] = (
        "credit_note_line_item"
    )

    class DiscountAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the discount.
        """
        discount: ExpandableField["Discount"]
        """
        The discount that was applied to get this discount amount.
        """

    class PretaxCreditAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the pretax credit amount.
        """
        credit_balance_transaction: Optional[
            ExpandableField["CreditBalanceTransaction"]
        ]
        """
        The credit balance transaction that was applied to get this pretax credit amount.
        """
        discount: Optional[ExpandableField["Discount"]]
        """
        The discount that was applied to get this pretax credit amount.
        """
        type: Literal["credit_balance_transaction", "discount"]
        """
        Type of the pretax credit amount referenced.
        """

    amount: int
    """
    The integer amount in cents (or local equivalent) representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.
    """
    description: Optional[str]
    """
    Description of the item being credited.
    """
    discount_amount: int
    """
    The integer amount in cents (or local equivalent) representing the discount being credited for this line item.
    """
    discount_amounts: List[DiscountAmount]
    """
    The amount of discount calculated per discount for this line item
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_line_item: Optional[str]
    """
    ID of the invoice line item being credited
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["credit_note_line_item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pretax_credit_amounts: List[PretaxCreditAmount]
    """
    The pretax credit amounts (ex: discount, credit grants, etc) for this line item.
    """
    quantity: Optional[int]
    """
    The number of units of product being credited.
    """
    tax_rates: List["TaxRate"]
    """
    The tax rates which apply to the line item.
    """
    type: Literal["custom_line_item", "invoice_line_item"]
    """
    The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice.
    """
    unit_amount: Optional[int]
    """
    The cost of each unit of product being credited.
    """
    unit_amount_decimal: Optional[str]
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.
    """
    _inner_class_types = {
        "discount_amounts": DiscountAmount,
        "pretax_credit_amounts": PretaxCreditAmount,
    }
