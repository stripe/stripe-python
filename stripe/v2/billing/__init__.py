# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing import (
        bill_settings as bill_settings,
        collection_settings as collection_settings,
        intents as intents,
        license_fees as license_fees,
        pricing_plan_subscriptions as pricing_plan_subscriptions,
        pricing_plans as pricing_plans,
        rate_cards as rate_cards,
    )
    from stripe.v2.billing._bill_setting import BillSetting as BillSetting
    from stripe.v2.billing._bill_setting_service import (
        BillSettingService as BillSettingService,
    )
    from stripe.v2.billing._bill_setting_version import (
        BillSettingVersion as BillSettingVersion,
    )
    from stripe.v2.billing._cadence import Cadence as Cadence
    from stripe.v2.billing._cadence_service import (
        CadenceService as CadenceService,
    )
    from stripe.v2.billing._collection_setting import (
        CollectionSetting as CollectionSetting,
    )
    from stripe.v2.billing._collection_setting_service import (
        CollectionSettingService as CollectionSettingService,
    )
    from stripe.v2.billing._collection_setting_version import (
        CollectionSettingVersion as CollectionSettingVersion,
    )
    from stripe.v2.billing._custom_pricing_unit import (
        CustomPricingUnit as CustomPricingUnit,
    )
    from stripe.v2.billing._custom_pricing_unit_service import (
        CustomPricingUnitService as CustomPricingUnitService,
    )
    from stripe.v2.billing._intent import Intent as Intent
    from stripe.v2.billing._intent_action import IntentAction as IntentAction
    from stripe.v2.billing._intent_service import (
        IntentService as IntentService,
    )
    from stripe.v2.billing._license_fee import LicenseFee as LicenseFee
    from stripe.v2.billing._license_fee_service import (
        LicenseFeeService as LicenseFeeService,
    )
    from stripe.v2.billing._license_fee_subscription import (
        LicenseFeeSubscription as LicenseFeeSubscription,
    )
    from stripe.v2.billing._license_fee_subscription_service import (
        LicenseFeeSubscriptionService as LicenseFeeSubscriptionService,
    )
    from stripe.v2.billing._license_fee_version import (
        LicenseFeeVersion as LicenseFeeVersion,
    )
    from stripe.v2.billing._licensed_item import LicensedItem as LicensedItem
    from stripe.v2.billing._licensed_item_service import (
        LicensedItemService as LicensedItemService,
    )
    from stripe.v2.billing._meter_event import MeterEvent as MeterEvent
    from stripe.v2.billing._meter_event_adjustment import (
        MeterEventAdjustment as MeterEventAdjustment,
    )
    from stripe.v2.billing._meter_event_adjustment_service import (
        MeterEventAdjustmentService as MeterEventAdjustmentService,
    )
    from stripe.v2.billing._meter_event_service import (
        MeterEventService as MeterEventService,
    )
    from stripe.v2.billing._meter_event_session import (
        MeterEventSession as MeterEventSession,
    )
    from stripe.v2.billing._meter_event_session_service import (
        MeterEventSessionService as MeterEventSessionService,
    )
    from stripe.v2.billing._meter_event_stream_service import (
        MeterEventStreamService as MeterEventStreamService,
    )
    from stripe.v2.billing._metered_item import MeteredItem as MeteredItem
    from stripe.v2.billing._metered_item_service import (
        MeteredItemService as MeteredItemService,
    )
    from stripe.v2.billing._pricing_plan import PricingPlan as PricingPlan
    from stripe.v2.billing._pricing_plan_component import (
        PricingPlanComponent as PricingPlanComponent,
    )
    from stripe.v2.billing._pricing_plan_service import (
        PricingPlanService as PricingPlanService,
    )
    from stripe.v2.billing._pricing_plan_subscription import (
        PricingPlanSubscription as PricingPlanSubscription,
    )
    from stripe.v2.billing._pricing_plan_subscription_components import (
        PricingPlanSubscriptionComponents as PricingPlanSubscriptionComponents,
    )
    from stripe.v2.billing._pricing_plan_subscription_service import (
        PricingPlanSubscriptionService as PricingPlanSubscriptionService,
    )
    from stripe.v2.billing._pricing_plan_version import (
        PricingPlanVersion as PricingPlanVersion,
    )
    from stripe.v2.billing._profile import Profile as Profile
    from stripe.v2.billing._profile_service import (
        ProfileService as ProfileService,
    )
    from stripe.v2.billing._rate_card import RateCard as RateCard
    from stripe.v2.billing._rate_card_rate import RateCardRate as RateCardRate
    from stripe.v2.billing._rate_card_service import (
        RateCardService as RateCardService,
    )
    from stripe.v2.billing._rate_card_subscription import (
        RateCardSubscription as RateCardSubscription,
    )
    from stripe.v2.billing._rate_card_subscription_service import (
        RateCardSubscriptionService as RateCardSubscriptionService,
    )
    from stripe.v2.billing._rate_card_version import (
        RateCardVersion as RateCardVersion,
    )
    from stripe.v2.billing._service_action import (
        ServiceAction as ServiceAction,
    )
    from stripe.v2.billing._service_action_service import (
        ServiceActionService as ServiceActionService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "bill_settings": ("stripe.v2.billing.bill_settings", True),
    "collection_settings": ("stripe.v2.billing.collection_settings", True),
    "intents": ("stripe.v2.billing.intents", True),
    "license_fees": ("stripe.v2.billing.license_fees", True),
    "pricing_plan_subscriptions": (
        "stripe.v2.billing.pricing_plan_subscriptions",
        True,
    ),
    "pricing_plans": ("stripe.v2.billing.pricing_plans", True),
    "rate_cards": ("stripe.v2.billing.rate_cards", True),
    "BillSetting": ("stripe.v2.billing._bill_setting", False),
    "BillSettingService": ("stripe.v2.billing._bill_setting_service", False),
    "BillSettingVersion": ("stripe.v2.billing._bill_setting_version", False),
    "Cadence": ("stripe.v2.billing._cadence", False),
    "CadenceService": ("stripe.v2.billing._cadence_service", False),
    "CollectionSetting": ("stripe.v2.billing._collection_setting", False),
    "CollectionSettingService": (
        "stripe.v2.billing._collection_setting_service",
        False,
    ),
    "CollectionSettingVersion": (
        "stripe.v2.billing._collection_setting_version",
        False,
    ),
    "CustomPricingUnit": ("stripe.v2.billing._custom_pricing_unit", False),
    "CustomPricingUnitService": (
        "stripe.v2.billing._custom_pricing_unit_service",
        False,
    ),
    "Intent": ("stripe.v2.billing._intent", False),
    "IntentAction": ("stripe.v2.billing._intent_action", False),
    "IntentService": ("stripe.v2.billing._intent_service", False),
    "LicenseFee": ("stripe.v2.billing._license_fee", False),
    "LicenseFeeService": ("stripe.v2.billing._license_fee_service", False),
    "LicenseFeeSubscription": (
        "stripe.v2.billing._license_fee_subscription",
        False,
    ),
    "LicenseFeeSubscriptionService": (
        "stripe.v2.billing._license_fee_subscription_service",
        False,
    ),
    "LicenseFeeVersion": ("stripe.v2.billing._license_fee_version", False),
    "LicensedItem": ("stripe.v2.billing._licensed_item", False),
    "LicensedItemService": ("stripe.v2.billing._licensed_item_service", False),
    "MeterEvent": ("stripe.v2.billing._meter_event", False),
    "MeterEventAdjustment": (
        "stripe.v2.billing._meter_event_adjustment",
        False,
    ),
    "MeterEventAdjustmentService": (
        "stripe.v2.billing._meter_event_adjustment_service",
        False,
    ),
    "MeterEventService": ("stripe.v2.billing._meter_event_service", False),
    "MeterEventSession": ("stripe.v2.billing._meter_event_session", False),
    "MeterEventSessionService": (
        "stripe.v2.billing._meter_event_session_service",
        False,
    ),
    "MeterEventStreamService": (
        "stripe.v2.billing._meter_event_stream_service",
        False,
    ),
    "MeteredItem": ("stripe.v2.billing._metered_item", False),
    "MeteredItemService": ("stripe.v2.billing._metered_item_service", False),
    "PricingPlan": ("stripe.v2.billing._pricing_plan", False),
    "PricingPlanComponent": (
        "stripe.v2.billing._pricing_plan_component",
        False,
    ),
    "PricingPlanService": ("stripe.v2.billing._pricing_plan_service", False),
    "PricingPlanSubscription": (
        "stripe.v2.billing._pricing_plan_subscription",
        False,
    ),
    "PricingPlanSubscriptionComponents": (
        "stripe.v2.billing._pricing_plan_subscription_components",
        False,
    ),
    "PricingPlanSubscriptionService": (
        "stripe.v2.billing._pricing_plan_subscription_service",
        False,
    ),
    "PricingPlanVersion": ("stripe.v2.billing._pricing_plan_version", False),
    "Profile": ("stripe.v2.billing._profile", False),
    "ProfileService": ("stripe.v2.billing._profile_service", False),
    "RateCard": ("stripe.v2.billing._rate_card", False),
    "RateCardRate": ("stripe.v2.billing._rate_card_rate", False),
    "RateCardService": ("stripe.v2.billing._rate_card_service", False),
    "RateCardSubscription": (
        "stripe.v2.billing._rate_card_subscription",
        False,
    ),
    "RateCardSubscriptionService": (
        "stripe.v2.billing._rate_card_subscription_service",
        False,
    ),
    "RateCardVersion": ("stripe.v2.billing._rate_card_version", False),
    "ServiceAction": ("stripe.v2.billing._service_action", False),
    "ServiceActionService": (
        "stripe.v2.billing._service_action_service",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
