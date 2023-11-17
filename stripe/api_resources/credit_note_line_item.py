# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.tax_rate import TaxRate


class CreditNoteLineItem(ListableAPIResource["CreditNoteLineItem"]):
    """
    The credit note line item object
    """

    OBJECT_NAME: ClassVar[
        Literal["credit_note_line_item"]
    ] = "credit_note_line_item"

    class DiscountAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the discount.
        """
        discount: ExpandableField["Discount"]
        """
        The discount that was applied to get this discount amount.
        """

    class TaxAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the tax.
        """
        inclusive: bool
        """
        Whether this tax amount is inclusive or exclusive.
        """
        tax_rate: ExpandableField["TaxRate"]
        """
        The tax rate that was applied to get this tax amount.
        """
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
        """
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
        """
        taxable_amount: Optional[int]
        """
        The amount on which tax is calculated, in cents (or local equivalent).
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    amount: int
    """
    The integer amount in cents (or local equivalent) representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.
    """
    amount_excluding_tax: Optional[int]
    """
    The integer amount in cents (or local equivalent) representing the amount being credited for this line item, excluding all tax and discounts.
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
    quantity: Optional[int]
    """
    The number of units of product being credited.
    """
    tax_amounts: List[TaxAmount]
    """
    The amount of tax calculated per tax rate for this line item
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
    unit_amount_excluding_tax: Optional[str]
    """
    The amount in cents (or local equivalent) representing the unit amount being credited for this line item, excluding all tax and discounts.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "CreditNoteLineItem.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["CreditNoteLineItem"]:
        """
        When retrieving a credit note, you'll get a lines property containing the the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
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
