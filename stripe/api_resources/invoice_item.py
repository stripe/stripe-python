# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.plan import Plan
    from stripe.api_resources.price import Price
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class InvoiceItem(
    CreateableAPIResource["InvoiceItem"],
    DeletableAPIResource["InvoiceItem"],
    ListableAPIResource["InvoiceItem"],
    UpdateableAPIResource["InvoiceItem"],
):
    """
    Invoice Items represent the component lines of an [invoice](https://stripe.com/docs/api/invoices). An invoice item is added to an
    invoice by creating or updating it with an `invoice` field, at which point it will be included as
    [an invoice line item](https://stripe.com/docs/api/invoices/line_item) within
    [invoice.lines](https://stripe.com/docs/api/invoices/object#invoice_object-lines).

    Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined
    with a [subscription](https://stripe.com/docs/api/subscriptions). Sometimes you want to add a charge or credit to a customer, but actually charge
    or credit the customer's card only at the end of a regular billing cycle. This is useful for combining several charges
    (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

    Related guides: [Integrate with the Invoicing API](https://stripe.com/docs/invoicing/integration), [Subscription Invoices](https://stripe.com/docs/billing/invoices/subscription#adding-upcoming-invoice-items).
    """

    OBJECT_NAME: ClassVar[Literal["invoiceitem"]] = "invoiceitem"

    class Period(StripeObject):
        end: int
        """
        The end of the period, which must be greater than or equal to the start. This value is inclusive.
        """
        start: int
        """
        The start of the period. This value is inclusive.
        """

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            customer: str
            """
            The ID of the customer who will be billed when this invoice item is billed.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
            """
            discountable: NotRequired["bool|None"]
            """
            Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.
            """
            discounts: NotRequired[
                "Literal['']|List[InvoiceItem.CreateParamsDiscount]|None"
            ]
            """
            The coupons to redeem into discounts for the invoice item or invoice line item.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice: NotRequired["str|None"]
            """
            The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            period: NotRequired["InvoiceItem.CreateParamsPeriod|None"]
            """
            The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired["InvoiceItem.CreateParamsPriceData|None"]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Non-negative integer. The quantity of units for the invoice item.
            """
            subscription: NotRequired["str|None"]
            """
            The ID of a subscription to add this invoice item to. When left blank, the invoice item will be be added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            tax_code: NotRequired["Literal['']|str|None"]
            """
            A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            """
            tax_rates: NotRequired["List[str]|None"]
            """
            The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
            """
            unit_amount: NotRequired["int|None"]
            """
            The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount` will reduce the `amount_due` on the invoice.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsPeriod(TypedDict):
            end: int
            """
            The end of the period, which must be greater than or equal to the start. This value is inclusive.
            """
            start: int
            """
            The start of the period. This value is inclusive.
            """

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["InvoiceItem.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            """
            The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice: NotRequired["str|None"]
            """
            Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            pending: NotRequired["bool|None"]
            """
            Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
            """
            discountable: NotRequired["bool|None"]
            """
            Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations.
            """
            discounts: NotRequired[
                "Literal['']|List[InvoiceItem.ModifyParamsDiscount]|None"
            ]
            """
            The coupons & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            period: NotRequired["InvoiceItem.ModifyParamsPeriod|None"]
            """
            The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object.
            """
            price_data: NotRequired["InvoiceItem.ModifyParamsPriceData|None"]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            """
            quantity: NotRequired["int|None"]
            """
            Non-negative integer. The quantity of units for the invoice item.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            tax_code: NotRequired["Literal['']|str|None"]
            """
            A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates.
            """
            unit_amount: NotRequired["int|None"]
            """
            The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsPeriod(TypedDict):
            end: int
            """
            The end of the period, which must be greater than or equal to the start. This value is inclusive.
            """
            start: int
            """
            The start of the period. This value is inclusive.
            """

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: int
    """
    Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: ExpandableField["Customer"]
    """
    The ID of the customer who will be billed when this invoice item is billed.
    """
    date: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discountable: bool
    """
    If true, discounts will apply to this invoice item. Always false for prorations.
    """
    discounts: Optional[List[ExpandableField["Discount"]]]
    """
    The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice: Optional[ExpandableField["Invoice"]]
    """
    The ID of the invoice this invoice item belongs to.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["invoiceitem"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    period: Period
    plan: Optional["Plan"]
    """
    If the invoice item is a proration, the plan of the subscription that the proration was computed for.
    """
    price: Optional["Price"]
    """
    The price of the invoice item.
    """
    proration: bool
    """
    Whether the invoice item was created automatically as a proration adjustment when the customer switched plans.
    """
    quantity: int
    """
    Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for.
    """
    subscription: Optional[ExpandableField["Subscription"]]
    """
    The subscription that this invoice item has been created for, if any.
    """
    subscription_item: Optional[str]
    """
    The subscription item that this invoice item has been created for, if any.
    """
    tax_rates: Optional[List["TaxRate"]]
    """
    The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this invoice item belongs to.
    """
    unit_amount: Optional[int]
    """
    Unit amount (in the `currency` specified) of the invoice item.
    """
    unit_amount_decimal: Optional[str]
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["InvoiceItem.CreateParams"]
    ) -> "InvoiceItem":
        return cast(
            "InvoiceItem",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["InvoiceItem.DeleteParams"]
    ) -> "InvoiceItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "InvoiceItem",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @classmethod
    def delete(
        cls, sid: str, **params: Unpack["InvoiceItem.DeleteParams"]
    ) -> "InvoiceItem":
        ...

    @overload
    def delete(
        self, **params: Unpack["InvoiceItem.DeleteParams"]
    ) -> "InvoiceItem":
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["InvoiceItem.DeleteParams"]
    ) -> "InvoiceItem":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["InvoiceItem.ListParams"]
    ) -> ListObject["InvoiceItem"]:
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
        cls, id: str, **params: Unpack["InvoiceItem.ModifyParams"]
    ) -> "InvoiceItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "InvoiceItem",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["InvoiceItem.RetrieveParams"]
    ) -> "InvoiceItem":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"period": Period}
