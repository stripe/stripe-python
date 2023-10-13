# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
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
    from stripe.api_resources.coupon import Coupon
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.plan import Plan
    from stripe.api_resources.price import Price
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class SubscriptionSchedule(
    CreateableAPIResource["SubscriptionSchedule"],
    ListableAPIResource["SubscriptionSchedule"],
    UpdateableAPIResource["SubscriptionSchedule"],
):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)
    """

    OBJECT_NAME = "subscription_schedule"

    class CurrentPhase(StripeObject):
        end_date: int
        start_date: int

    class DefaultSettings(StripeObject):
        class AutomaticTax(StripeObject):
            class Liability(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            enabled: bool
            liability: Optional[Liability]
            _inner_class_types = {"liability": Liability}

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            reset_billing_cycle_anchor: Optional[bool]

        class InvoiceSettings(StripeObject):
            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            days_until_due: Optional[int]
            issuer: Optional[Issuer]
            _inner_class_types = {"issuer": Issuer}

        class TransferData(StripeObject):
            amount_percent: Optional[float]
            destination: ExpandableField["Account"]

        application_fee_percent: Optional[float]
        automatic_tax: Optional[AutomaticTax]
        billing_cycle_anchor: Literal["automatic", "phase_start"]
        billing_thresholds: Optional[BillingThresholds]
        collection_method: Optional[
            Literal["charge_automatically", "send_invoice"]
        ]
        default_payment_method: Optional[ExpandableField["PaymentMethod"]]
        description: Optional[str]
        invoice_settings: Optional[InvoiceSettings]
        on_behalf_of: Optional[ExpandableField["Account"]]
        transfer_data: Optional[TransferData]
        _inner_class_types = {
            "automatic_tax": AutomaticTax,
            "billing_thresholds": BillingThresholds,
            "invoice_settings": InvoiceSettings,
            "transfer_data": TransferData,
        }

    class Phase(StripeObject):
        class AddInvoiceItem(StripeObject):
            class Discount(StripeObject):
                class DiscountEnd(StripeObject):
                    timestamp: Optional[int]
                    type: Literal["timestamp"]

                coupon: Optional[ExpandableField["Coupon"]]
                discount: Optional[ExpandableField["DiscountResource"]]
                discount_end: Optional[DiscountEnd]
                _inner_class_types = {"discount_end": DiscountEnd}

            discounts: Optional[List[Discount]]
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]
            _inner_class_types = {"discounts": Discount}

        class AutomaticTax(StripeObject):
            class Liability(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            enabled: bool
            liability: Optional[Liability]
            _inner_class_types = {"liability": Liability}

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            reset_billing_cycle_anchor: Optional[bool]

        class Discount(StripeObject):
            class DiscountEnd(StripeObject):
                timestamp: Optional[int]
                type: Literal["timestamp"]

            coupon: Optional[ExpandableField["Coupon"]]
            discount: Optional[ExpandableField["DiscountResource"]]
            discount_end: Optional[DiscountEnd]
            _inner_class_types = {"discount_end": DiscountEnd}

        class InvoiceSettings(StripeObject):
            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            days_until_due: Optional[int]
            issuer: Optional[Issuer]
            _inner_class_types = {"issuer": Issuer}

        class Item(StripeObject):
            class BillingThresholds(StripeObject):
                usage_gte: Optional[int]

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

            billing_thresholds: Optional[BillingThresholds]
            discounts: Optional[List[Discount]]
            metadata: Optional[Dict[str, str]]
            plan: ExpandableField["Plan"]
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]
            trial: Optional[Trial]
            _inner_class_types = {
                "billing_thresholds": BillingThresholds,
                "discounts": Discount,
                "trial": Trial,
            }

        class PauseCollection(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class TransferData(StripeObject):
            amount_percent: Optional[float]
            destination: ExpandableField["Account"]

        class TrialSettings(StripeObject):
            class EndBehavior(StripeObject):
                prorate_up_front: Optional[Literal["defer", "include"]]

            end_behavior: Optional[EndBehavior]
            _inner_class_types = {"end_behavior": EndBehavior}

        add_invoice_items: List[AddInvoiceItem]
        application_fee_percent: Optional[float]
        automatic_tax: Optional[AutomaticTax]
        billing_cycle_anchor: Optional[Literal["automatic", "phase_start"]]
        billing_thresholds: Optional[BillingThresholds]
        collection_method: Optional[
            Literal["charge_automatically", "send_invoice"]
        ]
        coupon: Optional[ExpandableField["Coupon"]]
        currency: str
        default_payment_method: Optional[ExpandableField["PaymentMethod"]]
        default_tax_rates: Optional[List["TaxRate"]]
        description: Optional[str]
        discounts: Optional[List[Discount]]
        end_date: int
        invoice_settings: Optional[InvoiceSettings]
        items: List[Item]
        metadata: Optional[Dict[str, str]]
        on_behalf_of: Optional[ExpandableField["Account"]]
        pause_collection: Optional[PauseCollection]
        proration_behavior: Literal[
            "always_invoice", "create_prorations", "none"
        ]
        start_date: int
        transfer_data: Optional[TransferData]
        trial_continuation: Optional[Literal["continue", "none"]]
        trial_end: Optional[int]
        trial_settings: Optional[TrialSettings]
        _inner_class_types = {
            "add_invoice_items": AddInvoiceItem,
            "automatic_tax": AutomaticTax,
            "billing_thresholds": BillingThresholds,
            "discounts": Discount,
            "invoice_settings": InvoiceSettings,
            "items": Item,
            "pause_collection": PauseCollection,
            "transfer_data": TransferData,
            "trial_settings": TrialSettings,
        }

    class Prebilling(StripeObject):
        invoice: ExpandableField["Invoice"]
        period_end: int
        period_start: int
        update_behavior: Optional[Literal["prebill", "reset"]]

    if TYPE_CHECKING:

        class AmendParams(RequestOptions):
            amendments: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendment]|None"
            ]
            expand: NotRequired["List[str]|None"]
            prebilling: NotRequired[
                "Literal['']|List[SubscriptionSchedule.AmendParamsPrebilling]|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            schedule_settings: NotRequired[
                "SubscriptionSchedule.AmendParamsScheduleSettings|None"
            ]

        class AmendParamsScheduleSettings(TypedDict):
            end_behavior: NotRequired["Literal['cancel', 'release']|None"]

        class AmendParamsPrebilling(TypedDict):
            bill_from: NotRequired[
                "SubscriptionSchedule.AmendParamsPrebillingBillFrom|None"
            ]
            bill_until: NotRequired[
                "SubscriptionSchedule.AmendParamsPrebillingBillUntil|None"
            ]
            invoice_at: NotRequired["Literal['now']|None"]
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]

        class AmendParamsPrebillingBillUntil(TypedDict):
            amendment_end: NotRequired[
                "SubscriptionSchedule.AmendParamsPrebillingBillUntilAmendmentEnd|None"
            ]
            duration: NotRequired[
                "SubscriptionSchedule.AmendParamsPrebillingBillUntilDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "amendment_end", "duration", "schedule_end", "timestamp"
            ]

        class AmendParamsPrebillingBillUntilDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class AmendParamsPrebillingBillUntilAmendmentEnd(TypedDict):
            index: int

        class AmendParamsPrebillingBillFrom(TypedDict):
            amendment_start: NotRequired[
                "SubscriptionSchedule.AmendParamsPrebillingBillFromAmendmentStart|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["amendment_start", "now", "timestamp"]

        class AmendParamsPrebillingBillFromAmendmentStart(TypedDict):
            index: int

        class AmendParamsAmendment(TypedDict):
            amendment_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentAmendmentEnd|None"
            ]
            amendment_start: "SubscriptionSchedule.AmendParamsAmendmentAmendmentStart"
            billing_cycle_anchor: NotRequired[
                "Literal['amendment_start', 'automatic']|None"
            ]
            discount_actions: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendmentDiscountAction]|None"
            ]
            item_actions: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendmentItemAction]|None"
            ]
            metadata_actions: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendmentMetadataAction]|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            set_pause_collection: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentSetPauseCollection|None"
            ]
            set_schedule_end: NotRequired[
                "Literal['amendment_end', 'amendment_start']|None"
            ]
            trial_settings: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentTrialSettings|None"
            ]

        class AmendParamsAmendmentTrialSettings(TypedDict):
            end_behavior: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentTrialSettingsEndBehavior|None"
            ]

        class AmendParamsAmendmentTrialSettingsEndBehavior(TypedDict):
            prorate_up_front: NotRequired["Literal['defer', 'include']|None"]

        class AmendParamsAmendmentSetPauseCollection(TypedDict):
            set: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentSetPauseCollectionSet|None"
            ]
            type: Literal["remove", "set"]

        class AmendParamsAmendmentSetPauseCollectionSet(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class AmendParamsAmendmentMetadataAction(TypedDict):
            add: NotRequired["Dict[str, str]|None"]
            remove: NotRequired["List[str]|None"]
            set: NotRequired["Literal['']|Dict[str, str]|None"]
            type: Literal["add", "remove", "set"]

        class AmendParamsAmendmentItemAction(TypedDict):
            add: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionAdd|None"
            ]
            remove: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionRemove|None"
            ]
            set: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionSet|None"
            ]
            type: Literal["add", "remove", "set"]

        class AmendParamsAmendmentItemActionSet(TypedDict):
            discounts: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendmentItemActionSetDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionSetTrial|None"
            ]

        class AmendParamsAmendmentItemActionSetTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class AmendParamsAmendmentItemActionSetDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionSetDiscountDiscountEnd|None"
            ]

        class AmendParamsAmendmentItemActionSetDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionSetDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class AmendParamsAmendmentItemActionSetDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class AmendParamsAmendmentItemActionRemove(TypedDict):
            price: str

        class AmendParamsAmendmentItemActionAdd(TypedDict):
            discounts: NotRequired[
                "List[SubscriptionSchedule.AmendParamsAmendmentItemActionAddDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            price: str
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]
            trial: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionAddTrial|None"
            ]

        class AmendParamsAmendmentItemActionAddTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class AmendParamsAmendmentItemActionAddDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionAddDiscountDiscountEnd|None"
            ]

        class AmendParamsAmendmentItemActionAddDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentItemActionAddDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class AmendParamsAmendmentItemActionAddDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class AmendParamsAmendmentDiscountAction(TypedDict):
            add: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentDiscountActionAdd|None"
            ]
            remove: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentDiscountActionRemove|None"
            ]
            set: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentDiscountActionSet|None"
            ]
            type: Literal["add", "remove", "set"]

        class AmendParamsAmendmentDiscountActionSet(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class AmendParamsAmendmentDiscountActionRemove(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class AmendParamsAmendmentDiscountActionAdd(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentDiscountActionAddDiscountEnd|None"
            ]
            index: NotRequired["int|None"]

        class AmendParamsAmendmentDiscountActionAddDiscountEnd(TypedDict):
            type: Literal["amendment_end"]

        class AmendParamsAmendmentAmendmentStart(TypedDict):
            amendment_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentAmendmentStartAmendmentEnd|None"
            ]
            discount_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentAmendmentStartDiscountEnd|None"
            ]
            timestamp: NotRequired["int|None"]
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

        class AmendParamsAmendmentAmendmentStartDiscountEnd(TypedDict):
            discount: str

        class AmendParamsAmendmentAmendmentStartAmendmentEnd(TypedDict):
            index: int

        class AmendParamsAmendmentAmendmentEnd(TypedDict):
            discount_end: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentAmendmentEndDiscountEnd|None"
            ]
            duration: NotRequired[
                "SubscriptionSchedule.AmendParamsAmendmentAmendmentEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal[
                "discount_end",
                "duration",
                "schedule_end",
                "timestamp",
                "trial_end",
                "trial_start",
                "upcoming_invoice",
            ]

        class AmendParamsAmendmentAmendmentEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class AmendParamsAmendmentAmendmentEndDiscountEnd(TypedDict):
            discount: str

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            invoice_now: NotRequired["bool|None"]
            prorate: NotRequired["bool|None"]

        class CreateParams(RequestOptions):
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            customer: NotRequired["str|None"]
            default_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettings|None"
            ]
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            expand: NotRequired["List[str]|None"]
            from_subscription: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            phases: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhase]|None"
            ]
            prebilling: NotRequired[
                "SubscriptionSchedule.CreateParamsPrebilling|None"
            ]
            start_date: NotRequired["int|Literal['now']|None"]

        class CreateParamsPrebilling(TypedDict):
            iterations: int
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]

        class CreateParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            default_payment_method: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[SubscriptionSchedule.CreateParamsPhaseDiscount]|None"
            ]
            end_date: NotRequired["int|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseInvoiceSettings|None"
            ]
            items: List["SubscriptionSchedule.CreateParamsPhaseItem"]
            iterations: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            pause_collection: NotRequired[
                "SubscriptionSchedule.CreateParamsPhasePauseCollection|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            transfer_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseTransferData|None"
            ]
            trial: NotRequired["bool|None"]
            trial_continuation: NotRequired["Literal['continue', 'none']|None"]
            trial_end: NotRequired["int|None"]
            trial_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseTrialSettings|None"
            ]

        class CreateParamsPhaseTrialSettings(TypedDict):
            end_behavior: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseTrialSettingsEndBehavior|None"
            ]

        class CreateParamsPhaseTrialSettingsEndBehavior(TypedDict):
            prorate_up_front: NotRequired["Literal['defer', 'include']|None"]

        class CreateParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsPhasePauseCollection(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class CreateParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseItemBillingThresholds|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[SubscriptionSchedule.CreateParamsPhaseItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            trial: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemTrial|None"
            ]

        class CreateParamsPhaseItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class CreateParamsPhaseItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionSchedule.CreateParamsPhaseItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsPhaseItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemDiscountDiscountEnd|None"
            ]

        class CreateParamsPhaseItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsPhaseItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int

        class CreateParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseInvoiceSettingsIssuer|None"
            ]

        class CreateParamsPhaseInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsPhaseDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseDiscountDiscountEnd|None"
            ]

        class CreateParamsPhaseDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsPhaseDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class CreateParamsPhaseAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAutomaticTaxLiability|None"
            ]

        class CreateParamsPhaseAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsPhaseAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPhaseAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemDiscountDiscountEnd|None"
            ]

        class CreateParamsPhaseAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsPhaseAddInvoiceItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_payment_method: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsInvoiceSettings|None"
            ]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsTransferData|None"
            ]

        class CreateParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsInvoiceSettingsIssuer|None"
            ]

        class CreateParamsDefaultSettingsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class CreateParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsAutomaticTaxLiability|None"
            ]

        class CreateParamsDefaultSettingsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ListParams(RequestOptions):
            canceled_at: NotRequired[
                "SubscriptionSchedule.ListParamsCanceledAt|int|None"
            ]
            completed_at: NotRequired[
                "SubscriptionSchedule.ListParamsCompletedAt|int|None"
            ]
            created: NotRequired[
                "SubscriptionSchedule.ListParamsCreated|int|None"
            ]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            released_at: NotRequired[
                "SubscriptionSchedule.ListParamsReleasedAt|int|None"
            ]
            scheduled: NotRequired["bool|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsReleasedAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCompletedAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCanceledAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            billing_behavior: NotRequired[
                "Literal['prorate_on_next_phase', 'prorate_up_front']|None"
            ]
            default_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettings|None"
            ]
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            phases: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhase]|None"
            ]
            prebilling: NotRequired[
                "SubscriptionSchedule.ModifyParamsPrebilling|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class ModifyParamsPrebilling(TypedDict):
            iterations: int
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]

        class ModifyParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            default_payment_method: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[SubscriptionSchedule.ModifyParamsPhaseDiscount]|None"
            ]
            end_date: NotRequired["int|Literal['now']|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseInvoiceSettings|None"
            ]
            items: List["SubscriptionSchedule.ModifyParamsPhaseItem"]
            iterations: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            pause_collection: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhasePauseCollection|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            start_date: NotRequired["int|Literal['now']|None"]
            transfer_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseTransferData|None"
            ]
            trial: NotRequired["bool|None"]
            trial_continuation: NotRequired["Literal['continue', 'none']|None"]
            trial_end: NotRequired["int|Literal['now']|None"]
            trial_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseTrialSettings|None"
            ]

        class ModifyParamsPhaseTrialSettings(TypedDict):
            end_behavior: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseTrialSettingsEndBehavior|None"
            ]

        class ModifyParamsPhaseTrialSettingsEndBehavior(TypedDict):
            prorate_up_front: NotRequired["Literal['defer', 'include']|None"]

        class ModifyParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsPhasePauseCollection(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]

        class ModifyParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseItemBillingThresholds|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[SubscriptionSchedule.ModifyParamsPhaseItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            trial: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemTrial|None"
            ]

        class ModifyParamsPhaseItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class ModifyParamsPhaseItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionSchedule.ModifyParamsPhaseItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsPhaseItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsPhaseItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsPhaseItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int

        class ModifyParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseInvoiceSettingsIssuer|None"
            ]

        class ModifyParamsPhaseInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsPhaseDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseDiscountDiscountEnd|None"
            ]

        class ModifyParamsPhaseDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsPhaseDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class ModifyParamsPhaseAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAutomaticTaxLiability|None"
            ]

        class ModifyParamsPhaseAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsPhaseAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPhaseAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsPhaseAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsPhaseAddInvoiceItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_payment_method: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsInvoiceSettings|None"
            ]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsTransferData|None"
            ]

        class ModifyParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            issuer: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsInvoiceSettingsIssuer|None"
            ]

        class ModifyParamsDefaultSettingsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class ModifyParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsAutomaticTaxLiability|None"
            ]

        class ModifyParamsDefaultSettingsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ReleaseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            preserve_cancel_date: NotRequired["bool|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    application: Optional[ExpandableField["Application"]]
    billing_behavior: Optional[
        Literal["prorate_on_next_phase", "prorate_up_front"]
    ]
    canceled_at: Optional[int]
    completed_at: Optional[int]
    created: int
    current_phase: Optional[CurrentPhase]
    customer: ExpandableField["Customer"]
    default_settings: DefaultSettings
    end_behavior: Literal["cancel", "none", "release", "renew"]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["subscription_schedule"]
    phases: List[Phase]
    prebilling: Optional[Prebilling]
    released_at: Optional[int]
    released_subscription: Optional[str]
    status: Literal[
        "active", "canceled", "completed", "not_started", "released"
    ]
    subscription: Optional[ExpandableField["Subscription"]]
    test_clock: Optional[ExpandableField["TestClock"]]

    @classmethod
    def _cls_amend(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.AmendParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/amend".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_amend")
    def amend(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.AmendParams"]
    ):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/amend".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(self.get("id"))
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
        **params: Unpack["SubscriptionSchedule.CreateParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ListParams"]
    ) -> ListObject["SubscriptionSchedule"]:
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
        cls, id, **params: Unpack["SubscriptionSchedule.ModifyParams"]
    ) -> "SubscriptionSchedule":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SubscriptionSchedule",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_release(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_release")
    def release(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SubscriptionSchedule.RetrieveParams"]
    ) -> "SubscriptionSchedule":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "current_phase": CurrentPhase,
        "default_settings": DefaultSettings,
        "phases": Phase,
        "prebilling": Prebilling,
    }
