---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1350
is_stripe_api_change: true
released_in_version: 10.0.0
---

This release changes the pinned API version to 2024-06-20. Please read the [API Changelog](https://docs.stripe.com/changelog/2024-06-20) and carefully review the API changes before upgrading.

### ⚠️ Breaking changes

  * Remove the unused resource `PlatformTaxFee`
  * Rename `volume_decimal` to `quantity_decimal` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`

### Additions

* Add support for `fleet` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetails`, `stripe.issuing.Authorization.CreateParams`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetails`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetails`, resource `stripe.issuing.Authorization`, and resource class `stripe.issuing.Transaction.PurchaseDetails`
* Add support for new values `platform_disabled`, `paused.inactivity` and `other` on enums `Capability.Requirements.disabled_reason` and `Capability.FutureRequirements.disabled_reason`
* Add support for `industry_product_code` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`
* Add support for `quantity_decimal` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`
* Add support for `fuel` on parameter class `stripe.issuing.Authorization.CreateParams` and resource `stripe.issuing.Authorization`
* Add support for `_cls_finalize_amount` on resource `stripe.issuing.Authorization`
* Add support for `finalize_amount` on resource `stripe.issuing.Authorization`
* Change type of `disabled_reason` on  `stripe.Capability.FutureRequirements` and `stripe.Capability.Requirements` from `str` to `Literal['other', 'paused.inactivity', 'pending.onboarding', 'pending.review', 'platform_disabled', 'platform_paused', 'rejected.inactivity', 'rejected.other', 'rejected.unsupported_business', 'requirements.fields_needed']`
* Add support for `ch_uid` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
* Add support for `card_canceled`, `card_expired`,  `cardholder_blocked`, `insecure_authorization_method` and `pin_blocked`  on enum `stripe.issuing.Authorization.RequestHistory.reason`
* Add support for `charging_minute`, `imperial_gallon`, `kilogram`,  `kilowatt_hour`, `pound`, on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`
* Add support for `2024-06-20` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
