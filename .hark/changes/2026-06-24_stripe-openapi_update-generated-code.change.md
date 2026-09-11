---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1836
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.3.0
---

* Add support for `release_details` on `Reserve.Hold`
* ⚠️ Add support for new value `tax_fund` on enum `BalanceTransaction.type`
* Change `Billing.CreditGrant.priority` to be required
* Add support for `buyer_id` on `Charge.PaymentMethodDetail.Bizum`, `ConfirmationToken.PaymentMethodPreview.Bizum`, `ConfirmationToken.PaymentMethodPreview.Blik`, `PaymentAttemptRecord.PaymentMethodDetail.Bizum`, `PaymentMethod.Bizum`, `PaymentMethod.Blik`, and `PaymentRecord.PaymentMethodDetail.Bizum`
* Add support for `transaction_link_id` on `Charge.PaymentMethodDetail.Card`
* ⚠️ Add support for new value `sui` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
* ⚠️ Add support for new value `usdsui` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
* Add support for `fingerprint` on `Charge.PaymentMethodDetail.Pix`, `ConfirmationToken.PaymentMethodPreview.Pix`, `PaymentMethod.Pix`, and `SetupAttempt.PaymentMethodDetail.Pix`
* Add support for `sunbit` on `Checkout.Session.PaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for `billing_cycle_anchor_config` on `checkout.SessionCreateParamsSubscriptionDatum`
* Add support for `wechat_pay` on `Checkout.Session.PaymentMethodOption`
* Add support for `mastercard_compliance` on `Dispute.Evidence.EnhancedEvidence`, `Dispute.EvidenceDetail.EnhancedEligibility`, and `DisputeModifyParamsEvidenceEnhancedEvidence`
* ⚠️ Add support for new value `mastercard_compliance` on enum `Dispute.enhanced_eligibility_types`
* Add support for `status_details` on `FinancialConnections.Account`
* ⚠️ Add support for new value `validated` on enum `Identity.VerificationSession.Redaction.status`
* Add support for new value `satispay` on enums `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* ⚠️ Add support for new value `satispay` on enums `Invoice.PaymentSetting.payment_method_types` and `Subscription.PaymentSetting.payment_method_types`
* ⚠️ Remove support for `stored_credential_usage` on `PaymentAttemptRecord.PaymentMethodDetail.Card` and `PaymentRecord.PaymentMethodDetail.Card`
* ⚠️ Change `PaymentAttemptRecord.PaymentMethodDetail.Card.description` and `PaymentRecord.PaymentMethodDetail.Card.description` to be optional
* ⚠️ Change `PaymentAttemptRecord.PaymentMethodDetail.Card.iin` and `PaymentRecord.PaymentMethodDetail.Card.iin` to be optional
* ⚠️ Change `PaymentAttemptRecord.PaymentMethodDetail.Card.issuer` and `PaymentRecord.PaymentMethodDetail.Card.issuer` to be optional
* Add support for `setup_future_usage` on `PaymentIntent.PaymentMethodOption.Satispay`, `PaymentIntentConfirmParamsPaymentMethodOptionSatispay`, `PaymentIntentCreateParamsPaymentMethodOptionSatispay`, and `PaymentIntentModifyParamsPaymentMethodOptionSatispay`
* Change `PaymentRecordReportRefundParams.refunded` to be optional
* Add support for `satispay` on `SetupAttempt.PaymentMethodDetail`
* Add support for `custom_fields`, `description`, and `footer` on `Subscription.InvoiceSetting`, `SubscriptionCreateParamsInvoiceSetting`, and `SubscriptionModifyParamsInvoiceSetting`
* Add support for `payment_method_options` and `payment_method` on `TopupCreateParams`
* Add support for new value `2026-06-24.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `mode` on `V2.Commerce.ProductCatalogImport`
* ⚠️ Add support for new value `promotion` on enum `V2.Commerce.ProductCatalogImport.feed_type`
* Add support for `sunbit_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `crypto_money_manager` and `money_manager` on `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `crypto_storer` and `storer` on `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* Add support for new value `promotion` on enum `v2.commerce.ProductCatalogImportCreateParams.feed_type`
* ⚠️ Add support for new value `sunbit_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
* Add support for error codes `anomalous_money_movement_request`, `failed_tax_calculation`, `financial_account_balance_does_not_support_currency`, `financial_account_capability_not_enabled`, and `financial_account_capability_restricted` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, and `Terminal.Reader.Action.ApiError`
