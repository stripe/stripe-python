# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
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
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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

    OBJECT_NAME = "invoiceitem"

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        customer: str
        description: NotRequired[Optional[str]]
        discountable: NotRequired[Optional[bool]]
        discounts: NotRequired[
            Optional[
                Union[Literal[""], List["InvoiceItem.CreateParamsDiscount"]]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        period: NotRequired[Optional["InvoiceItem.CreateParamsPeriod"]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[Optional["InvoiceItem.CreateParamsPriceData"]]
        quantity: NotRequired[Optional[int]]
        subscription: NotRequired[Optional[str]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[Union[Literal[""], str]]]
        tax_rates: NotRequired[Optional[List[str]]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsPeriod(TypedDict):
        end: int
        start: int

    class CreateParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["InvoiceItem.ListParamsCreated", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice: NotRequired[Optional[str]]
        limit: NotRequired[Optional[int]]
        pending: NotRequired[Optional[bool]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        discountable: NotRequired[Optional[bool]]
        discounts: NotRequired[
            Optional[
                Union[Literal[""], List["InvoiceItem.ModifyParamsDiscount"]]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        period: NotRequired[Optional["InvoiceItem.ModifyParamsPeriod"]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[Optional["InvoiceItem.ModifyParamsPriceData"]]
        quantity: NotRequired[Optional[int]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[Union[Literal[""], str]]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsPeriod(TypedDict):
        end: int
        start: int

    class ModifyParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    amount: int
    currency: str
    customer: ExpandableField["Customer"]
    date: int
    description: Optional[str]
    discountable: bool
    discounts: Optional[List[ExpandableField["Discount"]]]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["invoiceitem"]
    period: StripeObject
    plan: Optional["Plan"]
    price: Optional["Price"]
    proration: bool
    quantity: int
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_item: Optional[str]
    tax_rates: Optional[List["TaxRate"]]
    test_clock: Optional[ExpandableField["TestClock"]]
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[float]
    deleted: Optional[Literal[True]]

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

    @util.class_method_variant("_cls_delete")
    def delete(
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
        cls, id, **params: Unpack["InvoiceItem.ModifyParams"]
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
