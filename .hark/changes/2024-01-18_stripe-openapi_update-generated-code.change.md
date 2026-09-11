---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1193
is_stripe_api_change: true
released_in_version: 7.13.0
---

* Add support for providing details about `BankAccount`, `Card`, and `CardToken` on `Account.CreateExternalAccountParams.external_account` and `Account.CreateParams.external_account`
* Add support for new value `nn` on enums `Charge.PaymentMethodDetails.Ideal.bank`, `PaymentIntent.ConfirmParamsPaymentMethodDataIdeal.bank`, `PaymentIntent.CreateParamsPaymenMethodDataIdeal.bank`, `PaymentIntent.UpdateParamsPaymentMethodDataIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethod.CreateParamsIdeal.bank`, `SetupAttempt.PaymentMethodDetails.Ideal.bank`, `SetupIntent.ConfirmParamsPaymenMethodDataIdeal.bank`, `SetupIntent.CreateParamsPaymenMethodDataIdeal.bank`, and `SetupIntent.UpdateParamsPaymenMethodDataIdeal.bank`
* Add support for new value `NNBANL2G` on enums `Charge.PaymentMethodDetails.Ideal.bic`, `PaymentMethod.Ideal.bic`, and `SetupAttempt.PaymentMethodDetails.Ideal.bic`
* Change `CustomerSession.Components.buy_button` and `CustomerSession.Components.pricing_table` to be required
* Add support for `issuer` on `Invoice.CreateParams`, `Invoice.UpcomingLinesParams`, `Invoice.UpcomingParams`, `Invoice.UpdateParams`, and `Invoice`
* Add support for `liability` on `Invoice.automatic_tax`, `Invoice.CreateParams.automatic_tax`, `Invoice.UpcomingLinesParams.automatic_tax`, `Invoice.UpcomingParams.automatic_tax`, `Invoice.UpdateParams.automatic_tax`, `Subscription.automatic_tax`, `Subscription.CreateParams.automatic_tax`, and `Subscription.UpdateParams.automatic_tax`
* Add support for `on_behalf_of` on `Invoice.UpcomingLinesParams` and `Invoice.UpcomingParams`
* Add support for `pin` on `issuing.Card.CreateParams`
* Add support for `revocation_reason` on `Mandate.PaymentMethodDetails.bacs_debit`
* Add support for `customer_balance` on `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, and `PaymentMethodConfiguration`
* Add support for `invoice_settings` on `Subscription.CreateParams` and `Subscription.UpdateParams`
