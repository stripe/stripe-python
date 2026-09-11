---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1838
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.5.0b1
---

* Add support for `list` and `retrieve` methods on resource `product_catalog.TrialOffer`
* Add support for `tax_items` on `ChargeCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeCaptureParamsPaymentDetailFlightDatumTotalTax`, `ChargeCaptureParamsPaymentDetailLodgingDatumTotalTax`, `ChargeModifyParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeModifyParamsPaymentDetailFlightDatumTotalTax`, `ChargeModifyParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`, `PaymentIntentCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailFlightDatumTotalTax`, and `PaymentIntentModifyParamsPaymentDetailLodgingDatumTotalTax`
* ⚠️ Remove support for `taxes` on `ChargeCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeCaptureParamsPaymentDetailFlightDatumTotalTax`, `ChargeCaptureParamsPaymentDetailLodgingDatumTotalTax`, `ChargeModifyParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeModifyParamsPaymentDetailFlightDatumTotalTax`, `ChargeModifyParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`, `PaymentIntentCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailFlightDatumTotalTax`, and `PaymentIntentModifyParamsPaymentDetailLodgingDatumTotalTax`
* Add support for `tax_id` on `Checkout.Session.CollectedInformation`
* ⚠️ Remove support for `tax_ids` on `Checkout.Session.CollectedInformation`
* Add support for new value `disabled` on enum `financial_connections.SessionCreateParamsManualEntry.mode`
* Add support for `mode` on `FinancialConnections.Session.ManualEntry`
* Add support for `name` on `issuing.CardholderModifyParams`
* Add support for new value `ic_nif` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
* ⚠️ Add support for new value `ic_nif` on enums `Order.TaxDetail.TaxId.type` and `QuotePreviewInvoice.CustomerTaxId.type`
* Add support for new values `alipay` and `mb_way` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Add support for `custom_fields`, `description`, and `footer` on `QuotePreviewSubscriptionSchedule.DefaultSetting.InvoiceSetting` and `QuotePreviewSubscriptionSchedule.Phase.InvoiceSetting`
* Add support for `trial` on `QuotePreviewSubscriptionSchedule.Phase`
* ⚠️ Remove support for `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `customer_balance`, `eps`, `fpx`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` on `SharedPayment.GrantedToken.PaymentMethodDetail`
* ⚠️ Remove support for values `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `custom`, `customer_balance`, `eps`, `fpx`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` from enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
* Add support for `use_stripe_sdk` on `SharedPayment.IssuedToken` and `shared_payment.IssuedTokenCreateParams`
* Add support for `redirect_to_url` on `SharedPayment.IssuedToken.NextAction`
* ⚠️ Change type of `SharedPayment.IssuedToken.NextAction.type` from `literal('use_stripe_sdk')` to `enum('redirect_to_url'|'use_stripe_sdk')`
* Add support for `livemode` on `Tax.Location`
* Add support for `source` on `V2.Iam.ActivityLog.Detail.UserRole`
* Add support for `payout` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
* ⚠️ Remove support for `payout_v1` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
* Add support for new value `payout` on enum `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type`
* ⚠️ Change `V2.MoneyManagement.ReceivedDebit.BankTransfer.us_bank_account` to be optional
* Add support for error codes `us_bank_account_microdeposits_cannot_be_confirmed` and `us_bank_account_microdeposits_cannot_be_sent` on `ControlledByAlternateResourceError`
