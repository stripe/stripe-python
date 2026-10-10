---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1943
semver_level: major
is_stripe_api_change: true
---

* ⚠️ Remove support for `capture` method on resource `v2.payments.OffSessionPayment`
* ⚠️ Remove support for `acknowledge_confirmation_of_payee` and `initiate_confirmation_of_payee` methods on resource `v2.core.vault.GbBankAccount`
* Add support for `wechat_pay_mobile_web_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
* ⚠️ Remove support for `wechat_pay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
* Add support for `settlement_reserved` on `Balance`
* Add support for new value `settlement_reserved` on enum `BalanceTransaction.balance_type`
* Add support for `carecredit`, `getflex`, and `sezzle` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for new value `auto` on enums `Checkout.Session.payment_method_collection` and `checkout.SessionCreateParams.payment_method_collection`
* Add support for `mandate_options` on `checkout.SessionCreateParamsPaymentMethodOptionCard`
* Change `Checkout.Session.Item.Subscription.backdate_start_date` to be required
* Add support for new values `carecredit`, `getflex`, and `sezzle` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for new values `carecredit`, `getflex`, and `sezzle` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for new values `carecredit`, `getflex`, and `sezzle` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for new values `three_d_secure.authentication.canceled`, `three_d_secure.authentication.challenge_started`, `three_d_secure.authentication.errored`, `three_d_secure.authentication.failed`, `three_d_secure.authentication.requires_challenge`, `three_d_secure.authentication.requires_submission`, and `three_d_secure.authentication.succeeded` on enum `Event.type`
* Add support for new values `carecredit`, `getflex`, and `sezzle` on enums `PaymentIntent.allowed_payment_method_types`, `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, `PaymentIntentModifyParams.allowed_payment_method_types`, `SetupIntent.allowed_payment_method_types`, `SetupIntentConfirmParams.allowed_payment_method_types`, `SetupIntentCreateParams.allowed_payment_method_types`, and `SetupIntentModifyParams.allowed_payment_method_types`
* Add support for new values `carecredit`, `getflex`, and `sezzle` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for new values `simulated_stripe_t600` and `stripe_t600` on enum `terminal.ReaderListParams.device_type`
* Add support for new values `three_d_secure.authentication.canceled`, `three_d_secure.authentication.challenge_started`, `three_d_secure.authentication.errored`, `three_d_secure.authentication.failed`, `three_d_secure.authentication.requires_challenge`, `three_d_secure.authentication.requires_submission`, and `three_d_secure.authentication.succeeded` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for `contact_email` on `V2.Core.AccountEvaluation.AccountDatum`, `V2.Signals.AccountActivity.AccountDetail.Datum`, `V2.Signals.AccountEvaluation.AccountDetail.Datum`, `v2.core.AccountEvaluationCreateParamsAccountDatum`, `v2.signals.AccountActivityCreateParamsAccountDetailData`, and `v2.signals.AccountEvaluationCreateParamsAccountDetailData`
* Add support for `bre_b`, `nip`, and `pix` on `V2.MoneyManagement.FinancialAddress.BankAccount` and `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount`
* Add support for new values `bre_b`, `nip`, and `pix` on enum `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.type`
* ⚠️ Remove support for `amount_capturable` on `V2.Payments.OffSessionPayment`
* ⚠️ Remove support for `capture` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPaymentCreateParams`
* Add support for new values `bre_b` and `pix` on enum `v2.money_management.FinancialAddressCreditSimulationCreditParams.network`
* Add support for snapshot events `three_d_secure.authentication.canceled`, `three_d_secure.authentication.challenge_started`, `three_d_secure.authentication.errored`, `three_d_secure.authentication.failed`, `three_d_secure.authentication.requires_challenge`, `three_d_secure.authentication.requires_submission`, and `three_d_secure.authentication.succeeded` with resource `three_d_secure.Authentication`
* ⚠️ Remove support for event notification `V2PaymentsOffSessionPaymentRequiresCaptureEvent` with related object `v2.payments.OffSessionPayment`
