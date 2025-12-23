# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class QuoteCreateParams(RequestOptions):
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
    automatic_tax: NotRequired["QuoteCreateParamsAutomaticTax"]
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
    discounts: NotRequired["Literal['']|List[QuoteCreateParamsDiscount]"]
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
    from_quote: NotRequired["QuoteCreateParamsFromQuote"]
    """
    Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
    """
    header: NotRequired["Literal['']|str"]
    """
    A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    """
    invoice_settings: NotRequired["QuoteCreateParamsInvoiceSettings"]
    """
    All invoices will be billed using the specified settings.
    """
    line_items: NotRequired[List["QuoteCreateParamsLineItem"]]
    """
    A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
    """
    lines: NotRequired[List["QuoteCreateParamsLine"]]
    """
    A list of [quote lines](https://docs.stripe.com/api/quote_lines) on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    on_behalf_of: NotRequired["Literal['']|str"]
    """
    The account on behalf of which to charge.
    """
    subscription_data: NotRequired["QuoteCreateParamsSubscriptionData"]
    """
    When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    """
    subscription_data_overrides: NotRequired[
        List["QuoteCreateParamsSubscriptionDataOverride"]
    ]
    """
    List representing overrides for `subscription_data` configurations for specific subscription schedules.
    """
    test_clock: NotRequired[str]
    """
    ID of the test clock to attach to the quote.
    """
    transfer_data: NotRequired["Literal['']|QuoteCreateParamsTransferData"]
    """
    The data with which to automatically create a Transfer for each of the invoices.
    """


class QuoteCreateParamsAutomaticTax(TypedDict):
    enabled: bool
    """
    Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
    """
    liability: NotRequired["QuoteCreateParamsAutomaticTaxLiability"]
    """
    The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
    """


class QuoteCreateParamsAutomaticTaxLiability(TypedDict):
    account: NotRequired[str]
    """
    The connected account being referenced when `type` is `account`.
    """
    type: Literal["account", "self"]
    """
    Type of the account referenced in the request.
    """


class QuoteCreateParamsDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired["QuoteCreateParamsDiscountDiscountEnd"]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class QuoteCreateParamsDiscountDiscountEnd(TypedDict):
    duration: NotRequired["QuoteCreateParamsDiscountDiscountEndDuration"]
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


class QuoteCreateParamsDiscountDiscountEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class QuoteCreateParamsFromQuote(TypedDict):
    is_revision: NotRequired[bool]
    """
    Whether this quote is a revision of the previous quote.
    """
    quote: str
    """
    The `id` of the quote that will be cloned.
    """


class QuoteCreateParamsInvoiceSettings(TypedDict):
    days_until_due: NotRequired[int]
    """
    Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
    """
    issuer: NotRequired["QuoteCreateParamsInvoiceSettingsIssuer"]
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """


class QuoteCreateParamsInvoiceSettingsIssuer(TypedDict):
    account: NotRequired[str]
    """
    The connected account being referenced when `type` is `account`.
    """
    type: Literal["account", "self"]
    """
    Type of the account referenced in the request.
    """


class QuoteCreateParamsLineItem(TypedDict):
    discounts: NotRequired[
        "Literal['']|List[QuoteCreateParamsLineItemDiscount]"
    ]
    """
    The discounts applied to this line item.
    """
    price: NotRequired[str]
    """
    The ID of the price object. One of `price` or `price_data` is required.
    """
    price_data: NotRequired["QuoteCreateParamsLineItemPriceData"]
    """
    Data used to generate a new [Price](https://docs.stripe.com/api/prices) object inline. One of `price` or `price_data` is required.
    """
    quantity: NotRequired[int]
    """
    The quantity of the line item.
    """
    tax_rates: NotRequired["Literal['']|List[str]"]
    """
    The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
    """


class QuoteCreateParamsLineItemDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired["QuoteCreateParamsLineItemDiscountDiscountEnd"]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class QuoteCreateParamsLineItemDiscountDiscountEnd(TypedDict):
    duration: NotRequired[
        "QuoteCreateParamsLineItemDiscountDiscountEndDuration"
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


class QuoteCreateParamsLineItemDiscountDiscountEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class QuoteCreateParamsLineItemPriceData(TypedDict):
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    product: str
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
    """
    recurring: NotRequired["QuoteCreateParamsLineItemPriceDataRecurring"]
    """
    The recurring components of a price such as `interval` and `interval_count`.
    """
    tax_behavior: NotRequired[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Only required if a [default tax behavior](https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """
    unit_amount: NotRequired[int]
    """
    A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
    """
    unit_amount_decimal: NotRequired[str]
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
    """


class QuoteCreateParamsLineItemPriceDataRecurring(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies billing frequency. Either `day`, `week`, `month` or `year`.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
    """


class QuoteCreateParamsLine(TypedDict):
    actions: NotRequired[List["QuoteCreateParamsLineAction"]]
    """
    An array of operations the quote line performs.
    """
    applies_to: NotRequired["QuoteCreateParamsLineAppliesTo"]
    """
    Details to identify the subscription schedule the quote line applies to.
    """
    billing_cycle_anchor: NotRequired[Literal["automatic", "line_starts_at"]]
    """
    For point-in-time quote lines (having no `ends_at` timestamp), this attribute lets you set or remove whether the subscription's billing cycle anchor is reset at the Quote Line `starts_at` timestamp.For time-span based quote lines (having both `starts_at` and `ends_at`), the only valid value is `automatic`, which removes any previously configured billing cycle anchor resets during the window of time spanning the quote line.
    """
    cancel_subscription_schedule: NotRequired[
        "QuoteCreateParamsLineCancelSubscriptionSchedule"
    ]
    """
    A point-in-time operation that cancels an existing subscription schedule at the line's starts_at timestamp. Currently only compatible with `quote_acceptance_date` for `starts_at`. When using cancel_subscription_schedule, the subscription schedule on the quote remains unalterable, except for modifications to the metadata, collection_method or invoice_settings.
    """
    effective_at: NotRequired[Literal["billing_period_start", "line_start"]]
    """
    Configures how the quote handles billing for line transitions.
    """
    ends_at: NotRequired["QuoteCreateParamsLineEndsAt"]
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
        "QuoteCreateParamsLineSetPauseCollection"
    ]
    """
    Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
    """
    set_schedule_end: NotRequired[Literal["line_ends_at", "line_starts_at"]]
    """
    Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
    """
    starts_at: NotRequired["QuoteCreateParamsLineStartsAt"]
    """
    Details to identify the earliest timestamp where the proposed change should take effect.
    """
    trial_settings: NotRequired["QuoteCreateParamsLineTrialSettings"]
    """
    Settings related to subscription trials.
    """


class QuoteCreateParamsLineAction(TypedDict):
    add_discount: NotRequired["QuoteCreateParamsLineActionAddDiscount"]
    """
    Details for the `add_discount` type.
    """
    add_item: NotRequired["QuoteCreateParamsLineActionAddItem"]
    """
    Details for the `add_item` type.
    """
    add_metadata: NotRequired[Dict[str, str]]
    """
    Details for the `add_metadata` type: specify a hash of key-value pairs.
    """
    remove_discount: NotRequired["QuoteCreateParamsLineActionRemoveDiscount"]
    """
    Details for the `remove_discount` type.
    """
    remove_item: NotRequired["QuoteCreateParamsLineActionRemoveItem"]
    """
    Details for the `remove_item` type.
    """
    remove_metadata: NotRequired[List[str]]
    """
    Details for the `remove_metadata` type: specify an array of metadata keys.
    """
    set_discounts: NotRequired[List["QuoteCreateParamsLineActionSetDiscount"]]
    """
    Details for the `set_discounts` type.
    """
    set_items: NotRequired[List["QuoteCreateParamsLineActionSetItem"]]
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


class QuoteCreateParamsLineActionAddDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    The coupon code to redeem.
    """
    discount: NotRequired[str]
    """
    An ID of an existing discount for a coupon that was already redeemed.
    """
    discount_end: NotRequired[
        "QuoteCreateParamsLineActionAddDiscountDiscountEnd"
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


class QuoteCreateParamsLineActionAddDiscountDiscountEnd(TypedDict):
    type: Literal["line_ends_at"]
    """
    The type of calculation made to determine when the discount ends.
    """


class QuoteCreateParamsLineActionAddItem(TypedDict):
    discounts: NotRequired[List["QuoteCreateParamsLineActionAddItemDiscount"]]
    """
    The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
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
    trial: NotRequired["QuoteCreateParamsLineActionAddItemTrial"]
    """
    Options that configure the trial on the subscription item.
    """
    trial_offer: NotRequired[str]
    """
    The ID of the trial offer to apply to the configuration item.
    """


class QuoteCreateParamsLineActionAddItemDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired[
        "QuoteCreateParamsLineActionAddItemDiscountDiscountEnd"
    ]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class QuoteCreateParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
    duration: NotRequired[
        "QuoteCreateParamsLineActionAddItemDiscountDiscountEndDuration"
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


class QuoteCreateParamsLineActionAddItemDiscountDiscountEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class QuoteCreateParamsLineActionAddItemTrial(TypedDict):
    converts_to: NotRequired[List[str]]
    """
    List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
    """
    type: Literal["free", "paid"]
    """
    Determines the type of trial for this item.
    """


class QuoteCreateParamsLineActionRemoveDiscount(TypedDict):
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


class QuoteCreateParamsLineActionRemoveItem(TypedDict):
    price: str
    """
    ID of a price to remove.
    """


class QuoteCreateParamsLineActionSetDiscount(TypedDict):
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


class QuoteCreateParamsLineActionSetItem(TypedDict):
    discounts: NotRequired[List["QuoteCreateParamsLineActionSetItemDiscount"]]
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
    trial: NotRequired["QuoteCreateParamsLineActionSetItemTrial"]
    """
    If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
    """
    trial_offer: NotRequired[str]
    """
    The ID of the trial offer to apply to the configuration item.
    """


class QuoteCreateParamsLineActionSetItemDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired[
        "QuoteCreateParamsLineActionSetItemDiscountDiscountEnd"
    ]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class QuoteCreateParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
    duration: NotRequired[
        "QuoteCreateParamsLineActionSetItemDiscountDiscountEndDuration"
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


class QuoteCreateParamsLineActionSetItemDiscountDiscountEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class QuoteCreateParamsLineActionSetItemTrial(TypedDict):
    converts_to: NotRequired[List[str]]
    """
    List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
    """
    type: Literal["free", "paid"]
    """
    Determines the type of trial for this item.
    """


class QuoteCreateParamsLineAppliesTo(TypedDict):
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


class QuoteCreateParamsLineCancelSubscriptionSchedule(TypedDict):
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


class QuoteCreateParamsLineEndsAt(TypedDict):
    discount_end: NotRequired["QuoteCreateParamsLineEndsAtDiscountEnd"]
    """
    Use the `end` time of a given discount.
    """
    duration: NotRequired["QuoteCreateParamsLineEndsAtDuration"]
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


class QuoteCreateParamsLineEndsAtDiscountEnd(TypedDict):
    discount: str
    """
    The ID of a specific discount.
    """


class QuoteCreateParamsLineEndsAtDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class QuoteCreateParamsLineSetPauseCollection(TypedDict):
    set: NotRequired["QuoteCreateParamsLineSetPauseCollectionSet"]
    """
    Details of the pause_collection behavior to apply to the amendment.
    """
    type: Literal["remove", "set"]
    """
    Determines the type of the pause_collection amendment.
    """


class QuoteCreateParamsLineSetPauseCollectionSet(TypedDict):
    behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
    """
    The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
    """


class QuoteCreateParamsLineStartsAt(TypedDict):
    discount_end: NotRequired["QuoteCreateParamsLineStartsAtDiscountEnd"]
    """
    Use the `end` time of a given discount.
    """
    line_ends_at: NotRequired["QuoteCreateParamsLineStartsAtLineEndsAt"]
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


class QuoteCreateParamsLineStartsAtDiscountEnd(TypedDict):
    discount: str
    """
    The ID of a specific discount.
    """


class QuoteCreateParamsLineStartsAtLineEndsAt(TypedDict):
    index: NotRequired[int]
    """
    The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
    """


class QuoteCreateParamsLineTrialSettings(TypedDict):
    end_behavior: NotRequired["QuoteCreateParamsLineTrialSettingsEndBehavior"]
    """
    Defines how the subscription should behave when a trial ends.
    """


class QuoteCreateParamsLineTrialSettingsEndBehavior(TypedDict):
    prorate_up_front: NotRequired[Literal["defer", "include"]]
    """
    Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
    """


class QuoteCreateParamsSubscriptionData(TypedDict):
    bill_on_acceptance: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptance"
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
    billing_mode: NotRequired["QuoteCreateParamsSubscriptionDataBillingMode"]
    """
    Controls how prorations and invoices for subscriptions are calculated and orchestrated.
    """
    billing_schedules: NotRequired[
        List["QuoteCreateParamsSubscriptionDataBillingSchedule"]
    ]
    """
    Billing schedules that will be applied to the subscription or subscription schedule created when the quote is accepted.
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
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
    """
    phase_effective_at: NotRequired[
        Literal["billing_period_start", "phase_start"]
    ]
    """
    Configures how the subscription schedule handles billing for phase transitions when the quote is accepted.
    """
    prebilling: NotRequired[
        "Literal['']|QuoteCreateParamsSubscriptionDataPrebilling"
    ]
    """
    If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
    """
    proration_behavior: NotRequired[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://docs.stripe.com/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

    When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

    Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

    Prorations can be disabled by passing `none`.
    """
    trial_period_days: NotRequired["Literal['']|int"]
    """
    Integer representing the number of trial period days before the customer is charged for the first time.
    """


class QuoteCreateParamsSubscriptionDataBillOnAcceptance(TypedDict):
    bill_from: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillFrom"
    ]
    """
    The start of the period to bill from when the Quote is accepted.
    """
    bill_until: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntil"
    ]
    """
    The end of the period to bill until when the Quote is accepted.
    """


class QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
    line_starts_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt"
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


class QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
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


class QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
    duration: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration"
    ]
    """
    Details of the duration over which to bill.
    """
    line_ends_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt"
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


class QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
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


class QuoteCreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
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


class QuoteCreateParamsSubscriptionDataBillingMode(TypedDict):
    flexible: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillingModeFlexible"
    ]
    """
    Configure behavior for flexible billing mode.
    """
    type: Literal["classic", "flexible"]
    """
    Controls the calculation and orchestration of prorations and invoices for subscriptions. If no value is passed, the default is `flexible`.
    """


class QuoteCreateParamsSubscriptionDataBillingModeFlexible(TypedDict):
    proration_discounts: NotRequired[Literal["included", "itemized"]]
    """
    Controls how invoices and invoice items display proration amounts and discount amounts.
    """


class QuoteCreateParamsSubscriptionDataBillingSchedule(TypedDict):
    applies_to: NotRequired[
        List["QuoteCreateParamsSubscriptionDataBillingScheduleAppliesTo"]
    ]
    """
    Configure billing schedule differently for individual subscription items.
    """
    bill_from: "QuoteCreateParamsSubscriptionDataBillingScheduleBillFrom"
    """
    The start of the period to bill from when the Quote is accepted.
    """
    bill_until: "QuoteCreateParamsSubscriptionDataBillingScheduleBillUntil"
    """
    The end of the period to bill until when the Quote is accepted.
    """
    key: NotRequired[str]
    """
    Specify a key for the billing schedule. Must be unique to this field, alphanumeric, and up to 200 characters. If not provided, a unique key will be generated.
    """


class QuoteCreateParamsSubscriptionDataBillingScheduleAppliesTo(TypedDict):
    price: NotRequired[str]
    """
    The ID of the price object.
    """
    type: Literal["price"]
    """
    Controls which subscription items the billing schedule applies to.
    """


class QuoteCreateParamsSubscriptionDataBillingScheduleBillFrom(TypedDict):
    line_starts_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillingScheduleBillFromLineStartsAt"
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


class QuoteCreateParamsSubscriptionDataBillingScheduleBillFromLineStartsAt(
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


class QuoteCreateParamsSubscriptionDataBillingScheduleBillUntil(TypedDict):
    duration: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillingScheduleBillUntilDuration"
    ]
    """
    Details of the duration over which to bill.
    """
    line_ends_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataBillingScheduleBillUntilLineEndsAt"
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


class QuoteCreateParamsSubscriptionDataBillingScheduleBillUntilDuration(
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


class QuoteCreateParamsSubscriptionDataBillingScheduleBillUntilLineEndsAt(
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


class QuoteCreateParamsSubscriptionDataPrebilling(TypedDict):
    iterations: int
    """
    This is used to determine the number of billing cycles to prebill.
    """


class QuoteCreateParamsSubscriptionDataOverride(TypedDict):
    applies_to: "QuoteCreateParamsSubscriptionDataOverrideAppliesTo"
    """
    Whether the override applies to an existing Subscription Schedule or a new Subscription Schedule.
    """
    bill_on_acceptance: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptance"
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
    billing_schedules: NotRequired[
        List["QuoteCreateParamsSubscriptionDataOverrideBillingSchedule"]
    ]
    """
    Billing schedules that will be applied to the subscription or subscription schedule created when the quote is accepted.
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
    phase_effective_at: NotRequired[
        Literal["billing_period_start", "phase_start"]
    ]
    """
    Configures how the subscription schedule handles billing for phase transitions when the quote is accepted.
    """
    proration_behavior: NotRequired[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://docs.stripe.com/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

    When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

    Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

    Prorations can be disabled by passing `none`.
    """


class QuoteCreateParamsSubscriptionDataOverrideAppliesTo(TypedDict):
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


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
    bill_from: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom"
    ]
    """
    The start of the period to bill from when the Quote is accepted.
    """
    bill_until: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil"
    ]
    """
    The end of the period to bill until when the Quote is accepted.
    """


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
    TypedDict,
):
    line_starts_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt"
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


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
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


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
    TypedDict,
):
    duration: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration"
    ]
    """
    Details of the duration over which to bill.
    """
    line_ends_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt"
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


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
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


class QuoteCreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
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


class QuoteCreateParamsSubscriptionDataOverrideBillingSchedule(TypedDict):
    applies_to: NotRequired[
        List[
            "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleAppliesTo"
        ]
    ]
    """
    Configure billing schedule differently for individual subscription items.
    """
    bill_from: (
        "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFrom"
    )
    """
    The start of the period to bill from when the Quote is accepted.
    """
    bill_until: (
        "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntil"
    )
    """
    The end of the period to bill until when the Quote is accepted.
    """
    key: NotRequired[str]
    """
    Specify a key for the billing schedule. Must be unique to this field, alphanumeric, and up to 200 characters. If not provided, a unique key will be generated.
    """


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleAppliesTo(
    TypedDict,
):
    price: NotRequired[str]
    """
    The ID of the price object.
    """
    type: Literal["price"]
    """
    Controls which subscription items the billing schedule applies to.
    """


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFrom(
    TypedDict,
):
    line_starts_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFromLineStartsAt"
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


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFromLineStartsAt(
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


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntil(
    TypedDict,
):
    duration: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntilDuration"
    ]
    """
    Details of the duration over which to bill.
    """
    line_ends_at: NotRequired[
        "QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntilLineEndsAt"
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


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntilDuration(
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


class QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillUntilLineEndsAt(
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


class QuoteCreateParamsTransferData(TypedDict):
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
