# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
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
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.subscription_schedule import (
        SubscriptionSchedule as SubscriptionScheduleResource,
    )
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


@nested_resource_class_methods("preview_invoice")
@nested_resource_class_methods("preview_subscription_schedule")
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

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        _inner_class_types = {"liability": Liability}

    class Computed(StripeObject):
        class Recurring(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        discount: "DiscountResource"

                    class Tax(StripeObject):
                        amount: int
                        rate: "TaxRate"
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        taxable_amount: Optional[int]

                    discounts: List[Discount]
                    taxes: List[Tax]
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                amount_shipping: Optional[int]
                amount_tax: int
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            amount_total: int
            interval: Literal["day", "month", "week", "year"]
            interval_count: int
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        class Upfront(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        discount: "DiscountResource"

                    class Tax(StripeObject):
                        amount: int
                        rate: "TaxRate"
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        taxable_amount: Optional[int]

                    discounts: List[Discount]
                    taxes: List[Tax]
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                amount_shipping: Optional[int]
                amount_tax: int
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            amount_total: int
            line_items: Optional[ListObject["LineItem"]]
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        recurring: Optional[Recurring]
        updated_at: Optional[int]
        upfront: Upfront
        _inner_class_types = {"recurring": Recurring, "upfront": Upfront}

    class FromQuote(StripeObject):
        is_revision: bool
        quote: ExpandableField["Quote"]

    class InvoiceSettings(StripeObject):
        class Issuer(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        days_until_due: Optional[int]
        issuer: Optional[Issuer]
        _inner_class_types = {"issuer": Issuer}

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Optional[
                Literal[
                    "canceled",
                    "quote_accepted",
                    "quote_expired",
                    "quote_superseded",
                    "subscription_canceled",
                ]
            ]
            transitioned_at: Optional[int]

        class Stale(StripeObject):
            class LastReason(StripeObject):
                class SubscriptionChanged(StripeObject):
                    previous_subscription: Optional["Subscription"]

                class SubscriptionScheduleChanged(StripeObject):
                    previous_subscription_schedule: Optional[
                        "SubscriptionScheduleResource"
                    ]

                line_invalid: Optional[str]
                marked_stale: Optional[str]
                subscription_canceled: Optional[str]
                subscription_changed: Optional[SubscriptionChanged]
                subscription_expired: Optional[str]
                subscription_schedule_canceled: Optional[str]
                subscription_schedule_changed: Optional[
                    SubscriptionScheduleChanged
                ]
                subscription_schedule_released: Optional[str]
                type: Optional[
                    Literal[
                        "bill_on_acceptance_invalid",
                        "line_invalid",
                        "marked_stale",
                        "subscription_canceled",
                        "subscription_changed",
                        "subscription_expired",
                        "subscription_schedule_canceled",
                        "subscription_schedule_changed",
                        "subscription_schedule_released",
                    ]
                ]
                _inner_class_types = {
                    "subscription_changed": SubscriptionChanged,
                    "subscription_schedule_changed": SubscriptionScheduleChanged,
                }

            expires_at: Optional[int]
            last_reason: Optional[LastReason]
            last_updated_at: Optional[int]
            transitioned_at: Optional[int]
            _inner_class_types = {"last_reason": LastReason}

        canceled: Optional[Canceled]
        stale: Optional[Stale]
        _inner_class_types = {"canceled": Canceled, "stale": Stale}

    class StatusTransitions(StripeObject):
        accepted_at: Optional[int]
        canceled_at: Optional[int]
        finalized_at: Optional[int]

    class SubscriptionData(StripeObject):
        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str

                computed: Optional[int]
                line_starts_at: Optional[LineStartsAt]
                timestamp: Optional[int]
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    interval_count: int

                class LineEndsAt(StripeObject):
                    id: str

                computed: Optional[int]
                duration: Optional[Duration]
                line_ends_at: Optional[LineEndsAt]
                timestamp: Optional[int]
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            bill_until: Optional[BillUntil]
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        class Prebilling(StripeObject):
            iterations: int

        bill_on_acceptance: Optional[BillOnAcceptance]
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        billing_cycle_anchor: Optional[Literal["reset"]]
        description: Optional[str]
        effective_date: Optional[int]
        end_behavior: Optional[Literal["cancel", "release"]]
        from_schedule: Optional[
            ExpandableField["SubscriptionScheduleResource"]
        ]
        from_subscription: Optional[ExpandableField["Subscription"]]
        prebilling: Optional[Prebilling]
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        trial_period_days: Optional[int]
        _inner_class_types = {
            "bill_on_acceptance": BillOnAcceptance,
            "prebilling": Prebilling,
        }

    class SubscriptionDataOverride(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            subscription_schedule: Optional[str]
            type: Literal["new_reference", "subscription_schedule"]

        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str

                computed: Optional[int]
                line_starts_at: Optional[LineStartsAt]
                timestamp: Optional[int]
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    interval_count: int

                class LineEndsAt(StripeObject):
                    id: str

                computed: Optional[int]
                duration: Optional[Duration]
                line_ends_at: Optional[LineEndsAt]
                timestamp: Optional[int]
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            bill_until: Optional[BillUntil]
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        applies_to: AppliesTo
        bill_on_acceptance: Optional[BillOnAcceptance]
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        customer: Optional[str]
        description: Optional[str]
        end_behavior: Optional[Literal["cancel", "release"]]
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        _inner_class_types = {
            "applies_to": AppliesTo,
            "bill_on_acceptance": BillOnAcceptance,
        }

    class SubscriptionSchedule(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            subscription_schedule: Optional[str]
            type: Literal["new_reference", "subscription_schedule"]

        applies_to: AppliesTo
        subscription_schedule: str
        _inner_class_types = {"applies_to": AppliesTo}

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                discount: "DiscountResource"

            class Tax(StripeObject):
                amount: int
                rate: "TaxRate"
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                taxable_amount: Optional[int]

            discounts: List[Discount]
            taxes: List[Tax]
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        amount_shipping: Optional[int]
        amount_tax: int
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    class TransferData(StripeObject):
        amount: Optional[int]
        amount_percent: Optional[float]
        destination: ExpandableField["Account"]

    if TYPE_CHECKING:

        class AcceptParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            allow_backdated_lines: NotRequired["bool|None"]
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
            lines: NotRequired["List[Quote.CreateParamsLine]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            phases: NotRequired["List[Quote.CreateParamsPhase]|None"]
            subscription_data: NotRequired[
                "Quote.CreateParamsSubscriptionData|None"
            ]
            subscription_data_overrides: NotRequired[
                "List[Quote.CreateParamsSubscriptionDataOverride]|None"
            ]
            test_clock: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Literal['']|Quote.CreateParamsTransferData|None"
            ]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsSubscriptionDataOverride(TypedDict):
            applies_to: "Quote.CreateParamsSubscriptionDataOverrideAppliesTo"
            bill_on_acceptance: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptance|None"
            ]
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            end_behavior: NotRequired["Literal['cancel', 'release']|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class CreateParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
            bill_from: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom|None"
            ]
            bill_until: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil|None"
            ]

        class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
            TypedDict,
        ):
            duration: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration|None"
            ]
            line_ends_at: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "duration",
                "line_ends_at",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
            TypedDict,
        ):
            line_starts_at: NotRequired[
                "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "line_starts_at",
                "now",
                "pause_collection_start",
                "quote_acceptance_date",
                "timestamp",
            ]

        class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class CreateParamsSubscriptionDataOverrideAppliesTo(TypedDict):
            new_reference: NotRequired["str|None"]
            subscription_schedule: NotRequired["str|None"]
            type: Literal["new_reference", "subscription_schedule"]

        class CreateParamsSubscriptionData(TypedDict):
            bill_on_acceptance: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptance|None"
            ]
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['']|Literal['reset']|None"
            ]
            description: NotRequired["str|None"]
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            end_behavior: NotRequired["Literal['cancel', 'release']|None"]
            from_schedule: NotRequired["str|None"]
            from_subscription: NotRequired["str|None"]
            prebilling: NotRequired[
                "Literal['']|Quote.CreateParamsSubscriptionDataPrebilling|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            trial_period_days: NotRequired["Literal['']|int|None"]

        class CreateParamsSubscriptionDataPrebilling(TypedDict):
            iterations: int

        class CreateParamsSubscriptionDataBillOnAcceptance(TypedDict):
            bill_from: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillFrom|None"
            ]
            bill_until: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntil|None"
            ]

        class CreateParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration|None"
            ]
            line_ends_at: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "duration",
                "line_ends_at",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
            line_starts_at: NotRequired[
                "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "line_starts_at",
                "now",
                "pause_collection_start",
                "quote_acceptance_date",
                "timestamp",
            ]

        class CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class CreateParamsPhase(TypedDict):
            billing_cycle_anchor: NotRequired["Literal['reset']|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            discounts: NotRequired[
                "Literal['']|List[Quote.CreateParamsPhaseDiscount]|None"
            ]
            end_date: NotRequired["int|None"]
            invoice_settings: NotRequired[
                "Quote.CreateParamsPhaseInvoiceSettings|None"
            ]
            iterations: NotRequired["int|None"]
            line_items: List["Quote.CreateParamsPhaseLineItem"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            trial: NotRequired["bool|None"]
            trial_end: NotRequired["int|None"]

        class CreateParamsPhaseLineItem(TypedDict):
            discounts: NotRequired[
                "Literal['']|List[Quote.CreateParamsPhaseLineItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Quote.CreateParamsPhaseLineItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsPhaseLineItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: NotRequired[
                "Quote.CreateParamsPhaseLineItemPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPhaseLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsPhaseLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsPhaseLineItemDiscountDiscountEnd|None"
            ]

        class CreateParamsPhaseLineItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsPhaseLineItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsPhaseLineItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class CreateParamsPhaseDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsPhaseDiscountDiscountEnd|None"
            ]

        class CreateParamsPhaseDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsPhaseDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsPhaseDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsLine(TypedDict):
            actions: NotRequired["List[Quote.CreateParamsLineAction]|None"]
            applies_to: NotRequired["Quote.CreateParamsLineAppliesTo|None"]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'line_starts_at']|None"
            ]
            ends_at: NotRequired["Quote.CreateParamsLineEndsAt|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            set_pause_collection: NotRequired[
                "Quote.CreateParamsLineSetPauseCollection|None"
            ]
            set_schedule_end: NotRequired[
                "Literal['line_ends_at', 'line_starts_at']|None"
            ]
            starts_at: NotRequired["Quote.CreateParamsLineStartsAt|None"]
            trial_settings: NotRequired[
                "Quote.CreateParamsLineTrialSettings|None"
            ]

        class CreateParamsLineTrialSettings(TypedDict):
            end_behavior: NotRequired[
                "Quote.CreateParamsLineTrialSettingsEndBehavior|None"
            ]

        class CreateParamsLineTrialSettingsEndBehavior(TypedDict):
            prorate_up_front: NotRequired["Literal['defer', 'include']|None"]

        class CreateParamsLineStartsAt(TypedDict):
            discount_end: NotRequired[
                "Quote.CreateParamsLineStartsAtDiscountEnd|None"
            ]
            line_ends_at: NotRequired[
                "Quote.CreateParamsLineStartsAtLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "discount_end",
                "line_ends_at",
                "now",
                "quote_acceptance_date",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class CreateParamsLineStartsAtLineEndsAt(TypedDict):
            index: NotRequired["int|None"]

        class CreateParamsLineStartsAtDiscountEnd(TypedDict):
            discount: str

        class CreateParamsLineSetPauseCollection(TypedDict):
            set: NotRequired[
                "Quote.CreateParamsLineSetPauseCollectionSet|None"
            ]
            type: Literal["remove", "set"]

        class CreateParamsLineSetPauseCollectionSet(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class CreateParamsLineEndsAt(TypedDict):
            discount_end: NotRequired[
                "Quote.CreateParamsLineEndsAtDiscountEnd|None"
            ]
            duration: NotRequired["Quote.CreateParamsLineEndsAtDuration|None"]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "discount_end",
                "duration",
                "quote_acceptance_date",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class CreateParamsLineEndsAtDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsLineEndsAtDiscountEnd(TypedDict):
            discount: str

        class CreateParamsLineAppliesTo(TypedDict):
            new_reference: NotRequired["str|None"]
            subscription_schedule: NotRequired["str|None"]
            type: Literal["new_reference", "subscription_schedule"]

        class CreateParamsLineAction(TypedDict):
            add_discount: NotRequired[
                "Quote.CreateParamsLineActionAddDiscount|None"
            ]
            add_item: NotRequired["Quote.CreateParamsLineActionAddItem|None"]
            add_metadata: NotRequired["Dict[str, str]|None"]
            remove_discount: NotRequired[
                "Quote.CreateParamsLineActionRemoveDiscount|None"
            ]
            remove_item: NotRequired[
                "Quote.CreateParamsLineActionRemoveItem|None"
            ]
            remove_metadata: NotRequired["List[str]|None"]
            set_discounts: NotRequired[
                "List[Quote.CreateParamsLineActionSetDiscount]|None"
            ]
            set_items: NotRequired[
                "List[Quote.CreateParamsLineActionSetItem]|None"
            ]
            set_metadata: NotRequired["Literal['']|Dict[str, str]|None"]
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

        class CreateParamsLineActionSetItem(TypedDict):
            discounts: NotRequired[
                "List[Quote.CreateParamsLineActionSetItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired["Quote.CreateParamsLineActionSetItemTrial|None"]

        class CreateParamsLineActionSetItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class CreateParamsLineActionSetItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsLineActionSetItemDiscountDiscountEnd|None"
            ]

        class CreateParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsLineActionSetItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsLineActionSetItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsLineActionSetDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class CreateParamsLineActionRemoveItem(TypedDict):
            price: str

        class CreateParamsLineActionRemoveDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class CreateParamsLineActionAddItem(TypedDict):
            discounts: NotRequired[
                "List[Quote.CreateParamsLineActionAddItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired["Quote.CreateParamsLineActionAddItemTrial|None"]

        class CreateParamsLineActionAddItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class CreateParamsLineActionAddItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsLineActionAddItemDiscountDiscountEnd|None"
            ]

        class CreateParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsLineActionAddItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsLineActionAddItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsLineActionAddDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsLineActionAddDiscountDiscountEnd|None"
            ]
            index: NotRequired["int|None"]

        class CreateParamsLineActionAddDiscountDiscountEnd(TypedDict):
            type: Literal["line_ends_at"]

        class CreateParamsLineItem(TypedDict):
            discounts: NotRequired[
                "Literal['']|List[Quote.CreateParamsLineItemDiscount]|None"
            ]
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

        class CreateParamsLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsLineItemDiscountDiscountEnd|None"
            ]

        class CreateParamsLineItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsLineItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsLineItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired["Quote.CreateParamsInvoiceSettingsIssuer|None"]

        class CreateParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsFromQuote(TypedDict):
            is_revision: NotRequired["bool|None"]
            quote: str

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.CreateParamsDiscountDiscountEnd|None"
            ]

        class CreateParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.CreateParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Quote.CreateParamsAutomaticTaxLiability|None"
            ]

        class CreateParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class FinalizeQuoteParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            from_subscription: NotRequired["str|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['accepted', 'accepting', 'canceled', 'draft', 'open', 'stale']|None"
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

        class ListLinesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListPreviewInvoiceLinesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class MarkDraftParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class MarkStaleParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            reason: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            allow_backdated_lines: NotRequired["bool|None"]
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
            lines: NotRequired["List[Quote.ModifyParamsLine]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            phases: NotRequired["List[Quote.ModifyParamsPhase]|None"]
            subscription_data: NotRequired[
                "Quote.ModifyParamsSubscriptionData|None"
            ]
            subscription_data_overrides: NotRequired[
                "Literal['']|List[Quote.ModifyParamsSubscriptionDataOverride]|None"
            ]
            transfer_data: NotRequired[
                "Literal['']|Quote.ModifyParamsTransferData|None"
            ]

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsSubscriptionDataOverride(TypedDict):
            applies_to: "Quote.ModifyParamsSubscriptionDataOverrideAppliesTo"
            bill_on_acceptance: NotRequired[
                "Literal['']|Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptance|None"
            ]
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            customer: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            end_behavior: NotRequired["Literal['cancel', 'release']|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
            bill_from: NotRequired[
                "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom|None"
            ]
            bill_until: NotRequired[
                "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil|None"
            ]

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
            TypedDict,
        ):
            duration: NotRequired[
                "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration|None"
            ]
            line_ends_at: NotRequired[
                "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "duration",
                "line_ends_at",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
            TypedDict,
        ):
            line_starts_at: NotRequired[
                "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "line_starts_at",
                "now",
                "pause_collection_start",
                "quote_acceptance_date",
                "timestamp",
            ]

        class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class ModifyParamsSubscriptionDataOverrideAppliesTo(TypedDict):
            new_reference: NotRequired["str|None"]
            subscription_schedule: NotRequired["str|None"]
            type: Literal["new_reference", "subscription_schedule"]

        class ModifyParamsSubscriptionData(TypedDict):
            bill_on_acceptance: NotRequired[
                "Literal['']|Quote.ModifyParamsSubscriptionDataBillOnAcceptance|None"
            ]
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['']|Literal['reset']|None"
            ]
            description: NotRequired["Literal['']|str|None"]
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            end_behavior: NotRequired["Literal['cancel', 'release']|None"]
            prebilling: NotRequired[
                "Literal['']|Quote.ModifyParamsSubscriptionDataPrebilling|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            trial_period_days: NotRequired["Literal['']|int|None"]

        class ModifyParamsSubscriptionDataPrebilling(TypedDict):
            iterations: int

        class ModifyParamsSubscriptionDataBillOnAcceptance(TypedDict):
            bill_from: NotRequired[
                "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillFrom|None"
            ]
            bill_until: NotRequired[
                "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntil|None"
            ]

        class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilDuration|None"
            ]
            line_ends_at: NotRequired[
                "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "duration",
                "line_ends_at",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
            line_starts_at: NotRequired[
                "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "line_starts_at",
                "now",
                "pause_collection_start",
                "quote_acceptance_date",
                "timestamp",
            ]

        class ModifyParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
            TypedDict,
        ):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class ModifyParamsPhase(TypedDict):
            billing_cycle_anchor: NotRequired["Literal['reset']|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            discounts: NotRequired[
                "Literal['']|List[Quote.ModifyParamsPhaseDiscount]|None"
            ]
            end_date: NotRequired["int|None"]
            invoice_settings: NotRequired[
                "Quote.ModifyParamsPhaseInvoiceSettings|None"
            ]
            iterations: NotRequired["int|None"]
            line_items: List["Quote.ModifyParamsPhaseLineItem"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            trial: NotRequired["bool|None"]
            trial_end: NotRequired["int|None"]

        class ModifyParamsPhaseLineItem(TypedDict):
            discounts: NotRequired[
                "Literal['']|List[Quote.ModifyParamsPhaseLineItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Quote.ModifyParamsPhaseLineItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsPhaseLineItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: NotRequired[
                "Quote.ModifyParamsPhaseLineItemPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPhaseLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsPhaseLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsPhaseLineItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsPhaseLineItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsPhaseLineItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsPhaseLineItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class ModifyParamsPhaseDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsPhaseDiscountDiscountEnd|None"
            ]

        class ModifyParamsPhaseDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsPhaseDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsPhaseDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsLine(TypedDict):
            actions: NotRequired["List[Quote.ModifyParamsLineAction]|None"]
            applies_to: NotRequired["Quote.ModifyParamsLineAppliesTo|None"]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'line_starts_at']|None"
            ]
            ends_at: NotRequired["Quote.ModifyParamsLineEndsAt|None"]
            id: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            set_pause_collection: NotRequired[
                "Quote.ModifyParamsLineSetPauseCollection|None"
            ]
            set_schedule_end: NotRequired[
                "Literal['line_ends_at', 'line_starts_at']|None"
            ]
            starts_at: NotRequired["Quote.ModifyParamsLineStartsAt|None"]
            trial_settings: NotRequired[
                "Quote.ModifyParamsLineTrialSettings|None"
            ]

        class ModifyParamsLineTrialSettings(TypedDict):
            end_behavior: NotRequired[
                "Quote.ModifyParamsLineTrialSettingsEndBehavior|None"
            ]

        class ModifyParamsLineTrialSettingsEndBehavior(TypedDict):
            prorate_up_front: NotRequired["Literal['defer', 'include']|None"]

        class ModifyParamsLineStartsAt(TypedDict):
            discount_end: NotRequired[
                "Quote.ModifyParamsLineStartsAtDiscountEnd|None"
            ]
            line_ends_at: NotRequired[
                "Quote.ModifyParamsLineStartsAtLineEndsAt|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "discount_end",
                "line_ends_at",
                "now",
                "quote_acceptance_date",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class ModifyParamsLineStartsAtLineEndsAt(TypedDict):
            id: NotRequired["str|None"]
            index: NotRequired["int|None"]

        class ModifyParamsLineStartsAtDiscountEnd(TypedDict):
            discount: str

        class ModifyParamsLineSetPauseCollection(TypedDict):
            set: NotRequired[
                "Quote.ModifyParamsLineSetPauseCollectionSet|None"
            ]
            type: Literal["remove", "set"]

        class ModifyParamsLineSetPauseCollectionSet(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class ModifyParamsLineEndsAt(TypedDict):
            discount_end: NotRequired[
                "Quote.ModifyParamsLineEndsAtDiscountEnd|None"
            ]
            duration: NotRequired["Quote.ModifyParamsLineEndsAtDuration|None"]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "discount_end",
                "duration",
                "quote_acceptance_date",
                "schedule_end",
                "timestamp",
                "upcoming_invoice",
            ]

        class ModifyParamsLineEndsAtDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsLineEndsAtDiscountEnd(TypedDict):
            discount: str

        class ModifyParamsLineAppliesTo(TypedDict):
            new_reference: NotRequired["str|None"]
            subscription_schedule: NotRequired["str|None"]
            type: Literal["new_reference", "subscription_schedule"]

        class ModifyParamsLineAction(TypedDict):
            add_discount: NotRequired[
                "Quote.ModifyParamsLineActionAddDiscount|None"
            ]
            add_item: NotRequired["Quote.ModifyParamsLineActionAddItem|None"]
            add_metadata: NotRequired["Dict[str, str]|None"]
            remove_discount: NotRequired[
                "Quote.ModifyParamsLineActionRemoveDiscount|None"
            ]
            remove_item: NotRequired[
                "Quote.ModifyParamsLineActionRemoveItem|None"
            ]
            remove_metadata: NotRequired["List[str]|None"]
            set_discounts: NotRequired[
                "List[Quote.ModifyParamsLineActionSetDiscount]|None"
            ]
            set_items: NotRequired[
                "List[Quote.ModifyParamsLineActionSetItem]|None"
            ]
            set_metadata: NotRequired["Literal['']|Dict[str, str]|None"]
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

        class ModifyParamsLineActionSetItem(TypedDict):
            discounts: NotRequired[
                "List[Quote.ModifyParamsLineActionSetItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired["Quote.ModifyParamsLineActionSetItemTrial|None"]

        class ModifyParamsLineActionSetItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class ModifyParamsLineActionSetItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsLineActionSetItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsLineActionSetItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsLineActionSetItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsLineActionSetDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class ModifyParamsLineActionRemoveItem(TypedDict):
            price: str

        class ModifyParamsLineActionRemoveDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class ModifyParamsLineActionAddItem(TypedDict):
            discounts: NotRequired[
                "List[Quote.ModifyParamsLineActionAddItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired["Quote.ModifyParamsLineActionAddItemTrial|None"]

        class ModifyParamsLineActionAddItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class ModifyParamsLineActionAddItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsLineActionAddItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsLineActionAddItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsLineActionAddItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsLineActionAddDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsLineActionAddDiscountDiscountEnd|None"
            ]
            index: NotRequired["int|None"]

        class ModifyParamsLineActionAddDiscountDiscountEnd(TypedDict):
            type: Literal["line_ends_at"]

        class ModifyParamsLineItem(TypedDict):
            discounts: NotRequired[
                "Literal['']|List[Quote.ModifyParamsLineItemDiscount]|None"
            ]
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

        class ModifyParamsLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsLineItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsLineItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsLineItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsLineItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired["Quote.ModifyParamsInvoiceSettingsIssuer|None"]

        class ModifyParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Quote.ModifyParamsDiscountDiscountEnd|None"
            ]

        class ModifyParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Quote.ModifyParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Quote.ModifyParamsAutomaticTaxLiability|None"
            ]

        class ModifyParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ReestimateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListPreviewInvoicesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListPreviewSubscriptionSchedulesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

    allow_backdated_lines: Optional[bool]
    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: AutomaticTax
    collection_method: Literal["charge_automatically", "send_invoice"]
    computed: Computed
    created: int
    currency: Optional[str]
    customer: Optional[ExpandableField["Customer"]]
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    description: Optional[str]
    discounts: List[ExpandableField["DiscountResource"]]
    expires_at: int
    footer: Optional[str]
    from_quote: Optional[FromQuote]
    header: Optional[str]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_settings: Optional[InvoiceSettings]
    line_items: Optional[ListObject["LineItem"]]
    lines: Optional[List[str]]
    livemode: bool
    metadata: Dict[str, str]
    number: Optional[str]
    object: Literal["quote"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    status: Literal[
        "accepted", "accepting", "canceled", "draft", "open", "stale"
    ]
    status_details: Optional[StatusDetails]
    status_transitions: StatusTransitions
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_data: SubscriptionData
    subscription_data_overrides: Optional[List[SubscriptionDataOverride]]
    subscription_schedule: Optional[
        ExpandableField["SubscriptionScheduleResource"]
    ]
    subscription_schedules: Optional[List[SubscriptionSchedule]]
    test_clock: Optional[ExpandableField["TestClock"]]
    total_details: TotalDetails
    transfer_data: Optional[TransferData]

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
    def _cls_list_lines(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListLinesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/lines".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_lines")
    def list_lines(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListLinesParams"]
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/lines".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_preview_invoice_lines(
        cls,
        quote: str,
        preview_invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                quote=util.sanitize_id(quote),
                preview_invoice=util.sanitize_id(preview_invoice),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_preview_invoice_lines")
    def list_preview_invoice_lines(
        self,
        preview_invoice: str,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                quote=util.sanitize_id(self.get("id")),
                preview_invoice=util.sanitize_id(preview_invoice),
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_mark_draft(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.MarkDraftParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/mark_draft".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_draft")
    def mark_draft(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.MarkDraftParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/mark_draft".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_mark_stale(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.MarkStaleParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/mark_stale".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_stale")
    def mark_stale(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.MarkStaleParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/mark_stale".format(
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
    def _cls_reestimate(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ReestimateParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/reestimate".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reestimate")
    def reestimate(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ReestimateParams"]
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/reestimate".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
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

    @classmethod
    def list_preview_invoices(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListPreviewInvoicesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_invoices".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_preview_subscription_schedules(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListPreviewSubscriptionSchedulesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_subscription_schedules".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "computed": Computed,
        "from_quote": FromQuote,
        "invoice_settings": InvoiceSettings,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "subscription_data": SubscriptionData,
        "subscription_data_overrides": SubscriptionDataOverride,
        "subscription_schedules": SubscriptionSchedule,
        "total_details": TotalDetails,
        "transfer_data": TransferData,
    }
