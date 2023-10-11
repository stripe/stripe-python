# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

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


class QuotePreviewSubscriptionSchedule(
    ListableAPIResource["QuotePreviewSubscriptionSchedule"],
):
    OBJECT_NAME = "quote_preview_subscription_schedule"

    class AppliesTo(StripeObject):
        new_reference: Optional[str]
        subscription_schedule: Optional[str]
        type: Literal["new_reference", "subscription_schedule"]

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

    application: Optional[ExpandableField["Application"]]
    applies_to: AppliesTo
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
    object: Literal["quote_preview_subscription_schedule"]
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["QuotePreviewSubscriptionSchedule"]:
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

    _inner_class_types = {
        "applies_to": AppliesTo,
        "current_phase": CurrentPhase,
        "default_settings": DefaultSettings,
        "phases": Phase,
        "prebilling": Prebilling,
    }
