# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
        V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_identity_updated_event import (
        V2CoreAccountIncludingIdentityUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_requirements_updated_event import (
        V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_link_returned_event import (
        V2CoreAccountLinkReturnedEventNotification,
    )
    from stripe.events._v2_core_account_person_created_event import (
        V2CoreAccountPersonCreatedEventNotification,
    )
    from stripe.events._v2_core_account_person_deleted_event import (
        V2CoreAccountPersonDeletedEventNotification,
    )
    from stripe.events._v2_core_account_person_updated_event import (
        V2CoreAccountPersonUpdatedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_money_management_adjustment_created_event import (
        V2MoneyManagementAdjustmentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_created_event import (
        V2MoneyManagementFinancialAccountCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_updated_event import (
        V2MoneyManagementFinancialAccountUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_activated_event import (
        V2MoneyManagementFinancialAddressActivatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_failed_event import (
        V2MoneyManagementFinancialAddressFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_available_event import (
        V2MoneyManagementInboundTransferAvailableEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
        V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
        V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
        V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
        V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
        V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_canceled_event import (
        V2MoneyManagementOutboundPaymentCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_created_event import (
        V2MoneyManagementOutboundPaymentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_failed_event import (
        V2MoneyManagementOutboundPaymentFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_posted_event import (
        V2MoneyManagementOutboundPaymentPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_returned_event import (
        V2MoneyManagementOutboundPaymentReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_updated_event import (
        V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
        V2MoneyManagementOutboundTransferCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_created_event import (
        V2MoneyManagementOutboundTransferCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_failed_event import (
        V2MoneyManagementOutboundTransferFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_posted_event import (
        V2MoneyManagementOutboundTransferPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_returned_event import (
        V2MoneyManagementOutboundTransferReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_updated_event import (
        V2MoneyManagementOutboundTransferUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_updated_event import (
        V2MoneyManagementPayoutMethodUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_available_event import (
        V2MoneyManagementReceivedCreditAvailableEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_failed_event import (
        V2MoneyManagementReceivedCreditFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_returned_event import (
        V2MoneyManagementReceivedCreditReturnedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_succeeded_event import (
        V2MoneyManagementReceivedCreditSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_canceled_event import (
        V2MoneyManagementReceivedDebitCanceledEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_failed_event import (
        V2MoneyManagementReceivedDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_pending_event import (
        V2MoneyManagementReceivedDebitPendingEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_succeeded_event import (
        V2MoneyManagementReceivedDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_updated_event import (
        V2MoneyManagementReceivedDebitUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEventNotification,
    )


_V2_EVENT_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEvent",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEvent",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEvent",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEvent",
    ),
    "v2.core.account[configuration.customer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.customer].updated": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerUpdatedEvent",
    ),
    "v2.core.account[configuration.merchant].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.merchant].updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantUpdatedEvent",
    ),
    "v2.core.account[configuration.recipient].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.recipient].updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientUpdatedEvent",
    ),
    "v2.core.account[configuration.storer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.storer].updated": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        "V2CoreAccountIncludingConfigurationStorerUpdatedEvent",
    ),
    "v2.core.account[defaults].updated": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        "V2CoreAccountIncludingDefaultsUpdatedEvent",
    ),
    "v2.core.account[identity].updated": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        "V2CoreAccountIncludingIdentityUpdatedEvent",
    ),
    "v2.core.account[requirements].updated": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        "V2CoreAccountIncludingRequirementsUpdatedEvent",
    ),
    "v2.core.account_link.returned": (
        "stripe.events._v2_core_account_link_returned_event",
        "V2CoreAccountLinkReturnedEvent",
    ),
    "v2.core.account_person.created": (
        "stripe.events._v2_core_account_person_created_event",
        "V2CoreAccountPersonCreatedEvent",
    ),
    "v2.core.account_person.deleted": (
        "stripe.events._v2_core_account_person_deleted_event",
        "V2CoreAccountPersonDeletedEvent",
    ),
    "v2.core.account_person.updated": (
        "stripe.events._v2_core_account_person_updated_event",
        "V2CoreAccountPersonUpdatedEvent",
    ),
    "v2.core.account.updated": (
        "stripe.events._v2_core_account_updated_event",
        "V2CoreAccountUpdatedEvent",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEvent",
    ),
    "v2.core.health.event_generation_failure.resolved": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        "V2CoreHealthEventGenerationFailureResolvedEvent",
    ),
    "v2.money_management.adjustment.created": (
        "stripe.events._v2_money_management_adjustment_created_event",
        "V2MoneyManagementAdjustmentCreatedEvent",
    ),
    "v2.money_management.financial_account.created": (
        "stripe.events._v2_money_management_financial_account_created_event",
        "V2MoneyManagementFinancialAccountCreatedEvent",
    ),
    "v2.money_management.financial_account.updated": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        "V2MoneyManagementFinancialAccountUpdatedEvent",
    ),
    "v2.money_management.financial_address.activated": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        "V2MoneyManagementFinancialAddressActivatedEvent",
    ),
    "v2.money_management.financial_address.failed": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        "V2MoneyManagementFinancialAddressFailedEvent",
    ),
    "v2.money_management.inbound_transfer.available": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        "V2MoneyManagementInboundTransferAvailableEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_failed": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        "V2MoneyManagementInboundTransferBankDebitFailedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_processing": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        "V2MoneyManagementInboundTransferBankDebitProcessingEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_queued": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        "V2MoneyManagementInboundTransferBankDebitQueuedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_returned": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        "V2MoneyManagementInboundTransferBankDebitReturnedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_succeeded": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        "V2MoneyManagementInboundTransferBankDebitSucceededEvent",
    ),
    "v2.money_management.outbound_payment.canceled": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        "V2MoneyManagementOutboundPaymentCanceledEvent",
    ),
    "v2.money_management.outbound_payment.created": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        "V2MoneyManagementOutboundPaymentCreatedEvent",
    ),
    "v2.money_management.outbound_payment.failed": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        "V2MoneyManagementOutboundPaymentFailedEvent",
    ),
    "v2.money_management.outbound_payment.posted": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        "V2MoneyManagementOutboundPaymentPostedEvent",
    ),
    "v2.money_management.outbound_payment.returned": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        "V2MoneyManagementOutboundPaymentReturnedEvent",
    ),
    "v2.money_management.outbound_payment.updated": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        "V2MoneyManagementOutboundPaymentUpdatedEvent",
    ),
    "v2.money_management.outbound_transfer.canceled": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        "V2MoneyManagementOutboundTransferCanceledEvent",
    ),
    "v2.money_management.outbound_transfer.created": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        "V2MoneyManagementOutboundTransferCreatedEvent",
    ),
    "v2.money_management.outbound_transfer.failed": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        "V2MoneyManagementOutboundTransferFailedEvent",
    ),
    "v2.money_management.outbound_transfer.posted": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        "V2MoneyManagementOutboundTransferPostedEvent",
    ),
    "v2.money_management.outbound_transfer.returned": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        "V2MoneyManagementOutboundTransferReturnedEvent",
    ),
    "v2.money_management.outbound_transfer.updated": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        "V2MoneyManagementOutboundTransferUpdatedEvent",
    ),
    "v2.money_management.payout_method.updated": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        "V2MoneyManagementPayoutMethodUpdatedEvent",
    ),
    "v2.money_management.received_credit.available": (
        "stripe.events._v2_money_management_received_credit_available_event",
        "V2MoneyManagementReceivedCreditAvailableEvent",
    ),
    "v2.money_management.received_credit.failed": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        "V2MoneyManagementReceivedCreditFailedEvent",
    ),
    "v2.money_management.received_credit.returned": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        "V2MoneyManagementReceivedCreditReturnedEvent",
    ),
    "v2.money_management.received_credit.succeeded": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        "V2MoneyManagementReceivedCreditSucceededEvent",
    ),
    "v2.money_management.received_debit.canceled": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        "V2MoneyManagementReceivedDebitCanceledEvent",
    ),
    "v2.money_management.received_debit.failed": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        "V2MoneyManagementReceivedDebitFailedEvent",
    ),
    "v2.money_management.received_debit.pending": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        "V2MoneyManagementReceivedDebitPendingEvent",
    ),
    "v2.money_management.received_debit.succeeded": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        "V2MoneyManagementReceivedDebitSucceededEvent",
    ),
    "v2.money_management.received_debit.updated": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        "V2MoneyManagementReceivedDebitUpdatedEvent",
    ),
    "v2.money_management.transaction.created": (
        "stripe.events._v2_money_management_transaction_created_event",
        "V2MoneyManagementTransactionCreatedEvent",
    ),
    "v2.money_management.transaction.updated": (
        "stripe.events._v2_money_management_transaction_updated_event",
        "V2MoneyManagementTransactionUpdatedEvent",
    ),
}


def get_v2_event_class(type_: str):
    if type_ not in _V2_EVENT_CLASS_LOOKUP:
        return StripeObject

    import_path, class_name = _V2_EVENT_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


_V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEventNotification",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEventNotification",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEventNotification",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEventNotification",
    ),
    "v2.core.account[configuration.customer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.customer].updated": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification",
    ),
    "v2.core.account[configuration.merchant].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.merchant].updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification",
    ),
    "v2.core.account[configuration.recipient].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.recipient].updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification",
    ),
    "v2.core.account[configuration.storer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.storer].updated": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification",
    ),
    "v2.core.account[defaults].updated": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        "V2CoreAccountIncludingDefaultsUpdatedEventNotification",
    ),
    "v2.core.account[identity].updated": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        "V2CoreAccountIncludingIdentityUpdatedEventNotification",
    ),
    "v2.core.account[requirements].updated": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        "V2CoreAccountIncludingRequirementsUpdatedEventNotification",
    ),
    "v2.core.account_link.returned": (
        "stripe.events._v2_core_account_link_returned_event",
        "V2CoreAccountLinkReturnedEventNotification",
    ),
    "v2.core.account_person.created": (
        "stripe.events._v2_core_account_person_created_event",
        "V2CoreAccountPersonCreatedEventNotification",
    ),
    "v2.core.account_person.deleted": (
        "stripe.events._v2_core_account_person_deleted_event",
        "V2CoreAccountPersonDeletedEventNotification",
    ),
    "v2.core.account_person.updated": (
        "stripe.events._v2_core_account_person_updated_event",
        "V2CoreAccountPersonUpdatedEventNotification",
    ),
    "v2.core.account.updated": (
        "stripe.events._v2_core_account_updated_event",
        "V2CoreAccountUpdatedEventNotification",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEventNotification",
    ),
    "v2.core.health.event_generation_failure.resolved": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        "V2CoreHealthEventGenerationFailureResolvedEventNotification",
    ),
    "v2.money_management.adjustment.created": (
        "stripe.events._v2_money_management_adjustment_created_event",
        "V2MoneyManagementAdjustmentCreatedEventNotification",
    ),
    "v2.money_management.financial_account.created": (
        "stripe.events._v2_money_management_financial_account_created_event",
        "V2MoneyManagementFinancialAccountCreatedEventNotification",
    ),
    "v2.money_management.financial_account.updated": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        "V2MoneyManagementFinancialAccountUpdatedEventNotification",
    ),
    "v2.money_management.financial_address.activated": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        "V2MoneyManagementFinancialAddressActivatedEventNotification",
    ),
    "v2.money_management.financial_address.failed": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        "V2MoneyManagementFinancialAddressFailedEventNotification",
    ),
    "v2.money_management.inbound_transfer.available": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        "V2MoneyManagementInboundTransferAvailableEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_failed": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        "V2MoneyManagementInboundTransferBankDebitFailedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_processing": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_queued": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_returned": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_succeeded": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification",
    ),
    "v2.money_management.outbound_payment.canceled": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        "V2MoneyManagementOutboundPaymentCanceledEventNotification",
    ),
    "v2.money_management.outbound_payment.created": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        "V2MoneyManagementOutboundPaymentCreatedEventNotification",
    ),
    "v2.money_management.outbound_payment.failed": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        "V2MoneyManagementOutboundPaymentFailedEventNotification",
    ),
    "v2.money_management.outbound_payment.posted": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        "V2MoneyManagementOutboundPaymentPostedEventNotification",
    ),
    "v2.money_management.outbound_payment.returned": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        "V2MoneyManagementOutboundPaymentReturnedEventNotification",
    ),
    "v2.money_management.outbound_payment.updated": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        "V2MoneyManagementOutboundPaymentUpdatedEventNotification",
    ),
    "v2.money_management.outbound_transfer.canceled": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        "V2MoneyManagementOutboundTransferCanceledEventNotification",
    ),
    "v2.money_management.outbound_transfer.created": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        "V2MoneyManagementOutboundTransferCreatedEventNotification",
    ),
    "v2.money_management.outbound_transfer.failed": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        "V2MoneyManagementOutboundTransferFailedEventNotification",
    ),
    "v2.money_management.outbound_transfer.posted": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        "V2MoneyManagementOutboundTransferPostedEventNotification",
    ),
    "v2.money_management.outbound_transfer.returned": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        "V2MoneyManagementOutboundTransferReturnedEventNotification",
    ),
    "v2.money_management.outbound_transfer.updated": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        "V2MoneyManagementOutboundTransferUpdatedEventNotification",
    ),
    "v2.money_management.payout_method.updated": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        "V2MoneyManagementPayoutMethodUpdatedEventNotification",
    ),
    "v2.money_management.received_credit.available": (
        "stripe.events._v2_money_management_received_credit_available_event",
        "V2MoneyManagementReceivedCreditAvailableEventNotification",
    ),
    "v2.money_management.received_credit.failed": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        "V2MoneyManagementReceivedCreditFailedEventNotification",
    ),
    "v2.money_management.received_credit.returned": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        "V2MoneyManagementReceivedCreditReturnedEventNotification",
    ),
    "v2.money_management.received_credit.succeeded": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        "V2MoneyManagementReceivedCreditSucceededEventNotification",
    ),
    "v2.money_management.received_debit.canceled": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        "V2MoneyManagementReceivedDebitCanceledEventNotification",
    ),
    "v2.money_management.received_debit.failed": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        "V2MoneyManagementReceivedDebitFailedEventNotification",
    ),
    "v2.money_management.received_debit.pending": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        "V2MoneyManagementReceivedDebitPendingEventNotification",
    ),
    "v2.money_management.received_debit.succeeded": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        "V2MoneyManagementReceivedDebitSucceededEventNotification",
    ),
    "v2.money_management.received_debit.updated": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        "V2MoneyManagementReceivedDebitUpdatedEventNotification",
    ),
    "v2.money_management.transaction.created": (
        "stripe.events._v2_money_management_transaction_created_event",
        "V2MoneyManagementTransactionCreatedEventNotification",
    ),
    "v2.money_management.transaction.updated": (
        "stripe.events._v2_money_management_transaction_updated_event",
        "V2MoneyManagementTransactionUpdatedEventNotification",
    ),
}


def get_v2_event_notification_class(type_: str):
    if type_ not in _V2_EVENT_NOTIFICATION_CLASS_LOOKUP:
        return UnknownEventNotification

    import_path, class_name = _V2_EVENT_NOTIFICATION_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


ALL_EVENT_NOTIFICATIONS = Union[
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V2CoreAccountClosedEventNotification",
    "V2CoreAccountCreatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification",
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification",
    "V2CoreAccountIncludingIdentityUpdatedEventNotification",
    "V2CoreAccountIncludingRequirementsUpdatedEventNotification",
    "V2CoreAccountLinkReturnedEventNotification",
    "V2CoreAccountPersonCreatedEventNotification",
    "V2CoreAccountPersonDeletedEventNotification",
    "V2CoreAccountPersonUpdatedEventNotification",
    "V2CoreAccountUpdatedEventNotification",
    "V2CoreEventDestinationPingEventNotification",
    "V2CoreHealthEventGenerationFailureResolvedEventNotification",
    "V2MoneyManagementAdjustmentCreatedEventNotification",
    "V2MoneyManagementFinancialAccountCreatedEventNotification",
    "V2MoneyManagementFinancialAccountUpdatedEventNotification",
    "V2MoneyManagementFinancialAddressActivatedEventNotification",
    "V2MoneyManagementFinancialAddressFailedEventNotification",
    "V2MoneyManagementInboundTransferAvailableEventNotification",
    "V2MoneyManagementInboundTransferBankDebitFailedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification",
    "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification",
    "V2MoneyManagementOutboundPaymentCanceledEventNotification",
    "V2MoneyManagementOutboundPaymentCreatedEventNotification",
    "V2MoneyManagementOutboundPaymentFailedEventNotification",
    "V2MoneyManagementOutboundPaymentPostedEventNotification",
    "V2MoneyManagementOutboundPaymentReturnedEventNotification",
    "V2MoneyManagementOutboundPaymentUpdatedEventNotification",
    "V2MoneyManagementOutboundTransferCanceledEventNotification",
    "V2MoneyManagementOutboundTransferCreatedEventNotification",
    "V2MoneyManagementOutboundTransferFailedEventNotification",
    "V2MoneyManagementOutboundTransferPostedEventNotification",
    "V2MoneyManagementOutboundTransferReturnedEventNotification",
    "V2MoneyManagementOutboundTransferUpdatedEventNotification",
    "V2MoneyManagementPayoutMethodUpdatedEventNotification",
    "V2MoneyManagementReceivedCreditAvailableEventNotification",
    "V2MoneyManagementReceivedCreditFailedEventNotification",
    "V2MoneyManagementReceivedCreditReturnedEventNotification",
    "V2MoneyManagementReceivedCreditSucceededEventNotification",
    "V2MoneyManagementReceivedDebitCanceledEventNotification",
    "V2MoneyManagementReceivedDebitFailedEventNotification",
    "V2MoneyManagementReceivedDebitPendingEventNotification",
    "V2MoneyManagementReceivedDebitSucceededEventNotification",
    "V2MoneyManagementReceivedDebitUpdatedEventNotification",
    "V2MoneyManagementTransactionCreatedEventNotification",
    "V2MoneyManagementTransactionUpdatedEventNotification",
]
