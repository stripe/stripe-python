# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class SubscriptionScheduleAmendParams(RequestOptions):
    amendments: NotRequired[List["SubscriptionScheduleAmendParamsAmendment"]]
    """
    Changes to apply to the phases of the subscription schedule, in the order provided.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    prebilling: NotRequired[
        "Literal['']|List[SubscriptionScheduleAmendParamsPrebilling]"
    ]
    """
    Provide any time periods to bill in advance.
    """
    proration_behavior: NotRequired[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    In cases where the amendment changes the currently active phase,
     specifies if and how to prorate at the time of the request.
    """
    schedule_settings: NotRequired[
        "SubscriptionScheduleAmendParamsScheduleSettings"
    ]
    """
    Changes to apply to the subscription schedule.
    """


class SubscriptionScheduleAmendParamsAmendment(TypedDict):
    amendment_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentAmendmentEnd"
    ]
    """
    Details to identify the end of the time range modified by the proposed change. If not supplied, the amendment is considered a point-in-time operation that only affects the exact timestamp at `amendment_start`, and a restricted set of attributes is supported on the amendment.
    """
    amendment_start: "SubscriptionScheduleAmendParamsAmendmentAmendmentStart"
    """
    Details to identify the earliest timestamp where the proposed change should take effect.
    """
    billing_cycle_anchor: NotRequired[Literal["amendment_start", "automatic"]]
    """
    For point-in-time amendments (having no `amendment_end`), this attribute lets you set or remove whether the subscription's billing cycle anchor is reset at the `amendment_start` timestamp.For time-span based amendments (having both `amendment_start` and `amendment_end`), the only value valid is `automatic`, which removes any previously configured billing cycle anchor resets scheduled to occur during the window of time spanned by the amendment.
    """
    billing_schedules_actions: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentBillingSchedulesAction"]
    ]
    """
    Actions to apply to the billing schedules.
    """
    discount_actions: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentDiscountAction"]
    ]
    """
    Changes to the coupons being redeemed or discounts being applied during the amendment time span.
    """
    effective_at: NotRequired[
        Literal["amendment_start", "billing_period_start"]
    ]
    """
    Configures how the subscription schedule handles billing for phase transitions.
    """
    item_actions: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentItemAction"]
    ]
    """
    Changes to the subscription items during the amendment time span.
    """
    metadata_actions: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentMetadataAction"]
    ]
    """
    Instructions for how to modify phase metadata
    """
    proration_behavior: NotRequired[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Changes to how Stripe handles prorations during the amendment time span. Affects if and how prorations are created when a future phase starts. In cases where the amendment changes the currently active phase, it is used to determine whether or how to prorate now, at the time of the request. Also supported as a point-in-time operation when `amendment_end` is `null`.
    """
    set_pause_collection: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentSetPauseCollection"
    ]
    """
    Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
    """
    set_schedule_end: NotRequired[Literal["amendment_end", "amendment_start"]]
    """
    Ends the subscription schedule early as dictated by either the accompanying amendment's start or end.
    """
    trial_settings: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentTrialSettings"
    ]
    """
    Settings related to subscription trials.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentEnd(TypedDict):
    discount_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentAmendmentEndDiscountEnd"
    ]
    """
    Use the `end` time of a given discount.
    """
    duration: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentAmendmentEndDuration"
    ]
    """
    Time span for the amendment starting from the `amendment_start`.
    """
    timestamp: NotRequired[int]
    """
    A precise Unix timestamp for the amendment to end. Must be after the `amendment_start`.
    """
    type: Literal[
        "discount_end",
        "duration",
        "schedule_end",
        "timestamp",
        "trial_end",
        "trial_start",
        "upcoming_invoice",
    ]
    """
    Select one of three ways to pass the `amendment_end`.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentEndDiscountEnd(
    TypedDict,
):
    discount: str
    """
    The ID of a specific discount.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentEndDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentStart(TypedDict):
    amendment_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentAmendmentStartAmendmentEnd"
    ]
    """
    Details of another amendment in the same array, immediately after which this amendment should begin.
    """
    discount_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentAmendmentStartDiscountEnd"
    ]
    """
    Use the `end` time of a given discount.
    """
    timestamp: NotRequired[int]
    """
    A precise Unix timestamp for the amendment to start.
    """
    type: Literal[
        "amendment_end",
        "discount_end",
        "now",
        "schedule_end",
        "timestamp",
        "trial_end",
        "trial_start",
        "upcoming_invoice",
    ]
    """
    Select one of three ways to pass the `amendment_start`.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentStartAmendmentEnd(
    TypedDict,
):
    index: int
    """
    The position of the previous amendment in the `amendments` array after which this amendment should begin. Indexes start from 0 and must be less than the index of the current amendment in the array.
    """


class SubscriptionScheduleAmendParamsAmendmentAmendmentStartDiscountEnd(
    TypedDict,
):
    discount: str
    """
    The ID of a specific discount.
    """


class SubscriptionScheduleAmendParamsAmendmentBillingSchedulesAction(
    TypedDict
):
    applies_to: NotRequired[
        List[
            "SubscriptionScheduleAmendParamsAmendmentBillingSchedulesActionAppliesTo"
        ]
    ]
    """
    Specify which subscription items the billing schedule applies to.
    """
    type: Literal["remove", "set"]
    """
    Select the action.
    """


class SubscriptionScheduleAmendParamsAmendmentBillingSchedulesActionAppliesTo(
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


class SubscriptionScheduleAmendParamsAmendmentDiscountAction(TypedDict):
    add: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentDiscountActionAdd"
    ]
    """
    Details of the discount to add.
    """
    remove: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentDiscountActionRemove"
    ]
    """
    Details of the discount to remove.
    """
    set: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentDiscountActionSet"
    ]
    """
    Details of the discount to replace the existing discounts with.
    """
    type: Literal["add", "remove", "set"]
    """
    Determines the type of discount action.
    """


class SubscriptionScheduleAmendParamsAmendmentDiscountActionAdd(TypedDict):
    coupon: NotRequired[str]
    """
    The coupon code to redeem.
    """
    discount: NotRequired[str]
    """
    An ID of an existing discount for a coupon that was already redeemed.
    """
    discount_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentDiscountActionAddDiscountEnd"
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


class SubscriptionScheduleAmendParamsAmendmentDiscountActionAddDiscountEnd(
    TypedDict,
):
    type: Literal["amendment_end"]
    """
    The type of calculation made to determine when the discount ends.
    """


class SubscriptionScheduleAmendParamsAmendmentDiscountActionRemove(TypedDict):
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


class SubscriptionScheduleAmendParamsAmendmentDiscountActionSet(TypedDict):
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


class SubscriptionScheduleAmendParamsAmendmentItemAction(TypedDict):
    add: NotRequired["SubscriptionScheduleAmendParamsAmendmentItemActionAdd"]
    """
    Details of the subscription item to add. If an item with the same `price` exists, it will be replaced by this new item. Otherwise, it adds the new item.
    """
    remove: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionRemove"
    ]
    """
    Details of the subscription item to remove.
    """
    set: NotRequired["SubscriptionScheduleAmendParamsAmendmentItemActionSet"]
    """
    Details of the subscription item to replace the existing items with. If an item with the `set[price]` already exists, the `items` array is not cleared. Instead, all of the other `set` properties that are passed in this request will replace the existing values for the configuration item.
    """
    type: Literal["add", "remove", "set"]
    """
    Determines the type of item action.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionAdd(TypedDict):
    discounts: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscount"]
    ]
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
    trial: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionAddTrial"
    ]
    """
    Options that configure the trial on the subscription item.
    """
    trial_offer: NotRequired[str]
    """
    The ID of the trial offer to apply to the configuration item.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscountDiscountEnd"
    ]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscountDiscountEnd(
    TypedDict,
):
    duration: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscountDiscountEndDuration"
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


class SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscountDiscountEndDuration(
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


class SubscriptionScheduleAmendParamsAmendmentItemActionAddTrial(TypedDict):
    converts_to: NotRequired[List[str]]
    """
    List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
    """
    type: Literal["free", "paid"]
    """
    Determines the type of trial for this item.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionRemove(TypedDict):
    price: str
    """
    ID of a price to remove.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionSet(TypedDict):
    discounts: NotRequired[
        List["SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscount"]
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
    trial: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionSetTrial"
    ]
    """
    If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
    """
    trial_offer: NotRequired[str]
    """
    The ID of the trial offer to apply to the configuration item.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscount(TypedDict):
    coupon: NotRequired[str]
    """
    ID of the coupon to create a new discount for.
    """
    discount: NotRequired[str]
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    discount_end: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscountDiscountEnd"
    ]
    """
    Details to determine how long the discount should be applied for.
    """
    promotion_code: NotRequired[str]
    """
    ID of the promotion code to create a new discount for.
    """


class SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscountDiscountEnd(
    TypedDict,
):
    duration: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscountDiscountEndDuration"
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


class SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscountDiscountEndDuration(
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


class SubscriptionScheduleAmendParamsAmendmentItemActionSetTrial(TypedDict):
    converts_to: NotRequired[List[str]]
    """
    List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial. Currently only supports at most 1 price ID.
    """
    type: Literal["free", "paid"]
    """
    Determines the type of trial for this item.
    """


class SubscriptionScheduleAmendParamsAmendmentMetadataAction(TypedDict):
    add: NotRequired[Dict[str, str]]
    """
    Key-value pairs to add to schedule phase metadata. These values will merge with existing schedule phase metadata.
    """
    remove: NotRequired[List[str]]
    """
    Keys to remove from schedule phase metadata.
    """
    set: NotRequired["Literal['']|Dict[str, str]"]
    """
    Key-value pairs to set as schedule phase metadata. Existing schedule phase metadata will be overwritten.
    """
    type: Literal["add", "remove", "set"]
    """
    Select one of three ways to update phase-level `metadata` on subscription schedules.
    """


class SubscriptionScheduleAmendParamsAmendmentSetPauseCollection(TypedDict):
    set: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentSetPauseCollectionSet"
    ]
    """
    Details of the pause_collection behavior to apply to the amendment.
    """
    type: Literal["remove", "set"]
    """
    Determines the type of the pause_collection amendment.
    """


class SubscriptionScheduleAmendParamsAmendmentSetPauseCollectionSet(TypedDict):
    behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
    """
    The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
    """


class SubscriptionScheduleAmendParamsAmendmentTrialSettings(TypedDict):
    end_behavior: NotRequired[
        "SubscriptionScheduleAmendParamsAmendmentTrialSettingsEndBehavior"
    ]
    """
    Defines how the subscription should behave when a trial ends.
    """


class SubscriptionScheduleAmendParamsAmendmentTrialSettingsEndBehavior(
    TypedDict,
):
    prorate_up_front: NotRequired[Literal["defer", "include"]]
    """
    Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
    """


class SubscriptionScheduleAmendParamsPrebilling(TypedDict):
    bill_from: NotRequired["SubscriptionScheduleAmendParamsPrebillingBillFrom"]
    """
    The beginning of the prebilled time period. The default value is `now`.
    """
    bill_until: NotRequired[
        "SubscriptionScheduleAmendParamsPrebillingBillUntil"
    ]
    """
    The end of the prebilled time period.
    """
    invoice_at: NotRequired[Literal["now"]]
    """
    When the prebilling invoice should be created. The default value is `now`.
    """
    update_behavior: NotRequired[Literal["prebill", "reset"]]
    """
    Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
    """


class SubscriptionScheduleAmendParamsPrebillingBillFrom(TypedDict):
    amendment_start: NotRequired[
        "SubscriptionScheduleAmendParamsPrebillingBillFromAmendmentStart"
    ]
    """
    Start the prebilled period when a specified amendment begins.
    """
    timestamp: NotRequired[int]
    """
    Start the prebilled period at a precise integer timestamp, starting from the Unix epoch.
    """
    type: Literal["amendment_start", "now", "timestamp"]
    """
    Select one of several ways to pass the `bill_from` value.
    """


class SubscriptionScheduleAmendParamsPrebillingBillFromAmendmentStart(
    TypedDict,
):
    index: int
    """
    The position of the amendment in the `amendments` array with which prebilling should begin. Indexes start from 0 and must be less than the total number of supplied amendments.
    """


class SubscriptionScheduleAmendParamsPrebillingBillUntil(TypedDict):
    amendment_end: NotRequired[
        "SubscriptionScheduleAmendParamsPrebillingBillUntilAmendmentEnd"
    ]
    """
    End the prebilled period when a specified amendment ends.
    """
    duration: NotRequired[
        "SubscriptionScheduleAmendParamsPrebillingBillUntilDuration"
    ]
    """
    Time span for prebilling, starting from `bill_from`.
    """
    timestamp: NotRequired[int]
    """
    End the prebilled period at a precise integer timestamp, starting from the Unix epoch.
    """
    type: Literal["amendment_end", "duration", "schedule_end", "timestamp"]
    """
    Select one of several ways to pass the `bill_until` value.
    """


class SubscriptionScheduleAmendParamsPrebillingBillUntilAmendmentEnd(
    TypedDict
):
    index: int
    """
    The position of the amendment in the `amendments` array at which prebilling should end. Indexes start from 0 and must be less than the total number of supplied amendments.
    """


class SubscriptionScheduleAmendParamsPrebillingBillUntilDuration(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """


class SubscriptionScheduleAmendParamsScheduleSettings(TypedDict):
    end_behavior: NotRequired[Literal["cancel", "release"]]
    """
    Behavior of the subscription schedule and underlying subscription when it ends.
    """
