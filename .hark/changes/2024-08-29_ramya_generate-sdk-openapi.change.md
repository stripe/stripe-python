---
title: Generate SDK for OpenAPI spec version 1230
pr_url: https://github.com/stripe/stripe-python/pull/1385
is_stripe_api_change: true
released_in_version: 10.9.0
---

* Add support for `status_details` on resource `stripe.test_helpers.TestClock`
* Change type of `fields` on  `stripe.AccountLink.CreateParamsCollectionOptions` from `Literal['currently_due', 'eventually_due']` to `NotRequired[Literal['currently_due', 'eventually_due']]`
* Add support for `hr_oib` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
* Add support for `issuing_regulatory_reporting` on enums `stripe.File.purpose`, `stripe.File.CreateParams.purpose`, and `stripe.File.ListParams.purpose`
