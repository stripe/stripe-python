---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1804
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0a4
---

* Add support for new resource `PaymentLocation`
* Add support for `create`, `delete`, `modify`, and `retrieve` methods on resource `PaymentLocation`
* Add support for `protections` on `AccountCreateParamsCapabilityCardPayment`, `AccountModifyParamsCapabilityCardPayment`, and `Capability`
* Add support for `gift_card` on `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodCreateParams`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, `SetupIntentModifyParamsPaymentMethodDatum`, and `SharedPayment.GrantedToken.PaymentMethodDetail`
* Add support for new value `gift_card` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* ⚠️ Add support for new value `gift_card` on enums `ConfirmationToken.PaymentMethodPreview.type`, `PaymentMethod.type`, and `SharedPayment.GrantedToken.PaymentMethodDetail.type`
* Add support for new value `gift_card` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `metadata` on `delegated_checkout.RequestedSessionConfirmParams`
* Add support for `credited_items` on `InvoiceItem.ProrationDetail`
* Add support for `network_lifecycle` on `Issuing.Dispute`
* Add support for new value `gift_card` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* ⚠️ Add support for new value `gift_card` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
* Add support for `status_details` on `Subscription`
