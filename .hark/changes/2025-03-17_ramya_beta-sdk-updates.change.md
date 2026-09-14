---
title: Beta SDK updates between Open API versions 1473 and 1505
pr_url: https://github.com/stripe/stripe-python/pull/1469
released_in_version: 11.7.0b1
---

* Add support for `target_date` on parameter classes `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit`, `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit`, `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit`, and `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit` and resource classes `stripe.Order.Payment.Settings.PaymentMethodOptions.AcssDebit` and `stripe.Order.Payment.Settings.PaymentMethodOptions.SepaDebit`
* Add support for `succeed_input_collection` and `timeout_input_collection` on resource `stripe.terminal.Reader`
