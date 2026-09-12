---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1827
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.3.0a3
---

* Add support for new resources `GiftCardOperation`, `GiftCard`, and `TaxFund`
* Add support for `retrieve` method on resource `GiftCardOperation`
* Add support for `activate`, `cashout`, `check_balance`, `create`, `reload`, `retrieve`, and `void_operation` methods on resource `GiftCard`
* Add support for `list` and `retrieve` methods on resource `TaxFund`
* Add support for `update_crypto_refund_address` method on resource `PaymentIntent`
* Add support for `performance_location_details` on `Tax.CalculationLineItem`, `Tax.TransactionLineItem`, and `tax.CalculationCreateParamsLineItem`
* ⚠️ Remove support for `money_services` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, and `PaymentIntentCaptureParamsPaymentDetail`
* Add support for `fr_meal_voucher` on `Charge.PaymentMethodDetail.Card.Benefit`
* Add support for `multicapture` on `Charge.PaymentMethodDetail.CardPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
* Add support for `pix` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail`
* ⚠️ Add support for new value `jaywan` on enum `Checkout.Session.CurrentAttempt.PaymentMethodDetail.Card.brand`
* Add support for `provisional_credit` on `Issuing.Dispute` and `issuing.DisputeModifyParams`
* Add support for `reason` on `PaymentAttemptRecordReportCanceledParams` and `PaymentRecordReportPaymentAttemptCanceledParams`
* Add support for `fiserv_valuelink`, `givex`, and `svs` on `PaymentAttemptRecord.ProcessorDetail` and `PaymentRecord.ProcessorDetail`
* ⚠️ Change type of `PaymentAttemptRecord.ProcessorDetail.type` and `PaymentRecord.ProcessorDetail.type` from `literal('custom')` to `enum('custom'|'fiserv_valuelink'|'givex'|'svs')`
* Add support for `capture_by` and `capture_delay` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
* ⚠️ Remove support for `liquid_asset` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
* Add support for `request_multicapture` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
* Add support for new value `transaction_verification` on enums `PaymentIntentConfirmParamsPaymentMethodOptionCrypto.mode`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto.mode`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto.mode`
* Add support for `ignore_application_fee`, `ignore_transfer_data`, and `request_partial_authorization` on `PaymentIntentConfirmParamsPaymentMethodOptionGiftCard`, `PaymentIntentCreateParamsPaymentMethodOptionGiftCard`, and `PaymentIntentModifyParamsPaymentMethodOptionGiftCard`
* Change `PaymentIntentConfirmParamsPaymentDetailBenefitFrMealVoucher.siret`, `PaymentIntentCreateParamsPaymentDetailBenefitFrMealVoucher.siret`, `PaymentIntentModifyParamsPaymentDetailBenefitFrMealVoucher.siret`, `SetupIntentConfirmParamsSetupDetailBenefitFrMealVoucher.siret`, `SetupIntentCreateParamsSetupDetailBenefitFrMealVoucher.siret`, and `SetupIntentModifyParamsSetupDetailBenefitFrMealVoucher.siret` to be optional
* Add support for `latest_payment_attempt_record` and `payment_record` on `PaymentIntent`
* ⚠️ Remove support for `reauthorization` and `reauthorize_before` on `PaymentIntent.AdvancedFeatureDetail`
* Add support for `refund_address` on `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Base`, `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Solana`, and `PaymentIntent.NextAction.CryptoDisplayDetail.DepositAddress.Tempo`
* Add support for `location` on `PaymentIntent.PaymentDetail` and `SetupIntent.SetupDetail`
* ⚠️ Add support for new value `transaction_verification` on enum `PaymentIntent.PaymentMethodOption.Crypto.mode`
* Add support for `data` on `radar.AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetail`, `radar.AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetail`, and `radar.CustomerEvaluationCreateParamsEvaluationContextClientDetail`
* Change `radar.AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetail.radar_session`, `radar.AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetail.radar_session`, and `radar.CustomerEvaluationCreateParamsEvaluationContextClientDetail.radar_session` to be optional
* ⚠️ Add support for new value `promotion` on enum `V2.Commerce.ProductCatalogImport.feed_type`
* ⚠️ Change type of `V2.Core.FeeBatch.Adjustment.tax_adjustment` from `amount` to `an object`
* ⚠️ Change type of `V2.Core.FeeBatch.CollectionRecord.Tax.amount`, `V2.Core.FeeBatch.CollectionRecord.amount`, `V2.Core.FeeBatch.Tax.amount`, `V2.Core.FeeBatch.amount`, `V2.Core.FeeEntry.Tax.amount`, and `V2.Core.FeeEntry.amount` from `amount` to `an object`
* ⚠️ Add support for new value `tax_fund` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for `tax_fund` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* ⚠️ Add support for new value `tax_fund` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for new value `promotion` on enum `v2.commerce.ProductCatalogImportCreateParams.feed_type`
* Add support for error code `default_us_bank_account_cannot_be_archived` on `CannotProceedError`
