---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1741
is_breaking: true
is_stripe_api_change: true
released_in_version: 14.5.0a2
---

* Add support for new resources `Profile` and `billing.AlertRecovered`
* Add support for `reauthorize` method on resource `PaymentIntent`
* Add support for `settings` on `QuoteLine.Action.AddDiscount`, `QuoteLine.Action.AddItem.Discount`, `QuoteLine.Action.SetDiscount`, `QuoteLine.Action.SetItem.Discount`, `QuotePreviewSubscriptionSchedule.Phase.Discount`, `QuotePreviewSubscriptionSchedule.Phase.Item.Discount`, `SubscriptionSchedule.Phase.Discount`, and `SubscriptionSchedule.Phase.Item.Discount`
* Add support for `smart_disputes` on `Account.Setting`, `AccountCreateParamsSetting`, `AccountModifyParamsSetting`, `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
* Add support for `email_customers_on_successful_payment` on `Account.Setting.Payment`, `AccountCreateParamsSettingPayment`, and `AccountModifyParamsSettingPayment`
* Add support for `balance_update_details` on `Billing.CreditBalanceSummary.Balance`
* Add support for `reauthorization` and `reauthorize_before` on `Charge.PaymentMethodDetail.CardPresent`, `Charge.PaymentMethodDetail.Card`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.CardPresent`, `Charge.PaymentMethodDetail.InteracPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.InteracPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentRecord.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.InteracPresent`
* Add support for `managed_payments` on `Checkout.Session`, `PaymentIntent`, `SetupIntent`, `Subscription`, and `checkout.SessionCreateParams`
* Add support for new value `lk_vat` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* Add support for new value `lk_vat` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `OrderCreateParamsTaxDetailTaxId.type`, `OrderModifyParamsTaxDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
* Add support for `digital` on `DelegatedCheckout.RequestedSession.FulfillmentDetail.FulfillmentOption`, `DelegatedCheckout.RequestedSession.FulfillmentDetail.SelectedFulfillmentOption`, and `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOption`
* Change `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailSelectedFulfillmentOption.shipping` to be optional
* Add support for `affiliate_attributions` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionConfirmParams`, and `delegated_checkout.RequestedSessionCreateParams`
* Add support for `fulfillment_type` on `DelegatedCheckout.RequestedSession.LineItemDetail`
* Add support for `marketplace_seller_details`, `network_profile`, `privacy_notice_url`, `return_policy_url`, `store_policy_url`, and `terms_of_service_url` on `DelegatedCheckout.RequestedSession.SellerDetail`
* Add support for `amount_to_counter` on `DisputeModifyParams`
* Add support for new values `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, and `reserve.release.created` on enum `Event.type`
* Add support for new values `terminal_wifi_certificate` and `terminal_wifi_private_key` on enums `File.purpose` and `FileListParams.purpose`
* Add support for new values `terminal_wifi_certificate` and `terminal_wifi_private_key` on enum `FileCreateParams.purpose`
* Add support for new value `pay_by_bank` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for `display_name` and `service_user_number` on `Mandate.PaymentMethodDetail.BacsDebit`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Boleto.tax_id` and `PaymentRecord.PaymentMethodDetail.Boleto.tax_id` from `string` to `nullable(string)`
* Change type of `PaymentAttemptRecord.PaymentMethodDetail.UsBankAccount.expected_debit_date` and `PaymentRecord.PaymentMethodDetail.UsBankAccount.expected_debit_date` from `nullable(string)` to `string`
* Add support for `request_reauthorization` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
* Add support for `transaction_purpose` on `PaymentIntent.PaymentMethodOption.UsBankAccount`, `PaymentIntentConfirmParamsPaymentMethodOptionUsBankAccount`, `PaymentIntentCreateParamsPaymentMethodOptionUsBankAccount`, and `PaymentIntentModifyParamsPaymentMethodOptionUsBankAccount`
* Add support for new value `requires_reauthorization` on enum `PaymentIntent.status`
* Add support for `optional_items` on `PaymentLinkModifyParams`
* Add support for new value `billing_schedules_invalid` on enum `Quote.StatusDetail.Stale.LastReason.type`
* ⚠️ Remove support for `card_issuer_decline` on `Radar.PaymentEvaluation.Insight`
* Add support for `payment_behavior` on `SubscriptionItemDeleteParams`
* Add support for `billing_cycle_anchor` on `Subscription.TrialSetting.EndBehavior`
* Add support for `lk` on `Tax.Registration.CountryOption` and `tax.RegistrationCreateParamsCountryOption`
* Add support for `cellular` and `stripe_s710` on `Terminal.Configuration`, `terminal.ConfigurationCreateParams`, and `terminal.ConfigurationModifyParams`
* Add support for new values `simulated_stripe_s710` and `stripe_s710` on enums `Terminal.Reader.device_type` and `terminal.ReaderListParams.device_type`
* Add support for new values `reserve.hold.created`, `reserve.hold.updated`, `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, `reserve.plan.updated`, and `reserve.release.created` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for new value `2026-02-25.clover` on enum `WebhookEndpointCreateParams.api_version`
* Add support for new values `ar_bank_account`, `bt_bank_account`, `co_bank_account`, `cr_bank_account`, `do_bank_account`, `gt_bank_account`, `md_bank_account`, `mk_bank_account`, `mo_bank_account`, `mz_bank_account`, `pe_bank_account`, `pk_bank_account`, `tw_bank_account`, and `uz_bank_account` on enums `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type` and `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `recipient_onboarding` and `recipient_update` on `V2.Core.AccountLink.UseCase` and `v2.core.AccountLinkCreateParamsUseCase`
* Add support for new values `recipient_onboarding` and `recipient_update` on enums `V2.Core.AccountLink.UseCase.type` and `v2.core.AccountLinkCreateParamsUseCase.type`
* Add support for `consumer` on `V2.Core.Account.Configuration.Storer.Capability`, `v2.core.AccountCreateParamsConfigurationStorerCapability`, and `v2.core.AccountModifyParamsConfigurationStorerCapability`
* Add support for new value `consumer.holds_currencies.usd` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `funds_usage_type` on `V2.MoneyManagement.FinancialAccount.Storage` and `v2.money_management.FinancialAccountCreateParamsStorage`
* Add support for `purpose` on `V2.MoneyManagement.OutboundPayment` and `v2.money_management.OutboundPaymentCreateParams`
* Add support for `branch_number` and `swift_code` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* Add support for new values `dispute`, `inbound_payment_failure`, `inbound_payment`, `india_mdr_processing_fee`, `payment_method_passthrough_fee`, `refund`, and `tax_withholding` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* ⚠️ Remove support for values `charge_failure` and `charge` from enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* ⚠️ Change `V2.MoneyManagement.Transaction.flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.flow` to be optional
* Add support for new value `consumer.holds_currencies.usd` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for snapshot event `billing.alert.recovered` with resource `billing.AlertRecovered`
* Add support for snapshot events `reserve.hold.created` and `reserve.hold.updated` with resource `reserve.Hold`
* Add support for snapshot events `reserve.plan.created`, `reserve.plan.disabled`, `reserve.plan.expired`, and `reserve.plan.updated` with resource `reserve.Plan`
* Add support for snapshot event `reserve.release.created` with resource `reserve.Release`
* Add support for event notification `V2BillingRateCardCustomPricingUnitOverageRateCreatedEvent` with related object `v2.billing.RateCardCustomPricingUnitOverageRate`
* Add support for event notifications `V2IamStripeAccessGrantApprovedEvent`, `V2IamStripeAccessGrantCanceledEvent`, `V2IamStripeAccessGrantDeniedEvent`, `V2IamStripeAccessGrantRemovedEvent`, `V2IamStripeAccessGrantRequestedEvent`, and `V2IamStripeAccessGrantUpdatedEvent`
* Add support for error codes `storer_capability_missing` and `storer_capability_not_active` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
