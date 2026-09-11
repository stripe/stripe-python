---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1797
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0b2
---

* Add support for new resources `v2.commerce.ProductCatalogImport`, `v2.data.reporting.QueryRun`, `v2.extend.WorkflowRun`, `v2.extend.Workflow`, `v2.iam.ActivityLog`, `v2.network.BusinessProfile`, and `v2.orchestrated_commerce.Agreement`
* Add support for `confirm`, `create`, `list`, `retrieve`, and `terminate` methods on resource `v2.orchestrated_commerce.Agreement`
* Add support for `me` and `retrieve` methods on resource `v2.network.BusinessProfile`
* Add support for `list` method on resource `v2.iam.ActivityLog`
* Add support for `list` and `retrieve` methods on resource `v2.extend.WorkflowRun`
* Add support for `invoke`, `list`, and `retrieve` methods on resource `v2.extend.Workflow`
* Add support for `create` and `retrieve` methods on resources `v2.commerce.ProductCatalogImport` and `v2.data.reporting.QueryRun`
* ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.konbini`, `V2.Billing.CollectionSetting.PaymentMethodOption.konbini`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.konbini`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.konbini`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.konbini` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSetting.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.sepa_debit`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.sepa_debit`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.sepa_debit` from `map(string: dynamic)` to `an object`
* ⚠️ Add support for new values `cn_bank_account` and `jp_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* ⚠️ Add support for new values `futsu` and `toza` on enums `V2.Core.Vault.GbBankAccount.bank_account_type` and `V2.MoneyManagement.PayoutMethod.BankAccount.bank_account_type`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_processing` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_queued` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_succeeded` from `map(string: dynamic)` to `an object`
* ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
* ⚠️ Add support for new values `inbound_transfer_reversal`, `outbound_payment_reversal`, `outbound_transfer_reversal`, `received_credit_reversal`, `received_debit_reversal`, and `stripe_fee_tax` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* ⚠️ Remove support for value `return` from enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for new values `futsu` and `toza` on enums `v2.core.vault.GbBankAccountCreateParams.bank_account_type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount.bank_account_type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount.bank_account_type`
* Change type of `v2.core.BatchJobCreateParamsEndpoint.http_method` from `literal('post')` to `enum('delete'|'post')`
* ⚠️ Add support for new value `meter_event_value_too_many_digits` on enums `EventsV1BillingMeterErrorReportTriggeredEvent.Reason.ErrorType.code` and `EventsV1BillingMeterNoMeterFoundEvent.Reason.ErrorType.code`
* Add support for `treasury_transaction` on `EventsV2MoneyManagementTransactionCreatedEvent`
* Add support for event notifications `V2CommerceProductCatalogImportsFailedEvent`, `V2CommerceProductCatalogImportsProcessingEvent`, `V2CommerceProductCatalogImportsSucceededEvent`, and `V2CommerceProductCatalogImportsSucceededWithErrorsEvent` with related object `v2.commerce.ProductCatalogImport`
* Add support for event notifications `V2DataReportingQueryRunCreatedEvent`, `V2DataReportingQueryRunFailedEvent`, `V2DataReportingQueryRunSucceededEvent`, and `V2DataReportingQueryRunUpdatedEvent` with related object `v2.data.reporting.QueryRun`
* Add support for event notifications `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, and `V2ExtendWorkflowRunSucceededEvent` with related object `v2.extend.WorkflowRun`
* Add support for event notifications `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, and `V2OrchestratedCommerceAgreementTerminatedEvent` with related object `v2.orchestrated_commerce.Agreement`
* Add support for error type `CannotProceedError`
