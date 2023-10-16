# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
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
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.subscription_schedule import SubscriptionSchedule
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Quote(
    CreateableAPIResource["Quote"],
    ListableAPIResource["Quote"],
    UpdateableAPIResource["Quote"],
):
    """
    A Quote is a way to model prices that you'd like to provide to a customer.
    Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    """

    OBJECT_NAME = "quote"
    if TYPE_CHECKING:

        class AcceptParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            application_fee_amount: NotRequired["Literal['']|int|None"]
            application_fee_percent: NotRequired["Literal['']|float|None"]
            automatic_tax: NotRequired["Quote.CreateParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            customer: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[Quote.CreateParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]
            footer: NotRequired["Literal['']|str|None"]
            from_quote: NotRequired["Quote.CreateParamsFromQuote|None"]
            header: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "Quote.CreateParamsInvoiceSettings|None"
            ]
            line_items: NotRequired["List[Quote.CreateParamsLineItem]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            subscription_data: NotRequired[
                "Quote.CreateParamsSubscriptionData|None"
            ]
            test_clock: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Literal['']|Quote.CreateParamsTransferData|None"
            ]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsSubscriptionData(TypedDict):
            description: NotRequired["str|None"]
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            trial_period_days: NotRequired["Literal['']|int|None"]

        class CreateParamsLineItem(TypedDict):
            price: NotRequired["str|None"]
            price_data: NotRequired["Quote.CreateParamsLineItemPriceData|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsLineItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: NotRequired[
                "Quote.CreateParamsLineItemPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class CreateParamsFromQuote(TypedDict):
            is_revision: NotRequired["bool|None"]
            quote: str

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool

        class FinalizeQuoteParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['accepted', 'canceled', 'draft', 'open']|None"
            ]
            test_clock: NotRequired["str|None"]

        class ListComputedUpfrontLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            application_fee_amount: NotRequired["Literal['']|int|None"]
            application_fee_percent: NotRequired["Literal['']|float|None"]
            automatic_tax: NotRequired["Quote.ModifyParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            customer: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[Quote.ModifyParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]
            footer: NotRequired["Literal['']|str|None"]
            header: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "Quote.ModifyParamsInvoiceSettings|None"
            ]
            line_items: NotRequired["List[Quote.ModifyParamsLineItem]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            subscription_data: NotRequired[
                "Quote.ModifyParamsSubscriptionData|None"
            ]
            transfer_data: NotRequired[
                "Literal['']|Quote.ModifyParamsTransferData|None"
            ]

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsSubscriptionData(TypedDict):
            description: NotRequired["Literal['']|str|None"]
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            trial_period_days: NotRequired["Literal['']|int|None"]

        class ModifyParamsLineItem(TypedDict):
            id: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired["Quote.ModifyParamsLineItemPriceData|None"]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsLineItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: NotRequired[
                "Quote.ModifyParamsLineItemPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    collection_method: Literal["charge_automatically", "send_invoice"]
    computed: StripeObject
    created: int
    currency: Optional[str]
    customer: Optional[ExpandableField["Customer"]]
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    description: Optional[str]
    discounts: List[ExpandableField["Discount"]]
    expires_at: int
    footer: Optional[str]
    from_quote: Optional[StripeObject]
    header: Optional[str]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_settings: Optional[StripeObject]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Dict[str, str]
    number: Optional[str]
    object: Literal["quote"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    status: Literal["accepted", "canceled", "draft", "open"]
    status_transitions: StripeObject
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_data: StripeObject
    subscription_schedule: Optional[ExpandableField["SubscriptionSchedule"]]
    test_clock: Optional[ExpandableField["TestClock"]]
    total_details: StripeObject
    transfer_data: Optional[StripeObject]

    @classmethod
    def _cls_accept(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/accept".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_accept")
    def accept(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/accept".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/cancel".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/cancel".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.CreateParams"]
    ) -> "Quote":
        return cast(
            "Quote",
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
    def _cls_finalize_quote(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/finalize".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_finalize_quote")
    def finalize_quote(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/finalize".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListParams"]
    ) -> ListObject["Quote"]:
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
    def _cls_list_computed_upfront_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/computed_upfront_line_items".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_computed_upfront_line_items")
    def list_computed_upfront_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/computed_upfront_line_items".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/line_items".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/line_items".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Unpack["Quote.ModifyParams"]) -> "Quote":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Quote",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Quote.RetrieveParams"]
    ) -> "Quote":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(sid),
            "pdf",
        )
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @util.class_method_variant("_cls_pdf")
    def pdf(
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)
