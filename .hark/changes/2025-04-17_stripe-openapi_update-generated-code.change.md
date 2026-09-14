---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1495
is_stripe_api_change: true
released_in_version: 12.1.0b3
---

* Add support for new resources `FxQuote` and `PaymentIntentAmountDetailsLineItem`
* Add support for `create`, `list`, and `retrieve` methods on resource `FxQuote`
* Remove support for `attach_payment_intent` method on resource `Invoice`
* Add support for `registration_date` on `Account.Company`, `Account.CreateParamsCompany`, `Account.UpdateParamsCompany`, and `Token.CreateParamsAccountCompany`
* Add support for `customer_reference` and `order_reference` on `Charge.CaptureParamsPaymentDetail`, `Charge.UpdateParamsPaymentDetail`, `PaymentIntent.CaptureParamsPaymentDetail`, `PaymentIntent.ConfirmParamsPaymentDetail`, `PaymentIntent.CreateParamsPaymentDetail`, `PaymentIntent.PaymentDetail`, and `PaymentIntent.UpdateParamsPaymentDetail`
* Add support for `tax_id` on `Charge.BillingDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatumBillingDetail`, `ConfirmationToken.PaymentMethodPreview.BillingDetail`, `PaymentIntent.ConfirmParamsPaymentMethodDatumBillingDetail`, `PaymentIntent.CreateParamsPaymentMethodDatumBillingDetail`, `PaymentIntent.UpdateParamsPaymentMethodDatumBillingDetail`, `PaymentMethod.BillingDetail`, `PaymentMethod.CreateParamsBillingDetail`, `PaymentMethod.UpdateParamsBillingDetail`, `SetupIntent.ConfirmParamsPaymentMethodDatumBillingDetail`, `SetupIntent.CreateParamsPaymentMethodDatumBillingDetail`, `SetupIntent.UpdateParamsPaymentMethodDatumBillingDetail`, and `treasury.OutboundPayment.CreateParamsDestinationPaymentMethodDatumBillingDetail`
* Add support for `price_data` on `checkout.Session.UpdateParamsLineItem`
* Change type of `checkout.Session.UpdateParamsLineItem.quantity` from `longInteger` to `emptyable(longInteger)`
* Add support for `script` on `Coupon.CreateParams` and `Coupon`
* Add support for `type` on `Coupon`
* Add support for new value `fx_quote.expired` on enum `Event.type`
* Add support for new value `affirm` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `Invoice.UpdateParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, and `Subscription.UpdateParamsPaymentSetting.payment_method_types`
* Add support for `fx_quote` on `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.UpdateParams`, `PaymentIntent`, `Transfer.CreateParams`, and `Transfer`
* Add support for `discount_amount`, `line_items`, `shipping`, and `tax` on `PaymentIntent.AmountDetail`
* Add support for `pix` on `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, and `PaymentMethodConfiguration`
* Add support for `us_cfpb_data` on `Person` and `Token.CreateParamsPerson`
* Add support for `pending_reason` on `Refund`
* Add support for `aw`, `az`, `bd`, `bj`, `et`, `kg`, `la`, and `ph` on `TaxRegistration.CountryOption` and `tax.Registration.CreateParamsCountryOption`
* Add support for new value `fx_quote.expired` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.UpdateParams.enabled_events`
* Add support for snapshot event `fx_quote.expired` with resource `FxQuote`
