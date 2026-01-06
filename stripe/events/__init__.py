# -*- coding: utf-8 -*-

from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import (
    UnknownEventNotification as UnknownEventNotification,
)


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.events._event_classes import (
        ALL_EVENT_NOTIFICATIONS as ALL_EVENT_NOTIFICATIONS,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEvent as V1BillingMeterErrorReportTriggeredEvent,
        V1BillingMeterErrorReportTriggeredEventNotification as V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEvent as V1BillingMeterNoMeterFoundEvent,
        V1BillingMeterNoMeterFoundEventNotification as V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_billing_cadence_billed_event import (
        V2BillingCadenceBilledEvent as V2BillingCadenceBilledEvent,
        V2BillingCadenceBilledEventNotification as V2BillingCadenceBilledEventNotification,
    )
    from stripe.events._v2_billing_cadence_canceled_event import (
        V2BillingCadenceCanceledEvent as V2BillingCadenceCanceledEvent,
        V2BillingCadenceCanceledEventNotification as V2BillingCadenceCanceledEventNotification,
    )
    from stripe.events._v2_billing_cadence_created_event import (
        V2BillingCadenceCreatedEvent as V2BillingCadenceCreatedEvent,
        V2BillingCadenceCreatedEventNotification as V2BillingCadenceCreatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_created_event import (
        V2BillingLicenseFeeCreatedEvent as V2BillingLicenseFeeCreatedEvent,
        V2BillingLicenseFeeCreatedEventNotification as V2BillingLicenseFeeCreatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_updated_event import (
        V2BillingLicenseFeeUpdatedEvent as V2BillingLicenseFeeUpdatedEvent,
        V2BillingLicenseFeeUpdatedEventNotification as V2BillingLicenseFeeUpdatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_version_created_event import (
        V2BillingLicenseFeeVersionCreatedEvent as V2BillingLicenseFeeVersionCreatedEvent,
        V2BillingLicenseFeeVersionCreatedEventNotification as V2BillingLicenseFeeVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_created_event import (
        V2BillingLicensedItemCreatedEvent as V2BillingLicensedItemCreatedEvent,
        V2BillingLicensedItemCreatedEventNotification as V2BillingLicensedItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_updated_event import (
        V2BillingLicensedItemUpdatedEvent as V2BillingLicensedItemUpdatedEvent,
        V2BillingLicensedItemUpdatedEventNotification as V2BillingLicensedItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_created_event import (
        V2BillingMeteredItemCreatedEvent as V2BillingMeteredItemCreatedEvent,
        V2BillingMeteredItemCreatedEventNotification as V2BillingMeteredItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_updated_event import (
        V2BillingMeteredItemUpdatedEvent as V2BillingMeteredItemUpdatedEvent,
        V2BillingMeteredItemUpdatedEventNotification as V2BillingMeteredItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_created_event import (
        V2BillingPricingPlanComponentCreatedEvent as V2BillingPricingPlanComponentCreatedEvent,
        V2BillingPricingPlanComponentCreatedEventNotification as V2BillingPricingPlanComponentCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_updated_event import (
        V2BillingPricingPlanComponentUpdatedEvent as V2BillingPricingPlanComponentUpdatedEvent,
        V2BillingPricingPlanComponentUpdatedEventNotification as V2BillingPricingPlanComponentUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_created_event import (
        V2BillingPricingPlanCreatedEvent as V2BillingPricingPlanCreatedEvent,
        V2BillingPricingPlanCreatedEventNotification as V2BillingPricingPlanCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event import (
        V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent as V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent,
        V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification as V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_current_event import (
        V2BillingPricingPlanSubscriptionCollectionCurrentEvent as V2BillingPricingPlanSubscriptionCollectionCurrentEvent,
        V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification as V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event import (
        V2BillingPricingPlanSubscriptionCollectionPastDueEvent as V2BillingPricingPlanSubscriptionCollectionPastDueEvent,
        V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification as V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event import (
        V2BillingPricingPlanSubscriptionCollectionPausedEvent as V2BillingPricingPlanSubscriptionCollectionPausedEvent,
        V2BillingPricingPlanSubscriptionCollectionPausedEventNotification as V2BillingPricingPlanSubscriptionCollectionPausedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event import (
        V2BillingPricingPlanSubscriptionCollectionUnpaidEvent as V2BillingPricingPlanSubscriptionCollectionUnpaidEvent,
        V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification as V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event import (
        V2BillingPricingPlanSubscriptionServicingActivatedEvent as V2BillingPricingPlanSubscriptionServicingActivatedEvent,
        V2BillingPricingPlanSubscriptionServicingActivatedEventNotification as V2BillingPricingPlanSubscriptionServicingActivatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event import (
        V2BillingPricingPlanSubscriptionServicingCanceledEvent as V2BillingPricingPlanSubscriptionServicingCanceledEvent,
        V2BillingPricingPlanSubscriptionServicingCanceledEventNotification as V2BillingPricingPlanSubscriptionServicingCanceledEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event import (
        V2BillingPricingPlanSubscriptionServicingPausedEvent as V2BillingPricingPlanSubscriptionServicingPausedEvent,
        V2BillingPricingPlanSubscriptionServicingPausedEventNotification as V2BillingPricingPlanSubscriptionServicingPausedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_updated_event import (
        V2BillingPricingPlanUpdatedEvent as V2BillingPricingPlanUpdatedEvent,
        V2BillingPricingPlanUpdatedEventNotification as V2BillingPricingPlanUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_version_created_event import (
        V2BillingPricingPlanVersionCreatedEvent as V2BillingPricingPlanVersionCreatedEvent,
        V2BillingPricingPlanVersionCreatedEventNotification as V2BillingPricingPlanVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_created_event import (
        V2BillingRateCardCreatedEvent as V2BillingRateCardCreatedEvent,
        V2BillingRateCardCreatedEventNotification as V2BillingRateCardCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_rate_created_event import (
        V2BillingRateCardRateCreatedEvent as V2BillingRateCardRateCreatedEvent,
        V2BillingRateCardRateCreatedEventNotification as V2BillingRateCardRateCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_activated_event import (
        V2BillingRateCardSubscriptionActivatedEvent as V2BillingRateCardSubscriptionActivatedEvent,
        V2BillingRateCardSubscriptionActivatedEventNotification as V2BillingRateCardSubscriptionActivatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_canceled_event import (
        V2BillingRateCardSubscriptionCanceledEvent as V2BillingRateCardSubscriptionCanceledEvent,
        V2BillingRateCardSubscriptionCanceledEventNotification as V2BillingRateCardSubscriptionCanceledEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event import (
        V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent as V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent,
        V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification as V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_current_event import (
        V2BillingRateCardSubscriptionCollectionCurrentEvent as V2BillingRateCardSubscriptionCollectionCurrentEvent,
        V2BillingRateCardSubscriptionCollectionCurrentEventNotification as V2BillingRateCardSubscriptionCollectionCurrentEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_past_due_event import (
        V2BillingRateCardSubscriptionCollectionPastDueEvent as V2BillingRateCardSubscriptionCollectionPastDueEvent,
        V2BillingRateCardSubscriptionCollectionPastDueEventNotification as V2BillingRateCardSubscriptionCollectionPastDueEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_paused_event import (
        V2BillingRateCardSubscriptionCollectionPausedEvent as V2BillingRateCardSubscriptionCollectionPausedEvent,
        V2BillingRateCardSubscriptionCollectionPausedEventNotification as V2BillingRateCardSubscriptionCollectionPausedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event import (
        V2BillingRateCardSubscriptionCollectionUnpaidEvent as V2BillingRateCardSubscriptionCollectionUnpaidEvent,
        V2BillingRateCardSubscriptionCollectionUnpaidEventNotification as V2BillingRateCardSubscriptionCollectionUnpaidEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_activated_event import (
        V2BillingRateCardSubscriptionServicingActivatedEvent as V2BillingRateCardSubscriptionServicingActivatedEvent,
        V2BillingRateCardSubscriptionServicingActivatedEventNotification as V2BillingRateCardSubscriptionServicingActivatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event import (
        V2BillingRateCardSubscriptionServicingCanceledEvent as V2BillingRateCardSubscriptionServicingCanceledEvent,
        V2BillingRateCardSubscriptionServicingCanceledEventNotification as V2BillingRateCardSubscriptionServicingCanceledEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_paused_event import (
        V2BillingRateCardSubscriptionServicingPausedEvent as V2BillingRateCardSubscriptionServicingPausedEvent,
        V2BillingRateCardSubscriptionServicingPausedEventNotification as V2BillingRateCardSubscriptionServicingPausedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_updated_event import (
        V2BillingRateCardUpdatedEvent as V2BillingRateCardUpdatedEvent,
        V2BillingRateCardUpdatedEventNotification as V2BillingRateCardUpdatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_version_created_event import (
        V2BillingRateCardVersionCreatedEvent as V2BillingRateCardVersionCreatedEvent,
        V2BillingRateCardVersionCreatedEventNotification as V2BillingRateCardVersionCreatedEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEvent as V2CoreAccountClosedEvent,
        V2CoreAccountClosedEventNotification as V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEvent as V2CoreAccountCreatedEvent,
        V2CoreAccountCreatedEventNotification as V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_card_creator_updated_event import (
        V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent as V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent,
        V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification as V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerUpdatedEvent as V2CoreAccountIncludingConfigurationCustomerUpdatedEvent,
        V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification as V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantUpdatedEvent as V2CoreAccountIncludingConfigurationMerchantUpdatedEvent,
        V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification as V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientUpdatedEvent as V2CoreAccountIncludingConfigurationRecipientUpdatedEvent,
        V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification as V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
        V2CoreAccountIncludingConfigurationStorerUpdatedEvent as V2CoreAccountIncludingConfigurationStorerUpdatedEvent,
        V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification as V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEvent as V2CoreAccountIncludingDefaultsUpdatedEvent,
        V2CoreAccountIncludingDefaultsUpdatedEventNotification as V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_future_requirements_updated_event import (
        V2CoreAccountIncludingFutureRequirementsUpdatedEvent as V2CoreAccountIncludingFutureRequirementsUpdatedEvent,
        V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification as V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_identity_updated_event import (
        V2CoreAccountIncludingIdentityUpdatedEvent as V2CoreAccountIncludingIdentityUpdatedEvent,
        V2CoreAccountIncludingIdentityUpdatedEventNotification as V2CoreAccountIncludingIdentityUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_requirements_updated_event import (
        V2CoreAccountIncludingRequirementsUpdatedEvent as V2CoreAccountIncludingRequirementsUpdatedEvent,
        V2CoreAccountIncludingRequirementsUpdatedEventNotification as V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_link_returned_event import (
        V2CoreAccountLinkReturnedEvent as V2CoreAccountLinkReturnedEvent,
        V2CoreAccountLinkReturnedEventNotification as V2CoreAccountLinkReturnedEventNotification,
    )
    from stripe.events._v2_core_account_person_created_event import (
        V2CoreAccountPersonCreatedEvent as V2CoreAccountPersonCreatedEvent,
        V2CoreAccountPersonCreatedEventNotification as V2CoreAccountPersonCreatedEventNotification,
    )
    from stripe.events._v2_core_account_person_deleted_event import (
        V2CoreAccountPersonDeletedEvent as V2CoreAccountPersonDeletedEvent,
        V2CoreAccountPersonDeletedEventNotification as V2CoreAccountPersonDeletedEventNotification,
    )
    from stripe.events._v2_core_account_person_updated_event import (
        V2CoreAccountPersonUpdatedEvent as V2CoreAccountPersonUpdatedEvent,
        V2CoreAccountPersonUpdatedEventNotification as V2CoreAccountPersonUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEvent as V2CoreAccountUpdatedEvent,
        V2CoreAccountUpdatedEventNotification as V2CoreAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_claimed_event import (
        V2CoreClaimableSandboxClaimedEvent as V2CoreClaimableSandboxClaimedEvent,
        V2CoreClaimableSandboxClaimedEventNotification as V2CoreClaimableSandboxClaimedEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_created_event import (
        V2CoreClaimableSandboxCreatedEvent as V2CoreClaimableSandboxCreatedEvent,
        V2CoreClaimableSandboxCreatedEventNotification as V2CoreClaimableSandboxCreatedEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_expired_event import (
        V2CoreClaimableSandboxExpiredEvent as V2CoreClaimableSandboxExpiredEvent,
        V2CoreClaimableSandboxExpiredEventNotification as V2CoreClaimableSandboxExpiredEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_expiring_event import (
        V2CoreClaimableSandboxExpiringEvent as V2CoreClaimableSandboxExpiringEvent,
        V2CoreClaimableSandboxExpiringEventNotification as V2CoreClaimableSandboxExpiringEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event import (
        V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent as V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent,
        V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification as V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEvent as V2CoreEventDestinationPingEvent,
        V2CoreEventDestinationPingEventNotification as V2CoreEventDestinationPingEventNotification,
    )
    from stripe.events._v2_core_health_api_error_firing_event import (
        V2CoreHealthApiErrorFiringEvent as V2CoreHealthApiErrorFiringEvent,
        V2CoreHealthApiErrorFiringEventNotification as V2CoreHealthApiErrorFiringEventNotification,
    )
    from stripe.events._v2_core_health_api_error_resolved_event import (
        V2CoreHealthApiErrorResolvedEvent as V2CoreHealthApiErrorResolvedEvent,
        V2CoreHealthApiErrorResolvedEventNotification as V2CoreHealthApiErrorResolvedEventNotification,
    )
    from stripe.events._v2_core_health_api_latency_firing_event import (
        V2CoreHealthApiLatencyFiringEvent as V2CoreHealthApiLatencyFiringEvent,
        V2CoreHealthApiLatencyFiringEventNotification as V2CoreHealthApiLatencyFiringEventNotification,
    )
    from stripe.events._v2_core_health_api_latency_resolved_event import (
        V2CoreHealthApiLatencyResolvedEvent as V2CoreHealthApiLatencyResolvedEvent,
        V2CoreHealthApiLatencyResolvedEventNotification as V2CoreHealthApiLatencyResolvedEventNotification,
    )
    from stripe.events._v2_core_health_authorization_rate_drop_firing_event import (
        V2CoreHealthAuthorizationRateDropFiringEvent as V2CoreHealthAuthorizationRateDropFiringEvent,
        V2CoreHealthAuthorizationRateDropFiringEventNotification as V2CoreHealthAuthorizationRateDropFiringEventNotification,
    )
    from stripe.events._v2_core_health_authorization_rate_drop_resolved_event import (
        V2CoreHealthAuthorizationRateDropResolvedEvent as V2CoreHealthAuthorizationRateDropResolvedEvent,
        V2CoreHealthAuthorizationRateDropResolvedEventNotification as V2CoreHealthAuthorizationRateDropResolvedEventNotification,
    )
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEvent as V2CoreHealthEventGenerationFailureResolvedEvent,
        V2CoreHealthEventGenerationFailureResolvedEventNotification as V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_core_health_fraud_rate_increased_event import (
        V2CoreHealthFraudRateIncreasedEvent as V2CoreHealthFraudRateIncreasedEvent,
        V2CoreHealthFraudRateIncreasedEventNotification as V2CoreHealthFraudRateIncreasedEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event import (
        V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent as V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent,
        V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification as V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event import (
        V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent as V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent,
        V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification as V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event import (
        V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent as V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent,
        V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification as V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event import (
        V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent as V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent,
        V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification as V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification,
    )
    from stripe.events._v2_core_health_payment_method_error_firing_event import (
        V2CoreHealthPaymentMethodErrorFiringEvent as V2CoreHealthPaymentMethodErrorFiringEvent,
        V2CoreHealthPaymentMethodErrorFiringEventNotification as V2CoreHealthPaymentMethodErrorFiringEventNotification,
    )
    from stripe.events._v2_core_health_payment_method_error_resolved_event import (
        V2CoreHealthPaymentMethodErrorResolvedEvent as V2CoreHealthPaymentMethodErrorResolvedEvent,
        V2CoreHealthPaymentMethodErrorResolvedEventNotification as V2CoreHealthPaymentMethodErrorResolvedEventNotification,
    )
    from stripe.events._v2_core_health_sepa_debit_delayed_firing_event import (
        V2CoreHealthSepaDebitDelayedFiringEvent as V2CoreHealthSepaDebitDelayedFiringEvent,
        V2CoreHealthSepaDebitDelayedFiringEventNotification as V2CoreHealthSepaDebitDelayedFiringEventNotification,
    )
    from stripe.events._v2_core_health_sepa_debit_delayed_resolved_event import (
        V2CoreHealthSepaDebitDelayedResolvedEvent as V2CoreHealthSepaDebitDelayedResolvedEvent,
        V2CoreHealthSepaDebitDelayedResolvedEventNotification as V2CoreHealthSepaDebitDelayedResolvedEventNotification,
    )
    from stripe.events._v2_core_health_traffic_volume_drop_firing_event import (
        V2CoreHealthTrafficVolumeDropFiringEvent as V2CoreHealthTrafficVolumeDropFiringEvent,
        V2CoreHealthTrafficVolumeDropFiringEventNotification as V2CoreHealthTrafficVolumeDropFiringEventNotification,
    )
    from stripe.events._v2_core_health_traffic_volume_drop_resolved_event import (
        V2CoreHealthTrafficVolumeDropResolvedEvent as V2CoreHealthTrafficVolumeDropResolvedEvent,
        V2CoreHealthTrafficVolumeDropResolvedEventNotification as V2CoreHealthTrafficVolumeDropResolvedEventNotification,
    )
    from stripe.events._v2_core_health_webhook_latency_firing_event import (
        V2CoreHealthWebhookLatencyFiringEvent as V2CoreHealthWebhookLatencyFiringEvent,
        V2CoreHealthWebhookLatencyFiringEventNotification as V2CoreHealthWebhookLatencyFiringEventNotification,
    )
    from stripe.events._v2_core_health_webhook_latency_resolved_event import (
        V2CoreHealthWebhookLatencyResolvedEvent as V2CoreHealthWebhookLatencyResolvedEvent,
        V2CoreHealthWebhookLatencyResolvedEventNotification as V2CoreHealthWebhookLatencyResolvedEventNotification,
    )
    from stripe.events._v2_iam_api_key_created_event import (
        V2IamApiKeyCreatedEvent as V2IamApiKeyCreatedEvent,
        V2IamApiKeyCreatedEventNotification as V2IamApiKeyCreatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_default_secret_revealed_event import (
        V2IamApiKeyDefaultSecretRevealedEvent as V2IamApiKeyDefaultSecretRevealedEvent,
        V2IamApiKeyDefaultSecretRevealedEventNotification as V2IamApiKeyDefaultSecretRevealedEventNotification,
    )
    from stripe.events._v2_iam_api_key_expired_event import (
        V2IamApiKeyExpiredEvent as V2IamApiKeyExpiredEvent,
        V2IamApiKeyExpiredEventNotification as V2IamApiKeyExpiredEventNotification,
    )
    from stripe.events._v2_iam_api_key_permissions_updated_event import (
        V2IamApiKeyPermissionsUpdatedEvent as V2IamApiKeyPermissionsUpdatedEvent,
        V2IamApiKeyPermissionsUpdatedEventNotification as V2IamApiKeyPermissionsUpdatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_rotated_event import (
        V2IamApiKeyRotatedEvent as V2IamApiKeyRotatedEvent,
        V2IamApiKeyRotatedEventNotification as V2IamApiKeyRotatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_updated_event import (
        V2IamApiKeyUpdatedEvent as V2IamApiKeyUpdatedEvent,
        V2IamApiKeyUpdatedEventNotification as V2IamApiKeyUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_adjustment_created_event import (
        V2MoneyManagementAdjustmentCreatedEvent as V2MoneyManagementAdjustmentCreatedEvent,
        V2MoneyManagementAdjustmentCreatedEventNotification as V2MoneyManagementAdjustmentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_created_event import (
        V2MoneyManagementFinancialAccountCreatedEvent as V2MoneyManagementFinancialAccountCreatedEvent,
        V2MoneyManagementFinancialAccountCreatedEventNotification as V2MoneyManagementFinancialAccountCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_updated_event import (
        V2MoneyManagementFinancialAccountUpdatedEvent as V2MoneyManagementFinancialAccountUpdatedEvent,
        V2MoneyManagementFinancialAccountUpdatedEventNotification as V2MoneyManagementFinancialAccountUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_activated_event import (
        V2MoneyManagementFinancialAddressActivatedEvent as V2MoneyManagementFinancialAddressActivatedEvent,
        V2MoneyManagementFinancialAddressActivatedEventNotification as V2MoneyManagementFinancialAddressActivatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_failed_event import (
        V2MoneyManagementFinancialAddressFailedEvent as V2MoneyManagementFinancialAddressFailedEvent,
        V2MoneyManagementFinancialAddressFailedEventNotification as V2MoneyManagementFinancialAddressFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_available_event import (
        V2MoneyManagementInboundTransferAvailableEvent as V2MoneyManagementInboundTransferAvailableEvent,
        V2MoneyManagementInboundTransferAvailableEventNotification as V2MoneyManagementInboundTransferAvailableEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
        V2MoneyManagementInboundTransferBankDebitFailedEvent as V2MoneyManagementInboundTransferBankDebitFailedEvent,
        V2MoneyManagementInboundTransferBankDebitFailedEventNotification as V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
        V2MoneyManagementInboundTransferBankDebitProcessingEvent as V2MoneyManagementInboundTransferBankDebitProcessingEvent,
        V2MoneyManagementInboundTransferBankDebitProcessingEventNotification as V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
        V2MoneyManagementInboundTransferBankDebitQueuedEvent as V2MoneyManagementInboundTransferBankDebitQueuedEvent,
        V2MoneyManagementInboundTransferBankDebitQueuedEventNotification as V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
        V2MoneyManagementInboundTransferBankDebitReturnedEvent as V2MoneyManagementInboundTransferBankDebitReturnedEvent,
        V2MoneyManagementInboundTransferBankDebitReturnedEventNotification as V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
        V2MoneyManagementInboundTransferBankDebitSucceededEvent as V2MoneyManagementInboundTransferBankDebitSucceededEvent,
        V2MoneyManagementInboundTransferBankDebitSucceededEventNotification as V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_canceled_event import (
        V2MoneyManagementOutboundPaymentCanceledEvent as V2MoneyManagementOutboundPaymentCanceledEvent,
        V2MoneyManagementOutboundPaymentCanceledEventNotification as V2MoneyManagementOutboundPaymentCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_created_event import (
        V2MoneyManagementOutboundPaymentCreatedEvent as V2MoneyManagementOutboundPaymentCreatedEvent,
        V2MoneyManagementOutboundPaymentCreatedEventNotification as V2MoneyManagementOutboundPaymentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_failed_event import (
        V2MoneyManagementOutboundPaymentFailedEvent as V2MoneyManagementOutboundPaymentFailedEvent,
        V2MoneyManagementOutboundPaymentFailedEventNotification as V2MoneyManagementOutboundPaymentFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_posted_event import (
        V2MoneyManagementOutboundPaymentPostedEvent as V2MoneyManagementOutboundPaymentPostedEvent,
        V2MoneyManagementOutboundPaymentPostedEventNotification as V2MoneyManagementOutboundPaymentPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_returned_event import (
        V2MoneyManagementOutboundPaymentReturnedEvent as V2MoneyManagementOutboundPaymentReturnedEvent,
        V2MoneyManagementOutboundPaymentReturnedEventNotification as V2MoneyManagementOutboundPaymentReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_updated_event import (
        V2MoneyManagementOutboundPaymentUpdatedEvent as V2MoneyManagementOutboundPaymentUpdatedEvent,
        V2MoneyManagementOutboundPaymentUpdatedEventNotification as V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
        V2MoneyManagementOutboundTransferCanceledEvent as V2MoneyManagementOutboundTransferCanceledEvent,
        V2MoneyManagementOutboundTransferCanceledEventNotification as V2MoneyManagementOutboundTransferCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_created_event import (
        V2MoneyManagementOutboundTransferCreatedEvent as V2MoneyManagementOutboundTransferCreatedEvent,
        V2MoneyManagementOutboundTransferCreatedEventNotification as V2MoneyManagementOutboundTransferCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_failed_event import (
        V2MoneyManagementOutboundTransferFailedEvent as V2MoneyManagementOutboundTransferFailedEvent,
        V2MoneyManagementOutboundTransferFailedEventNotification as V2MoneyManagementOutboundTransferFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_posted_event import (
        V2MoneyManagementOutboundTransferPostedEvent as V2MoneyManagementOutboundTransferPostedEvent,
        V2MoneyManagementOutboundTransferPostedEventNotification as V2MoneyManagementOutboundTransferPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_returned_event import (
        V2MoneyManagementOutboundTransferReturnedEvent as V2MoneyManagementOutboundTransferReturnedEvent,
        V2MoneyManagementOutboundTransferReturnedEventNotification as V2MoneyManagementOutboundTransferReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_updated_event import (
        V2MoneyManagementOutboundTransferUpdatedEvent as V2MoneyManagementOutboundTransferUpdatedEvent,
        V2MoneyManagementOutboundTransferUpdatedEventNotification as V2MoneyManagementOutboundTransferUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_created_event import (
        V2MoneyManagementPayoutMethodCreatedEvent as V2MoneyManagementPayoutMethodCreatedEvent,
        V2MoneyManagementPayoutMethodCreatedEventNotification as V2MoneyManagementPayoutMethodCreatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_updated_event import (
        V2MoneyManagementPayoutMethodUpdatedEvent as V2MoneyManagementPayoutMethodUpdatedEvent,
        V2MoneyManagementPayoutMethodUpdatedEventNotification as V2MoneyManagementPayoutMethodUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_available_event import (
        V2MoneyManagementReceivedCreditAvailableEvent as V2MoneyManagementReceivedCreditAvailableEvent,
        V2MoneyManagementReceivedCreditAvailableEventNotification as V2MoneyManagementReceivedCreditAvailableEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_failed_event import (
        V2MoneyManagementReceivedCreditFailedEvent as V2MoneyManagementReceivedCreditFailedEvent,
        V2MoneyManagementReceivedCreditFailedEventNotification as V2MoneyManagementReceivedCreditFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_returned_event import (
        V2MoneyManagementReceivedCreditReturnedEvent as V2MoneyManagementReceivedCreditReturnedEvent,
        V2MoneyManagementReceivedCreditReturnedEventNotification as V2MoneyManagementReceivedCreditReturnedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_succeeded_event import (
        V2MoneyManagementReceivedCreditSucceededEvent as V2MoneyManagementReceivedCreditSucceededEvent,
        V2MoneyManagementReceivedCreditSucceededEventNotification as V2MoneyManagementReceivedCreditSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_canceled_event import (
        V2MoneyManagementReceivedDebitCanceledEvent as V2MoneyManagementReceivedDebitCanceledEvent,
        V2MoneyManagementReceivedDebitCanceledEventNotification as V2MoneyManagementReceivedDebitCanceledEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_failed_event import (
        V2MoneyManagementReceivedDebitFailedEvent as V2MoneyManagementReceivedDebitFailedEvent,
        V2MoneyManagementReceivedDebitFailedEventNotification as V2MoneyManagementReceivedDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_pending_event import (
        V2MoneyManagementReceivedDebitPendingEvent as V2MoneyManagementReceivedDebitPendingEvent,
        V2MoneyManagementReceivedDebitPendingEventNotification as V2MoneyManagementReceivedDebitPendingEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_succeeded_event import (
        V2MoneyManagementReceivedDebitSucceededEvent as V2MoneyManagementReceivedDebitSucceededEvent,
        V2MoneyManagementReceivedDebitSucceededEventNotification as V2MoneyManagementReceivedDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_updated_event import (
        V2MoneyManagementReceivedDebitUpdatedEvent as V2MoneyManagementReceivedDebitUpdatedEvent,
        V2MoneyManagementReceivedDebitUpdatedEventNotification as V2MoneyManagementReceivedDebitUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_recipient_verification_created_event import (
        V2MoneyManagementRecipientVerificationCreatedEvent as V2MoneyManagementRecipientVerificationCreatedEvent,
        V2MoneyManagementRecipientVerificationCreatedEventNotification as V2MoneyManagementRecipientVerificationCreatedEventNotification,
    )
    from stripe.events._v2_money_management_recipient_verification_updated_event import (
        V2MoneyManagementRecipientVerificationUpdatedEvent as V2MoneyManagementRecipientVerificationUpdatedEvent,
        V2MoneyManagementRecipientVerificationUpdatedEventNotification as V2MoneyManagementRecipientVerificationUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEvent as V2MoneyManagementTransactionCreatedEvent,
        V2MoneyManagementTransactionCreatedEventNotification as V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEvent as V2MoneyManagementTransactionUpdatedEvent,
        V2MoneyManagementTransactionUpdatedEventNotification as V2MoneyManagementTransactionUpdatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAttemptFailedEvent as V2PaymentsOffSessionPaymentAttemptFailedEvent,
        V2PaymentsOffSessionPaymentAttemptFailedEventNotification as V2PaymentsOffSessionPaymentAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_started_event import (
        V2PaymentsOffSessionPaymentAttemptStartedEvent as V2PaymentsOffSessionPaymentAttemptStartedEvent,
        V2PaymentsOffSessionPaymentAttemptStartedEventNotification as V2PaymentsOffSessionPaymentAttemptStartedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent as V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
        V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification as V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent as V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
        V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification as V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_canceled_event import (
        V2PaymentsOffSessionPaymentCanceledEvent as V2PaymentsOffSessionPaymentCanceledEvent,
        V2PaymentsOffSessionPaymentCanceledEventNotification as V2PaymentsOffSessionPaymentCanceledEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_created_event import (
        V2PaymentsOffSessionPaymentCreatedEvent as V2PaymentsOffSessionPaymentCreatedEvent,
        V2PaymentsOffSessionPaymentCreatedEventNotification as V2PaymentsOffSessionPaymentCreatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_failed_event import (
        V2PaymentsOffSessionPaymentFailedEvent as V2PaymentsOffSessionPaymentFailedEvent,
        V2PaymentsOffSessionPaymentFailedEventNotification as V2PaymentsOffSessionPaymentFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_requires_capture_event import (
        V2PaymentsOffSessionPaymentRequiresCaptureEvent as V2PaymentsOffSessionPaymentRequiresCaptureEvent,
        V2PaymentsOffSessionPaymentRequiresCaptureEventNotification as V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_succeeded_event import (
        V2PaymentsOffSessionPaymentSucceededEvent as V2PaymentsOffSessionPaymentSucceededEvent,
        V2PaymentsOffSessionPaymentSucceededEventNotification as V2PaymentsOffSessionPaymentSucceededEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_canceled_event import (
        V2PaymentsSettlementAllocationIntentCanceledEvent as V2PaymentsSettlementAllocationIntentCanceledEvent,
        V2PaymentsSettlementAllocationIntentCanceledEventNotification as V2PaymentsSettlementAllocationIntentCanceledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_created_event import (
        V2PaymentsSettlementAllocationIntentCreatedEvent as V2PaymentsSettlementAllocationIntentCreatedEvent,
        V2PaymentsSettlementAllocationIntentCreatedEventNotification as V2PaymentsSettlementAllocationIntentCreatedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_errored_event import (
        V2PaymentsSettlementAllocationIntentErroredEvent as V2PaymentsSettlementAllocationIntentErroredEvent,
        V2PaymentsSettlementAllocationIntentErroredEventNotification as V2PaymentsSettlementAllocationIntentErroredEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event import (
        V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent as V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent,
        V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification as V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_matched_event import (
        V2PaymentsSettlementAllocationIntentMatchedEvent as V2PaymentsSettlementAllocationIntentMatchedEvent,
        V2PaymentsSettlementAllocationIntentMatchedEventNotification as V2PaymentsSettlementAllocationIntentMatchedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_not_found_event import (
        V2PaymentsSettlementAllocationIntentNotFoundEvent as V2PaymentsSettlementAllocationIntentNotFoundEvent,
        V2PaymentsSettlementAllocationIntentNotFoundEventNotification as V2PaymentsSettlementAllocationIntentNotFoundEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_settled_event import (
        V2PaymentsSettlementAllocationIntentSettledEvent as V2PaymentsSettlementAllocationIntentSettledEvent,
        V2PaymentsSettlementAllocationIntentSettledEventNotification as V2PaymentsSettlementAllocationIntentSettledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event import (
        V2PaymentsSettlementAllocationIntentSplitCanceledEvent as V2PaymentsSettlementAllocationIntentSplitCanceledEvent,
        V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification as V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_created_event import (
        V2PaymentsSettlementAllocationIntentSplitCreatedEvent as V2PaymentsSettlementAllocationIntentSplitCreatedEvent,
        V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification as V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_settled_event import (
        V2PaymentsSettlementAllocationIntentSplitSettledEvent as V2PaymentsSettlementAllocationIntentSplitSettledEvent,
        V2PaymentsSettlementAllocationIntentSplitSettledEventNotification as V2PaymentsSettlementAllocationIntentSplitSettledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_submitted_event import (
        V2PaymentsSettlementAllocationIntentSubmittedEvent as V2PaymentsSettlementAllocationIntentSubmittedEvent,
        V2PaymentsSettlementAllocationIntentSubmittedEventNotification as V2PaymentsSettlementAllocationIntentSubmittedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_created_event import (
        V2ReportingReportRunCreatedEvent as V2ReportingReportRunCreatedEvent,
        V2ReportingReportRunCreatedEventNotification as V2ReportingReportRunCreatedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_failed_event import (
        V2ReportingReportRunFailedEvent as V2ReportingReportRunFailedEvent,
        V2ReportingReportRunFailedEventNotification as V2ReportingReportRunFailedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_succeeded_event import (
        V2ReportingReportRunSucceededEvent as V2ReportingReportRunSucceededEvent,
        V2ReportingReportRunSucceededEventNotification as V2ReportingReportRunSucceededEventNotification,
    )
    from stripe.events._v2_reporting_report_run_updated_event import (
        V2ReportingReportRunUpdatedEvent as V2ReportingReportRunUpdatedEvent,
        V2ReportingReportRunUpdatedEventNotification as V2ReportingReportRunUpdatedEventNotification,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ALL_EVENT_NOTIFICATIONS": ("stripe.events._event_classes", False),
    "V1BillingMeterErrorReportTriggeredEvent": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterErrorReportTriggeredEventNotification": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEvent": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEventNotification": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V2BillingCadenceBilledEvent": (
        "stripe.events._v2_billing_cadence_billed_event",
        False,
    ),
    "V2BillingCadenceBilledEventNotification": (
        "stripe.events._v2_billing_cadence_billed_event",
        False,
    ),
    "V2BillingCadenceCanceledEvent": (
        "stripe.events._v2_billing_cadence_canceled_event",
        False,
    ),
    "V2BillingCadenceCanceledEventNotification": (
        "stripe.events._v2_billing_cadence_canceled_event",
        False,
    ),
    "V2BillingCadenceCreatedEvent": (
        "stripe.events._v2_billing_cadence_created_event",
        False,
    ),
    "V2BillingCadenceCreatedEventNotification": (
        "stripe.events._v2_billing_cadence_created_event",
        False,
    ),
    "V2BillingLicenseFeeCreatedEvent": (
        "stripe.events._v2_billing_license_fee_created_event",
        False,
    ),
    "V2BillingLicenseFeeCreatedEventNotification": (
        "stripe.events._v2_billing_license_fee_created_event",
        False,
    ),
    "V2BillingLicenseFeeUpdatedEvent": (
        "stripe.events._v2_billing_license_fee_updated_event",
        False,
    ),
    "V2BillingLicenseFeeUpdatedEventNotification": (
        "stripe.events._v2_billing_license_fee_updated_event",
        False,
    ),
    "V2BillingLicenseFeeVersionCreatedEvent": (
        "stripe.events._v2_billing_license_fee_version_created_event",
        False,
    ),
    "V2BillingLicenseFeeVersionCreatedEventNotification": (
        "stripe.events._v2_billing_license_fee_version_created_event",
        False,
    ),
    "V2BillingLicensedItemCreatedEvent": (
        "stripe.events._v2_billing_licensed_item_created_event",
        False,
    ),
    "V2BillingLicensedItemCreatedEventNotification": (
        "stripe.events._v2_billing_licensed_item_created_event",
        False,
    ),
    "V2BillingLicensedItemUpdatedEvent": (
        "stripe.events._v2_billing_licensed_item_updated_event",
        False,
    ),
    "V2BillingLicensedItemUpdatedEventNotification": (
        "stripe.events._v2_billing_licensed_item_updated_event",
        False,
    ),
    "V2BillingMeteredItemCreatedEvent": (
        "stripe.events._v2_billing_metered_item_created_event",
        False,
    ),
    "V2BillingMeteredItemCreatedEventNotification": (
        "stripe.events._v2_billing_metered_item_created_event",
        False,
    ),
    "V2BillingMeteredItemUpdatedEvent": (
        "stripe.events._v2_billing_metered_item_updated_event",
        False,
    ),
    "V2BillingMeteredItemUpdatedEventNotification": (
        "stripe.events._v2_billing_metered_item_updated_event",
        False,
    ),
    "V2BillingPricingPlanComponentCreatedEvent": (
        "stripe.events._v2_billing_pricing_plan_component_created_event",
        False,
    ),
    "V2BillingPricingPlanComponentCreatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_component_created_event",
        False,
    ),
    "V2BillingPricingPlanComponentUpdatedEvent": (
        "stripe.events._v2_billing_pricing_plan_component_updated_event",
        False,
    ),
    "V2BillingPricingPlanComponentUpdatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_component_updated_event",
        False,
    ),
    "V2BillingPricingPlanCreatedEvent": (
        "stripe.events._v2_billing_pricing_plan_created_event",
        False,
    ),
    "V2BillingPricingPlanCreatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_created_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionCurrentEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_current_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_current_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionPastDueEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionPausedEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionPausedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionUnpaidEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingActivatedEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingActivatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingCanceledEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingCanceledEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingPausedEvent": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event",
        False,
    ),
    "V2BillingPricingPlanSubscriptionServicingPausedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event",
        False,
    ),
    "V2BillingPricingPlanUpdatedEvent": (
        "stripe.events._v2_billing_pricing_plan_updated_event",
        False,
    ),
    "V2BillingPricingPlanUpdatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_updated_event",
        False,
    ),
    "V2BillingPricingPlanVersionCreatedEvent": (
        "stripe.events._v2_billing_pricing_plan_version_created_event",
        False,
    ),
    "V2BillingPricingPlanVersionCreatedEventNotification": (
        "stripe.events._v2_billing_pricing_plan_version_created_event",
        False,
    ),
    "V2BillingRateCardCreatedEvent": (
        "stripe.events._v2_billing_rate_card_created_event",
        False,
    ),
    "V2BillingRateCardCreatedEventNotification": (
        "stripe.events._v2_billing_rate_card_created_event",
        False,
    ),
    "V2BillingRateCardRateCreatedEvent": (
        "stripe.events._v2_billing_rate_card_rate_created_event",
        False,
    ),
    "V2BillingRateCardRateCreatedEventNotification": (
        "stripe.events._v2_billing_rate_card_rate_created_event",
        False,
    ),
    "V2BillingRateCardSubscriptionActivatedEvent": (
        "stripe.events._v2_billing_rate_card_subscription_activated_event",
        False,
    ),
    "V2BillingRateCardSubscriptionActivatedEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_activated_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCanceledEvent": (
        "stripe.events._v2_billing_rate_card_subscription_canceled_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCanceledEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_canceled_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent": (
        "stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionCurrentEvent": (
        "stripe.events._v2_billing_rate_card_subscription_collection_current_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionCurrentEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_collection_current_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionPastDueEvent": (
        "stripe.events._v2_billing_rate_card_subscription_collection_past_due_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionPastDueEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_collection_past_due_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionPausedEvent": (
        "stripe.events._v2_billing_rate_card_subscription_collection_paused_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionPausedEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_collection_paused_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionUnpaidEvent": (
        "stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event",
        False,
    ),
    "V2BillingRateCardSubscriptionCollectionUnpaidEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingActivatedEvent": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_activated_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingActivatedEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_activated_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingCanceledEvent": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingCanceledEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingPausedEvent": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_paused_event",
        False,
    ),
    "V2BillingRateCardSubscriptionServicingPausedEventNotification": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_paused_event",
        False,
    ),
    "V2BillingRateCardUpdatedEvent": (
        "stripe.events._v2_billing_rate_card_updated_event",
        False,
    ),
    "V2BillingRateCardUpdatedEventNotification": (
        "stripe.events._v2_billing_rate_card_updated_event",
        False,
    ),
    "V2BillingRateCardVersionCreatedEvent": (
        "stripe.events._v2_billing_rate_card_version_created_event",
        False,
    ),
    "V2BillingRateCardVersionCreatedEventNotification": (
        "stripe.events._v2_billing_rate_card_version_created_event",
        False,
    ),
    "V2CoreAccountClosedEvent": (
        "stripe.events._v2_core_account_closed_event",
        False,
    ),
    "V2CoreAccountClosedEventNotification": (
        "stripe.events._v2_core_account_closed_event",
        False,
    ),
    "V2CoreAccountCreatedEvent": (
        "stripe.events._v2_core_account_created_event",
        False,
    ),
    "V2CoreAccountCreatedEventNotification": (
        "stripe.events._v2_core_account_created_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_card_creator_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_card_creator_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingDefaultsUpdatedEvent": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingFutureRequirementsUpdatedEvent": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
        False,
    ),
    "V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
        False,
    ),
    "V2CoreAccountIncludingIdentityUpdatedEvent": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        False,
    ),
    "V2CoreAccountIncludingIdentityUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        False,
    ),
    "V2CoreAccountIncludingRequirementsUpdatedEvent": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        False,
    ),
    "V2CoreAccountIncludingRequirementsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        False,
    ),
    "V2CoreAccountLinkReturnedEvent": (
        "stripe.events._v2_core_account_link_returned_event",
        False,
    ),
    "V2CoreAccountLinkReturnedEventNotification": (
        "stripe.events._v2_core_account_link_returned_event",
        False,
    ),
    "V2CoreAccountPersonCreatedEvent": (
        "stripe.events._v2_core_account_person_created_event",
        False,
    ),
    "V2CoreAccountPersonCreatedEventNotification": (
        "stripe.events._v2_core_account_person_created_event",
        False,
    ),
    "V2CoreAccountPersonDeletedEvent": (
        "stripe.events._v2_core_account_person_deleted_event",
        False,
    ),
    "V2CoreAccountPersonDeletedEventNotification": (
        "stripe.events._v2_core_account_person_deleted_event",
        False,
    ),
    "V2CoreAccountPersonUpdatedEvent": (
        "stripe.events._v2_core_account_person_updated_event",
        False,
    ),
    "V2CoreAccountPersonUpdatedEventNotification": (
        "stripe.events._v2_core_account_person_updated_event",
        False,
    ),
    "V2CoreAccountUpdatedEvent": (
        "stripe.events._v2_core_account_updated_event",
        False,
    ),
    "V2CoreAccountUpdatedEventNotification": (
        "stripe.events._v2_core_account_updated_event",
        False,
    ),
    "V2CoreClaimableSandboxClaimedEvent": (
        "stripe.events._v2_core_claimable_sandbox_claimed_event",
        False,
    ),
    "V2CoreClaimableSandboxClaimedEventNotification": (
        "stripe.events._v2_core_claimable_sandbox_claimed_event",
        False,
    ),
    "V2CoreClaimableSandboxCreatedEvent": (
        "stripe.events._v2_core_claimable_sandbox_created_event",
        False,
    ),
    "V2CoreClaimableSandboxCreatedEventNotification": (
        "stripe.events._v2_core_claimable_sandbox_created_event",
        False,
    ),
    "V2CoreClaimableSandboxExpiredEvent": (
        "stripe.events._v2_core_claimable_sandbox_expired_event",
        False,
    ),
    "V2CoreClaimableSandboxExpiredEventNotification": (
        "stripe.events._v2_core_claimable_sandbox_expired_event",
        False,
    ),
    "V2CoreClaimableSandboxExpiringEvent": (
        "stripe.events._v2_core_claimable_sandbox_expiring_event",
        False,
    ),
    "V2CoreClaimableSandboxExpiringEventNotification": (
        "stripe.events._v2_core_claimable_sandbox_expiring_event",
        False,
    ),
    "V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent": (
        "stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event",
        False,
    ),
    "V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification": (
        "stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event",
        False,
    ),
    "V2CoreEventDestinationPingEvent": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
    "V2CoreEventDestinationPingEventNotification": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
    "V2CoreHealthApiErrorFiringEvent": (
        "stripe.events._v2_core_health_api_error_firing_event",
        False,
    ),
    "V2CoreHealthApiErrorFiringEventNotification": (
        "stripe.events._v2_core_health_api_error_firing_event",
        False,
    ),
    "V2CoreHealthApiErrorResolvedEvent": (
        "stripe.events._v2_core_health_api_error_resolved_event",
        False,
    ),
    "V2CoreHealthApiErrorResolvedEventNotification": (
        "stripe.events._v2_core_health_api_error_resolved_event",
        False,
    ),
    "V2CoreHealthApiLatencyFiringEvent": (
        "stripe.events._v2_core_health_api_latency_firing_event",
        False,
    ),
    "V2CoreHealthApiLatencyFiringEventNotification": (
        "stripe.events._v2_core_health_api_latency_firing_event",
        False,
    ),
    "V2CoreHealthApiLatencyResolvedEvent": (
        "stripe.events._v2_core_health_api_latency_resolved_event",
        False,
    ),
    "V2CoreHealthApiLatencyResolvedEventNotification": (
        "stripe.events._v2_core_health_api_latency_resolved_event",
        False,
    ),
    "V2CoreHealthAuthorizationRateDropFiringEvent": (
        "stripe.events._v2_core_health_authorization_rate_drop_firing_event",
        False,
    ),
    "V2CoreHealthAuthorizationRateDropFiringEventNotification": (
        "stripe.events._v2_core_health_authorization_rate_drop_firing_event",
        False,
    ),
    "V2CoreHealthAuthorizationRateDropResolvedEvent": (
        "stripe.events._v2_core_health_authorization_rate_drop_resolved_event",
        False,
    ),
    "V2CoreHealthAuthorizationRateDropResolvedEventNotification": (
        "stripe.events._v2_core_health_authorization_rate_drop_resolved_event",
        False,
    ),
    "V2CoreHealthEventGenerationFailureResolvedEvent": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        False,
    ),
    "V2CoreHealthEventGenerationFailureResolvedEventNotification": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        False,
    ),
    "V2CoreHealthFraudRateIncreasedEvent": (
        "stripe.events._v2_core_health_fraud_rate_increased_event",
        False,
    ),
    "V2CoreHealthFraudRateIncreasedEventNotification": (
        "stripe.events._v2_core_health_fraud_rate_increased_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event",
        False,
    ),
    "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event",
        False,
    ),
    "V2CoreHealthPaymentMethodErrorFiringEvent": (
        "stripe.events._v2_core_health_payment_method_error_firing_event",
        False,
    ),
    "V2CoreHealthPaymentMethodErrorFiringEventNotification": (
        "stripe.events._v2_core_health_payment_method_error_firing_event",
        False,
    ),
    "V2CoreHealthPaymentMethodErrorResolvedEvent": (
        "stripe.events._v2_core_health_payment_method_error_resolved_event",
        False,
    ),
    "V2CoreHealthPaymentMethodErrorResolvedEventNotification": (
        "stripe.events._v2_core_health_payment_method_error_resolved_event",
        False,
    ),
    "V2CoreHealthSepaDebitDelayedFiringEvent": (
        "stripe.events._v2_core_health_sepa_debit_delayed_firing_event",
        False,
    ),
    "V2CoreHealthSepaDebitDelayedFiringEventNotification": (
        "stripe.events._v2_core_health_sepa_debit_delayed_firing_event",
        False,
    ),
    "V2CoreHealthSepaDebitDelayedResolvedEvent": (
        "stripe.events._v2_core_health_sepa_debit_delayed_resolved_event",
        False,
    ),
    "V2CoreHealthSepaDebitDelayedResolvedEventNotification": (
        "stripe.events._v2_core_health_sepa_debit_delayed_resolved_event",
        False,
    ),
    "V2CoreHealthTrafficVolumeDropFiringEvent": (
        "stripe.events._v2_core_health_traffic_volume_drop_firing_event",
        False,
    ),
    "V2CoreHealthTrafficVolumeDropFiringEventNotification": (
        "stripe.events._v2_core_health_traffic_volume_drop_firing_event",
        False,
    ),
    "V2CoreHealthTrafficVolumeDropResolvedEvent": (
        "stripe.events._v2_core_health_traffic_volume_drop_resolved_event",
        False,
    ),
    "V2CoreHealthTrafficVolumeDropResolvedEventNotification": (
        "stripe.events._v2_core_health_traffic_volume_drop_resolved_event",
        False,
    ),
    "V2CoreHealthWebhookLatencyFiringEvent": (
        "stripe.events._v2_core_health_webhook_latency_firing_event",
        False,
    ),
    "V2CoreHealthWebhookLatencyFiringEventNotification": (
        "stripe.events._v2_core_health_webhook_latency_firing_event",
        False,
    ),
    "V2CoreHealthWebhookLatencyResolvedEvent": (
        "stripe.events._v2_core_health_webhook_latency_resolved_event",
        False,
    ),
    "V2CoreHealthWebhookLatencyResolvedEventNotification": (
        "stripe.events._v2_core_health_webhook_latency_resolved_event",
        False,
    ),
    "V2IamApiKeyCreatedEvent": (
        "stripe.events._v2_iam_api_key_created_event",
        False,
    ),
    "V2IamApiKeyCreatedEventNotification": (
        "stripe.events._v2_iam_api_key_created_event",
        False,
    ),
    "V2IamApiKeyDefaultSecretRevealedEvent": (
        "stripe.events._v2_iam_api_key_default_secret_revealed_event",
        False,
    ),
    "V2IamApiKeyDefaultSecretRevealedEventNotification": (
        "stripe.events._v2_iam_api_key_default_secret_revealed_event",
        False,
    ),
    "V2IamApiKeyExpiredEvent": (
        "stripe.events._v2_iam_api_key_expired_event",
        False,
    ),
    "V2IamApiKeyExpiredEventNotification": (
        "stripe.events._v2_iam_api_key_expired_event",
        False,
    ),
    "V2IamApiKeyPermissionsUpdatedEvent": (
        "stripe.events._v2_iam_api_key_permissions_updated_event",
        False,
    ),
    "V2IamApiKeyPermissionsUpdatedEventNotification": (
        "stripe.events._v2_iam_api_key_permissions_updated_event",
        False,
    ),
    "V2IamApiKeyRotatedEvent": (
        "stripe.events._v2_iam_api_key_rotated_event",
        False,
    ),
    "V2IamApiKeyRotatedEventNotification": (
        "stripe.events._v2_iam_api_key_rotated_event",
        False,
    ),
    "V2IamApiKeyUpdatedEvent": (
        "stripe.events._v2_iam_api_key_updated_event",
        False,
    ),
    "V2IamApiKeyUpdatedEventNotification": (
        "stripe.events._v2_iam_api_key_updated_event",
        False,
    ),
    "V2MoneyManagementAdjustmentCreatedEvent": (
        "stripe.events._v2_money_management_adjustment_created_event",
        False,
    ),
    "V2MoneyManagementAdjustmentCreatedEventNotification": (
        "stripe.events._v2_money_management_adjustment_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountCreatedEvent": (
        "stripe.events._v2_money_management_financial_account_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountCreatedEventNotification": (
        "stripe.events._v2_money_management_financial_account_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountUpdatedEvent": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountUpdatedEventNotification": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressActivatedEvent": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressActivatedEventNotification": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressFailedEvent": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressFailedEventNotification": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferAvailableEvent": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        False,
    ),
    "V2MoneyManagementInboundTransferAvailableEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitFailedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitFailedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitProcessingEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitQueuedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitReturnedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitSucceededEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCanceledEvent": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCanceledEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCreatedEvent": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCreatedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentFailedEvent": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentFailedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentPostedEvent": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentPostedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentReturnedEvent": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentReturnedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentUpdatedEvent": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentUpdatedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCanceledEvent": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCanceledEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCreatedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCreatedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferFailedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferFailedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferPostedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferPostedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferReturnedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferReturnedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferUpdatedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferUpdatedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodCreatedEvent": (
        "stripe.events._v2_money_management_payout_method_created_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodCreatedEventNotification": (
        "stripe.events._v2_money_management_payout_method_created_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodUpdatedEvent": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodUpdatedEventNotification": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditAvailableEvent": (
        "stripe.events._v2_money_management_received_credit_available_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditAvailableEventNotification": (
        "stripe.events._v2_money_management_received_credit_available_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditFailedEvent": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditFailedEventNotification": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditReturnedEvent": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditReturnedEventNotification": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditSucceededEvent": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditSucceededEventNotification": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitCanceledEvent": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitCanceledEventNotification": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitFailedEvent": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitFailedEventNotification": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitPendingEvent": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitPendingEventNotification": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitSucceededEvent": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitSucceededEventNotification": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitUpdatedEvent": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitUpdatedEventNotification": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationCreatedEvent": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationCreatedEventNotification": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationUpdatedEvent": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationUpdatedEventNotification": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
        False,
    ),
    "V2MoneyManagementTransactionCreatedEvent": (
        "stripe.events._v2_money_management_transaction_created_event",
        False,
    ),
    "V2MoneyManagementTransactionCreatedEventNotification": (
        "stripe.events._v2_money_management_transaction_created_event",
        False,
    ),
    "V2MoneyManagementTransactionUpdatedEvent": (
        "stripe.events._v2_money_management_transaction_updated_event",
        False,
    ),
    "V2MoneyManagementTransactionUpdatedEventNotification": (
        "stripe.events._v2_money_management_transaction_updated_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptStartedEvent": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptStartedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCanceledEvent": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCanceledEventNotification": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCreatedEvent": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCreatedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentRequiresCaptureEvent": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentRequiresCaptureEventNotification": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentSucceededEvent": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentSucceededEventNotification": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentCanceledEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_canceled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentCanceledEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_canceled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentCreatedEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_created_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentCreatedEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_created_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentErroredEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_errored_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentErroredEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_errored_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentMatchedEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_matched_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentMatchedEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_matched_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentNotFoundEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_not_found_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentNotFoundEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_not_found_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSettledEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_settled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSettledEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_settled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitCanceledEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitCreatedEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_created_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_created_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitSettledEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_settled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSplitSettledEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_settled_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSubmittedEvent": (
        "stripe.events._v2_payments_settlement_allocation_intent_submitted_event",
        False,
    ),
    "V2PaymentsSettlementAllocationIntentSubmittedEventNotification": (
        "stripe.events._v2_payments_settlement_allocation_intent_submitted_event",
        False,
    ),
    "V2ReportingReportRunCreatedEvent": (
        "stripe.events._v2_reporting_report_run_created_event",
        False,
    ),
    "V2ReportingReportRunCreatedEventNotification": (
        "stripe.events._v2_reporting_report_run_created_event",
        False,
    ),
    "V2ReportingReportRunFailedEvent": (
        "stripe.events._v2_reporting_report_run_failed_event",
        False,
    ),
    "V2ReportingReportRunFailedEventNotification": (
        "stripe.events._v2_reporting_report_run_failed_event",
        False,
    ),
    "V2ReportingReportRunSucceededEvent": (
        "stripe.events._v2_reporting_report_run_succeeded_event",
        False,
    ),
    "V2ReportingReportRunSucceededEventNotification": (
        "stripe.events._v2_reporting_report_run_succeeded_event",
        False,
    ),
    "V2ReportingReportRunUpdatedEvent": (
        "stripe.events._v2_reporting_report_run_updated_event",
        False,
    ),
    "V2ReportingReportRunUpdatedEventNotification": (
        "stripe.events._v2_reporting_report_run_updated_event",
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

# The end of the section generated from our OpenAPI spec
