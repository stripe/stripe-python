---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1844
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.4.0a4
---

* ⚠️ Remove support for resource `FrMealVouchersOnboarding`
* ⚠️ Remove support for `create`, `list`, `modify`, and `retrieve` methods on resource `FrMealVouchersOnboarding`
* Add support for `create` method on resource `PaymentRecord`
* Add support for new value `chaps` on enums `FundingInstructions.BankTransfer.FinancialAddress.supported_networks` and `PaymentIntent.NextAction.DisplayBankTransferInstruction.FinancialAddress.supported_networks`
* ⚠️ Remove support for `financial_accounts_transactions`, `financial_accounts`, and `recipients_list` on `AccountSessionCreateParamsComponent`
* Add support for `smart_disputes_management` on `AccountSession.Component.DisputesList.Feature`, `AccountSession.Component.Payment.Feature`, `AccountSession.Component.PaymentDetail.Feature`, and `AccountSession.Component.PaymentDispute.Feature`
* ⚠️ Add support for new value `ic_nif` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, and `Tax.Transaction.CustomerDetail.TaxId.type`
* Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enum `Event.type`
* Add support for `mode` on `FinancialConnections.Session.ManualEntry`
* Add support for new values `alipay` and `sequra` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for new value `stripe_internal_error` on enum `Issuing.Authorization.RequestHistory.reason`
* Add support for `business_name` on `Issuing.Card.Shipping`
* Add support for new value `correos` on enum `Issuing.Card.Shipping.carrier`
* ⚠️ Change type of `Issuing.Transaction.NetworkDatum.trace_id` from `IssuingTransactionTraceId` to `nullable(IssuingTransactionTraceId)`
* Add support for `pause_schedules` on `QuotePreviewSubscriptionSchedule`, `SubscriptionScheduleCreateParams`, `SubscriptionScheduleModifyParams`, and `SubscriptionSchedule`
* Add support for `trial` on `QuotePreviewSubscriptionSchedule.Phase` and `SubscriptionSchedule.Phase`
* Add support for `payment_record` on `RefundCreateParams`
* Add support for `redirect_to_url` on `SharedPayment.IssuedToken.NextAction`
* ⚠️ Change type of `SharedPayment.IssuedToken.NextAction.type` from `literal('use_stripe_sdk')` to `enum('redirect_to_url'|'use_stripe_sdk')`
* Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for snapshot events `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, and `financial_connections.account.upcoming_deactivation` with resource `financial_connections.Account`
* Add support for snapshot events `financial_connections.authorization.expected_deactivation_date_updated` and `financial_connections.authorization.upcoming_deactivation` with resource `financial_connections.Authorization`
