---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1349
is_stripe_api_change: true
released_in_version: 10.2.0b1
---

* Add support for `filters` on resource class `stripe.QuotePreviewInvoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`
* Remove support for `payment_method_set_as_default` on resource class `stripe.CustomerSession.Components.PaymentElement.Features` and parameter class `stripe.CustomerSession.CreateParamsComponentsPaymentElementFeatures`
* Add support for `ch_uid` on enums `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
