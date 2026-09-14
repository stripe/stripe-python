---
title: API Updates
pr_url: https://github.com/stripe/stripe-python/pull/1286
released_in_version: 9.0.0
---

* This release changes the pinned API version to `2024-04-10`. Please read the [API Changelog](https://docs.stripe.com/changelog/2024-04-10) and carefully review the API changes before upgrading.

### ⚠️ Breaking changes

* Remove `FinancialAccountFeaturesService.CreateParams`, `FinancialAccountFeaturesService.ListParams`, `FinancialAccountFeaturesService.create()`, `FinancialAccountFeaturesService.list()` as Financial account features is a singleton and so should have retrieve and update methods instead of create and list methods.
* Rename `features` to `marketing_features` on parameter classes `stripe.Product.CreateParams` and `stripe.Product.ModifyParams` and resource `stripe.Product`.

#### ⚠️ Removal of enum values, properties and events that are no longer part of the publicly documented Stripe API
 * Remove `.subscription_pause` from the below as the feature to pause subscription on the portal has been deprecated
    * `Configuration.Features`
    * `ConfigurationService.CreateParamsFeatures`
    * `ConfigurationService.UpdateParamsFeatures`
 * Remove the below deprecated values for `BalanceTransaction.type`
    * `obligation_inbound`
    * `obligation_payout`
    * `obligation_payout_failure`
    * `obligation_reversal_outbound`
 * Remove the below deprecated events from `Event.type`, `WebhookEndpoint.CreateParams.enabled_events`, `WebhookEndpoint.ModifyParams.enabled_events`, `WebhookEndpointService.CreateParams.enabled_events`, `WebhookEndpointService.ModifyParams.enabled_events`
   * `invoiceitem.updated`
   * `order.created`
   * `recipient.created`
   * `recipient.deleted`
   * `recipient.updated`
   * `sku.created`
   * `sku.deleted`
   * `sku.updated`
 * Remove the deprecated value `include_and_require` for `Invoice.CreateParams.pending_invoice_items_behavior` and `InvoiceService.CreateParams.pending_invoice_items_behavior`
 * Remove the deprecated value `service_tax` for
   * `TaxRate.RetrieveParams.tax_type`
   * `TaxRate.CreateParams.tax_type`
   * `TaxRate.ModifyParams.tax_type`
   * `TaxRateService.CreateParams.tax_type`
   * `TaxRateService.UpdateParams.tax_type`
   * `InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`
   * `InvoiceLineItemService.UpdateParamsTaxAmountTaxRateData.tax_type`
 * Remove `request_incremental_authorization` from
   * `PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent`
   * `PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent`
   * `PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent`
   * `PaymentIntentService.ConfirmParamsPaymentMethodOptionsCardPresent`
   * `PaymentIntentService.CreateParamsPaymentMethodOptionsCardPresent`
   * `PaymentIntentService.ModifyParamsPaymentMethodOptionsCardPresent`
 * Remove support for `id_bank_transfer`, `multibanco`, `netbanking`, `pay_by_bank`, and `upi` on `PaymentMethodConfiguration`
 * Remove the deprecated value `challenge_only` from `SetupIntent.PaymentMethodOptions.Card.request_three_d_secure`
 * Remove deprecated value `various` for `Climate.Supplier.removal_pathway`
 * Remove the deprecated value `obligation` for `ReportRun.CreateParamsParameters.reporting_category` and `ReportRunService.CreateParamsParameters.reporting_category`
 * Remove the legacy field `rendering_options` on parameter classes `stripe.Invoice.CreateParams` and `stripe.Invoice.ModifyParams` and resource `stripe.Invoice`. Use `rendering` instead.
