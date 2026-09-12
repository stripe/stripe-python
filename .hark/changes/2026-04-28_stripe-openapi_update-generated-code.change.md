---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1800
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0a2
---

* Add support for new resource `v2.data.analytics.MetricQueryResult`
* Add support for `create`, `retrieve`, and `revoke` methods on resource `shared_payment.IssuedToken`
* Add support for `create` method on resource `v2.data.analytics.MetricQueryResult`
* Add support for `balance_report` and `payout_reconciliation_report` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
* Add support for `app_distribution` and `sunbit_payments` on `Account.Capability`, `AccountCreateParamsCapability`, and `AccountModifyParamsCapability`
* ⚠️ Add support for new values `fee_credit_funding`, `inbound_transfer_reversal`, and `inbound_transfer` on enum `BalanceTransaction.type`
* Add support for `sunbit` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* ⚠️ Add support for new values `phantom_cash` and `usdt` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
* Add support for `last4` on `Charge.PaymentMethodDetail.GiftCard`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Klarna`, `PaymentAttemptRecord.PaymentMethodDetail.Klarna`, and `PaymentRecord.PaymentMethodDetail.Klarna`
* Add support for new value `sunbit` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `blik` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `sunbit` on enum `checkout.SessionCreateParams.payment_method_types`
* ⚠️ Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* Change `Checkout.Session.managed_payments`, `PaymentIntent.managed_payments`, `PaymentLink.managed_payments`, and `Subscription.managed_payments` to be required
* Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for new value `sunbit` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* ⚠️ Add support for new value `sunbit` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* ⚠️ Change type of `CreditNote.TotalTax.TaxRateDetail.tax_rate`, `CreditNoteLineItem.Tax.TaxRateDetail.tax_rate`, `Invoice.TotalTax.TaxRateDetail.tax_rate`, `InvoiceLineItem.Tax.TaxRateDetail.tax_rate`, and `QuotePreviewInvoice.TotalTax.TaxRateDetail.tax_rate` from `string` to `expandable($TaxRate)`
* Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `OrderCreateParamsTaxDetailTaxId.type`, `OrderModifyParamsTaxDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
* Add support for new value `sunbit` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `buyer_consents` on `delegated_checkout.RequestedSessionConfirmParams`
* Add support for `consents` on `DelegatedCheckout.RequestedSession.BuyerConsent.Marketing`
* Add support for new value `blik` on enums `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* ⚠️ Add support for new value `blik` on enums `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
* Change `Invoice.PaymentSetting.PaymentMethodOption.pix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.pix`, and `Subscription.PaymentSetting.PaymentMethodOption.pix` to be required
* Change `Invoice.PaymentSetting.PaymentMethodOption.upi`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.upi`, and `Subscription.PaymentSetting.PaymentMethodOption.upi` to be required
* Add support for `payment_facilitator_id` and `sub_merchant_id` on `issuing.AuthorizationCreateParamsMerchantDatum`, `issuing.TransactionCreateForceCaptureParamsMerchantDatum`, and `issuing.TransactionCreateUnlinkedRefundParamsMerchantDatum`
* Add support for `card_presence` on `Issuing.Authorization`
* Add support for `allowed_card_presences` and `blocked_card_presences` on `Issuing.Card.SpendingControl`, `Issuing.Cardholder.SpendingControl`, `issuing.CardCreateParamsSpendingControl`, `issuing.CardModifyParamsSpendingControl`, `issuing.CardholderCreateParamsSpendingControl`, and `issuing.CardholderModifyParamsSpendingControl`
* ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.cancellation_reason`
* ⚠️ Add support for new value `fulfillment_error` on enum `Issuing.Card.replacement_reason`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.balance` and `PaymentRecord.PaymentMethodDetail.GiftCard.balance` from `PaymentFlowsPrivatePaymentMethodsGiftCardDeprecatedDetailsResourceBalanceAmount` to `nullable(PaymentsPrimitivesPaymentRecordsResourcePaymentMethodGiftCardDetailsResourceBalance)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.brand` and `PaymentRecord.PaymentMethodDetail.GiftCard.brand` from `enum('fiserv_valuelink'|'givex'|'svs')` to `nullable(enum('fiserv_valuelink'|'givex'|'svs'))`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.first6` and `PaymentRecord.PaymentMethodDetail.GiftCard.first6` from `string` to `nullable(string)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.GiftCard.transaction_id` and `PaymentRecord.PaymentMethodDetail.GiftCard.transaction_id` from `string` to `nullable(string)`
* Add support for new value `sunbit` on enums `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for `amount_to_confirm` on `PaymentIntentConfirmParams`
* ⚠️ Add support for new value `sunbit` on enums `PaymentIntent.excluded_payment_method_types` and `SetupIntent.excluded_payment_method_types`
* Add support for `klarna_display_qr_code` on `PaymentIntent.NextAction`
* Add support for new value `sunbit` on enums `PaymentLinkCreateParams.payment_method_types` and `PaymentLinkModifyParams.payment_method_types`
* ⚠️ Add support for new value `sunbit` on enum `PaymentLink.payment_method_types`
* Add support for `validation_errors` on `Privacy.RedactionJob`
* Add support for `tax_details` on `Product`
* ⚠️ Change type of `Radar.PaymentEvaluation.ClientDeviceMetadataDetail.radar_session` from `string` to `nullable(string)`
* ⚠️ Add support for new values `low`, `not_assessed`, and `unknown` on enum `Radar.PaymentEvaluation.Signal.FraudulentPayment.risk_level`
* Add support for new value `account` on enum `radar.ValueListCreateParams.item_type`
* ⚠️ Add support for new value `account` on enum `Radar.ValueList.item_type`
* Add support for `moto` on `SetupAttempt.PaymentMethodDetail.Card`
* Change `SetupIntent.NextAction.PixDisplayQrCode.data` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.expires_at` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.hosted_instructions_url` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_png` to be required
* Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_svg` to be required
* Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `tax.RegistrationCreateParamsCountryOptionMe`
* Add support for `purpose` on `Treasury.OutboundPayment` and `treasury.OutboundPaymentCreateParams`
* Add support for new value `2026-04-22.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `crypto_wallet` on `V2.MoneyManagement.FinancialAddress.Credential`
* Add support for `mx_bank_account` on `V2.MoneyManagement.FinancialAddress.Credential` and `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Add support for new values `crypto_wallet` and `mx_bank_account` on enum `V2.MoneyManagement.FinancialAddress.Credential.type`
* Add support for `crypto_wallet_transfer` on `V2.MoneyManagement.ReceivedCredit`
* Add support for `eu_bank_account` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Add support for new values `crypto_wallet`, `eu_bank_account`, and `mx_bank_account` on enum `V2.MoneyManagement.ReceivedCredit.BankTransfer.origin_type`
* ⚠️ Add support for new value `crypto_wallet_transfer` on enum `V2.MoneyManagement.ReceivedCredit.type`
* Change `v2.payments.OffSessionPaymentCaptureParams.metadata` and `v2.payments.OffSessionPaymentCreateParams.metadata` to be optional
* Add support for `crypto_properties` and `settlement_currency` on `v2.money_management.FinancialAddressCreateParams`
* Add support for new values `crypto_wallet` and `mx_bank_account` on enum `v2.money_management.FinancialAddressCreateParams.type`
* Add support for event notifications `V2CoreApprovalRequestCreatedEvent` and `V2CoreApprovalRequestExpiredEvent` with related object `v2.core.ApprovalRequest`
* Add support for event notification `V2ExtendExtensionRunFailedEvent`
* Add support for error codes `action_blocked` and `approval_required` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
