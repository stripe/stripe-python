---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1873
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.6.0a1
---

* Add support for new resource `v2.tax.OperationsResolveAddressResult`
* Add support for `resolve_address` method on resource `v2.tax.OperationsResolveAddressResult`
* Add support for `confirm` and `fx_quote` methods on resource `v2.money_management.PayoutIntent`
* ⚠️ Add support for new value `partner_disabled` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
* ⚠️ Remove support for values `partner_disabled_dispute_rate`, `partner_disabled_responsibilities`, `partner_disabled_restricted_business`, and `partner_disabled_suspected_fraud` from enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
* Add support for `customer_update` on `BillingPortal.Session.Flow`
* Add support for new value `customer_update` on enum `BillingPortal.Session.Flow.type`
* Add support for `funding_source_group` on `Charge.PaymentMethodDetail.Link`
* ⚠️ Remove support for `pricing_group` on `Charge.PaymentMethodDetail.Link`
* Add support for new value `celo` on enum `Crypto.CustomerConsumerWallet.network`
* Add support for new value `celo` on enums `Crypto.OnrampSession.TransactionDetail.destination_network`, `crypto.OnrampSessionCreateParams.destination_network`, `crypto.OnrampSessionListParams.destination_network`, and `crypto.OnrampTransactionLimitsRetrieveParams.destination_network`
* Add support for new value `celo` on enums `Crypto.OnrampSession.TransactionDetail.destination_networks` and `crypto.OnrampSessionCreateParams.destination_networks`
* Add support for `celo` on `Crypto.OnrampSession.TransactionDetail.WalletAddress`
* Add support for `customer_portal` on `CustomerSession.Component`
* Add support for `applied_to_invoice` and `type` on `CustomerCreateCustomerBalanceTransactionParams`
* Add support for `classification_state` and `enrichment_state` on `FinancialConnections.Account`
* Add support for `country` on `FinancialConnections.Session.Filter`
* Add support for `classifications` and `enrichments` on `FinancialConnections.Transaction`
* Add support for new values `billie`, `paypay`, and `vipps` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for `customer_balance` on `Invoice` and `QuotePreviewInvoice`
* Add support for `billie` on `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
* Add support for `hold_amount_details` and `hold_amount` on `Issuing.Authorization.PendingRequest` and `Issuing.Authorization.RequestHistory`
* Add support for new values `hu` and `ro` on enums `Issuing.Cardholder.preferred_locales`, `issuing.CardholderCreateParams.preferred_locales`, and `issuing.CardholderModifyParams.preferred_locales`
* Add support for new values `authentication_failure`, `expired_payment_method`, `incorrect_cvc`, `incorrect_number`, `incorrect_postal_code`, `insufficient_funds`, `payment_method_restricted`, and `processing_error` on enums `PaymentAttemptRecordReportFailedParams.failure_code`, `PaymentRecordReportPaymentAttemptFailedParams.failure_code`, `PaymentRecordReportPaymentAttemptParamsFailed.failure_code`, and `PaymentRecordReportPaymentParamsFailed.failure_code`
* Add support for `network_decline_code` on `PaymentAttemptRecordReportFailedParamsPaymentMethodDetailCard` and `PaymentRecordReportPaymentAttemptFailedParamsPaymentMethodDetailCard`
* Add support for `setup_future_usage` on `PaymentIntent.PaymentMethodOption.Sequra`
* Add support for `status` on `QuotePreviewSubscriptionSchedule.PauseSchedule.Pause`, `QuotePreviewSubscriptionSchedule.PauseSchedule.Resume`, `SubscriptionSchedule.PauseSchedule.Pause`, and `SubscriptionSchedule.PauseSchedule.Resume`
* Change `SubscriptionScheduleCreateParamsPauseSchedule.pause` to be optional
* Change type of `SubscriptionScheduleModifyParamsPauseSchedule.resume` from `pause_schedule_update_resume_params` to `emptyable(pause_schedule_update_resume_params)`
* Add support for `acquirer` on `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.Dimension`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.Dimension`, `V2.Core.Health.Alert.AuthorizationRateDrop.Dimension`, and `V2.Core.Health.AlertHistoryEntry.AuthorizationRateDrop.Dimension`
* ⚠️ Change type of `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.Dimension.type`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.Dimension.type`, `V2.Core.Health.Alert.AuthorizationRateDrop.Dimension.type`, and `V2.Core.Health.AlertHistoryEntry.AuthorizationRateDrop.Dimension.type` from `literal('issuer')` to `enum('acquirer'|'issuer')`
* Add support for `confirmation_method` on `V2.MoneyManagement.PayoutIntent` and `v2.money_management.PayoutIntentCreateParams`
* Add support for `estimated_fees` and `fx_quote` on `V2.MoneyManagement.PayoutIntent`
* Add support for `debited` on `V2.MoneyManagement.PayoutIntent.From`
* Add support for `confirm` on `V2.MoneyManagement.PayoutIntent.NextAction`
* ⚠️ Change type of `V2.MoneyManagement.PayoutIntent.NextAction.type` from `literal('handle_failure')` to `enum('confirm'|'handle_failure')`
* Add support for `credited` on `V2.MoneyManagement.PayoutIntent.To`
* Add support for new value `one_time_fees` on enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractListParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
* Add support for event notification `V1BalanceSettingsUpdatedEvent` with related object `BalanceSettings`
* Add support for event notification `V1BillingCreditBalanceTransactionCreatedEvent` with related object `billing.CreditBalanceTransaction`
* Add support for event notifications `V1BillingCreditGrantCreatedEvent` and `V1BillingCreditGrantUpdatedEvent` with related object `billing.CreditGrant`
* Add support for event notifications `V1BillingMeterCreatedEvent`, `V1BillingMeterDeactivatedEvent`, `V1BillingMeterReactivatedEvent`, and `V1BillingMeterUpdatedEvent` with related object `billing.Meter`
* Add support for event notifications `V1FinancialConnectionsAccountAccountNumbersUpdatedEvent`, `V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent`, `V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent`, `V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent`, and `V1FinancialConnectionsAccountUpcomingDeactivationEvent` with related object `financial_connections.Account`
* Add support for event notification `V1InvoicePaymentAttemptRequiredEvent` with related object `Invoice`
* Add support for error type `FxQuoteNeedsRefreshError`
