---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1839
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.4.0a2
---

* Add support for new resources `crypto.CustomerConsumerWallet`, `crypto.CustomerPaymentToken`, `crypto.Customer`, `crypto.OnrampSession`, and `crypto.OnrampTransactionLimits`
* Add support for `list` and `retrieve` methods on resource `crypto.Customer`
* Add support for `checkout`, `create`, `list`, `quote`, and `retrieve` methods on resource `crypto.OnrampSession`
* Add support for `retrieve` method on resource `crypto.OnrampTransactionLimits`
* Add support for `electronic_commerce_indicator` on `Charge.PaymentMethodDetail.Card`
* Add support for `amount_received` and `amount_requested` on `Charge.PaymentMethodDetail.Crypto`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto`, and `PaymentRecord.PaymentMethodDetail.Crypto`
* Add support for `fingerprint` on `Charge.PaymentMethodDetail.GiftCard`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
* Add support for `address_collection_precision` on `checkout.SessionCreateParamsAutomaticTax`
* Add support for `subscription` on `Checkout.Session.Item`
* ⚠️  Remove support for `deactivation` on `GiftCardOperation`
* ⚠️  Remove support for value `deactivation` from enum `GiftCardOperation.type`
* Add support for `merchant_amount_exchange_rate` on `Issuing.Authorization` and `Issuing.Transaction`
* Add support for `device_id` on `Issuing.Authorization.TokenDetail.NetworkDatum.Device` and `Issuing.Token.NetworkDatum.Device`
* Add support for `program` on `Issuing.Card`
* Add support for `payment_method_details` on `PaymentAttemptRecordReportFailedParams` and `PaymentRecordReportPaymentAttemptFailedParams`
* Add support for `reason` on `PaymentAttemptRecordReportRefundParams` and `PaymentRecordReportRefundParams`
* Add support for `amount_reconciliation` on `PaymentIntent.PaymentMethodOption.Crypto`, `PaymentIntentConfirmParamsPaymentMethodOptionCrypto`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto`
* Add support for `connect_permissions` and `permissions` on `V2.Iam.ApiKey`, `v2.iam.ApiKeyCreateParams`, and `v2.iam.ApiKeyModifyParams`
* Add support for `credit` on `V2.MoneyManagement.FinancialAccount`
* ⚠️  Add support for new value `credit` on enum `V2.MoneyManagement.FinancialAccount.type`
* Add support for new value `currency_required` on enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
* Add support for new values `issuing_authorization`, `issuing_transaction`, and `platform_funded_credit_transaction` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for `account`, `issuing_authorization`, `issuing_dispute`, and `issuing_transaction` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* Add support for new values `issuing_authorization`, `issuing_dispute`, and `issuing_transaction` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for new value `credit` on enum `v2.money_management.FinancialAccountListParams.types`
* Change type of `v2.money_management.FinancialAccountCreateParams.type` from `literal('storage')` to `enum('credit'|'storage')`
* Add support for `expires_at` on `v2.iam.ApiKeyCreateParams`
