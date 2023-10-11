# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.coupon import Coupon
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.price import Price
    from stripe.api_resources.tax_rate import TaxRate


class QuoteLine(StripeObject):
    """
    A quote line defines a set of changes, in the order provided, that will be applied upon quote acceptance.
    """

    OBJECT_NAME = "quote_line"

    class Action(StripeObject):
        class AddDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                type: Literal["line_ends_at"]

            coupon: Optional[ExpandableField["Coupon"]]
            discount: Optional[ExpandableField["DiscountResource"]]
            discount_end: Optional[DiscountEnd]
            index: Optional[int]
            _inner_class_types = {"discount_end": DiscountEnd}

        class AddItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    type: Literal["timestamp"]

                coupon: Optional[ExpandableField["Coupon"]]
                discount: Optional[ExpandableField["DiscountResource"]]
                discount_end: Optional[DiscountEnd]
                _inner_class_types = {"discount_end": DiscountEnd}

            class Trial(StripeObject):
                converts_to: Optional[List[str]]
                type: Literal["free", "paid"]

            discounts: Optional[List[Discount]]
            metadata: Optional[Dict[str, str]]
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]
            trial: Optional[Trial]
            _inner_class_types = {"discounts": Discount, "trial": Trial}

        class RemoveDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                type: Literal["timestamp"]

            coupon: Optional[ExpandableField["Coupon"]]
            discount: Optional[ExpandableField["DiscountResource"]]
            discount_end: Optional[DiscountEnd]
            _inner_class_types = {"discount_end": DiscountEnd}

        class RemoveItem(StripeObject):
            price: ExpandableField["Price"]

        class SetDiscount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                type: Literal["timestamp"]

            coupon: Optional[ExpandableField["Coupon"]]
            discount: Optional[ExpandableField["DiscountResource"]]
            discount_end: Optional[DiscountEnd]
            _inner_class_types = {"discount_end": DiscountEnd}

        class SetItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    type: Literal["timestamp"]

                coupon: Optional[ExpandableField["Coupon"]]
                discount: Optional[ExpandableField["DiscountResource"]]
                discount_end: Optional[DiscountEnd]
                _inner_class_types = {"discount_end": DiscountEnd}

            class Trial(StripeObject):
                converts_to: Optional[List[str]]
                type: Literal["free", "paid"]

            discounts: Optional[List[Discount]]
            metadata: Optional[Dict[str, str]]
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]
            trial: Optional[Trial]
            _inner_class_types = {"discounts": Discount, "trial": Trial}

        add_discount: Optional[AddDiscount]
        add_item: Optional[AddItem]
        add_metadata: Optional[Dict[str, str]]
        remove_discount: Optional[RemoveDiscount]
        remove_item: Optional[RemoveItem]
        remove_metadata: Optional[List[str]]
        set_discounts: Optional[List[SetDiscount]]
        set_items: Optional[List[SetItem]]
        set_metadata: Optional[Dict[str, str]]
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
        subscription_schedule: Optional[str]
        type: Literal["new_reference", "subscription_schedule"]

    class EndsAt(StripeObject):
        class DiscountEnd(StripeObject):
            discount: str

        class Duration(StripeObject):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        computed: Optional[int]
        discount_end: Optional[DiscountEnd]
        duration: Optional[Duration]
        timestamp: Optional[int]
        type: Literal[
            "discount_end",
            "duration",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        _inner_class_types = {
            "discount_end": DiscountEnd,
            "duration": Duration,
        }

    class SetPauseCollection(StripeObject):
        class Set(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        set: Optional[Set]
        type: Literal["remove", "set"]
        _inner_class_types = {"set": Set}

    class StartsAt(StripeObject):
        class DiscountEnd(StripeObject):
            discount: str

        class LineEndsAt(StripeObject):
            id: str

        computed: Optional[int]
        discount_end: Optional[DiscountEnd]
        line_ends_at: Optional[LineEndsAt]
        timestamp: Optional[int]
        type: Literal[
            "discount_end",
            "line_ends_at",
            "now",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        _inner_class_types = {
            "discount_end": DiscountEnd,
            "line_ends_at": LineEndsAt,
        }

    class TrialSettings(StripeObject):
        class EndBehavior(StripeObject):
            prorate_up_front: Optional[Literal["defer", "include"]]

        end_behavior: Optional[EndBehavior]
        _inner_class_types = {"end_behavior": EndBehavior}

    actions: Optional[List[Action]]
    applies_to: Optional[AppliesTo]
    billing_cycle_anchor: Optional[Literal["automatic", "line_starts_at"]]
    ends_at: Optional[EndsAt]
    id: str
    object: Literal["quote_line"]
    proration_behavior: Optional[
        Literal["always_invoice", "create_prorations", "none"]
    ]
    set_pause_collection: Optional[SetPauseCollection]
    set_schedule_end: Optional[Literal["line_ends_at", "line_starts_at"]]
    starts_at: Optional[StartsAt]
    trial_settings: Optional[TrialSettings]

    _inner_class_types = {
        "actions": Action,
        "applies_to": AppliesTo,
        "ends_at": EndsAt,
        "set_pause_collection": SetPauseCollection,
        "starts_at": StartsAt,
        "trial_settings": TrialSettings,
    }
