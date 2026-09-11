---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1777
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0b1
---

* Add support for new resources `shared_payment.GrantedToken` and `shared_payment.IssuedToken`
* Add support for `retrieve` method on resource `shared_payment.GrantedToken`
* Add support for `create` and `revoke` test helper methods on resource `shared_payment.GrantedToken`
* Add support for `create`, `retrieve`, and `revoke` methods on resource `shared_payment.IssuedToken`
* Add support for `blik` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
* ⚠️ Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Order.TaxDetail.TaxId.type`, and `QuotePreviewInvoice.CustomerTaxId.type`
* Change `Checkout.Session.managed_payments`, `PaymentIntent.managed_payments`, `PaymentLink.managed_payments`, and `Subscription.managed_payments` to be required
* Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Change `Invoice.PaymentSetting.PaymentMethodOption.pix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.pix`, and `Subscription.PaymentSetting.PaymentMethodOption.pix` to be required
* Change `Invoice.PaymentSetting.PaymentMethodOption.upi`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.upi`, and `Subscription.PaymentSetting.PaymentMethodOption.upi` to be required
* Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
* Add support for `validation_errors` on `Privacy.RedactionJob`
* Add support for `tax_details` on `Product`
* ⚠️ Add support for new value `blik` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* ⚠️ Change type of `QuotePreviewInvoice.TotalTax.TaxRateDetail.tax_rate` from `string` to `expandable($TaxRate)`
* ⚠️ Change type of `Radar.PaymentEvaluation.ClientDeviceMetadataDetail.radar_session` from `string` to `nullable(string)`
* Change `SetupIntent.NextAction.PixDisplayQrCode.data` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.expires_at` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.hosted_instructions_url` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_png` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_svg` to be required
* Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `tax.RegistrationCreateParamsCountryOptionMe`
* Add support for `purpose` on `Treasury.OutboundPayment` and `treasury.OutboundPaymentCreateParams`
* Add support for error codes `action_blocked` and `approval_required` on `QuotePreviewInvoice.LastFinalizationError`
