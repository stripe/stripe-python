---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1989
semver_level: major
is_stripe_api_change: true
released_in_version: 17.2.0a1
---

* Add support for new resources `v2.billing.GroupInvoice`, `v2.billing.GroupSpendModifier`, and `v2.billing.Group`
* ⚠️ Remove support for resources `v2.billing.CadenceSpendModifier` and `v2.billing.ContractPricingLineQuantityChange`
* Add support for `create` and `modify` methods on resource `InvoiceRenderingTemplate`
* Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.Group`
* Add support for `retrieve` method on resource `v2.billing.GroupSpendModifier`
* Add support for `create` method on resource `v2.billing.GroupInvoice`
* ⚠️ Remove support for `retrieve` method on resource `v2.billing.CadenceSpendModifier`
* ⚠️ Remove support for `billing_cadence` on `Billing.Alert.SpendThreshold.Filter`, `Billing.AlertTriggered.GroupBy`, `InvoiceCreatePreviewParams`, `InvoiceListParams`, `SubscriptionCreateParams`, `SubscriptionListParams`, `SubscriptionModifyParams`, `Subscription`, `V2.Billing.PricingPlanSubscription`, `V2.Billing.RateCardSubscription`, `billing.AlertCreateParamsSpendThresholdFilter`, `v2.billing.PricingPlanSubscriptionListParams`, `v2.billing.RateCardSubscriptionCreateParams`, and `v2.billing.RateCardSubscriptionListParams`
* ⚠️ Add support for new value `billing_group` on enum `Billing.AlertTriggered.GroupBy.type`
* ⚠️ Remove support for value `billing_cadence` from enum `Billing.AlertTriggered.GroupBy.type`
* Add support for `scheduled_fee` on `V2.Billing.ContractTerm`, `v2.billing.ContractCreateParamsTerm`, `v2.billing.ContractModifyParamsActionAddTerm`, and `v2.billing.ContractModifyParamsActionUpdateTerm`
* ⚠️ Remove support for `ad_hoc_product` on `V2.Billing.ContractTerm`, `v2.billing.ContractCreateParamsTerm`, `v2.billing.ContractModifyParamsActionAddTerm`, and `v2.billing.ContractModifyParamsActionUpdateTerm`
* ⚠️ Add support for new value `scheduled_fee` on enums `V2.Billing.ContractTerm.type`, `v2.billing.ContractCreateParamsTerm.type`, `v2.billing.ContractModifyParamsActionAddTerm.type`, and `v2.billing.ContractTermListContractTermsParams.type`
* ⚠️ Remove support for value `ad_hoc_product` from enums `V2.Billing.ContractTerm.type`, `v2.billing.ContractCreateParamsTerm.type`, `v2.billing.ContractModifyParamsActionAddTerm.type`, and `v2.billing.ContractTermListContractTermsParams.type`
* ⚠️ Add support for new value `billing_group` on enums `Billing.Alert.SpendThreshold.group_by` and `billing.AlertCreateParamsSpendThreshold.group_by`
* ⚠️ Remove support for value `billing_cadence` from enums `Billing.Alert.SpendThreshold.group_by` and `billing.AlertCreateParamsSpendThreshold.group_by`
* ⚠️ Remove support for `cadence` on `Billing.AlertNotification`, `V2.Billing.Intent`, `billing.BillingAlertListAlertNotificationParams`, and `v2.billing.IntentCreateParams`
* ⚠️ Remove support for `pricing_token` on `checkout.SessionCreateParams`
* Add support for `pass_through_fee_cost` on `Checkout.Session`
* Add support for new value `dealerfx` on enums `Checkout.Session.AutomaticSurcharge.provider` and `PaymentLink.AutomaticSurcharge.provider`
* Add support for `amount_pass_through_fee` on `Checkout.Session.TotalDetail`
* ⚠️ Change `GiftCardOperation.Activation.balance` and `GiftCardOperation.Reload.balance` to be optional
* Add support for `link_shared_data` on `identity.VerificationSessionCreateParams`
* Add support for `line_item_policy`, `rendering_settings`, and `summary_item_policies` on `InvoiceRenderingTemplate`
* Add support for `billing_group` on `InvoiceCreatePreviewParams`, `InvoiceListParams`, `V2.Billing.Intent`, `V2.Billing.PricingPlanSubscription`, `V2.Billing.RateCardSubscription`, `v2.billing.IntentCreateParams`, `v2.billing.PricingPlanSubscriptionListParams`, and `v2.billing.RateCardSubscriptionListParams`
* Add support for `applied_credit_memos` on `Invoice` and `QuotePreviewInvoice`
* Add support for `billing_group_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
* ⚠️ Remove support for `billing_cadence_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
* ⚠️ Add support for new value `billing_group_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
* ⚠️ Remove support for value `billing_cadence_details` from enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
* Add support for `token_service_provider_id` on `Issuing.Authorization.TokenDetail.NetworkDatum.Visa` and `Issuing.Token.NetworkDatum.Visa`
* Add support for `amount_type`, `amount`, `currency`, `description`, `end_date`, `interval_count`, `interval`, `reference`, and `start_date` on `Mandate.PaymentMethodDetail.Card.India`
* Add support for `three_d_secure` on `PaymentAttemptRecordReportFailedParamsPaymentMethodDetailCard` and `PaymentRecordReportPaymentAttemptFailedParamsPaymentMethodDetailCard`
* Add support for `provider_signature_data` and `provider_signature` on `PaymentIntent.PaymentMethodOption.CardPresent.AadeDatum`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentAadeDatum`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentAadeDatum`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentAadeDatum`
* ⚠️ Remove support for `mark_data` and `signed_mark` on `PaymentIntent.PaymentMethodOption.CardPresent.AadeDatum`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresentAadeDatum`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresentAadeDatum`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresentAadeDatum`
* Add support for `request_multicapture` on `PaymentIntent.PaymentMethodOption.Vipp`, `PaymentIntentConfirmParamsPaymentMethodOptionVipp`, `PaymentIntentCreateParamsPaymentMethodOptionVipp`, and `PaymentIntentModifyParamsPaymentMethodOptionVipp`
* Add support for `is_free_trial_transaction` on `PaymentIntentConfirmParamsRadarOption` and `PaymentIntentCreateParamsRadarOption`
* Add support for new value `tron` on enum `PaymentIntentUpdateCryptoRefundAddressParams.network`
* Add support for `radar_options` on `PaymentIntent`
* Add support for `aeon_pay`, `au_pay`, `dbarai`, and `merpay` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, and `PaymentMethodConfiguration`
* Add support for `requested_signals` on `Radar.PaymentEvaluation` and `radar.PaymentEvaluationCreateParams`
* Add support for `gift_card` on `Refund.DestinationDetail`
* Add support for `days_after_fulfillment` on `Reserve.Plan.RollingRelease`
* Add support for `rendering` on `SubscriptionScheduleCreateParamsDefaultSettingInvoiceSetting` and `SubscriptionScheduleModifyParamsDefaultSettingInvoiceSetting`
* Add support for `debit_behavior` on `Subscription.PaymentSetting.PaymentMethodOption.Card`, `Subscription.PaymentSetting.PaymentMethodOption.Pix`, `Subscription.PaymentSetting.PaymentMethodOption.Upi`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionCard`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionPix`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionUpi`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionCard`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionPix`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionUpi`
* Add support for `presentment_details` on `Subscription.PendingUpdate`
* ⚠️ Remove support for `device_health_details` and `device_health` on `Terminal.Reader`
* Add support for `billing_group_data` on `V2.Billing.Intent` and `v2.billing.IntentCreateParams`
* ⚠️ Remove support for `cadence_data` on `V2.Billing.Intent` and `v2.billing.IntentCreateParams`
* Add support for new value `group` on enums `V2.Billing.IntentAction.Apply.InvoiceDiscountRule.applies_to` and `v2.billing.IntentCreateParamsActionApplyInvoiceDiscountRule.applies_to`
* Add support for new value `account_dashboard` on enums `V2.Core.AccountLink.UseCase.type` and `v2.core.AccountLinkCreateParamsUseCase.type`
* Add support for `touch_n_go_payments`, `truemoney_payments`, `wechat_pay_mobile_web_payments`, `wechat_pay_payments`, and `wero_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `business_demand_deposit_account_fifth_third_storage` on `V2.Core.Account.Configuration.MoneyManager.Capability`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapability`, and `v2.core.AccountModifyParamsConfigurationMoneyManagerCapability`
* Add support for `tips` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* Add support for `business_demand_deposit_account_fifth_third` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* Add support for `channel` on `V2.Core.ClaimableSandbox` and `v2.core.ClaimableSandboxCreateParams`
* ⚠️ Remove support for `app_channel` on `V2.Core.ClaimableSandbox` and `v2.core.ClaimableSandboxCreateParams`
* Add support for `return_url` on `V2.Core.ClaimableSandbox.OnboardingLinkDetail`, `v2.core.ClaimableSandboxCreateParamsOnboardingLinkDetail`, and `v2.core.ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetail`
* ⚠️ Change type of `V2.Core.ClaimableSandbox.SandboxDetail.ApiKey.mcp` from `string` to `an object`
* ⚠️ Change type of `V2.Core.ClaimableSandbox.SandboxDetail.ApiKey.publishable` from `string` to `an object`
* ⚠️ Change type of `V2.Core.ClaimableSandbox.SandboxDetail.ApiKey.secret` from `string` to `an object`
* ⚠️ Change `V2.Core.ClaimableSandbox.onboarding_link_details` to be optional
* ⚠️ Change `V2.Core.ClaimableSandbox.OwnerDetail.app_install_status` to be optional
* Add support for `custom_payment_method_adapter_degraded` on `V2.Core.Health.AlertHistoryEntry` and `V2.Core.Health.Alert`
* Add support for new value `custom_payment_method_adapter_degraded` on enums `V2.Core.Health.Alert.type` and `V2.Core.Health.AlertHistoryEntry.type`
* Add support for `funds_holding_structure` on `V2.MoneyManagement.FinancialAccount.Storage` and `v2.money_management.FinancialAccountCreateParamsStorage`
* Add support for `au_becs_debit` on `V2.MoneyManagement.InboundTransfer.From.PaymentMethod`
* Add support for new value `tips` on enums `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.NetworkFeeDetail.network` and `V2.MoneyManagement.PayoutIntent.EstimatedFee.NetworkFeeDetail.network`
* Add support for new value `tips` on enums `V2.MoneyManagement.OutboundPayment.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.OutboundPaymentQuote.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.OutboundTransfer.To.PayoutMethodOption.BankAccount.preferred_networks`, `V2.MoneyManagement.PayoutIntent.To.PayoutMethodOption.BankAccount.preferred_networks`, `v2.money_management.OutboundPaymentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.OutboundPaymentQuoteCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.OutboundTransferCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, `v2.money_management.PayoutIntentCreateParamsToPayoutMethodOptionBankAccount.preferred_networks`, and `v2.money_management.PayoutIntentModifyParamsToPayoutMethodOptionBankAccount.preferred_networks`
* Add support for `network` on `V2.MoneyManagement.ReceivedDebit.BankTransfer`
* Add support for new values `inbound_funding_reversal` and `inbound_funding` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for new value `inbound_funding` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for `settlement_timing` on `v2.money_management.FundingIntentModifyParams`
* Add support for new value `custom_payment_method_adapter_degraded` on enum `v2.core.health.AlertListParams.types`
* Add support for `include` on `v2.core.ClaimableSandboxRetrieveParams`
* Change `v2.core.ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetail.refresh_url` to be optional
* ⚠️ Add support for `billing_group` on `v2.billing.RateCardSubscriptionCreateParams`
* ⚠️ Remove support for `one_time_fees`, `pricing_lines`, and `pricing_overrides` on `v2.billing.ContractCreateParams`
* Add support for new value `now` on enums `v2.billing.ContractCreateParamsTermPricingOverrideEndsAt.type`, `v2.billing.ContractCreateParamsTermRecurringPriceEndsAt.type`, `v2.billing.ContractModifyParamsActionAddTermPricingOverrideEndsAt.type`, `v2.billing.ContractModifyParamsActionAddTermRecurringPriceEndsAt.type`, `v2.billing.ContractModifyParamsActionUpdateTermPricingOverrideEndsAt.type`, and `v2.billing.ContractModifyParamsActionUpdateTermRecurringPriceEndsAt.type`
* Add support for new value `now` on enums `v2.billing.ContractCreateParamsTermPricingOverrideStartsAt.type`, `v2.billing.ContractCreateParamsTermRecurringPriceStartsAt.type`, `v2.billing.ContractModifyParamsActionAddTermPricingOverrideStartsAt.type`, `v2.billing.ContractModifyParamsActionAddTermRecurringPriceStartsAt.type`, `v2.billing.ContractModifyParamsActionUpdateTermPricingOverrideStartsAt.type`, and `v2.billing.ContractModifyParamsActionUpdateTermRecurringPriceStartsAt.type`
* Add support for `contract_number` on `v2.billing.ContractModifyParams`
* ⚠️ Remove support for `one_time_fee_actions`, `pricing_line_actions`, and `pricing_override_actions` on `v2.billing.ContractModifyParams`
* ⚠️ Remove support for `cancel_pricing_lines` on `v2.billing.ContractCancelParams`
* Add support for new values `business_demand_deposit_account_fifth_third_storage.inbound.usd` and `business_demand_deposit_account_fifth_third_storage.outbound.usd` on enum `EventsV2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for new value `bank_accounts.tips` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
* Add support for `charge` on `EventsV2PaymentsOffSessionPaymentAttemptFailedEvent`, `EventsV2PaymentsOffSessionPaymentFailedEvent`, and `EventsV2PaymentsOffSessionPaymentSucceededEvent`
* Add support for `last_attempt_error` on `EventsV2PaymentsOffSessionPaymentAttemptFailedEvent` and `EventsV2PaymentsOffSessionPaymentFailedEvent`
* Add support for `payment_attempt_record` on `EventsV2PaymentsOffSessionPaymentSucceededEvent`
* Add support for event notifications `V2BillingContractTermPricingOverrideEndedEvent`, `V2BillingContractTermPricingOverrideStartedEvent`, `V2BillingContractTermRecurringPriceEndedEvent`, `V2BillingContractTermRecurringPriceStartedEvent`, `V2BillingContractTermScheduledFeeServicePeriodEndedEvent`, and `V2BillingContractTermScheduledFeeServicePeriodStartedEvent` with related object `v2.billing.ContractTerm`
* Add support for event notifications `V2CoreHealthCustomPaymentMethodAdapterDegradedFiringEvent` and `V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent`
* Add support for event notifications `V2SignalsPaymentRetryEvaluationCanceledEvent`, `V2SignalsPaymentRetryEvaluationCompletedEvent`, `V2SignalsPaymentRetryEvaluationCreatedEvent`, `V2SignalsPaymentRetryEvaluationExpiredEvent`, and `V2SignalsPaymentRetryEvaluationUpdatedEvent` with related object `v2.signals.PaymentRetryEvaluation`
* ⚠️ Remove support for event notifications `V2BillingCadenceBilledEvent`, `V2BillingCadenceCanceledEvent`, and `V2BillingCadenceCreatedEvent` with related object `v2.billing.Cadence`
* ⚠️ Add error type `RateLimitError` on `v2.core.ClaimableSandbox#create`
* Add support for error code `scheduled_cancellation_conflicts_with_updated_terms` on `CannotProceedError`
