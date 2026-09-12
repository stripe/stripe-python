---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1667
is_stripe_api_change: true
released_in_version: 14.0.0
---

* Add support for new resources `tax.Association` and `terminal.OnboardingLink`
* Add support for `find` method on resource `tax.Association`
* Add support for `create` method on resource `terminal.OnboardingLink`
* Add support for `payment_method_configuration` on `BillingPortal.Configuration.Feature.PaymentMethodUpdate`
* Add support for `transaction_id` on `Charge.PaymentMethodDetail.Ideal`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal`, and `PaymentRecord.PaymentMethodDetail.Ideal`
* Add support for new value `finom` on enums `Charge.PaymentMethodDetail.Ideal.bank`, `ConfirmationToken.PaymentMethodPreview.Ideal.bank`, `ConfirmationTokenCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentModifyParamsPaymentMethodDatumIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethodCreateParamsIdeal.bank`, `PaymentRecord.PaymentMethodDetail.Ideal.bank`, `SetupAttempt.PaymentMethodDetail.Ideal.bank`, `SetupIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `SetupIntentCreateParamsPaymentMethodDatumIdeal.bank`, and `SetupIntentModifyParamsPaymentMethodDatumIdeal.bank`
* Add support for new value `FNOMNL22` on enums `Charge.PaymentMethodDetail.Ideal.bic`, `ConfirmationToken.PaymentMethodPreview.Ideal.bic`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bic`, `PaymentMethod.Ideal.bic`, `PaymentRecord.PaymentMethodDetail.Ideal.bic`, and `SetupAttempt.PaymentMethodDetail.Ideal.bic`
* Add support for new value `tokenized_account_number_deactivated` on enums `ConfirmationToken.PaymentMethodPreview.UsBankAccount.StatusDetail.Blocked.reason` and `PaymentMethod.UsBankAccount.StatusDetail.Blocked.reason`
* Add support for `created` on `CustomerListCustomerBalanceTransactionParams` and `InvoicePaymentListParams`
* Add support for new values `financial_connections.account.account_numbers_updated` and `financial_connections.account.upcoming_account_number_expiry` on enum `Event.type`
* Add support for `account_numbers` on `FinancialConnections.Account`
* Change type of `FinancialConnections.Session.client_secret` from `string` to `nullable(string)`
* Add support for `fraud_risk` on `issuing.AuthorizationCreateParamsRiskAssessment`
* Add support for `latest_fraud_warning` on `Issuing.Card`
* Add support for `hooks` on `PaymentIntentCaptureParams`, `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentIncrementAuthorizationParams`, `PaymentIntentModifyParams`, and `PaymentIntent`
* Add support for `mb_way` and `twint` on `Refund.DestinationDetail`
* Add support for new values `financial_connections.account.account_numbers_updated` and `financial_connections.account.upcoming_account_number_expiry` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for snapshot events `financial_connections.account.account_numbers_updated` and `financial_connections.account.upcoming_account_number_expiry` with resource `financial_connections.Account`
