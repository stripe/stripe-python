---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1937
semver_level: major
is_stripe_api_change: true
---

* Add support for new resources `radar.Rule` and `v2.money_management.FundingSession`
* Add support for `create` method on resource `v2.money_management.FundingSession`
* ⚠️ Change type of `Charge.Outcome.rule` from `RadarRule` to `$Radar.Rule`
* Add support for new value `ousd` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
* Add support for `payment_settings` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for `on_behalf_of` on `Checkout.Session`
* Add support for new values `fednow` and `rtp` on enum `CustomerCashBalanceTransaction.Funded.BankTransfer.UsBankTransfer.network`
* Add support for `fuels` on `Issuing.Transaction.PurchaseDetail`
* Add support for `fleet` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
* Add support for `subscription_reference` on `PaymentIntent.PaymentMethodOption.Paypay`, `PaymentIntentConfirmParamsPaymentMethodOptionPaypay`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay`
* Add support for `us_bank_account` on `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail` and `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail`
* Change type of `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail.money_movement_type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for `rules` on `Radar.PaymentEvaluation`
* ⚠️ Change type of `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail.money_movement_type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for new values `request_three_d_secure` and `reroute` on enum `Radar.PaymentEvaluation.recommended_action`
* Add support for `bank_initiated_return` on `Radar.PaymentEvaluation.Signal`
* Add support for `account` on `V2.MoneyManagement.FinancialAddress`, `v2.money_management.FinancialAddressCreateParams`, and `v2.money_management.FinancialAddressListParams`
* Add support for new values `bre_b` and `pix` on enum `V2.MoneyManagement.FinancialAddress.BankAccount.type`
* Add support for `supported_network_details` on `V2.MoneyManagement.FinancialAddress.CryptoWallet`
* Add support for new value `bitcoin` on enums `V2.MoneyManagement.FinancialAddress.CryptoWallet.network`, `V2.MoneyManagement.ReceivedCredit.CryptoWalletTransfer.CryptoWallet.network`, and `v2.money_management.FinancialAddressCreateParamsCryptoWallet.network`
* Add support for `network_details` on `V2.MoneyManagement.InboundTransfer` and `v2.money_management.InboundTransferCreateParams`
* Add support for `originating_crypto_wallet`, `token_currency`, and `transaction_hash` on `V2.MoneyManagement.ReceivedCredit.CryptoWalletTransfer`
* Add support for new values `brl` and `cop` on enum `v2.money_management.FinancialAddressCreateParamsBankAccount.currency`
* Add support for `customer` and `subscription` on `EventsV1InvoiceUpcomingEvent`
