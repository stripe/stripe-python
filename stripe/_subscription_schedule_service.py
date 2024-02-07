# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._subscription_schedule import SubscriptionSchedule
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class SubscriptionScheduleService(StripeService):
    class AmendParams(TypedDict):
        amendments: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendment]"
        ]
        """
        Changes to apply to the phases of the subscription schedule, in the order provided.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        prebilling: NotRequired[
            "Literal['']|List[SubscriptionScheduleService.AmendParamsPrebilling]"
        ]
        """
        Provide any time periods to bill in advance.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        In cases where the amendment changes the currently active phase,
         specifies if and how to prorate at the time of the request.
        """
        schedule_settings: NotRequired[
            "SubscriptionScheduleService.AmendParamsScheduleSettings"
        ]
        """
        Changes to apply to the subscription schedule.
        """

    class AmendParamsAmendment(TypedDict):
        amendment_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentAmendmentEnd"
        ]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the amendment is considered a point-in-time operation that only affects the exact timestamp at `amendment_start`, and a restricted set of attributes is supported on the amendment.
        """
        amendment_start: "SubscriptionScheduleService.AmendParamsAmendmentAmendmentStart"
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['amendment_start', 'automatic']"
        ]
        """
        For a point-in-time amendment, this attribute lets you set or update whether the subscription's billing cycle anchor is reset at the `amendment_start` timestamp.
        """
        discount_actions: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendmentDiscountAction]"
        ]
        """
        Changes to the coupons being redeemed or discounts being applied during the amendment time span.
        """
        item_actions: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendmentItemAction]"
        ]
        """
        Changes to the subscription items during the amendment time span.
        """
        metadata_actions: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendmentMetadataAction]"
        ]
        """
        Instructions for how to modify phase metadata
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Changes to how Stripe handles prorations during the amendment time span. Affects if and how prorations are created when a future phase starts. In cases where the amendment changes the currently active phase, it is used to determine whether or how to prorate now, at the time of the request. Also supported as a point-in-time operation when `amendment_end` is `null`.
        """
        set_pause_collection: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            "Literal['amendment_end', 'amendment_start']"
        ]
        """
        Ends the subscription schedule early as dictated by either the accompanying amendment's start or end.
        """
        trial_settings: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class AmendParamsAmendmentAmendmentEnd(TypedDict):
        discount_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentAmendmentEndDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentAmendmentEndDuration"
        ]
        """
        Time span for the amendment starting from the `amendment_start`.
        """
        timestamp: NotRequired["int"]
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

    class AmendParamsAmendmentAmendmentEndDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class AmendParamsAmendmentAmendmentEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class AmendParamsAmendmentAmendmentStart(TypedDict):
        amendment_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentAmendmentStartAmendmentEnd"
        ]
        """
        Details of another amendment in the same array, immediately after which this amendment should begin.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentAmendmentStartDiscountEnd"
        ]
        """
        Use the `end` time of a given discount.
        """
        timestamp: NotRequired["int"]
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

    class AmendParamsAmendmentAmendmentStartAmendmentEnd(TypedDict):
        index: int
        """
        The position of the previous amendment in the `amendments` array after which this amendment should begin. Indexes start from 0 and must be less than the index of the current amendment in the array.
        """

    class AmendParamsAmendmentAmendmentStartDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class AmendParamsAmendmentDiscountAction(TypedDict):
        add: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentDiscountActionAdd"
        ]
        """
        Details of the discount to add.
        """
        remove: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentDiscountActionRemove"
        ]
        """
        Details of the discount to remove.
        """
        set: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentDiscountActionSet"
        ]
        """
        Details of the discount to replace the existing discounts with.
        """
        type: Literal["add", "remove", "set"]
        """
        Determines the type of discount action.
        """

    class AmendParamsAmendmentDiscountActionAdd(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to redeem.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentDiscountActionAddDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired["int"]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The promotion code to redeem.
        """

    class AmendParamsAmendmentDiscountActionAddDiscountEnd(TypedDict):
        type: Literal["amendment_end"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class AmendParamsAmendmentDiscountActionRemove(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired["str"]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class AmendParamsAmendmentDiscountActionSet(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired["str"]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class AmendParamsAmendmentItemAction(TypedDict):
        add: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionAdd"
        ]
        """
        Details of the subscription item to add. If an item with the same `price` exists, it will be replaced by this new item. Otherwise, it adds the new item.
        """
        remove: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionRemove"
        ]
        """
        Details of the subscription item to remove.
        """
        set: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionSet"
        ]
        """
        Details of the subscription item to replace the existing items with. If an item with the `set[price]` already exists, the `items` array is not cleared. Instead, all of the other `set` properties that are passed in this request will replace the existing values for the configuration item.
        """
        type: Literal["add", "remove", "set"]
        """
        Determines the type of item action.
        """

    class AmendParamsAmendmentItemActionAdd(TypedDict):
        discounts: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendmentItemActionAddDiscount]"
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["List[str]"]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionAddTrial"
        ]
        """
        Options that configure the trial on the subscription item.
        """

    class AmendParamsAmendmentItemActionAddDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class AmendParamsAmendmentItemActionAddDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionAddDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class AmendParamsAmendmentItemActionAddDiscountDiscountEndDuration(
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

    class AmendParamsAmendmentItemActionAddTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class AmendParamsAmendmentItemActionRemove(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class AmendParamsAmendmentItemActionSet(TypedDict):
        discounts: NotRequired[
            "List[SubscriptionScheduleService.AmendParamsAmendmentItemActionSetDiscount]"
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired["List[str]"]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionSetTrial"
        ]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class AmendParamsAmendmentItemActionSetDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionSetDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class AmendParamsAmendmentItemActionSetDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentItemActionSetDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class AmendParamsAmendmentItemActionSetDiscountDiscountEndDuration(
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

    class AmendParamsAmendmentItemActionSetTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class AmendParamsAmendmentMetadataAction(TypedDict):
        add: NotRequired["Dict[str, str]"]
        """
        Key-value pairs to add to schedule phase metadata. These values will merge with existing schedule phase metadata.
        """
        remove: NotRequired["List[str]"]
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

    class AmendParamsAmendmentSetPauseCollection(TypedDict):
        set: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentSetPauseCollectionSet"
        ]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class AmendParamsAmendmentSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class AmendParamsAmendmentTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "SubscriptionScheduleService.AmendParamsAmendmentTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class AmendParamsAmendmentTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class AmendParamsPrebilling(TypedDict):
        bill_from: NotRequired[
            "SubscriptionScheduleService.AmendParamsPrebillingBillFrom"
        ]
        """
        The beginning of the prebilled time period. The default value is `now`.
        """
        bill_until: NotRequired[
            "SubscriptionScheduleService.AmendParamsPrebillingBillUntil"
        ]
        """
        The end of the prebilled time period.
        """
        invoice_at: NotRequired["Literal['now']"]
        """
        When the prebilling invoice should be created. The default value is `now`.
        """
        update_behavior: NotRequired["Literal['prebill', 'reset']"]
        """
        Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
        """

    class AmendParamsPrebillingBillFrom(TypedDict):
        amendment_start: NotRequired[
            "SubscriptionScheduleService.AmendParamsPrebillingBillFromAmendmentStart"
        ]
        """
        Start the prebilled period when a specified amendment begins.
        """
        timestamp: NotRequired["int"]
        """
        Start the prebilled period at a precise integer timestamp, starting from the Unix epoch.
        """
        type: Literal["amendment_start", "now", "timestamp"]
        """
        Select one of several ways to pass the `bill_from` value.
        """

    class AmendParamsPrebillingBillFromAmendmentStart(TypedDict):
        index: int
        """
        The position of the amendment in the `amendments` array with which prebilling should begin. Indexes start from 0 and must be less than the total number of supplied amendments.
        """

    class AmendParamsPrebillingBillUntil(TypedDict):
        amendment_end: NotRequired[
            "SubscriptionScheduleService.AmendParamsPrebillingBillUntilAmendmentEnd"
        ]
        """
        End the prebilled period when a specified amendment ends.
        """
        duration: NotRequired[
            "SubscriptionScheduleService.AmendParamsPrebillingBillUntilDuration"
        ]
        """
        Time span for prebilling, starting from `bill_from`.
        """
        timestamp: NotRequired["int"]
        """
        End the prebilled period at a precise integer timestamp, starting from the Unix epoch.
        """
        type: Literal["amendment_end", "duration", "schedule_end", "timestamp"]
        """
        Select one of several ways to pass the `bill_until` value.
        """

    class AmendParamsPrebillingBillUntilAmendmentEnd(TypedDict):
        index: int
        """
        The position of the amendment in the `amendments` array at which prebilling should end. Indexes start from 0 and must be less than the total number of supplied amendments.
        """

    class AmendParamsPrebillingBillUntilDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class AmendParamsScheduleSettings(TypedDict):
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """

    class CancelParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice_now: NotRequired["bool"]
        """
        If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`.
        """
        prorate: NotRequired["bool"]
        """
        If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`.
        """

    class CreateParams(TypedDict):
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: NotRequired["str"]
        """
        The identifier of the customer to create the subscription schedule for.
        """
        default_settings: NotRequired[
            "SubscriptionScheduleService.CreateParamsDefaultSettings"
        ]
        """
        Object representing the subscription schedule's default settings.
        """
        end_behavior: NotRequired[
            "Literal['cancel', 'none', 'release', 'renew']"
        ]
        """
        Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        from_subscription: NotRequired["str"]
        """
        Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        phases: NotRequired[
            "List[SubscriptionScheduleService.CreateParamsPhase]"
        ]
        """
        List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.
        """
        prebilling: NotRequired[
            "SubscriptionScheduleService.CreateParamsPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed now.
        """
        start_date: NotRequired["int|Literal['now']"]
        """
        When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.
        """

    class CreateParamsDefaultSettings(TypedDict):
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
        """
        automatic_tax: NotRequired[
            "SubscriptionScheduleService.CreateParamsDefaultSettingsAutomaticTax"
        ]
        """
        Default settings for automatic tax computation.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'phase_start']"
        ]
        """
        Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.CreateParamsDefaultSettingsBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        default_payment_method: NotRequired["str"]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        description: NotRequired["Literal['']|str"]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        invoice_settings: NotRequired[
            "SubscriptionScheduleService.CreateParamsDefaultSettingsInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge, for each of the associated subscription's invoices.
        """
        transfer_data: NotRequired[
            "Literal['']|SubscriptionScheduleService.CreateParamsDefaultSettingsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the associated subscription's invoices.
        """

    class CreateParamsDefaultSettingsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
        """
        liability: NotRequired[
            "SubscriptionScheduleService.CreateParamsDefaultSettingsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class CreateParamsDefaultSettingsAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsDefaultSettingsBillingThresholds(TypedDict):
        amount_gte: NotRequired["int"]
        """
        Monetary threshold that triggers the subscription to advance to a new billing period
        """
        reset_billing_cycle_anchor: NotRequired["bool"]
        """
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
        """

    class CreateParamsDefaultSettingsInvoiceSettings(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with the subscription schedule. Will be set on invoices generated by the subscription schedule.
        """
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `collection_method=charge_automatically`.
        """
        issuer: NotRequired[
            "SubscriptionScheduleService.CreateParamsDefaultSettingsInvoiceSettingsIssuer"
        ]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class CreateParamsDefaultSettingsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsDefaultSettingsTransferData(TypedDict):
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class CreateParamsPhase(TypedDict):
        add_invoice_items: NotRequired[
            "List[SubscriptionScheduleService.CreateParamsPhaseAddInvoiceItem]"
        ]
        """
        A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.
        """
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
        """
        automatic_tax: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseAutomaticTax"
        ]
        """
        Automatic tax settings for this phase.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'phase_start']"
        ]
        """
        Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.CreateParamsPhaseBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        coupon: NotRequired["str"]
        """
        The identifier of the coupon to apply to this phase of the subscription schedule.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        default_payment_method: NotRequired["str"]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
        """
        description: NotRequired["Literal['']|str"]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        discounts: NotRequired[
            "Literal['']|List[SubscriptionScheduleService.CreateParamsPhaseDiscount]"
        ]
        """
        The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription's customer. Pass an empty string to avoid inheriting any discounts.
        """
        end_date: NotRequired["int"]
        """
        The date at which this phase of the subscription schedule ends. If set, `iterations` must not be set.
        """
        invoice_settings: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        items: List["SubscriptionScheduleService.CreateParamsPhaseItem"]
        """
        List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.
        """
        iterations: NotRequired["int"]
        """
        Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription's `metadata`. Individual keys in the subscription's `metadata` can be unset by posting an empty value to them in the phase's `metadata`. To unset all keys in the subscription's `metadata`, update the subscription directly or unset every key individually from the phase's `metadata`.
        """
        on_behalf_of: NotRequired["str"]
        """
        The account on behalf of which to charge, for each of the associated subscription's invoices.
        """
        pause_collection: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhasePauseCollection"
        ]
        """
        If specified, payment collection for this subscription will be paused.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Whether the subscription schedule will create [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when transitioning to this phase. The default value is `create_prorations`. This setting controls prorations when a phase is started asynchronously and it is persisted as a field on the phase. It's different from the request-level [proration_behavior](https://stripe.com/docs/api/subscription_schedules/update#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration of the current phase.
        """
        transfer_data: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the associated subscription's invoices.
        """
        trial: NotRequired["bool"]
        """
        If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
        """
        trial_continuation: NotRequired["Literal['continue', 'none']"]
        """
        Specify trial behavior when crossing phase boundaries
        """
        trial_end: NotRequired["int"]
        """
        Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`
        """
        trial_settings: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class CreateParamsPhaseAddInvoiceItem(TypedDict):
        discounts: NotRequired[
            "List[SubscriptionScheduleService.CreateParamsPhaseAddInvoiceItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseAddInvoiceItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item. Defaults to 1.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
        """

    class CreateParamsPhaseAddInvoiceItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseAddInvoiceItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsPhaseAddInvoiceItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration(
        TypedDict
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsPhaseAddInvoiceItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsPhaseAutomaticTax(TypedDict):
        enabled: bool
        """
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
        """
        liability: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class CreateParamsPhaseAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsPhaseBillingThresholds(TypedDict):
        amount_gte: NotRequired["int"]
        """
        Monetary threshold that triggers the subscription to advance to a new billing period
        """
        reset_billing_cycle_anchor: NotRequired["bool"]
        """
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
        """

    class CreateParamsPhaseDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsPhaseDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsPhaseDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsPhaseInvoiceSettings(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with this phase of the subscription schedule. Will be set on invoices generated by this phase of the subscription schedule.
        """
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """
        issuer: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseInvoiceSettingsIssuer"
        ]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class CreateParamsPhaseInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsPhaseItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.CreateParamsPhaseItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        discounts: NotRequired[
            "Literal['']|List[SubscriptionScheduleService.CreateParamsPhaseItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item's `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item's `metadata` can be unset by posting an empty value to them in the configuration item's `metadata`. To unset all keys in the subscription item's `metadata`, update the subscription item directly or unset every key individually from the configuration item's `metadata`.
        """
        plan: NotRequired["str"]
        """
        The plan ID to subscribe to. You may specify the same ID in `plan` and `price`.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for the given price. Can be set only if the price's `usage_type` is `licensed` and not `metered`.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """
        trial: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseItemTrial"
        ]
        """
        Options that configure the trial on the subscription item.
        """

    class CreateParamsPhaseItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class CreateParamsPhaseItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsPhaseItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsPhaseItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsPhaseItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "SubscriptionScheduleService.CreateParamsPhaseItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsPhaseItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class CreateParamsPhaseItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class CreateParamsPhasePauseCollection(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class CreateParamsPhaseTransferData(TypedDict):
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class CreateParamsPhaseTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "SubscriptionScheduleService.CreateParamsPhaseTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class CreateParamsPhaseTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class CreateParamsPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """
        update_behavior: NotRequired["Literal['prebill', 'reset']"]
        """
        Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
        """

    class ListParams(TypedDict):
        canceled_at: NotRequired[
            "SubscriptionScheduleService.ListParamsCanceledAt|int"
        ]
        """
        Only return subscription schedules that were created canceled the given date interval.
        """
        completed_at: NotRequired[
            "SubscriptionScheduleService.ListParamsCompletedAt|int"
        ]
        """
        Only return subscription schedules that completed during the given date interval.
        """
        created: NotRequired[
            "SubscriptionScheduleService.ListParamsCreated|int"
        ]
        """
        Only return subscription schedules that were created during the given date interval.
        """
        customer: NotRequired["str"]
        """
        Only return subscription schedules for the given customer.
        """
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
        released_at: NotRequired[
            "SubscriptionScheduleService.ListParamsReleasedAt|int"
        ]
        """
        Only return subscription schedules that were released during the given date interval.
        """
        scheduled: NotRequired["bool"]
        """
        Only return subscription schedules that have not started yet.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParamsCanceledAt(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ListParamsCompletedAt(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ListParamsReleasedAt(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ReleaseParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        preserve_cancel_date: NotRequired["bool"]
        """
        Keep any cancellation on the subscription that the schedule has set
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        default_settings: NotRequired[
            "SubscriptionScheduleService.UpdateParamsDefaultSettings"
        ]
        """
        Object representing the subscription schedule's default settings.
        """
        end_behavior: NotRequired[
            "Literal['cancel', 'none', 'release', 'renew']"
        ]
        """
        Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        phases: NotRequired[
            "List[SubscriptionScheduleService.UpdateParamsPhase]"
        ]
        """
        List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted.
        """
        prebilling: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed now.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`.
        """

    class UpdateParamsDefaultSettings(TypedDict):
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
        """
        automatic_tax: NotRequired[
            "SubscriptionScheduleService.UpdateParamsDefaultSettingsAutomaticTax"
        ]
        """
        Default settings for automatic tax computation.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'phase_start']"
        ]
        """
        Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.UpdateParamsDefaultSettingsBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        default_payment_method: NotRequired["str"]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        description: NotRequired["Literal['']|str"]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        invoice_settings: NotRequired[
            "SubscriptionScheduleService.UpdateParamsDefaultSettingsInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge, for each of the associated subscription's invoices.
        """
        transfer_data: NotRequired[
            "Literal['']|SubscriptionScheduleService.UpdateParamsDefaultSettingsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the associated subscription's invoices.
        """

    class UpdateParamsDefaultSettingsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
        """
        liability: NotRequired[
            "SubscriptionScheduleService.UpdateParamsDefaultSettingsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class UpdateParamsDefaultSettingsAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsDefaultSettingsBillingThresholds(TypedDict):
        amount_gte: NotRequired["int"]
        """
        Monetary threshold that triggers the subscription to advance to a new billing period
        """
        reset_billing_cycle_anchor: NotRequired["bool"]
        """
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
        """

    class UpdateParamsDefaultSettingsInvoiceSettings(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with the subscription schedule. Will be set on invoices generated by the subscription schedule.
        """
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `collection_method=charge_automatically`.
        """
        issuer: NotRequired[
            "SubscriptionScheduleService.UpdateParamsDefaultSettingsInvoiceSettingsIssuer"
        ]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class UpdateParamsDefaultSettingsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsDefaultSettingsTransferData(TypedDict):
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class UpdateParamsPhase(TypedDict):
        add_invoice_items: NotRequired[
            "List[SubscriptionScheduleService.UpdateParamsPhaseAddInvoiceItem]"
        ]
        """
        A list of prices and quantities that will generate invoice items appended to the next invoice for this phase. You may pass up to 20 items.
        """
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
        """
        automatic_tax: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseAutomaticTax"
        ]
        """
        Automatic tax settings for this phase.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'phase_start']"
        ]
        """
        Can be set to `phase_start` to set the anchor to the start of the phase or `automatic` to automatically change it if needed. Cannot be set to `phase_start` if this phase specifies a trial. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
        """
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.UpdateParamsPhaseBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        coupon: NotRequired["str"]
        """
        The identifier of the coupon to apply to this phase of the subscription schedule.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        default_payment_method: NotRequired["str"]
        """
        ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
        """
        description: NotRequired["Literal['']|str"]
        """
        Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        discounts: NotRequired[
            "Literal['']|List[SubscriptionScheduleService.UpdateParamsPhaseDiscount]"
        ]
        """
        The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription's customer. Pass an empty string to avoid inheriting any discounts.
        """
        end_date: NotRequired["int|Literal['now']"]
        """
        The date at which this phase of the subscription schedule ends. If set, `iterations` must not be set.
        """
        invoice_settings: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseInvoiceSettings"
        ]
        """
        All invoices will be billed using the specified settings.
        """
        items: List["SubscriptionScheduleService.UpdateParamsPhaseItem"]
        """
        List of configuration items, each with an attached price, to apply during this phase of the subscription schedule.
        """
        iterations: NotRequired["int"]
        """
        Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered, adding new keys and replacing existing keys in the subscription's `metadata`. Individual keys in the subscription's `metadata` can be unset by posting an empty value to them in the phase's `metadata`. To unset all keys in the subscription's `metadata`, update the subscription directly or unset every key individually from the phase's `metadata`.
        """
        on_behalf_of: NotRequired["str"]
        """
        The account on behalf of which to charge, for each of the associated subscription's invoices.
        """
        pause_collection: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhasePauseCollection"
        ]
        """
        If specified, payment collection for this subscription will be paused.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Whether the subscription schedule will create [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when transitioning to this phase. The default value is `create_prorations`. This setting controls prorations when a phase is started asynchronously and it is persisted as a field on the phase. It's different from the request-level [proration_behavior](https://stripe.com/docs/api/subscription_schedules/update#update_subscription_schedule-proration_behavior) parameter which controls what happens if the update request affects the billing configuration of the current phase.
        """
        start_date: NotRequired["int|Literal['now']"]
        """
        The date at which this phase of the subscription schedule starts or `now`. Must be set on the first phase.
        """
        transfer_data: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the associated subscription's invoices.
        """
        trial: NotRequired["bool"]
        """
        If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
        """
        trial_continuation: NotRequired["Literal['continue', 'none']"]
        """
        Specify trial behavior when crossing phase boundaries
        """
        trial_end: NotRequired["int|Literal['now']"]
        """
        Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`
        """
        trial_settings: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseTrialSettings"
        ]
        """
        Settings related to subscription trials.
        """

    class UpdateParamsPhaseAddInvoiceItem(TypedDict):
        discounts: NotRequired[
            "List[SubscriptionScheduleService.UpdateParamsPhaseAddInvoiceItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseAddInvoiceItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item. Defaults to 1.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
        """

    class UpdateParamsPhaseAddInvoiceItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseAddInvoiceItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsPhaseAddInvoiceItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration(
        TypedDict
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsPhaseAddInvoiceItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class UpdateParamsPhaseAutomaticTax(TypedDict):
        enabled: bool
        """
        Enabled automatic tax calculation which will automatically compute tax rates on all invoices generated by the subscription.
        """
        liability: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class UpdateParamsPhaseAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsPhaseBillingThresholds(TypedDict):
        amount_gte: NotRequired["int"]
        """
        Monetary threshold that triggers the subscription to advance to a new billing period
        """
        reset_billing_cycle_anchor: NotRequired["bool"]
        """
        Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged.
        """

    class UpdateParamsPhaseDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsPhaseDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsPhaseDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsPhaseInvoiceSettings(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with this phase of the subscription schedule. Will be set on invoices generated by this phase of the subscription schedule.
        """
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """
        issuer: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseInvoiceSettingsIssuer"
        ]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class UpdateParamsPhaseInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class UpdateParamsPhaseItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|SubscriptionScheduleService.UpdateParamsPhaseItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        discounts: NotRequired[
            "Literal['']|List[SubscriptionScheduleService.UpdateParamsPhaseItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a configuration item. Metadata on a configuration item will update the underlying subscription item's `metadata` when the phase is entered, adding new keys and replacing existing keys. Individual keys in the subscription item's `metadata` can be unset by posting an empty value to them in the configuration item's `metadata`. To unset all keys in the subscription item's `metadata`, update the subscription item directly or unset every key individually from the configuration item's `metadata`.
        """
        plan: NotRequired["str"]
        """
        The plan ID to subscribe to. You may specify the same ID in `plan` and `price`.
        """
        price: NotRequired["str"]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired["int"]
        """
        Quantity for the given price. Can be set only if the price's `usage_type` is `licensed` and not `metered`.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """
        trial: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseItemTrial"
        ]
        """
        Options that configure the trial on the subscription item.
        """

    class UpdateParamsPhaseItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class UpdateParamsPhaseItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class UpdateParamsPhaseItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class UpdateParamsPhaseItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class UpdateParamsPhaseItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "SubscriptionScheduleService.UpdateParamsPhaseItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class UpdateParamsPhaseItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class UpdateParamsPhaseItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class UpdateParamsPhasePauseCollection(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class UpdateParamsPhaseTransferData(TypedDict):
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class UpdateParamsPhaseTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "SubscriptionScheduleService.UpdateParamsPhaseTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class UpdateParamsPhaseTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class UpdateParamsPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """
        update_behavior: NotRequired["Literal['prebill', 'reset']"]
        """
        Whether to cancel or preserve `prebilling` if the subscription is updated during the prebilled period. The default value is `reset`.
        """

    def list(
        self,
        params: "SubscriptionScheduleService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[SubscriptionSchedule]:
        """
        Retrieves the list of your subscription schedules.
        """
        return cast(
            ListObject[SubscriptionSchedule],
            self._request(
                "get",
                "/v1/subscription_schedules",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "SubscriptionScheduleService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[SubscriptionSchedule]:
        """
        Retrieves the list of your subscription schedules.
        """
        return cast(
            ListObject[SubscriptionSchedule],
            await self._request_async(
                "get",
                "/v1/subscription_schedules",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "SubscriptionScheduleService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "post",
                "/v1/subscription_schedules",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "SubscriptionScheduleService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "post",
                "/v1/subscription_schedules",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "get",
                "/v1/subscription_schedules/{schedule}".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "get",
                "/v1/subscription_schedules/{schedule}".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Updates an existing subscription schedule.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Updates an existing subscription schedule.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "post",
                "/v1/subscription_schedules/{schedule}".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def amend(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.AmendParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Amends an existing subscription schedule.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}/amend".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def amend_async(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.AmendParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Amends an existing subscription schedule.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "post",
                "/v1/subscription_schedules/{schedule}/amend".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is not_started or active.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}/cancel".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is not_started or active.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "post",
                "/v1/subscription_schedules/{schedule}/cancel".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def release(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.ReleaseParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is not_started or active. If the subscription schedule is currently associated with a subscription, releasing it will remove its subscription property and set the subscription's ID to the released_subscription property.
        """
        return cast(
            SubscriptionSchedule,
            self._request(
                "post",
                "/v1/subscription_schedules/{schedule}/release".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def release_async(
        self,
        schedule: str,
        params: "SubscriptionScheduleService.ReleaseParams" = {},
        options: RequestOptions = {},
    ) -> SubscriptionSchedule:
        """
        Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is not_started or active. If the subscription schedule is currently associated with a subscription, releasing it will remove its subscription property and set the subscription's ID to the released_subscription property.
        """
        return cast(
            SubscriptionSchedule,
            await self._request_async(
                "post",
                "/v1/subscription_schedules/{schedule}/release".format(
                    schedule=sanitize_id(schedule),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
