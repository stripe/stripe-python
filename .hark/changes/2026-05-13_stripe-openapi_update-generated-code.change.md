---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1807
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0a5
---

* Add support for new resources `v2.core.FeeBatch`, `v2.core.FeeEntry`, `v2.money_management.DebitDispute`, and `v2.money_management.FinancialAccountStatement`
* Add support for `simulate_network_lifecycle_pre_arbitration_response` and `simulate_network_lifecycle_pre_arbitration_submission` test helper methods on resource `issuing.Dispute`
* Add support for `list` method on resource `PaymentLocation`
* Add support for `list` and `retrieve` methods on resources `v2.core.FeeBatch`, `v2.core.FeeEntry`, and `v2.money_management.FinancialAccountStatement`
* Add support for `create`, `list`, and `retrieve` methods on resource `v2.money_management.DebitDispute`
* Add support for `discounts` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
* Add support for `amount_sale` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
* Add support for `amount_discount` and `breakdown` on `DelegatedCheckout.RequestedSession.TotalDetail`
* ⚠️ Remove support for `check_deposit_address` on `Invoice.PaymentSetting.PaymentMethodOption.CheckScan`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionCheckScan`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionCheckScan`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.CheckScan`, `Subscription.PaymentSetting.PaymentMethodOption.CheckScan`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionCheckScan`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionCheckScan`
* Add support for `payment_evaluations` on `PaymentAttemptRecordReportGuaranteedParams`, `PaymentRecordReportPaymentAttemptGuaranteedParams`, `PaymentRecordReportPaymentAttemptParamsGuaranteed`, and `PaymentRecordReportPaymentParamsGuaranteed`
* Add support for `location` on `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, `PaymentIntentModifyParamsPaymentDetail`, `SetupIntentConfirmParamsSetupDetail`, `SetupIntentCreateParamsSetupDetail`, and `SetupIntentModifyParamsSetupDetail`
* Add support for `onboarding_data_update_acknowledged` on `PaymentLocationModifyParams`
* Change `PaymentLocationCreateParamsAddress.country` and `PaymentLocationModifyParamsAddress.country` to be optional
* Add support for `customer` on `radar.CustomerEvaluationModifyParams`
* Add support for `status` on `Radar.CustomerEvaluation` and `radar.CustomerEvaluationModifyParams`
* Change `radar.CustomerEvaluationModifyParams.type` to be optional
* Add support for `payment_behavior` on `SubscriptionResumeParams`
* Add support for `dispute_details` on `V2.MoneyManagement.ReceivedDebit`
* ⚠️ Add support for new value `debit_dispute` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for `debit_dispute` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* ⚠️ Add support for new value `debit_dispute` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for `payment_attempt_record` on `EventsV2PaymentsOffSessionPaymentAttemptFailedEvent` and `EventsV2PaymentsOffSessionPaymentFailedEvent`
* Add support for event notifications `V2MoneyManagementFinancialAccountStatementCreatedEvent` and `V2MoneyManagementFinancialAccountStatementRestatedEvent` with related object `v2.money_management.FinancialAccountStatement`
