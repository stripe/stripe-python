---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1725
is_stripe_api_change: true
released_in_version: 14.3.0
---

* Add support for new resource `radar.PaymentEvaluation`
* Add support for `create` method on resource `radar.PaymentEvaluation`
* Add support for `adjustable_quantity` on `LineItem`
* Add support for new value `risk_reserved` on enum `BalanceTransaction.balance_type`
* Add support for new values `reserve_hold` and `reserve_release` on enum `BalanceTransaction.type`
* Add support for new values `2.3.0` and `2.3.1` on enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.version`, `PaymentIntentConfirmParamsPaymentMethodOptionCardThreeDSecure.version`, `PaymentIntentCreateParamsPaymentMethodOptionCardThreeDSecure.version`, `PaymentIntentModifyParamsPaymentMethodOptionCardThreeDSecure.version`, `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.version`, `SetupIntentConfirmParamsPaymentMethodOptionCardThreeDSecure.version`, `SetupIntentCreateParamsPaymentMethodOptionCardThreeDSecure.version`, and `SetupIntentModifyParamsPaymentMethodOptionCardThreeDSecure.version`
* Add support for new value `adyen` on enums `Charge.PaymentMethodDetail.Ideal.bank`, `ConfirmationToken.PaymentMethodPreview.Ideal.bank`, `ConfirmationTokenCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentModifyParamsPaymentMethodDatumIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethodCreateParamsIdeal.bank`, `PaymentRecord.PaymentMethodDetail.Ideal.bank`, `SetupAttempt.PaymentMethodDetail.Ideal.bank`, `SetupIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `SetupIntentCreateParamsPaymentMethodDatumIdeal.bank`, and `SetupIntentModifyParamsPaymentMethodDatumIdeal.bank`
* Add support for new value `ADYBNL2A` on enums `Charge.PaymentMethodDetail.Ideal.bic`, `ConfirmationToken.PaymentMethodPreview.Ideal.bic`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bic`, `PaymentMethod.Ideal.bic`, `PaymentRecord.PaymentMethodDetail.Ideal.bic`, and `SetupAttempt.PaymentMethodDetail.Ideal.bic`
* Add support for new value `pl_nip` on enums `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* Add support for new value `pl_nip` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
* Change `Invoice.PaymentSetting.PaymentMethodOption.payto` and `Subscription.PaymentSetting.PaymentMethodOption.payto` to be required
* Add support for `enforce_arithmetic_validation` on `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
* Add support for `error` on `PaymentIntent.AmountDetail`
* Remove support for `bgn` on `Terminal.Configuration.Tipping`, `terminal.ConfigurationCreateParamsTipping`, and `terminal.ConfigurationModifyParamsTipping`
* Add support for `topup` on `Treasury.ReceivedDebit.LinkedFlow`
* Add support for `contact_phone` on `V2.Core.Account`, `v2.core.AccountCreateParams`, `v2.core.AccountModifyParams`, and `v2.core.AccountTokenCreateParams`
* Add support for `registration_date` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, `v2.core.AccountModifyParamsIdentityBusinessDetail`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetail`
* Add support for new value `gb_vat` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
* Add support for error code `request_blocked` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
