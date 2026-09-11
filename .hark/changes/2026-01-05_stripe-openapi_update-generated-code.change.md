---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1698
is_stripe_api_change: true
released_in_version: 14.2.0a2
---

* Add support for new resource `tax.Location`
* Add support for `create`, `list`, and `retrieve` methods on resource `tax.Location`
* Add support for `pause` method on resource `Subscription`
* Add support for `performance_location` on `InvoiceAddLinesParamsLinePriceDatumProductDatumTaxDetail`, `InvoiceLineItemModifyParamsPriceDatumProductDatumTaxDetail`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatumTaxDetail`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatumTaxDetail`, `ProductCreateParamsTaxDetail`, `ProductModifyParamsTaxDetail`, `Tax.CalculationLineItem`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatumTaxDetail`, `checkout.SessionModifyParamsLineItemPriceDatumProductDatumTaxDetail`, and `tax.CalculationCreateParamsLineItem`
* Add support for new value `performance` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.sourcing`, `Tax.CalculationLineItem.TaxBreakdown.sourcing`, and `Tax.Transaction.ShippingCost.TaxBreakdown.sourcing`
* Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
* Change type of `delegated_checkout.RequestedSessionModifyParams.metadata` from `map(string: string)` to `emptyable(map(string: string))`
* Change type of `delegated_checkout.RequestedSessionModifyParams.payment_method_data` from `payment_method_data` to `emptyable(payment_method_data)`
* Change type of `delegated_checkout.RequestedSessionModifyParams.shared_metadata` from `map(string: string)` to `emptyable(map(string: string))`
* Add support for `subscription` on `Invoice.Parent.ScheduleDetail` and `QuotePreviewInvoice.Parent.ScheduleDetail`
* Change type of `PaymentIntentConfirmParamsPaymentDetailBenefit.fr_meal_voucher`, `PaymentIntentCreateParamsPaymentDetailBenefit.fr_meal_voucher`, `PaymentIntentModifyParamsPaymentDetailBenefit.fr_meal_voucher`, `SetupIntentConfirmParamsSetupDetailBenefit.fr_meal_voucher`, `SetupIntentCreateParamsSetupDetailBenefit.fr_meal_voucher`, and `SetupIntentModifyParamsSetupDetailBenefit.fr_meal_voucher` from `payment_details_benefit_fr_meal_voucher` to `emptyable(payment_details_benefit_fr_meal_voucher)`
* Add support for `tax_details` on `PlanCreateParamsProduct` and `PriceCreateParamsProductDatum`
* Add support for `external_reference` on `Plan` and `Price`
* Add support for new value `phase_start` on enums `Quote.SubscriptionDataOverride.phase_effective_at`, `Quote.SubscriptionDatum.phase_effective_at`, `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
* Remove support for value `line_start` from enums `Quote.SubscriptionDataOverride.phase_effective_at`, `Quote.SubscriptionDatum.phase_effective_at`, `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
* Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
* Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `Tax.Registration.CountryOption.Me`
* Add support for `requirements` on `TaxCode`
