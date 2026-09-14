---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1273
is_stripe_api_change: true
released_in_version: 8.8.0
---

* Add support for new resources `ConfirmationToken` and `Forwarding.Request`
* Add support for `retrieve` method on resource `ConfirmationToken`
* Add support for `create`, `list`, and `retrieve` methods on resource `Request`
* Add support for `mobilepay_payments` on `Account.Capabilities`, `Account.CreateParamsCapabilities`, and `Account.UpdateParamsCapabilities`
* Add support for new values `forwarding_api_inactive`, `forwarding_api_invalid_parameter`, `forwarding_api_upstream_connection_error`, and `forwarding_api_upstream_connection_timeout` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `SetupAttempt.SetupError.code`, `SetupIntent.LastSetupError.code`, and `StripeError.code`
* Add support for `payment_reference` on `Charge.PaymentMethodDetails.UsBankAccount`
* Add support for `payout` on `Treasury.ReceivedDebit.LinkedFlows`
* Add support for `name` on `ConfigurationService.CreateParams`, `ConfigurationService.UpdateParams`, and `Configuration` for terminal
 * Add support for `confirmation_token` on `PaymentIntentService.ConfirmParams`, `PaymentIntentService.CreateParams`, `SetupIntentService.ConfirmParams`, and `SetupIntentService.CreateParams`
 * Add support for new value `mobilepay` on enums `Customer.ListPaymentMethodsParams.type`, `PaymentMethod.CreateParams.type`, and `PaymentMethod.ListParams.type`
 * Add support for `mobilepay` on `Charge.PaymentMethodDetails`, `PaymentIntent.PaymentMethodOptions`, `PaymentIntentService.ConfirmParamsPaymentMethodData`, `PaymentIntentService.ConfirmParamsPaymentMethodOptions`, `PaymentIntentService.CreateParamsPaymentMethodData`, `PaymentIntentService.CreateParamsPaymentMethodOptions`, `PaymentIntentService.UpdateParamsPaymentMethodData`, `PaymentIntentService.UpdateParamsPaymentMethodOptions`, `PaymentMethod.CreateParams`, `PaymentMethod`, `SetupIntentService.ConfirmParamsPaymentMethodData`, `SetupIntentService.CreateParamsPaymentMethodData`, and `SetupIntentService.UpdateParamsPaymentMethodData`
 * Add support for new value `mobilepay` on enums `PaymentIntentService.ConfirmParamsPaymentMethodData.type`, `PaymentIntentService.CreateParamsPaymentMethodData.type`, `PaymentIntentService.UpdateParamsPaymentMethodData.type`, `SetupIntentService.ConfirmParamsPaymentMethodData.type`, `SetupIntentService.CreateParamsPaymentMethodData.type`, and `SetupIntentService.UpdateParamsPaymentMethodData.type`
 * Add support for new value `mobilepay` on enum `PaymentMethod.type`
