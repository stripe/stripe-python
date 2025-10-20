# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._bill_setting_service import BillSettingService
    from stripe.v2.billing._cadence_service import CadenceService
    from stripe.v2.billing._collection_setting_service import (
        CollectionSettingService,
    )
    from stripe.v2.billing._custom_pricing_unit_service import (
        CustomPricingUnitService,
    )
    from stripe.v2.billing._intent_service import IntentService
    from stripe.v2.billing._license_fee_service import LicenseFeeService
    from stripe.v2.billing._license_fee_subscription_service import (
        LicenseFeeSubscriptionService,
    )
    from stripe.v2.billing._licensed_item_service import LicensedItemService
    from stripe.v2.billing._meter_event_adjustment_service import (
        MeterEventAdjustmentService,
    )
    from stripe.v2.billing._meter_event_service import MeterEventService
    from stripe.v2.billing._meter_event_session_service import (
        MeterEventSessionService,
    )
    from stripe.v2.billing._meter_event_stream_service import (
        MeterEventStreamService,
    )
    from stripe.v2.billing._metered_item_service import MeteredItemService
    from stripe.v2.billing._pricing_plan_service import PricingPlanService
    from stripe.v2.billing._pricing_plan_subscription_service import (
        PricingPlanSubscriptionService,
    )
    from stripe.v2.billing._profile_service import ProfileService
    from stripe.v2.billing._rate_card_service import RateCardService
    from stripe.v2.billing._rate_card_subscription_service import (
        RateCardSubscriptionService,
    )
    from stripe.v2.billing._service_action_service import ServiceActionService

_subservices = {
    "bill_settings": [
        "stripe.v2.billing._bill_setting_service",
        "BillSettingService",
    ],
    "cadences": ["stripe.v2.billing._cadence_service", "CadenceService"],
    "collection_settings": [
        "stripe.v2.billing._collection_setting_service",
        "CollectionSettingService",
    ],
    "custom_pricing_units": [
        "stripe.v2.billing._custom_pricing_unit_service",
        "CustomPricingUnitService",
    ],
    "intents": ["stripe.v2.billing._intent_service", "IntentService"],
    "license_fees": [
        "stripe.v2.billing._license_fee_service",
        "LicenseFeeService",
    ],
    "license_fee_subscriptions": [
        "stripe.v2.billing._license_fee_subscription_service",
        "LicenseFeeSubscriptionService",
    ],
    "licensed_items": [
        "stripe.v2.billing._licensed_item_service",
        "LicensedItemService",
    ],
    "meter_events": [
        "stripe.v2.billing._meter_event_service",
        "MeterEventService",
    ],
    "meter_event_adjustments": [
        "stripe.v2.billing._meter_event_adjustment_service",
        "MeterEventAdjustmentService",
    ],
    "meter_event_session": [
        "stripe.v2.billing._meter_event_session_service",
        "MeterEventSessionService",
    ],
    "meter_event_stream": [
        "stripe.v2.billing._meter_event_stream_service",
        "MeterEventStreamService",
    ],
    "metered_items": [
        "stripe.v2.billing._metered_item_service",
        "MeteredItemService",
    ],
    "pricing_plans": [
        "stripe.v2.billing._pricing_plan_service",
        "PricingPlanService",
    ],
    "pricing_plan_subscriptions": [
        "stripe.v2.billing._pricing_plan_subscription_service",
        "PricingPlanSubscriptionService",
    ],
    "profiles": ["stripe.v2.billing._profile_service", "ProfileService"],
    "rate_cards": ["stripe.v2.billing._rate_card_service", "RateCardService"],
    "rate_card_subscriptions": [
        "stripe.v2.billing._rate_card_subscription_service",
        "RateCardSubscriptionService",
    ],
    "service_actions": [
        "stripe.v2.billing._service_action_service",
        "ServiceActionService",
    ],
}


class BillingService(StripeService):
    bill_settings: "BillSettingService"
    cadences: "CadenceService"
    collection_settings: "CollectionSettingService"
    custom_pricing_units: "CustomPricingUnitService"
    intents: "IntentService"
    license_fees: "LicenseFeeService"
    license_fee_subscriptions: "LicenseFeeSubscriptionService"
    licensed_items: "LicensedItemService"
    meter_events: "MeterEventService"
    meter_event_adjustments: "MeterEventAdjustmentService"
    meter_event_session: "MeterEventSessionService"
    meter_event_stream: "MeterEventStreamService"
    metered_items: "MeteredItemService"
    pricing_plans: "PricingPlanService"
    pricing_plan_subscriptions: "PricingPlanSubscriptionService"
    profiles: "ProfileService"
    rate_cards: "RateCardService"
    rate_card_subscriptions: "RateCardSubscriptionService"
    service_actions: "ServiceActionService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
