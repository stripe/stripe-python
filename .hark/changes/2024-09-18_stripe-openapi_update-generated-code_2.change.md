---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1393
is_stripe_api_change: true
released_in_version: 10.12.0
---

* Add support for `payer_details` on resource class `stripe.Charge.PaymentMethodDetails.Klarna`
* Add support for `amazon_pay` on resource class `stripe.Dispute.PaymentMethodDetails`
* Add support for `automatically_finalizes_at` on resource `stripe.Invoice`
* Add support for `state_sales_tax` on resource class `stripe.tax.Registration.CountryOptions.Us` and parameter class `stripe.tax.Registration.CreateParamsCountryOptionsUs`
* Add support for `verification_supportability` on enums `stripe.Account.FutureRequirements.Error.code`, `stripe.Account.Requirements.Error.code`, `stripe.BankAccount.FutureRequirements.Error.code`, `stripe.BankAccount.Requirements.Error.code`, `stripe.Capability.FutureRequirements.Error.code`, `stripe.Capability.Requirements.Error.code`, `stripe.Person.FutureRequirements.Error.code`, and `stripe.Person.Requirements.Error.code`
* Add support for `amazon_pay` on enum `stripe.Dispute.PaymentMethodDetails.type`
* Add support for `terminal_reader_invalid_location_for_activation` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
