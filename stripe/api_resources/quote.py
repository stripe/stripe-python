# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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

    class AcceptParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        application_fee_amount: NotRequired[Optional[Union[Literal[""], int]]]
        application_fee_percent: NotRequired[
            Optional[Union[Literal[""], float]]
        ]
        automatic_tax: NotRequired[Optional["Quote.CreateAutomaticTaxParams"]]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        customer: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        discounts: NotRequired[
            Optional[Union[Literal[""], List["Quote.CreateDiscountParams"]]]
        ]
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]
        footer: NotRequired[Optional[Union[Literal[""], str]]]
        from_quote: NotRequired[Optional["Quote.CreateFromQuoteParams"]]
        header: NotRequired[Optional[Union[Literal[""], str]]]
        invoice_settings: NotRequired[
            Optional["Quote.CreateInvoiceSettingsParams"]
        ]
        line_items: NotRequired[Optional[List["Quote.CreateLineItemParams"]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        subscription_data: NotRequired[
            Optional["Quote.CreateSubscriptionDataParams"]
        ]
        test_clock: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional[Union[Literal[""], "Quote.CreateTransferDataParams"]]
        ]

    class CreateTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateSubscriptionDataParams(TypedDict):
        description: NotRequired[Optional[str]]
        effective_date: NotRequired[
            Optional[
                Union[Literal[""], Union[Literal["current_period_end"], int]]
            ]
        ]
        trial_period_days: NotRequired[Optional[Union[Literal[""], int]]]

    class CreateLineItemParams(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Quote.CreateLineItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateLineItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: NotRequired[
            Optional["Quote.CreateLineItemPriceDataRecurringParams"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateLineItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class CreateFromQuoteParams(TypedDict):
        is_revision: NotRequired[Optional[bool]]
        quote: str

    class CreateDiscountParams(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class CreateAutomaticTaxParams(TypedDict):
        enabled: bool

    class FinalizeQuoteParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[Literal["accepted", "canceled", "draft", "open"]]
        ]
        test_clock: NotRequired[Optional[str]]

    class ListComputedUpfrontLineItemsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        application_fee_amount: NotRequired[Optional[Union[Literal[""], int]]]
        application_fee_percent: NotRequired[
            Optional[Union[Literal[""], float]]
        ]
        automatic_tax: NotRequired[Optional["Quote.ModifyAutomaticTaxParams"]]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        customer: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        discounts: NotRequired[
            Optional[Union[Literal[""], List["Quote.ModifyDiscountParams"]]]
        ]
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]
        footer: NotRequired[Optional[Union[Literal[""], str]]]
        header: NotRequired[Optional[Union[Literal[""], str]]]
        invoice_settings: NotRequired[
            Optional["Quote.ModifyInvoiceSettingsParams"]
        ]
        line_items: NotRequired[Optional[List["Quote.ModifyLineItemParams"]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        subscription_data: NotRequired[
            Optional["Quote.ModifySubscriptionDataParams"]
        ]
        transfer_data: NotRequired[
            Optional[Union[Literal[""], "Quote.ModifyTransferDataParams"]]
        ]

    class ModifyTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifySubscriptionDataParams(TypedDict):
        description: NotRequired[Optional[Union[Literal[""], str]]]
        effective_date: NotRequired[
            Optional[
                Union[Literal[""], Union[Literal["current_period_end"], int]]
            ]
        ]
        trial_period_days: NotRequired[Optional[Union[Literal[""], int]]]

    class ModifyLineItemParams(TypedDict):
        id: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Quote.ModifyLineItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyLineItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: NotRequired[
            Optional["Quote.ModifyLineItemPriceDataRecurringParams"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyLineItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class ModifyDiscountParams(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class ModifyAutomaticTaxParams(TypedDict):
        enabled: bool

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
