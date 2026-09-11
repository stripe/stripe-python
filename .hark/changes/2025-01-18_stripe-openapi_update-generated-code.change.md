---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1439
is_stripe_api_change: true
released_in_version: 11.5.0b2
---

* Add support for `pay_by_bank_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
* Add support for `directorship_declaration` on parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
* Add support for `proof_of_ultimate_beneficial_ownership` on parameter class `stripe.Account.CreateParamsDocuments`
* Add support for `financial_account` on resource class `stripe.AccountSession.Components`
* Add support for `issuing_card` on resource class `stripe.AccountSession.Components`
* Add support for `tax_threshold_monitoring` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `pay_by_bank` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
* Add support for `discounts` on resource `stripe.checkout.Session`
* Add support for `jpy` on parameter classes `stripe.terminal.Configuration.CreateParamsTipping` and `stripe.terminal.Configuration.ModifyParamsTipping` and resource class `stripe.terminal.Configuration.Tipping`
* Add support for `always_invoice` on enums `stripe.billing_portal.Configuration.Features.SubscriptionCancel.proration_behavior`, `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionCancel.proration_behavior`, and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionCancel.proration_behavior`
* Add support for `SD` on enums `stripe.checkout.Session.ShippingAddressCollection.allowed_countries`, `stripe.checkout.Session.CreateParamsShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.ShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.CreateParamsShippingAddressCollection.allowed_countries`, and `stripe.PaymentLink.ModifyParamsShippingAddressCollection.allowed_countries`
* Add support for `pay_by_bank` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
* Add support for `2025-01-27.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
