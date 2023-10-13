# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            customer: str
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[InvoiceItem.CreateParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired["InvoiceItem.CreateParamsPeriod|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired["InvoiceItem.CreateParamsPriceData|None"]
            quantity: NotRequired["int|None"]
            subscription: NotRequired["str|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPeriod(TypedDict):
            end: int
            start: int

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["InvoiceItem.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            invoice: NotRequired["str|None"]
            limit: NotRequired["int|None"]
            pending: NotRequired["bool|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[InvoiceItem.ModifyParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired["InvoiceItem.ModifyParamsPeriod|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired["InvoiceItem.ModifyParamsPriceData|None"]
            quantity: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPeriod(TypedDict):
            end: int
            start: int

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
