# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._invoice_line_item import InvoiceLineItem
from stripe._list_object import ListObject
from stripe._quote import Quote
from stripe._quote_computed_upfront_line_items_service import (
    QuoteComputedUpfrontLineItemsService,
)
from stripe._quote_line_item_service import QuoteLineItemService
from stripe._quote_line_service import QuoteLineService
from stripe._quote_preview_invoice_service import QuotePreviewInvoiceService
from stripe._quote_preview_subscription_schedule_service import (
    QuotePreviewSubscriptionScheduleService,
)
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Any, Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class QuoteService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.preview_invoices = QuotePreviewInvoiceService(self._requestor)
        self.preview_subscription_schedules = (
            QuotePreviewSubscriptionScheduleService(
                self._requestor,
            )
        )
        self.lines = QuoteLineService(self._requestor)
        self.line_items = QuoteLineItemService(self._requestor)
        self.computed_upfront_line_items = (
            QuoteComputedUpfrontLineItemsService(
                self._requestor,
            )
        )

    class AcceptParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CancelParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(TypedDict):
        allow_backdated_lines: NotRequired[bool]
        """
        Set to true to allow quote lines to have `starts_at` in the past if collection is paused between `starts_at` and now.
        """
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
        """
        application_fee_percent: NotRequired["Literal['']|float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
        """
        automatic_tax: NotRequired["QuoteService.CreateParamsAutomaticTax"]
        """
        Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
        """
        collection_method: NotRequired[
            Literal["charge_automatically", "send_invoice"]
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
        """
        customer: NotRequired[str]
        """
        The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
        """
        customer_account: NotRequired[str]
        """
        The account for which this quote belongs to. A customer or account is required before finalizing the quote. Once specified, it cannot be changed.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that will apply to any line item that does not have `tax_rates` set.
        """
        description: NotRequired["Literal['']|str"]
        """
        A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        discounts: NotRequired[
            "Literal['']|List[QuoteService.CreateParamsDiscount]"
        ]
        """
        The discounts applied to the quote.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        footer: NotRequired["Literal['']|str"]
        """
        A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        from_quote: NotRequired["QuoteService.CreateParamsFromQuote"]
        """
        Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
        """
        header: NotRequired["Literal['']|str"]
        """
        A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        invoice_settings: NotRequired[
            "QuoteService.CreateParamsInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        line_items: NotRequired[List["QuoteService.CreateParamsLineItem"]]
        """
        A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        lines: NotRequired[List["QuoteService.CreateParamsLine"]]
        """
        A list of [quote lines](https://docs.stripe.com/api/quote_lines) on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge.
        """
        subscription_data: NotRequired[
            "QuoteService.CreateParamsSubscriptionData"
        ]
        """
        When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
        """
        subscription_data_overrides: NotRequired[
            List["QuoteService.CreateParamsSubscriptionDataOverride"]
        ]
        """
        List representing overrides for `subscription_data` configurations for specific subscription schedules.
        """
        test_clock: NotRequired[str]
        """
        ID of the test clock to attach to the quote.
        """
        transfer_data: NotRequired[
            "Literal['']|QuoteService.CreateParamsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the invoices.
        """

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
        """
        liability: NotRequired[
            "QuoteService.CreateParamsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class CreateParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.CreateParamsDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.CreateParamsDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsFromQuote(TypedDict):
        is_revision: NotRequired[bool]
        """
        Whether this quote is a revision of the previous quote.
        """
        quote: str
        """
        The `id` of the quote that will be cloned.
        """

    class CreateParamsInvoiceSettings(TypedDict):
        days_until_due: NotRequired[int]
        """
        Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
        """
        issuer: NotRequired["QuoteService.CreateParamsInvoiceSettingsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class CreateParamsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsLine(TypedDict):
        actions: NotRequired[List["QuoteService.CreateParamsLineAction"]]
        """
        An array of operations the quote line performs.
        """
        applies_to: NotRequired["QuoteService.CreateParamsLineAppliesTo"]
        """
        Details to identify the subscription schedule the quote line applies to.
        """
        billing_cycle_anchor: NotRequired[
            Literal["automatic", "line_starts_at"]
        ]
        """
        For point-in-time quote lines (having no `ends_at` timestamp), this attribute lets you set or remove whether the subscription's billing cycle anchor is reset at the Quote Line `starts_at` timestamp.For time-span based quote lines (having both `starts_at` and `ends_at`), the only valid value is `automatic`, which removes any previously configured billing cycle anchor resets during the window of time spanning the quote line.
        """
        cancel_subscription_schedule: NotRequired[
            "QuoteService.CreateParamsLineCancelSubscriptionSchedule"
        ]
        """
        A point-in-time operation that cancels an existing subscription schedule at the line's starts_at timestamp. Currently only compatible with `quote_acceptance_date` for `starts_at`. When using cancel_subscription_schedule, the subscription schedule on the quote remains unalterable, except for modifications to the metadata, collection_method or invoice_settings.
        """
        ends_at: NotRequired["QuoteService.CreateParamsLineEndsAt"]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the quote line is considered a point-in-time operation that only affects the exact timestamp at `starts_at`, and a restricted set of attributes is supported on the quote line.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Changes to how Stripe handles prorations during the quote line's time span. Affects if and how prorations are created when a future phase starts.
        """
        set_pause_collection: NotRequired[
            "QuoteService.CreateParamsLineSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            Literal["line_ends_at", "line_starts_at"]
        ]
        """
        Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
        """
        starts_at: NotRequired["QuoteService.CreateParamsLineStartsAt"]
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        trial_settings: NotRequired[
            "QuoteService.CreateParamsLineTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class CreateParamsLineAction(TypedDict):
        add_discount: NotRequired[
            "QuoteService.CreateParamsLineActionAddDiscount"
        ]
        """
        Details for the `add_discount` type.
        """
        add_item: NotRequired["QuoteService.CreateParamsLineActionAddItem"]
        """
        Details for the `add_item` type.
        """
        add_metadata: NotRequired[Dict[str, str]]
        """
        Details for the `add_metadata` type: specify a hash of key-value pairs.
        """
        remove_discount: NotRequired[
            "QuoteService.CreateParamsLineActionRemoveDiscount"
        ]
        """
        Details for the `remove_discount` type.
        """
        remove_item: NotRequired[
            "QuoteService.CreateParamsLineActionRemoveItem"
        ]
        """
        Details for the `remove_item` type.
        """
        remove_metadata: NotRequired[List[str]]
        """
        Details for the `remove_metadata` type: specify an array of metadata keys.
        """
        set_discounts: NotRequired[
            List["QuoteService.CreateParamsLineActionSetDiscount"]
        ]
        """
        Details for the `set_discounts` type.
        """
        set_items: NotRequired[
            List["QuoteService.CreateParamsLineActionSetItem"]
        ]
        """
        Details for the `set_items` type.
        """
        set_metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Details for the `set_metadata` type: specify an array of key-value pairs.
        """
        type: Literal[
            "add_discount",
            "add_item",
            "add_metadata",
            "clear_discounts",
            "clear_metadata",
            "remove_discount",
            "remove_item",
            "remove_metadata",
            "set_discounts",
            "set_items",
            "set_metadata",
        ]
        """
        The type of action the quote line performs.
        """

    class CreateParamsLineActionAddDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to redeem.
        """
        discount: NotRequired[str]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired[int]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """
        promotion_code: NotRequired[str]
        """
        The promotion code to redeem.
        """

    class CreateParamsLineActionAddDiscountDiscountEnd(TypedDict):
        type: Literal["line_ends_at"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionAddItem(TypedDict):
        discounts: NotRequired[
            List["QuoteService.CreateParamsLineActionAddItemDiscount"]
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired[int]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired[List[str]]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired["QuoteService.CreateParamsLineActionAddItemTrial"]
        """
        Options that configure the trial on the subscription item.
        """

    class CreateParamsLineActionAddItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineActionAddItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.CreateParamsLineActionAddItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionAddItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineActionAddItemTrial(TypedDict):
        converts_to: NotRequired[List[str]]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class CreateParamsLineActionRemoveDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired[str]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired[str]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class CreateParamsLineActionRemoveItem(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class CreateParamsLineActionSetDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired[str]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired[str]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class CreateParamsLineActionSetItem(TypedDict):
        discounts: NotRequired[
            List["QuoteService.CreateParamsLineActionSetItemDiscount"]
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired[int]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired[List[str]]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired["QuoteService.CreateParamsLineActionSetItemTrial"]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class CreateParamsLineActionSetItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineActionSetItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.CreateParamsLineActionSetItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionSetItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineActionSetItemTrial(TypedDict):
        converts_to: NotRequired[List[str]]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class CreateParamsLineAppliesTo(TypedDict):
        new_reference: NotRequired[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CreateParamsLineCancelSubscriptionSchedule(TypedDict):
        cancel_at: Literal["line_starts_at"]
        """
        Timestamp helper to cancel the underlying schedule on the accompanying line's start date. Must be set to `line_starts_at`.
        """
        invoice_now: NotRequired[bool]
        """
        If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Boolean that defaults to `true`.
        """
        prorate: NotRequired[bool]
        """
        If the subscription schedule is `active`, indicates if the cancellation should be prorated. Boolean that defaults to `true`.
        """

    class CreateParamsLineEndsAt(TypedDict):
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineEndsAtDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired["QuoteService.CreateParamsLineEndsAtDuration"]
        """
        Time span for the quote line starting from the `starts_at` date.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "billing_period_end",
            "discount_end",
            "duration",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `ends_at`.
        """

    class CreateParamsLineEndsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class CreateParamsLineEndsAtDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[QuoteService.CreateParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired[str]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["QuoteService.CreateParamsLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired[int]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class CreateParamsLineItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.CreateParamsLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
        """
        recurring: NotRequired[
            "QuoteService.CreateParamsLineItemPriceDataRecurring"
        ]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired[int]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired[int]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class CreateParamsLineSetPauseCollection(TypedDict):
        set: NotRequired["QuoteService.CreateParamsLineSetPauseCollectionSet"]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class CreateParamsLineSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class CreateParamsLineStartsAt(TypedDict):
        discount_end: NotRequired[
            "QuoteService.CreateParamsLineStartsAtDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        line_ends_at: NotRequired[
            "QuoteService.CreateParamsLineStartsAtLineEndsAt"
        ]
        """
        The timestamp the given line ends at.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "line_ends_at",
            "now",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `starts_at`.
        """

    class CreateParamsLineStartsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class CreateParamsLineStartsAtLineEndsAt(TypedDict):
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsLineTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "QuoteService.CreateParamsLineTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class CreateParamsLineTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired[Literal["defer", "include"]]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class CreateParamsSubscriptionData(TypedDict):
        bill_on_acceptance: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        billing_cycle_anchor: NotRequired["Literal['']|Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        billing_mode: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillingMode"
        ]
        """
        Controls how prorations and invoices for subscriptions are calculated and orchestrated.
        """
        description: NotRequired[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        effective_date: NotRequired[
            "Literal['']|Literal['current_period_end']|int"
        ]
        """
        When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
        """
        end_behavior: NotRequired[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        from_subscription: NotRequired[str]
        """
        The id of a subscription that the quote will update. By default, the quote will contain the state of the subscription (such as line items, collection method and billing thresholds) unless overridden.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        prebilling: NotRequired[
            "Literal['']|QuoteService.CreateParamsSubscriptionDataPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """
        trial_period_days: NotRequired["Literal['']|int"]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
        line_starts_at: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
        duration: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataBillingMode(TypedDict):
        type: Literal["classic", "flexible"]

    class CreateParamsSubscriptionDataOverride(TypedDict):
        applies_to: (
            "QuoteService.CreateParamsSubscriptionDataOverrideAppliesTo"
        )
        """
        Whether the override applies to an existing Subscription Schedule or a new Subscription Schedule.
        """
        bill_on_acceptance: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: NotRequired[str]
        """
        The customer the Subscription Data override applies to. This is only relevant when `applies_to.type=new_reference`.
        """
        description: NotRequired[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: NotRequired[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """

    class CreateParamsSubscriptionDataOverrideAppliesTo(TypedDict):
        new_reference: NotRequired[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
        TypedDict,
    ):
        line_starts_at: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
        TypedDict,
    ):
        duration: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "QuoteService.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[int]
        """
        The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        amount_percent: NotRequired[float]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class FinalizeQuoteParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
        """

    class ListParams(TypedDict):
        customer: NotRequired[str]
        """
        The ID of the customer whose quotes will be retrieved.
        """
        customer_account: NotRequired[str]
        """
        The ID of the account whose quotes will be retrieved.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        from_subscription: NotRequired[str]
        """
        The subscription which the quote updates.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            Literal[
                "accepted", "accepting", "canceled", "draft", "open", "stale"
            ]
        ]
        """
        The status of the quote.
        """
        test_clock: NotRequired[str]
        """
        Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.
        """

    class ListPreviewInvoiceLinesParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class MarkDraftParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class MarkStaleParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        reason: NotRequired[str]
        """
        Reason the Quote is being marked stale.
        """

    class PdfParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReestimateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        allow_backdated_lines: NotRequired[bool]
        """
        Set to true to allow quote lines to have `starts_at` in the past if collection is paused between `starts_at` and now.
        """
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
        """
        application_fee_percent: NotRequired["Literal['']|float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
        """
        automatic_tax: NotRequired["QuoteService.UpdateParamsAutomaticTax"]
        """
        Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
        """
        collection_method: NotRequired[
            Literal["charge_automatically", "send_invoice"]
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
        """
        customer: NotRequired[str]
        """
        The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
        """
        customer_account: NotRequired[str]
        """
        The account for which this quote belongs to. A customer or account is required before finalizing the quote. Once specified, it cannot be changed.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that will apply to any line item that does not have `tax_rates` set.
        """
        description: NotRequired["Literal['']|str"]
        """
        A description that will be displayed on the quote PDF.
        """
        discounts: NotRequired[
            "Literal['']|List[QuoteService.UpdateParamsDiscount]"
        ]
        """
        The discounts applied to the quote.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
        """
        footer: NotRequired["Literal['']|str"]
        """
        A footer that will be displayed on the quote PDF.
        """
        header: NotRequired["Literal['']|str"]
        """
        A header that will be displayed on the quote PDF.
        """
        invoice_settings: NotRequired[
            "QuoteService.UpdateParamsInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        line_items: NotRequired[List["QuoteService.UpdateParamsLineItem"]]
        """
        A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        lines: NotRequired[List["QuoteService.UpdateParamsLine"]]
        """
        A list of [quote lines](https://docs.stripe.com/api/quote_lines) on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge.
        """
        subscription_data: NotRequired[
            "QuoteService.UpdateParamsSubscriptionData"
        ]
        """
        When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
        """
        subscription_data_overrides: NotRequired[
            "Literal['']|List[QuoteService.UpdateParamsSubscriptionDataOverride]"
        ]
        """
        List representing overrides for `subscription_data` configurations for specific subscription schedules.
        """
        transfer_data: NotRequired[
            "Literal['']|QuoteService.UpdateParamsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the invoices.
        """

    class UpdateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
        """
        liability: NotRequired[
            "QuoteService.UpdateParamsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class UpdateParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.UpdateParamsDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.UpdateParamsDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsInvoiceSettings(TypedDict):
        days_until_due: NotRequired[int]
        """
        Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
        """
        issuer: NotRequired["QuoteService.UpdateParamsInvoiceSettingsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class UpdateParamsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsLine(TypedDict):
        actions: NotRequired[List["QuoteService.UpdateParamsLineAction"]]
        """
        An array of operations the quote line performs.
        """
        applies_to: NotRequired["QuoteService.UpdateParamsLineAppliesTo"]
        """
        Details to identify the subscription schedule the quote line applies to.
        """
        billing_cycle_anchor: NotRequired[
            Literal["automatic", "line_starts_at"]
        ]
        """
        For point-in-time quote lines (having no `ends_at` timestamp), this attribute lets you set or remove whether the subscription's billing cycle anchor is reset at the Quote Line `starts_at` timestamp.For time-span based quote lines (having both `starts_at` and `ends_at`), the only valid value is `automatic`, which removes any previously configured billing cycle anchor resets during the window of time spanning the quote line.
        """
        cancel_subscription_schedule: NotRequired[
            "QuoteService.UpdateParamsLineCancelSubscriptionSchedule"
        ]
        """
        A point-in-time operation that cancels an existing subscription schedule at the line's starts_at timestamp. Currently only compatible with `quote_acceptance_date` for `starts_at`. When using cancel_subscription_schedule, the subscription schedule on the quote remains unalterable, except for modifications to the metadata, collection_method or invoice_settings.
        """
        ends_at: NotRequired["QuoteService.UpdateParamsLineEndsAt"]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the quote line is considered a point-in-time operation that only affects the exact timestamp at `starts_at`, and a restricted set of attributes is supported on the quote line.
        """
        id: NotRequired[str]
        """
        The ID of an existing line on the quote.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Changes to how Stripe handles prorations during the quote line's time span. Affects if and how prorations are created when a future phase starts.
        """
        set_pause_collection: NotRequired[
            "QuoteService.UpdateParamsLineSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            Literal["line_ends_at", "line_starts_at"]
        ]
        """
        Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
        """
        starts_at: NotRequired["QuoteService.UpdateParamsLineStartsAt"]
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        trial_settings: NotRequired[
            "QuoteService.UpdateParamsLineTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class UpdateParamsLineAction(TypedDict):
        add_discount: NotRequired[
            "QuoteService.UpdateParamsLineActionAddDiscount"
        ]
        """
        Details for the `add_discount` type.
        """
        add_item: NotRequired["QuoteService.UpdateParamsLineActionAddItem"]
        """
        Details for the `add_item` type.
        """
        add_metadata: NotRequired[Dict[str, str]]
        """
        Details for the `add_metadata` type: specify a hash of key-value pairs.
        """
        remove_discount: NotRequired[
            "QuoteService.UpdateParamsLineActionRemoveDiscount"
        ]
        """
        Details for the `remove_discount` type.
        """
        remove_item: NotRequired[
            "QuoteService.UpdateParamsLineActionRemoveItem"
        ]
        """
        Details for the `remove_item` type.
        """
        remove_metadata: NotRequired[List[str]]
        """
        Details for the `remove_metadata` type: specify an array of metadata keys.
        """
        set_discounts: NotRequired[
            List["QuoteService.UpdateParamsLineActionSetDiscount"]
        ]
        """
        Details for the `set_discounts` type.
        """
        set_items: NotRequired[
            List["QuoteService.UpdateParamsLineActionSetItem"]
        ]
        """
        Details for the `set_items` type.
        """
        set_metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Details for the `set_metadata` type: specify an array of key-value pairs.
        """
        type: Literal[
            "add_discount",
            "add_item",
            "add_metadata",
            "clear_discounts",
            "clear_metadata",
            "remove_discount",
            "remove_item",
            "remove_metadata",
            "set_discounts",
            "set_items",
            "set_metadata",
        ]
        """
        The type of action the quote line performs.
        """

    class UpdateParamsLineActionAddDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to redeem.
        """
        discount: NotRequired[str]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired[int]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """
        promotion_code: NotRequired[str]
        """
        The promotion code to redeem.
        """

    class UpdateParamsLineActionAddDiscountDiscountEnd(TypedDict):
        type: Literal["line_ends_at"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsLineActionAddItem(TypedDict):
        discounts: NotRequired[
            List["QuoteService.UpdateParamsLineActionAddItemDiscount"]
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired[int]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired[List[str]]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired["QuoteService.UpdateParamsLineActionAddItemTrial"]
        """
        Options that configure the trial on the subscription item.
        """

    class UpdateParamsLineActionAddItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineActionAddItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.UpdateParamsLineActionAddItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsLineActionAddItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsLineActionAddItemTrial(TypedDict):
        converts_to: NotRequired[List[str]]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class UpdateParamsLineActionRemoveDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired[str]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired[str]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class UpdateParamsLineActionRemoveItem(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class UpdateParamsLineActionSetDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired[str]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired[str]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class UpdateParamsLineActionSetItem(TypedDict):
        discounts: NotRequired[
            List["QuoteService.UpdateParamsLineActionSetItemDiscount"]
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired[int]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired[List[str]]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired["QuoteService.UpdateParamsLineActionSetItemTrial"]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class UpdateParamsLineActionSetItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineActionSetItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.UpdateParamsLineActionSetItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsLineActionSetItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsLineActionSetItemTrial(TypedDict):
        converts_to: NotRequired[List[str]]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class UpdateParamsLineAppliesTo(TypedDict):
        new_reference: NotRequired[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class UpdateParamsLineCancelSubscriptionSchedule(TypedDict):
        cancel_at: Literal["line_starts_at"]
        """
        Timestamp helper to cancel the underlying schedule on the accompanying line's start date. Must be set to `line_starts_at`.
        """
        invoice_now: NotRequired[bool]
        """
        If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Boolean that defaults to `true`.
        """
        prorate: NotRequired[bool]
        """
        If the subscription schedule is `active`, indicates if the cancellation should be prorated. Boolean that defaults to `true`.
        """

    class UpdateParamsLineEndsAt(TypedDict):
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineEndsAtDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired["QuoteService.UpdateParamsLineEndsAtDuration"]
        """
        Time span for the quote line starting from the `starts_at` date.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "billing_period_end",
            "discount_end",
            "duration",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `ends_at`.
        """

    class UpdateParamsLineEndsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class UpdateParamsLineEndsAtDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[QuoteService.UpdateParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        id: NotRequired[str]
        """
        The ID of an existing line item on the quote.
        """
        price: NotRequired[str]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["QuoteService.UpdateParamsLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired[int]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class UpdateParamsLineItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "QuoteService.UpdateParamsLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
        """
        recurring: NotRequired[
            "QuoteService.UpdateParamsLineItemPriceDataRecurring"
        ]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired[int]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class UpdateParamsLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired[int]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class UpdateParamsLineSetPauseCollection(TypedDict):
        set: NotRequired["QuoteService.UpdateParamsLineSetPauseCollectionSet"]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class UpdateParamsLineSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class UpdateParamsLineStartsAt(TypedDict):
        discount_end: NotRequired[
            "QuoteService.UpdateParamsLineStartsAtDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        line_ends_at: NotRequired[
            "QuoteService.UpdateParamsLineStartsAtLineEndsAt"
        ]
        """
        The timestamp the given line ends at.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "line_ends_at",
            "now",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `starts_at`.
        """

    class UpdateParamsLineStartsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class UpdateParamsLineStartsAtLineEndsAt(TypedDict):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class UpdateParamsLineTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "QuoteService.UpdateParamsLineTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class UpdateParamsLineTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired[Literal["defer", "include"]]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class UpdateParamsSubscriptionData(TypedDict):
        bill_on_acceptance: NotRequired[
            "Literal['']|QuoteService.UpdateParamsSubscriptionDataBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        billing_cycle_anchor: NotRequired["Literal['']|Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        description: NotRequired["Literal['']|str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        effective_date: NotRequired[
            "Literal['']|Literal['current_period_end']|int"
        ]
        """
        When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
        """
        end_behavior: NotRequired[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        prebilling: NotRequired[
            "Literal['']|QuoteService.UpdateParamsSubscriptionDataPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """
        trial_period_days: NotRequired["Literal['']|int"]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
        line_starts_at: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
        duration: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class UpdateParamsSubscriptionDataOverride(TypedDict):
        applies_to: (
            "QuoteService.UpdateParamsSubscriptionDataOverrideAppliesTo"
        )
        """
        Whether the override applies to an existing Subscription Schedule or a new Subscription Schedule.
        """
        bill_on_acceptance: NotRequired[
            "Literal['']|QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: NotRequired[str]
        """
        The customer the Subscription Data override applies to.
        """
        description: NotRequired["Literal['']|str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: NotRequired[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """

    class UpdateParamsSubscriptionDataOverrideAppliesTo(TypedDict):
        new_reference: NotRequired[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
        TypedDict,
    ):
        line_starts_at: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
        TypedDict,
    ):
        duration: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "QuoteService.UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired[int]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired[str]
        """
        The ID of a quote line.
        """
        index: NotRequired[int]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class UpdateParamsSubscriptionDataPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class UpdateParamsTransferData(TypedDict):
        amount: NotRequired[int]
        """
        The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        amount_percent: NotRequired[float]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    def list(
        self,
        params: "QuoteService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Quote]:
        """
        Returns a list of your quotes.
        """
        return cast(
            ListObject[Quote],
            self._request(
                "get",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "QuoteService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Quote]:
        """
        Returns a list of your quotes.
        """
        return cast(
            ListObject[Quote],
            await self._request_async(
                "get",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "QuoteService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "QuoteService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        quote: str,
        params: "QuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Retrieves the quote with the given ID.
        """
        return cast(
            Quote,
            self._request(
                "get",
                "/v1/quotes/{quote}".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        quote: str,
        params: "QuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Retrieves the quote with the given ID.
        """
        return cast(
            Quote,
            await self._request_async(
                "get",
                "/v1/quotes/{quote}".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        quote: str,
        params: "QuoteService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        A quote models prices and services for a customer.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        quote: str,
        params: "QuoteService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        A quote models prices and services for a customer.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def accept(
        self,
        quote: str,
        params: "QuoteService.AcceptParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Accepts the specified quote.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/accept".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def accept_async(
        self,
        quote: str,
        params: "QuoteService.AcceptParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Accepts the specified quote.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/accept".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        quote: str,
        params: "QuoteService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Cancels the quote.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/cancel".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        quote: str,
        params: "QuoteService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Cancels the quote.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/cancel".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def finalize_quote(
        self,
        quote: str,
        params: "QuoteService.FinalizeQuoteParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Finalizes the quote.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/finalize".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def finalize_quote_async(
        self,
        quote: str,
        params: "QuoteService.FinalizeQuoteParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Finalizes the quote.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/finalize".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_draft(
        self,
        quote: str,
        params: "QuoteService.MarkDraftParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Converts a stale quote to draft.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_draft_async(
        self,
        quote: str,
        params: "QuoteService.MarkDraftParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Converts a stale quote to draft.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_stale(
        self,
        quote: str,
        params: "QuoteService.MarkStaleParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_stale_async(
        self,
        quote: str,
        params: "QuoteService.MarkStaleParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reestimate(
        self,
        quote: str,
        params: "QuoteService.ReestimateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            Quote,
            self._request(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reestimate_async(
        self,
        quote: str,
        params: "QuoteService.ReestimateParams" = {},
        options: RequestOptions = {},
    ) -> Quote:
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            Quote,
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(quote),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def pdf(
        self,
        quote: str,
        params: "QuoteService.PdfParams" = {},
        options: RequestOptions = {},
    ) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            Any,
            self._request_stream(
                "get",
                "/v1/quotes/{quote}/pdf".format(quote=sanitize_id(quote)),
                base_address="files",
                params=params,
                options=options,
            ),
        )

    async def pdf_async(
        self,
        quote: str,
        params: "QuoteService.PdfParams" = {},
        options: RequestOptions = {},
    ) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            Any,
            await self._request_stream_async(
                "get",
                "/v1/quotes/{quote}/pdf".format(quote=sanitize_id(quote)),
                base_address="files",
                params=params,
                options=options,
            ),
        )

    def list_preview_invoice_lines(
        self,
        quote: str,
        preview_invoice: str,
        params: "QuoteService.ListPreviewInvoiceLinesParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject[InvoiceLineItem],
            self._request(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(quote),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_preview_invoice_lines_async(
        self,
        quote: str,
        preview_invoice: str,
        params: "QuoteService.ListPreviewInvoiceLinesParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject[InvoiceLineItem],
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(quote),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
