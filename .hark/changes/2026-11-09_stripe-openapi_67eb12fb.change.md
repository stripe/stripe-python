---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1969
semver_level: major
is_stripe_api_change: true
released_in_version: 16.2.0a3
---

* Add support for new resource `v2.money_management.SpendingMandate`
* Add support for `cancel`, `list`, and `retrieve` methods on resource `v2.money_management.SpendingMandate`
* Add support for `cardholder_message` on `Charge.PaymentMethodDetail.CardPresent.Receipt`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent.Receipt`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent.Receipt`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent.Receipt`, and `PaymentRecord.PaymentMethodDetail.CardPresent.Receipt`
* Add support for `pricing_token` on `checkout.SessionCreateParams`
* Add support for `marketing_attributions` on `CustomerModifyParams`
* Add support for `fraudulent_selfie` on `Identity.VerificationReport.Signal`
* Add support for `toss_pay` on `Mandate.PaymentMethodDetail`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, and `SetupAttempt.PaymentMethodDetail`
* Add support for `payment_evaluations` on `PaymentAttemptRecordReportAuthenticatedParams`
* Add support for `three_d_secure` on `PaymentAttemptRecordReportAuthorizedParamsPaymentMethodDetailCard`, `PaymentAttemptRecordReportGuaranteedParamsPaymentMethodDetailCard`, `PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailCard`, `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetailCard`, and `PaymentRecordReportPaymentParamsPaymentMethodDetailCard`
* Add support for `wechat_pay_redirect_to_mini_program` on `PaymentIntent.NextAction`
* Add support for `customer_presence` and `payment_type` on `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail.SepaDebit` and `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetailSepaDebit`
* Add support for `financial_connections` on `SetupIntent.PaymentMethodOption.BacsDebit`, `SetupIntentConfirmParamsPaymentMethodOptionBacsDebit`, `SetupIntentCreateParamsPaymentMethodOptionBacsDebit`, and `SetupIntentModifyParamsPaymentMethodOptionBacsDebit`
* Add support for `referral_fee_details` on `SharedPayment.GrantedToken`, `SharedPayment.IssuedToken`, and `shared_payment.IssuedTokenCreateParams`
* Add support for new values `stripe_s700_devkit`, `stripe_s710_devkit`, `stripe_t600_devkit`, `verifone_ux700_devkit`, and `verifone_v660p_devkit` on enum `terminal.ReaderListParams.device_type`
* Add support for `device_health_details` and `device_health` on `Terminal.Reader`
* Add support for new values `check_attachment_too_large`, `check_expired`, and `check_undeliverable` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* Add support for `check_send` on `V2.MoneyManagement.OutboundPayment.To.PayoutMethodOption`, `V2.MoneyManagement.OutboundPayment.TrackingDetail`, `V2.MoneyManagement.PayoutIntent.To.PayoutMethodOption`, `V2.MoneyManagement.PayoutMethod`, `v2.money_management.OutboundPaymentCreateParamsToPayoutMethodOption`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum`, `v2.money_management.PayoutIntentCreateParamsToPayoutMethodOption`, and `v2.money_management.PayoutIntentModifyParamsToPayoutMethodOption`
* Add support for new values `check_attachment_too_large`, `check_expired`, and `check_undeliverable` on enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
* Add support for new value `check_send` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatum.type`
* Add support for `spending_mandate` on `V2.MoneyManagement.ReceivedDebit.BankTransfer` and `v2.money_management.ReceivedDebitListParams`
* Add support for event notifications `V2MoneyManagementSpendingMandateCanceledEvent`, `V2MoneyManagementSpendingMandateCreatedEvent`, `V2MoneyManagementSpendingMandateExpiredEvent`, `V2MoneyManagementSpendingMandatePendingCancellationEvent`, and `V2MoneyManagementSpendingMandateUpdatedEvent` with related object `v2.money_management.SpendingMandate`
* ⚠️ Add error type `MerchantNotGatedError` on `v2.core.vault.NetworkToken#create_from_credential`
