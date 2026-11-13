---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1526
is_stripe_api_change: true
released_in_version: 12.3.0
---

* Add support for `migrate` method on resource `Subscription`
* Add support for `collect_payment_method` and `confirm_payment_intent` methods on resource `terminal.Reader`
* Add support for `crypto_payments` on `Account.Capability`, `Account.CreateParamsCapability`, and `Account.ModifyParamsCapability`
* Add support for `proof_of_address` on `Account.CreateParamsDocument` and `Account.ModifyParamsDocument`
* Add support for `monthly_payout_days` and `weekly_payout_days` on `Account.CreateParamsSettingPayoutSchedule`, `Account.ModifyParamsSettingPayoutSchedule`, and `Account.Setting.Payout.Schedule`
* Change `Account.Setting.Invoice.hosted_payment_method_save` to be required
* Add support for `crypto` on `Charge.PaymentMethodDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatum`, `ConfirmationToken.PaymentMethodPreview`, `PaymentIntent.ConfirmParamsPaymentMethodDatum`, `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodDatum`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.ModifyParamsPaymentMethodDatum`, `PaymentIntent.ModifyParamsPaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, `PaymentMethod.CreateParams`, `PaymentMethod`, `SetupIntent.ConfirmParamsPaymentMethodDatum`, `SetupIntent.CreateParamsPaymentMethodDatum`, and `SetupIntent.ModifyParamsPaymentMethodDatum`
* Change type of `Charge.PaymentMethodDetail.Card.Installment.Plan.type`, `ConfirmationToken.CreateParamsPaymentMethodOptionCardInstallmentPlan.type`, `ConfirmationToken.PaymentMethodOption.Card.Installment.Plan.type`, `Invoice.CreateParamsPaymentSettingPaymentMethodOptionCardInstallmentPlan.type`, `Invoice.ModifyParamsPaymentSettingPaymentMethodOptionCardInstallmentPlan.type`, `PaymentIntent.ConfirmParamsPaymentMethodOptionCardInstallmentPlan.type`, `PaymentIntent.CreateParamsPaymentMethodOptionCardInstallmentPlan.type`, `PaymentIntent.ModifyParamsPaymentMethodOptionCardInstallmentPlan.type`, `PaymentIntent.PaymentMethodOption.Card.Installment.AvailablePlan.type`, and `PaymentIntent.PaymentMethodOption.Card.Installment.Plan.type` from `literal('fixed_count')` to `enum('bonus'|'fixed_count'|'revolving')`
* Add support for new value `buut` on enums `Charge.PaymentMethodDetail.Ideal.bank`, `ConfirmationToken.CreateParamsPaymentMethodDatumIdeal.bank`, `ConfirmationToken.PaymentMethodPreview.Ideal.bank`, `PaymentIntent.ConfirmParamsPaymentMethodDatumIdeal.bank`, `PaymentIntent.CreateParamsPaymentMethodDatumIdeal.bank`, `PaymentIntent.ModifyParamsPaymentMethodDatumIdeal.bank`, `PaymentMethod.CreateParamsIdeal.bank`, `PaymentMethod.Ideal.bank`, `SetupAttempt.PaymentMethodDetail.Ideal.bank`, `SetupIntent.ConfirmParamsPaymentMethodDatumIdeal.bank`, `SetupIntent.CreateParamsPaymentMethodDatumIdeal.bank`, and `SetupIntent.ModifyParamsPaymentMethodDatumIdeal.bank`
* Add support for new value `BUUTNL2A` on enums `Charge.PaymentMethodDetail.Ideal.bic`, `ConfirmationToken.PaymentMethodPreview.Ideal.bic`, `PaymentMethod.Ideal.bic`, and `SetupAttempt.PaymentMethodDetail.Ideal.bic`
* Add support for `subscriptions` on `PaymentIntent.ConfirmParamsPaymentMethodOptionKlarna`, `PaymentIntent.CreateParamsPaymentMethodOptionKlarna`, `PaymentIntent.ModifyParamsPaymentMethodOptionKlarna`, and `checkout.Session.CreateParamsPaymentMethodOptionKlarna`
* Add support for new value `crypto` on enum `checkout.Session.CreateParams.payment_method_types`
* Add support for `billing_mode` on `Invoice.CreatePreviewParamsScheduleDetail`, `Invoice.CreatePreviewParamsSubscriptionDetail`, `Quote.CreateParamsSubscriptionDatum`, `Quote.SubscriptionDatum`, `Subscription.CreateParams`, `SubscriptionSchedule.CreateParams`, `SubscriptionSchedule`, `Subscription`, and `checkout.Session.CreateParamsSubscriptionDatum`
* Add support for new value `crypto` on enums `ConfirmationToken.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.ConfirmParamsPaymentMethodDatum.type`, `PaymentIntent.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.ModifyParamsPaymentMethodDatum.type`, `SetupIntent.ConfirmParamsPaymentMethodDatum.type`, `SetupIntent.CreateParamsPaymentMethodDatum.type`, and `SetupIntent.ModifyParamsPaymentMethodDatum.type`
* Add support for new value `crypto` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for new value `crypto` on enums `Customer.ListPaymentMethodsParams.type`, `PaymentMethod.CreateParams.type`, and `PaymentMethod.ListParams.type`
* Change type of `Dispute.enhanced_eligibility_types` from `literal('visa_compelling_evidence_3')` to `enum('visa_compelling_evidence_3'|'visa_compliance')`
* Add support for new value `compliance` on enum `Dispute.PaymentMethodDetail.Card.case_type`
* Add support for new value `terminal.reader.action_updated` on enum `Event.type`
* Add support for `related_person` on `Identity.VerificationSession` and `identity.VerificationSession.CreateParams`
* Add support for `matching` on `Identity.VerificationSession.Option`
* Add support for new value `crypto` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.ModifyParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.ModifyParamsPaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
* Add support for `klarna` on `Mandate.PaymentMethodDetail`, `SetupIntent.ConfirmParamsPaymentMethodOption`, `SetupIntent.CreateParamsPaymentMethodOption`, `SetupIntent.ModifyParamsPaymentMethodOption`, and `SetupIntent.PaymentMethodOption`
* Add support for `on_demand` on `PaymentIntent.ConfirmParamsPaymentMethodOptionKlarna`, `PaymentIntent.CreateParamsPaymentMethodOptionKlarna`, and `PaymentIntent.ModifyParamsPaymentMethodOptionKlarna`
* Change type of `PaymentIntent.ConfirmParamsPaymentMethodOptionKlarna.setup_future_usage`, `PaymentIntent.CreateParamsPaymentMethodOptionKlarna.setup_future_usage`, `PaymentIntent.ModifyParamsPaymentMethodOptionKlarna.setup_future_usage`, and `PaymentIntent.PaymentMethodOption.Klarna.setup_future_usage` from `literal('none')` to `enum('none'|'off_session'|'on_session')`
* Add support for `ua` on `Tax.Registration.CountryOption` and `tax.Registration.CreateParamsCountryOption`
* Change type of `terminal.Location.ModifyParams.display_name` from `string` to `emptyable(string)`
* Add support for `collect_payment_method` and `confirm_payment_intent` on `Terminal.Reader.Action`
* Add support for new values `collect_payment_method` and `confirm_payment_intent` on enum `Terminal.Reader.Action.type`
* Add support for `status` on `treasury.FinancialAccount.ListParams`
* Add support for new value `terminal.reader.action_updated` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.ModifyParams.enabled_events`
* Add support for new value `2025-06-30.basil` on enum `WebhookEndpoint.CreateParams.api_version`
* Add support for snapshot event `terminal.reader.action_updated` with resource `terminal.Reader`
