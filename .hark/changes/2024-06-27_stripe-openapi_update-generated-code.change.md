---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1353
is_stripe_api_change: true
released_in_version: 10.1.0
---

* Add support for `email_type` on parameter classes `stripe.CreditNote.CreateParams`, `stripe.CreditNote.PreviewLinesParams`, and `stripe.CreditNote.PreviewParams`
* Add support for `filters` on parameter classes `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections` and resource classes `stripe.Invoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.PaymentIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.SetupIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`, and `stripe.checkout.Session.PaymentMethodOptions.UsBankAccount.FinancialConnections`
* Add support for `account_subcategories` on parameter class `stripe.financial_connections.Session.CreateParamsFilters` and resource class `stripe.financial_connections.Session.Filters`
* Add support for `reboot_window` on parameter classes `stripe.terminal.Configuration.CreateParams` and `stripe.terminal.Configuration.ModifyParams` and resource `stripe.terminal.Configuration`
* Add support for `day` on enum `stripe.billing.Meter.ListEventSummariesParams.value_grouping_window`
* Add support for `multibanco` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
* Add support for `twint` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
* Add support for `zip` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
