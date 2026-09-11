---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1429
is_stripe_api_change: true
released_in_version: 11.4.0b3
---

* Add support for `allow_redisplay` on resources `stripe.Card` and `stripe.Source`
* Add support for `account` on resource classes `stripe.terminal.Reader.Action.CollectPaymentMethod`, `stripe.terminal.Reader.Action.ConfirmPaymentIntent`, `stripe.terminal.Reader.Action.ProcessPaymentIntent`, and `stripe.terminal.Reader.Action.RefundPayment`
* Remove support for `amount_refunded` on resource `stripe.PaymentRecord`
* Add support for `am_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `ao_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `ba_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `bb_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `bs_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `cd_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `gn_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `kh_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `me_pib` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `mk_vat` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `mr_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `np_pan` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `sn_ninea` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `sr_fin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `tj_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `ug_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `zm_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `zw_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `network_fallback` on enum `stripe.issuing.Authorization.RequestHistory.reason`
