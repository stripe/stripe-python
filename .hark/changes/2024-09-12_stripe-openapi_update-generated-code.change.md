---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1391
is_stripe_api_change: true
released_in_version: 10.11.0
---

* Add support for `template` on parameter classes `stripe.Customer.CreateParamsInvoiceSettingsRenderingOptions`, `stripe.Customer.ModifyParamsInvoiceSettingsRenderingOptions`, `stripe.Invoice.CreateParamsRendering`, and `stripe.Invoice.ModifyParamsRendering` and resource classes `stripe.Customer.InvoiceSettings.RenderingOptions` and `stripe.Invoice.Rendering`
* Add support for resource `stripe.InvoiceRenderingTemplate`
* Add support for `required` on parameter classes `stripe.PaymentLink.CreateParamsTaxIdCollection`, `stripe.PaymentLink.ModifyParamsTaxIdCollection`, and `stripe.checkout.Session.CreateParamsTaxIdCollection` and resource classes `stripe.PaymentLink.TaxIdCollection` and `stripe.checkout.Session.TaxIdCollection`
* Add support for `submitted` on enum `stripe.issuing.Card.Shipping.status`
* Change type of `tax_amounts` on  `stripe.InvoiceLineItem` from `Optional[List[TaxAmount]]` to `List[TaxAmount]`
* Change type of `tax_rates` on  `stripe.InvoiceLineItem` from `Optional[List[TaxRate]]` to `List[TaxRate]`
* Change type of `status_details` on  `stripe.test_helpers.TestClock` from `Optional[StatusDetails]` to `StatusDetails`
