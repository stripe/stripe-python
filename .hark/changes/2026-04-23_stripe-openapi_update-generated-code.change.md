---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1793
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.1.0
---

* Add support for `balance_report` and `payout_reconciliation_report` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
* Add support for `app_distribution` and `sunbit_payments` on `Account.Capability`, `AccountCreateParamsCapability`, and `AccountModifyParamsCapability`
* ⚠️ Add support for new values `fee_credit_funding`, `inbound_transfer_reversal`, and `inbound_transfer` on enum `BalanceTransaction.type`
* Add support for `sunbit` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* ⚠️ Add support for new values `phantom_cash` and `usdt` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Klarna`, `PaymentAttemptRecord.PaymentMethodDetail.Klarna`, and `PaymentRecord.PaymentMethodDetail.Klarna`
* Add support for `mandate` on `Charge.PaymentMethodDetail.Pix`, `PaymentAttemptRecord.PaymentMethodDetail.Pix`, and `PaymentRecord.PaymentMethodDetail.Pix`
* Add support for `managed_payments` on `Checkout.Session`, `PaymentIntent`, `PaymentLinkCreateParams`, `PaymentLink`, `SetupIntent`, `Subscription`, and `checkout.SessionCreateParams`
* Add support for new value `sunbit` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, `SetupIntentModifyParams.excluded_payment_method_types`, and `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `mandate_options` on `Checkout.Session.PaymentMethodOption.Pix`, `PaymentIntent.PaymentMethodOption.Pix`, `PaymentIntentConfirmParamsPaymentMethodOptionPix`, `PaymentIntentCreateParamsPaymentMethodOptionPix`, `PaymentIntentModifyParamsPaymentMethodOptionPix`, and `checkout.SessionCreateParamsPaymentMethodOptionPix`
* Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntentCreateParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntentModifyParamsPaymentMethodOptionPix.setup_future_usage`, and `checkout.SessionCreateParamsPaymentMethodOptionPix.setup_future_usage` from `literal('none')` to `enum('none'|'off_session')`
* Add support for new value `sunbit` on enum `checkout.SessionCreateParams.payment_method_types`
* ⚠️ Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* ⚠️ Change type of `Checkout.Session.PaymentMethodOption.Pix.setup_future_usage` and `PaymentIntent.PaymentMethodOption.Pix.setup_future_usage` from `literal('none')` to `enum('none'|'off_session')`
* Add support for new value `sunbit` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* ⚠️ Add support for new value `sunbit` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
* Add support for new value `sunbit` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `pix` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `Mandate.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodOption`, `SetupIntentModifyParamsPaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
* Add support for `upi` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
* Add support for new values `pix` and `upi` on enums `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* ⚠️ Add support for new values `pix` and `upi` on enums `Invoice.PaymentSetting.payment_method_types` and `Subscription.PaymentSetting.payment_method_types`
* Add support for `card_presence` on `Issuing.Authorization`
* Add support for `allowed_card_presences` and `blocked_card_presences` on `Issuing.Card.SpendingControl`, `Issuing.Cardholder.SpendingControl`, `issuing.CardCreateParamsSpendingControl`, `issuing.CardModifyParamsSpendingControl`, `issuing.CardholderCreateParamsSpendingControl`, and `issuing.CardholderModifyParamsSpendingControl`
* ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.cancellation_reason`
* ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.replacement_reason`
* Add support for `amount` and `currency` on `Mandate.MultiUse`
* Add support for `amount_to_confirm` on `PaymentIntentConfirmParams`
* ⚠️ Add support for new value `sunbit` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
* Add support for `klarna_display_qr_code` on `PaymentIntent.NextAction`
* Add support for new value `sunbit` on enums `PaymentLinkCreateParams.payment_method_types` and `PaymentLinkModifyParams.payment_method_types`
* ⚠️ Add support for new value `sunbit` on enum `PaymentLink.payment_method_types`
* ⚠️ Add support for new values `low`, `not_assessed`, and `unknown` on enum `Radar.PaymentEvaluation.Signal.FraudulentPayment.risk_level`
* Add support for new value `account` on enum `radar.ValueListCreateParams.item_type`
* ⚠️ Add support for new value `account` on enum `Radar.ValueList.item_type`
* Add support for `moto` on `SetupAttempt.PaymentMethodDetail.Card`
* Add support for `pix_display_qr_code` on `SetupIntent.NextAction`
* Add support for new value `2026-04-22.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* Add support for error codes `action_blocked` and `approval_required` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
