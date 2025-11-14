# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._coupon import Coupon
    from stripe._discount import Discount as DiscountResource
    from stripe._price import Price
    from stripe._promotion_code import PromotionCode
    from stripe._tax_rate import TaxRate


class QuoteLine(StripeObject):
    """
    A quote line defines a set of changes, in the order provided, that will be applied upon quote acceptance.
    """

    OBJECT_NAME: ClassVar[Literal["quote_line"]] = "quote_line"

    class Action(StripeObject):
        class AddDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                type: Literal["line_ends_at"]
                """
                The discount end type.
                """

            coupon: Optional[ExpandableField["Coupon"]]
            """
            ID of the coupon to create a new discount for.
            """
            discount: Optional[ExpandableField["DiscountResource"]]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: Optional[DiscountEnd]
            """
            Details to determine how long the discount should be applied for.
            """
            index: Optional[int]
            """
            The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
            """
            promotion_code: Optional[ExpandableField["PromotionCode"]]
            """
            ID of the promotion code to create a new discount for.
            """
            _inner_class_types = {"discount_end": DiscountEnd}

        class AddItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    """
                    The discount end timestamp.
                    """
                    type: Literal["timestamp"]
                    """
                    The discount end type.
                    """

                coupon: Optional[ExpandableField["Coupon"]]
                """
                ID of the coupon to create a new discount for.
                """
                discount: Optional[ExpandableField["DiscountResource"]]
                """
                ID of an existing discount on the object (or one of its ancestors) to reuse.
                """
                discount_end: Optional[DiscountEnd]
                """
                Details to determine how long the discount should be applied for.
                """
                promotion_code: Optional[ExpandableField["PromotionCode"]]
                """
                ID of the promotion code to create a new discount for.
                """
                _inner_class_types = {"discount_end": DiscountEnd}

            class Trial(StripeObject):
                converts_to: Optional[List[str]]
                """
                List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
                """
                type: Literal["free", "paid"]
                """
                Determines the type of trial for this item.
                """

            discounts: List[Discount]
            """
            The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered.
            """
            price: ExpandableField["Price"]
            """
            ID of the price to which the customer should be subscribed.
            """
            quantity: Optional[int]
            """
            Quantity of the plan to which the customer should be subscribed.
            """
            tax_rates: Optional[List["TaxRate"]]
            """
            The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`.
            """
            trial: Optional[Trial]
            """
            Options that configure the trial on the subscription item.
            """
            _inner_class_types = {"discounts": Discount, "trial": Trial}

        class RemoveDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                """
                The discount end timestamp.
                """
                type: Literal["timestamp"]
                """
                The discount end type.
                """

            coupon: Optional[ExpandableField["Coupon"]]
            """
            ID of the coupon to create a new discount for.
            """
            discount: Optional[ExpandableField["DiscountResource"]]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: Optional[DiscountEnd]
            """
            Details to determine how long the discount should be applied for.
            """
            promotion_code: Optional[ExpandableField["PromotionCode"]]
            """
            ID of the promotion code to create a new discount for.
            """
            _inner_class_types = {"discount_end": DiscountEnd}

        class RemoveItem(StripeObject):
            price: ExpandableField["Price"]
            """
            ID of a price to remove.
            """

        class SetDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                """
                The discount end timestamp.
                """
                type: Literal["timestamp"]
                """
                The discount end type.
                """

            coupon: Optional[ExpandableField["Coupon"]]
            """
            ID of the coupon to create a new discount for.
            """
            discount: Optional[ExpandableField["DiscountResource"]]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """
            discount_end: Optional[DiscountEnd]
            """
            Details to determine how long the discount should be applied for.
            """
            promotion_code: Optional[ExpandableField["PromotionCode"]]
            """
            ID of the promotion code to create a new discount for.
            """
            _inner_class_types = {"discount_end": DiscountEnd}

        class SetItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    """
                    The discount end timestamp.
                    """
                    type: Literal["timestamp"]
                    """
                    The discount end type.
                    """

                coupon: Optional[ExpandableField["Coupon"]]
                """
                ID of the coupon to create a new discount for.
                """
                discount: Optional[ExpandableField["DiscountResource"]]
                """
                ID of an existing discount on the object (or one of its ancestors) to reuse.
                """
                discount_end: Optional[DiscountEnd]
                """
                Details to determine how long the discount should be applied for.
                """
                promotion_code: Optional[ExpandableField["PromotionCode"]]
                """
                ID of the promotion code to create a new discount for.
                """
                _inner_class_types = {"discount_end": DiscountEnd}

            class Trial(StripeObject):
                converts_to: Optional[List[str]]
                """
                List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
                """
                type: Literal["free", "paid"]
                """
                Determines the type of trial for this item.
                """

            discounts: List[Discount]
            """
            The discounts applied to the subscription item. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered.
            """
            price: ExpandableField["Price"]
            """
            ID of the price to which the customer should be subscribed.
            """
            quantity: Optional[int]
            """
            Quantity of the plan to which the customer should be subscribed.
            """
            tax_rates: Optional[List["TaxRate"]]
            """
            The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`.
            """
            trial: Optional[Trial]
            """
            Options that configure the trial on the subscription item.
            """
            _inner_class_types = {"discounts": Discount, "trial": Trial}

        add_discount: Optional[AddDiscount]
        """
        Details for the `add_discount` type.
        """
        add_item: Optional[AddItem]
        """
        Details for the `add_item` type.
        """
        add_metadata: Optional[Dict[str, str]]
        """
        Details for the `add_metadata` type: specify a hash of key-value pairs.
        """
        remove_discount: Optional[RemoveDiscount]
        """
        Details for the `remove_discount` type.
        """
        remove_item: Optional[RemoveItem]
        """
        Details for the `remove_item` type.
        """
        remove_metadata: Optional[List[str]]
        """
        Details for the `remove_metadata` type: specify an array of metadata keys.
        """
        set_discounts: Optional[List[SetDiscount]]
        """
        Details for the `set_discounts` type.
        """
        set_items: Optional[List[SetItem]]
        """
        Details for the `set_items` type.
        """
        set_metadata: Optional[Dict[str, str]]
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
        _inner_class_types = {
            "add_discount": AddDiscount,
            "add_item": AddItem,
            "remove_discount": RemoveDiscount,
            "remove_item": RemoveItem,
            "set_discounts": SetDiscount,
            "set_items": SetItem,
        }

    class AppliesTo(StripeObject):
        new_reference: Optional[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: Optional[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CancelSubscriptionSchedule(StripeObject):
        cancel_at: Literal["line_starts_at"]
        """
        Timestamp helper to cancel the underlying schedule on the accompanying line's start date. Must be set to `line_starts_at`.
        """
        invoice_now: Optional[bool]
        """
        If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Boolean that defaults to `true`.
        """
        prorate: Optional[bool]
        """
        If the subscription schedule is `active`, indicates if the cancellation should be prorated. Boolean that defaults to `true`.
        """

    class EndsAt(StripeObject):
        class DiscountEnd(StripeObject):
            discount: str
            """
            The ID of a specific discount.
            """

        class Duration(StripeObject):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
            """

        computed: Optional[int]
        """
        The timestamp value that will be used to determine when to make changes to the subscription schedule, as computed from the `ends_at` field. For example, if `ends_at[type]=upcoming_invoice`, the upcoming invoice date will be computed at the time the `ends_at` field was specified and saved. This field will not be recomputed upon future requests to update or finalize the quote unless `ends_at` is respecified. This field is guaranteed to be populated after quote acceptance.
        """
        discount_end: Optional[DiscountEnd]
        """
        Use the `end` time of a given discount.
        """
        duration: Optional[Duration]
        """
        Time span for the quote line starting from the `starts_at` date.
        """
        timestamp: Optional[int]
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
        _inner_class_types = {
            "discount_end": DiscountEnd,
            "duration": Duration,
        }

    class SetPauseCollection(StripeObject):
        class Set(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            """
            The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
            """

        set: Optional[Set]
        """
        If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment).
        """
        type: Literal["remove", "set"]
        """
        Defines the type of the pause_collection behavior for the quote line.
        """
        _inner_class_types = {"set": Set}

    class StartsAt(StripeObject):
        class DiscountEnd(StripeObject):
            discount: str
            """
            The ID of a specific discount.
            """

        class LineEndsAt(StripeObject):
            id: str
            """
            Unique identifier for the object.
            """

        computed: Optional[int]
        """
        The timestamp value that will be used to determine when to make changes to the subscription schedule, as computed from the `starts_at` field. For example, if `starts_at[type]=upcoming_invoice`, the upcoming invoice date will be computed at the time the `starts_at` field was specified and saved. This field will not be recomputed upon future requests to update or finalize the quote unless `starts_at` is respecified. This field is guaranteed to be populated after quote acceptance.
        """
        discount_end: Optional[DiscountEnd]
        """
        Use the `end` time of a given discount.
        """
        line_ends_at: Optional[LineEndsAt]
        """
        The timestamp the given line ends at.
        """
        timestamp: Optional[int]
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
        _inner_class_types = {
            "discount_end": DiscountEnd,
            "line_ends_at": LineEndsAt,
        }

    class TrialSettings(StripeObject):
        class EndBehavior(StripeObject):
            prorate_up_front: Optional[Literal["defer", "include"]]
            """
            Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
            """

        end_behavior: Optional[EndBehavior]
        """
        Defines how the subscription should behave when a trial ends.
        """
        _inner_class_types = {"end_behavior": EndBehavior}

    actions: Optional[List[Action]]
    """
    A list of items the customer is being quoted for.
    """
    applies_to: Optional[AppliesTo]
    """
    Details to identify the subscription schedule the quote line applies to.
    """
    billing_cycle_anchor: Optional[Literal["automatic", "line_starts_at"]]
    """
    For point-in-time quote lines (having no `ends_at` timestamp), this attribute lets you set or remove whether the subscription's billing cycle anchor is reset at the Quote Line `starts_at` timestamp.For time-span based quote lines (having both `starts_at` and `ends_at`), the only valid value is `automatic`, which removes any previously configured billing cycle anchor resets during the window of time spanning the quote line.
    """
    cancel_subscription_schedule: Optional[CancelSubscriptionSchedule]
    """
    A point-in-time operation that cancels an existing subscription schedule at the line's starts_at timestamp. Currently only compatible with `quote_acceptance_date` for `starts_at`. When using cancel_subscription_schedule, the subscription schedule on the quote remains unalterable, except for modifications to the metadata, collection_method or invoice_settings.
    """
    ends_at: Optional[EndsAt]
    """
    Details to identify the end of the time range modified by the proposed change. If not supplied, the quote line is considered a point-in-time operation that only affects the exact timestamp at `starts_at`, and a restricted set of attributes is supported on the quote line.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["quote_line"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    proration_behavior: Optional[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Changes to how Stripe handles prorations during the quote line's time span. Affects if and how prorations are created when a future phase starts.
    """
    set_pause_collection: Optional[SetPauseCollection]
    """
    Details to modify the pause_collection behavior of the subscription schedule.
    """
    set_schedule_end: Optional[Literal["line_ends_at", "line_starts_at"]]
    """
    Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
    """
    starts_at: Optional[StartsAt]
    """
    Details to identify the earliest timestamp where the proposed change should take effect.
    """
    trial_settings: Optional[TrialSettings]
    """
    Settings related to subscription trials.
    """
    _inner_class_types = {
        "actions": Action,
        "applies_to": AppliesTo,
        "cancel_subscription_schedule": CancelSubscriptionSchedule,
        "ends_at": EndsAt,
        "set_pause_collection": SetPauseCollection,
        "starts_at": StartsAt,
        "trial_settings": TrialSettings,
    }
