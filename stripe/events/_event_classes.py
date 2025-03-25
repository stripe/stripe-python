# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
)
from stripe.events._v2_money_management_financial_address_activated_event import (
    V2MoneyManagementFinancialAddressActivatedEvent,
)
from stripe.events._v2_money_management_financial_address_failed_event import (
    V2MoneyManagementFinancialAddressFailedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_available_event import (
    V2MoneyManagementInboundTransferAvailableEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
    V2MoneyManagementInboundTransferBankDebitFailedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
    V2MoneyManagementInboundTransferBankDebitProcessingEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
    V2MoneyManagementInboundTransferBankDebitQueuedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
    V2MoneyManagementInboundTransferBankDebitReturnedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
    V2MoneyManagementInboundTransferBankDebitSucceededEvent,
)
from stripe.events._v2_money_management_received_credit_available_event import (
    V2MoneyManagementReceivedCreditAvailableEvent,
)
from stripe.events._v2_money_management_received_credit_failed_event import (
    V2MoneyManagementReceivedCreditFailedEvent,
)
from stripe.events._v2_money_management_received_credit_returned_event import (
    V2MoneyManagementReceivedCreditReturnedEvent,
)
from stripe.events._v2_money_management_received_credit_succeeded_event import (
    V2MoneyManagementReceivedCreditSucceededEvent,
)
from stripe.events._v2_money_management_received_debit_canceled_event import (
    V2MoneyManagementReceivedDebitCanceledEvent,
)
from stripe.events._v2_money_management_received_debit_failed_event import (
    V2MoneyManagementReceivedDebitFailedEvent,
)
from stripe.events._v2_money_management_received_debit_pending_event import (
    V2MoneyManagementReceivedDebitPendingEvent,
)
from stripe.events._v2_money_management_received_debit_succeeded_event import (
    V2MoneyManagementReceivedDebitSucceededEvent,
)
from stripe.events._v2_money_management_received_debit_updated_event import (
    V2MoneyManagementReceivedDebitUpdatedEvent,
)


THIN_EVENT_CLASSES = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2MoneyManagementFinancialAddressActivatedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAddressActivatedEvent,
    V2MoneyManagementFinancialAddressFailedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAddressFailedEvent,
    V2MoneyManagementInboundTransferAvailableEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferAvailableEvent,
    V2MoneyManagementInboundTransferBankDebitFailedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitFailedEvent,
    V2MoneyManagementInboundTransferBankDebitProcessingEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitProcessingEvent,
    V2MoneyManagementInboundTransferBankDebitQueuedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitQueuedEvent,
    V2MoneyManagementInboundTransferBankDebitReturnedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitReturnedEvent,
    V2MoneyManagementInboundTransferBankDebitSucceededEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitSucceededEvent,
    V2MoneyManagementReceivedCreditAvailableEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditAvailableEvent,
    V2MoneyManagementReceivedCreditFailedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditFailedEvent,
    V2MoneyManagementReceivedCreditReturnedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditReturnedEvent,
    V2MoneyManagementReceivedCreditSucceededEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditSucceededEvent,
    V2MoneyManagementReceivedDebitCanceledEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitCanceledEvent,
    V2MoneyManagementReceivedDebitFailedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitFailedEvent,
    V2MoneyManagementReceivedDebitPendingEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitPendingEvent,
    V2MoneyManagementReceivedDebitSucceededEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitSucceededEvent,
    V2MoneyManagementReceivedDebitUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitUpdatedEvent,
}
