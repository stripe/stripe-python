# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
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


class BillingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.bill_settings = BillSettingService(self._requestor)
        self.cadences = CadenceService(self._requestor)
        self.collection_settings = CollectionSettingService(self._requestor)
        self.custom_pricing_units = CustomPricingUnitService(self._requestor)
        self.intents = IntentService(self._requestor)
        self.license_fees = LicenseFeeService(self._requestor)
        self.license_fee_subscriptions = LicenseFeeSubscriptionService(
            self._requestor,
        )
        self.licensed_items = LicensedItemService(self._requestor)
        self.meter_events = MeterEventService(self._requestor)
        self.meter_event_adjustments = MeterEventAdjustmentService(
            self._requestor,
        )
        self.meter_event_session = MeterEventSessionService(self._requestor)
        self.meter_event_stream = MeterEventStreamService(self._requestor)
        self.metered_items = MeteredItemService(self._requestor)
        self.pricing_plans = PricingPlanService(self._requestor)
        self.pricing_plan_subscriptions = PricingPlanSubscriptionService(
            self._requestor,
        )
        self.profiles = ProfileService(self._requestor)
        self.rate_cards = RateCardService(self._requestor)
        self.rate_card_subscriptions = RateCardSubscriptionService(
            self._requestor,
        )
        self.service_actions = ServiceActionService(self._requestor)
