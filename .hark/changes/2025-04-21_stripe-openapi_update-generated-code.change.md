---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1498
is_stripe_api_change: true
released_in_version: 12.2.0b1
---

* Add support for new values `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, and `la_tin` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* Change `Checkout.Session.AutomaticTax.provider`, `Invoice.AutomaticTax.provider`, `Quote.AutomaticTax.provider`, and `QuotePreviewInvoice.AutomaticTax.provider` to be required
* Add support for `account_number` on `ConfirmationToken.PaymentMethodPreview.AcssDebit` and `PaymentMethod.AcssDebit`
* Add support for new values `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, and `la_tin` on enums `Customer.CreateParams.type`, `Customer.CreateParamsTaxIdDatum.type`, `CustomerService.CreateParamsTaxIdDatum.type`, `CustomerTaxIdService.CreateParams.type`, `Invoice.CreatePreviewParamsCustomerDetailTaxId.type`, `InvoiceService.CreatePreviewParamsCustomerDetailTaxId.type`, `Order.CreateParamsTaxDetailTaxId.type`, `Order.ModifyParamsTaxDetailTaxId.type`, `OrderService.CreateParamsTaxDetailTaxId.type`, `OrderService.UpdateParamsTaxDetailTaxId.type`, `TaxId.CreateParams.type`, `TaxIdService.CreateParams.type`, `tax.Calculation.CreateParamsCustomerDetailTaxId.type`, and `tax.CalculationService.CreateParamsCustomerDetailTaxId.type`
* Change type of `InvoiceLineItem.Parent.SubscriptionItemDetail.subscription` from `string` to `nullable(string)`
* Add support for `billing_mode` on `Quote.CreateParamsSubscriptionDatum`, `QuoteService.CreateParamsSubscriptionDatum`, `Subscription.CreateParams`, `SubscriptionSchedule.CreateParams`, `SubscriptionScheduleService.CreateParams`, and `SubscriptionService.CreateParams`
* Add support for `bf`, `cm`, and `cv` on `Tax.Registration.CountryOption`, `tax.Registration.CreateParamsCountryOption`, and `tax.RegistrationService.CreateParamsCountryOption`
* Add support for new value `2025-04-30.basil` on enums `WebhookEndpoint.CreateParams.api_version` and `WebhookEndpointService.CreateParams.api_version`
