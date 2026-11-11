---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1969
semver_level: major
is_stripe_api_change: true
---

* Add support for new resources `tax.Certificate`, `tax.FormCorrection`, `v2.core.AccountSession`, `v2.extend.ObjectDefinitionVersion`, `v2.extend.ObjectDefinition`, and `v2.money_management.SpendingMandate`
* ⚠️ Remove support for resource `v2.core.AccountSessionResource`
* Add support for `create`, `delete`, `list`, and `retrieve` methods on resource `tax.Certificate`
* Add support for `create` method on resource `tax.Form`
* Add support for `cancel`, `list`, and `retrieve` methods on resource `v2.money_management.SpendingMandate`
* Add support for `list` and `retrieve` methods on resources `v2.extend.ObjectDefinitionVersion` and `v2.extend.ObjectDefinition`
* Add support for `bills`, `financial_account_rewards`, `financial_accounts_transactions`, `financial_accounts`, `network_cost_passthrough_report`, and `recipients_list` on `AccountSessionCreateParamsComponent`
* Add support for `business_profile_management` on `AccountSessionCreateParamsComponent` and `v2.core.AccountSessionResourceCreateParamsComponent`
* Add support for `export_tax_transactions`, `product_tax_code_selector`, and `tax_threshold_monitoring` on `AccountSession.Component`
* Add support for `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for `funding_sources` on `Charge.PaymentMethodDetail.Card.Wallet.Link` and `Charge.PaymentMethodDetail.Link`
* Add support for `fleet` on `Charge.PaymentMethodDetail.CardPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
* Add support for `cardholder_message` on `Charge.PaymentMethodDetail.CardPresent.Receipt`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent.Receipt`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent.Receipt`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent.Receipt`, and `PaymentRecord.PaymentMethodDetail.CardPresent.Receipt`
* Add support for `fingerprint` on `Charge.PaymentMethodDetail.Paypay`, `PaymentAttemptRecord.PaymentMethodDetail.Paypay`, `PaymentRecord.PaymentMethodDetail.Paypay`, and `SetupAttempt.PaymentMethodDetail.Paypay`
* Add support for `custom_payment_method_options` and `pricing_token` on `checkout.SessionCreateParams`
* Add support for new value `tamara` on enum `checkout.SessionCreateParams.allowed_payment_method_types`
* Add support for new value `tamara` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `stripe_balance` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `buyer_choice` on enums `Checkout.Session.PaymentMethodOption.AcssDebit.MandateOption.transaction_type` and `checkout.SessionCreateParamsPaymentMethodOptionAcssDebitMandateOption.transaction_type`
* Add support for new value `instant` on enums `Checkout.Session.PaymentMethodOption.BacsDebit.verification_method`, `Invoice.PaymentSetting.PaymentMethodOption.BacsDebit.verification_method`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionBacsDebit.verification_method`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionBacsDebit.verification_method`, `PaymentIntent.PaymentMethodOption.BacsDebit.verification_method`, `PaymentIntentConfirmParamsPaymentMethodOptionBacsDebit.verification_method`, `PaymentIntentCreateParamsPaymentMethodOptionBacsDebit.verification_method`, `PaymentIntentModifyParamsPaymentMethodOptionBacsDebit.verification_method`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.BacsDebit.verification_method`, `SetupIntent.PaymentMethodOption.BacsDebit.verification_method`, `SetupIntentConfirmParamsPaymentMethodOptionBacsDebit.verification_method`, `SetupIntentCreateParamsPaymentMethodOptionBacsDebit.verification_method`, `SetupIntentModifyParamsPaymentMethodOptionBacsDebit.verification_method`, `Subscription.PaymentSetting.PaymentMethodOption.BacsDebit.verification_method`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionBacsDebit.verification_method`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionBacsDebit.verification_method`, and `checkout.SessionCreateParamsPaymentMethodOptionBacsDebit.verification_method`
* Add support for `setup_future_usage` on `Checkout.Session.PaymentMethodOption.Paypay` and `checkout.SessionCreateParamsPaymentMethodOptionPaypay`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for `marketing_attributions` on `CustomerModifyParams`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `reason_details` and `reason` on `CustomerCreateCustomerTaxExemptionParams` and `CustomerTaxExemption`
* Add support for `tax_code_group` on `CustomerCreateCustomerTaxExemptionParamsMe` and `CustomerTaxExemption.Me`
* Change `Dispute.Evidence.appeal` to be required
* Add support for `fraudulent_selfie` on `Identity.VerificationReport.Signal`
* Add support for `target_date` on `Invoice.PaymentSetting.PaymentMethodOption.SepaDebit`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionSepaDebit`, and `InvoiceModifyParamsPaymentSettingPaymentMethodOptionSepaDebit`
* Change `Issuing.Card.Shipping.delivered_at` to be required
* Change `Issuing.Card.Shipping.shipped_at` to be required
* Add support for `toss_pay` on `Mandate.PaymentMethodDetail`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, and `SetupAttempt.PaymentMethodDetail`
* Add support for `payment_evaluations` and `payment_method_details` on `PaymentAttemptRecordReportAuthenticatedParams`
* Add support for `three_d_secure` on `PaymentAttemptRecordReportAuthorizedParamsPaymentMethodDetailCard`, `PaymentAttemptRecordReportGuaranteedParamsPaymentMethodDetailCard`, `PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetailCard`, `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetailCard`, and `PaymentRecordReportPaymentParamsPaymentMethodDetailCard`
* Change type of `PaymentAttemptRecordReportGuaranteedParamsPaymentMethodDetail.type` and `PaymentRecordReportPaymentAttemptGuaranteedParamsPaymentMethodDetail.type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for `dispute_details` on `PaymentAttemptRecord` and `PaymentRecord`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enums `PaymentIntent.allowed_payment_method_types`, `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, `PaymentIntentModifyParams.allowed_payment_method_types`, `SetupIntent.allowed_payment_method_types`, `SetupIntentConfirmParams.allowed_payment_method_types`, `SetupIntentCreateParams.allowed_payment_method_types`, and `SetupIntentModifyParams.allowed_payment_method_types`
* Add support for `ev_charging` and `fleet_data` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.CardPresent`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionCardPresent`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCardPresent`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionCardPresent`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for `financial_connections` on `PaymentIntent.PaymentMethodOption.BacsDebit`, `PaymentIntentConfirmParamsPaymentMethodOptionBacsDebit`, `PaymentIntentCreateParamsPaymentMethodOptionBacsDebit`, `PaymentIntentModifyParamsPaymentMethodOptionBacsDebit`, `SetupIntent.PaymentMethodOption.BacsDebit`, `SetupIntentConfirmParamsPaymentMethodOptionBacsDebit`, `SetupIntentCreateParamsPaymentMethodOptionBacsDebit`, and `SetupIntentModifyParamsPaymentMethodOptionBacsDebit`
* ⚠️ Remove support for value `on_session` from enums `PaymentIntent.PaymentMethodOption.Paypay.setup_future_usage`, `PaymentIntentConfirmParamsPaymentMethodOptionPaypay.setup_future_usage`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay.setup_future_usage`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay.setup_future_usage`
* Add support for `wechat_pay_redirect_to_mini_program` on `PaymentIntent.NextAction`
* Add support for `payment_details` on `PaymentIntent.PaymentMethodOption.CardPresent` and `PaymentIntent.PaymentMethodOption.Card`
* Add support for new value `tamara` on enums `PaymentLink.payment_method_types`, `PaymentLinkCreateParams.payment_method_types`, and `PaymentLinkModifyParams.payment_method_types`
* Add support for `rakuten_pay` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, and `PaymentMethodConfiguration`
* Add support for `sepa_debit` on `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail` and `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail`
* Add support for new value `sepa_debit` on enums `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail.money_movement_type` and `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail.money_movement_type`
* Add support for new value `continue_with_manual_review` on enum `Radar.PaymentEvaluation.recommended_action`
* Add support for `card_testing` on `Radar.PaymentEvaluation.Signal`
* Add support for `payment_method` on `RefundCreateParams`
* Add support for new values `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on enum `RefundCreateParamsPaymentMethodDatum.type`
* Add support for `payment_record` on `Refund`
* Add support for `bizum` and `upi` on `Refund.DestinationDetail`
* Add support for `tax_invoice_month` on `Reporting.ReportRun.Parameter`
* Add support for `radar_options` on `SetupIntentConfirmParams`, `SetupIntentCreateParams`, and `SetupIntent`
* Add support for `referral_fee_details` on `SharedPayment.GrantedToken`, `SharedPayment.IssuedToken`, and `shared_payment.IssuedTokenCreateParams`
* Add support for `billing_group` on `SubscriptionCreateParams`, `SubscriptionListParams`, `SubscriptionModifyParams`, and `Subscription`
* Add support for new values `stripe_s700_devkit`, `stripe_s710_devkit`, `stripe_t600_devkit`, `verifone_ux700_devkit`, and `verifone_v660p_devkit` on enum `terminal.ReaderListParams.device_type`
* Add support for `device_health_details` and `device_health` on `Terminal.Reader`
* Add support for `network_details` on `Treasury.InboundTransfer.FailureDetail`, `Treasury.OutboundPayment.ReturnedDetail`, and `Treasury.OutboundTransfer.ReturnedDetail`
* Add support for `reference` on `V2.MoneyManagement.FinancialAddress.BankAccount.Iban`
* Add support for new values `check_attachment_too_large`, `check_expired`, and `check_undeliverable` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* Add support for `check_send` on `V2.MoneyManagement.OutboundPayment.To.PayoutMethodOption`, `V2.MoneyManagement.OutboundPayment.TrackingDetail`, `V2.MoneyManagement.PayoutIntent.To.PayoutMethodOption`, `V2.MoneyManagement.PayoutMethod`, `v2.money_management.OutboundPaymentCreateParamsToPayoutMethodOption`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum`, `v2.money_management.PayoutIntentCreateParamsToPayoutMethodOption`, and `v2.money_management.PayoutIntentModifyParamsToPayoutMethodOption`
* Add support for new values `check_attachment_too_large`, `check_expired`, and `check_undeliverable` on enum `V2.MoneyManagement.PayoutIntent.NextAction.HandleFailure.failure_reason`
* Add support for new value `check_send` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatum.type`
* Add support for `spending_mandate` on `V2.MoneyManagement.ReceivedDebit.BankTransfer` and `v2.money_management.ReceivedDebitListParams`
* Add support for `additional_details` on `V2.Signals.AccountSignal.CustomerRisk`
* Add support for new value `pln` on enum `v2.money_management.FinancialAddressCreateParamsBankAccount.currency`
* Add support for event notification `V2ExtendObjectDefinitionCreatedEvent` with related object `v2.extend.ObjectDefinition`
* Add support for event notification `V2ExtendObjectDefinitionVersionCreatedEvent` with related object `v2.extend.ObjectDefinitionVersion`
* Add support for event notifications `V2MoneyManagementSpendingMandateCanceledEvent`, `V2MoneyManagementSpendingMandateCreatedEvent`, `V2MoneyManagementSpendingMandateExpiredEvent`, `V2MoneyManagementSpendingMandatePendingCancellationEvent`, and `V2MoneyManagementSpendingMandateUpdatedEvent` with related object `v2.money_management.SpendingMandate`
* ⚠️ Add error type `MerchantNotGatedError` on `v2.core.vault.NetworkToken#create_from_credential`
