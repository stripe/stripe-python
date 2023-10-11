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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.coupon import Coupon
    from stripe.api_resources.customer import Customer
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
            enabled: bool

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            reset_billing_cycle_anchor: Optional[bool]

        class InvoiceSettings(StripeObject):
            days_until_due: Optional[int]

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
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]

        class AutomaticTax(StripeObject):
            enabled: bool

        class BillingThresholds(StripeObject):
            amount_gte: Optional[int]
            reset_billing_cycle_anchor: Optional[bool]

        class InvoiceSettings(StripeObject):
            days_until_due: Optional[int]

        class Item(StripeObject):
            class BillingThresholds(StripeObject):
                usage_gte: Optional[int]

            billing_thresholds: Optional[BillingThresholds]
            metadata: Optional[Dict[str, str]]
            plan: ExpandableField["Plan"]
            price: ExpandableField["Price"]
            quantity: Optional[int]
            tax_rates: Optional[List["TaxRate"]]
            _inner_class_types = {"billing_thresholds": BillingThresholds}

        class TransferData(StripeObject):
            amount_percent: Optional[float]
            destination: ExpandableField["Account"]

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
        end_date: int
        invoice_settings: Optional[InvoiceSettings]
        items: List[Item]
        metadata: Optional[Dict[str, str]]
        on_behalf_of: Optional[ExpandableField["Account"]]
        proration_behavior: Literal[
            "always_invoice", "create_prorations", "none"
        ]
        start_date: int
        transfer_data: Optional[TransferData]
        trial_end: Optional[int]
        _inner_class_types = {
            "add_invoice_items": AddInvoiceItem,
            "automatic_tax": AutomaticTax,
            "billing_thresholds": BillingThresholds,
            "invoice_settings": InvoiceSettings,
            "items": Item,
            "transfer_data": TransferData,
        }

    application: Optional[ExpandableField["Application"]]
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
    released_at: Optional[int]
    released_subscription: Optional[str]
    status: Literal[
        "active", "canceled", "completed", "not_started", "released"
    ]
    subscription: Optional[ExpandableField["Subscription"]]
    test_clock: Optional[ExpandableField["TestClock"]]

    @classmethod
    def _cls_cancel(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
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
        **params: Any
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "SubscriptionSchedule":
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
        **params: Any
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
    def release(self, idempotency_key: Optional[str] = None, **params: Any):
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "SubscriptionSchedule":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "current_phase": CurrentPhase,
        "default_settings": DefaultSettings,
        "phases": Phase,
    }
