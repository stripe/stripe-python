---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1361
is_stripe_api_change: true
released_in_version: 10.6.0b1
---

* Add support for `capital` on parameter class `stripe.Account.CreateParamsSettings` and resource class `stripe.Account.Settings`
* Add support for `payment` on resource `stripe.InvoicePayment`
* Add support for `async_workflows` on parameter classes `stripe.PaymentIntent.CaptureParams`, `stripe.PaymentIntent.ConfirmParams`, `stripe.PaymentIntent.CreateParams`, `stripe.PaymentIntent.DecrementAuthorizationParams`, `stripe.PaymentIntent.IncrementAuthorizationParams`, and `stripe.PaymentIntent.ModifyParams` and resource `stripe.PaymentIntent`
* Add support for `payto` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for resource `stripe.billing.Alert`
* Add support for resource `stripe.tax.Association`
* Add support for `display_name` on parameter classes `stripe.treasury.FinancialAccount.CreateParams` and `stripe.treasury.FinancialAccount.ModifyParams` and resource `stripe.treasury.FinancialAccount`
* Remove support for `charge` on resource `stripe.InvoicePayment`
* Remove support for `payment_intent` on resource `stripe.InvoicePayment`
* Add support for `issuing.account_closed_for_not_providing_business_model_clarification` on enum `stripe.AccountNotice.reason`
* Add support for `issuing.account_closed_for_not_providing_url_clarification` on enum `stripe.AccountNotice.reason`
* Add support for `issuing.account_closed_for_not_providing_use_case_clarification` on enum `stripe.AccountNotice.reason`
* Add support for `billing.alert.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `multibanco` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`
