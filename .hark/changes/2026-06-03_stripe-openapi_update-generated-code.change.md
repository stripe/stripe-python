---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1818
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.3.0a2
---

* Add support for new resources `delegated_checkout.OrderEvent`, `delegated_checkout.Order`, `v2.billing.ContractLicensePricingQuantityChange`, `v2.billing.Contract`, and `v2.signals.AccountSignal`
* Add support for `retrieve` method on resource `delegated_checkout.Order`
* Add support for `list_orders` method on resource `delegated_checkout.RequestedSession`
* Add support for `list` and `retrieve` methods on resource `v2.signals.AccountSignal`
* Add support for `activate`, `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.Contract`
* Add support for `birth_address` on `AccountCreateParamsIndividual`, `AccountCreatePersonParams`, `AccountModifyParamsIndividual`, `AccountModifyPersonParams`, `Person`, `TokenCreateParamsAccountIndividual`, and `TokenCreateParamsPerson`
* Change type of `ChargeCaptureParamsPaymentDetailMoneyService.transaction_type`, `ChargeModifyParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCaptureParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentConfirmParamsPaymentDetailMoneyService.transaction_type`, `PaymentIntentCreateParamsPaymentDetailMoneyService.transaction_type`, and `PaymentIntentModifyParamsPaymentDetailMoneyService.transaction_type` from `literal('account_funding')` to `enum('account_funding'|'debt_repayment')`
* ⚠️ Add support for new value `proserv` on enums `Checkout.Session.AutomaticSurcharge.provider` and `PaymentLink.AutomaticSurcharge.provider`
* Add support for `provisioning_decision` and `token_type` on `Issuing.Authorization.TokenDetail` and `Issuing.Token`
* Add support for `token_decision_recommendation` on `Issuing.Authorization.TokenDetail.NetworkDatum.Visa` and `Issuing.Token.NetworkDatum.Visa`
* Add support for `language` on `Issuing.Token.NetworkDatum.Device`
* Add support for `digital_asset_category` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentModifyParamsPaymentMethodOptionCardPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentPaymentDetailMoneyServiceAccountFunding`
* Add support for `static_address` on `PaymentIntent.PaymentMethodOption.Crypto.DepositOption`, `PaymentIntentConfirmParamsPaymentMethodOptionCryptoDepositOption`, `PaymentIntentCreateParamsPaymentMethodOptionCryptoDepositOption`, and `PaymentIntentModifyParamsPaymentMethodOptionCryptoDepositOption`
* Add support for `payment_reference` on `PaymentIntentCreateParamsPaymentsOrchestration`
* ⚠️ Remove support for `payment_details` on `PaymentIntentCreateParamsPaymentsOrchestration`
* ⚠️ Change type of `PaymentIntent.PaymentDetail.MoneyService.transaction_type` from `literal('account_funding')` to `enum('account_funding'|'debt_repayment')`
* Add support for `ending_before`, `limit`, and `starting_after` on `PaymentLocationListParams`
* ⚠️ Change `radar.IssuingAuthorizationEvaluationCreateParamsCardDetail.last4` to be required
* Add support for `schema` on `V2.Data.Reporting.QueryRun.Result.File` and `V2.Reporting.ReportRun.Result.File`
* ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* Add support for `include` on `v2.data.reporting.QueryRunRetrieveParams` and `v2.reporting.ReportRunRetrieveParams`
* Add support for `requirements_collector` on `v2.core.AccountCreateParamsDefaultResponsibility` and `v2.core.AccountModifyParamsDefaultResponsibility`
* Add support for event notification `V2SignalsAccountSignalMerchantDelinquencyReadyEvent` with related object `v2.signals.AccountSignal`
