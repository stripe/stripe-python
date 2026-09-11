---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1742
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.1.0b1
---

* Add support for new resources `product_catalog.TrialOffer`, `tax.Location`, and `v2.core.BatchJob`
* Add support for `create` method on resource `product_catalog.TrialOffer`
* Add support for `create`, `list`, and `retrieve` methods on resource `tax.Location`
* Add support for `cancel`, `create`, and `retrieve` methods on resource `v2.core.BatchJob`
* Add support for `performance_location` on `Tax.CalculationLineItem` and `tax.CalculationCreateParamsLineItem`
* ⚠️ Add support for new value `performance` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.sourcing`, `Tax.CalculationLineItem.TaxBreakdown.sourcing`, and `Tax.Transaction.ShippingCost.TaxBreakdown.sourcing`
* ⚠️ Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
* Add support for `trial_offer` on `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSet`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItem`, `QuoteCreateParamsLineActionAddItem`, `QuoteCreateParamsLineActionSetItem`, `QuoteLine.Action.AddItem`, `QuoteLine.Action.SetItem`, `QuoteModifyParamsLineActionAddItem`, `QuoteModifyParamsLineActionSetItem`, `QuotePreviewSubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase.Item`, `SubscriptionScheduleAmendParamsAmendmentItemActionAdd`, `SubscriptionScheduleAmendParamsAmendmentItemActionSet`, `SubscriptionScheduleCreateParamsPhaseItem`, and `SubscriptionScheduleModifyParamsPhaseItem`
* Add support for `risk_reserved` on `Balance`
* ⚠️ Remove support for `source_type` on `Charge.PaymentMethodDetail.StripeBalance`, `ConfirmationToken.PaymentMethodPreview.StripeBalance`, `ConfirmationTokenCreateParamsPaymentMethodDatumStripeBalance`, `PaymentAttemptRecord.PaymentMethodDetail.StripeBalance`, `PaymentIntentConfirmParamsPaymentMethodDatumStripeBalance`, `PaymentIntentCreateParamsPaymentMethodDatumStripeBalance`, `PaymentIntentModifyParamsPaymentMethodDatumStripeBalance`, `PaymentMethod.StripeBalance`, `PaymentMethodCreateParamsStripeBalance`, `PaymentRecord.PaymentMethodDetail.StripeBalance`, `SetupIntentConfirmParamsPaymentMethodDatumStripeBalance`, `SetupIntentCreateParamsPaymentMethodDatumStripeBalance`, and `SetupIntentModifyParamsPaymentMethodDatumStripeBalance`
* Add support for `tax_details` on `InvoiceAddLinesParamsLinePriceDatumProductDatum`, `InvoiceLineItemModifyParamsPriceDatumProductDatum`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatum`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatum`, `PlanCreateParamsProduct`, `PriceCreateParamsProductDatum`, `ProductCreateParams`, `ProductModifyParams`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatum`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatum`
* Add support for `pending_invoice_item_interval` on `checkout.SessionModifyParamsSubscriptionDatum`
* Add support for `hosted` and `ui_mode` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
* Add support for `url` on `FinancialConnections.Session`
* Add support for `expires_after_seconds` on `Invoice.PaymentSetting.PaymentMethodOption.Pix`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionPix`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionPix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Pix`, `Subscription.PaymentSetting.PaymentMethodOption.Pix`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionPix`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionPix`
* Add support for `current_trial` on `InvoiceCreatePreviewParamsSubscriptionDetailItem`, `SubscriptionCreateParamsItem`, `SubscriptionItemCreateParams`, `SubscriptionItemModifyParams`, `SubscriptionItem`, and `SubscriptionModifyParamsItem`
* Add support for `surcharge` on `PaymentIntent.AmountDetail`, `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
* Add support for `amount_details` and `payment_details` on `PaymentIntentDecrementAuthorizationParams`
* Add support for `mandate_options` on `PaymentIntent.PaymentMethodOption.StripeBalance`
* Add support for `managed_payments` on `PaymentLinkCreateParams` and `PaymentLink`
* Add support for `stripe_balance` on `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodOption`, and `SetupIntentModifyParamsPaymentMethodOption`
* Add support for `billing_cycle_anchor` on `Subscription.TrialSetting.EndBehavior`, `SubscriptionCreateParamsTrialSettingEndBehavior`, and `SubscriptionModifyParamsTrialSettingEndBehavior`
* ⚠️ Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
* Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `Tax.Registration.CountryOption.Me`
* Add support for `requirements` on `TaxCode`
* ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.Card.MandateOption.amount`, `V2.Billing.CollectionSetting.PaymentMethodOption.Card.MandateOption.amount`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.Card.MandateOption.amount`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOptionCardMandateOption.amount`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOptionCardMandateOption.amount` from `longInteger` to `int64_string`
* ⚠️ Add support for new values `ar_bank_account`, `co_bank_account`, and `eg_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `timezone` on `V2.Core.Account.Default`, `v2.core.AccountCreateParamsDefault`, and `v2.core.AccountModifyParamsDefault`
* Add support for `azure_event_grid` on `V2.Core.EventDestination` and `v2.core.EventDestinationCreateParams`
* ⚠️ Add support for new value `no_azure_partner_topic_exists` on enum `V2.Core.EventDestination.StatusDetail.Disabled.reason`
* ⚠️ Add support for new value `azure_event_grid` on enums `V2.Core.EventDestination.type` and `v2.core.EventDestinationCreateParams.type`
* Add support for `supported_currencies` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod.Card`
* ⚠️ Change `V2.Core.Vault.GbBankAccount.sort_code` and `v2.core.vault.GbBankAccountCreateParams.sort_code` to be optional
* Add support for `restricted` on `V2.MoneyManagement.PayoutMethod`
* Add support for `currencies` on `V2.MoneyManagement.PayoutMethodsBankAccountSpec.Country.Field`
* Add support for `counterparty` and `description` on `V2.MoneyManagement.Transaction`
* ⚠️ Add support for `currency` on `v2.core.vault.GbBankAccountCreateParams`, `v2.core.vault.UsBankAccountCreateParams`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumCard`, `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumCard`
* Add support for `iban` on `v2.core.vault.GbBankAccountCreateParams`
* Change `v2.core.vault.GbBankAccountCreateParams.account_number` to be optional
* ⚠️ Add support for new value `currency` on enum `InvalidPaymentMethodError.invalid_param`
* Add support for event notifications `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, and `V2CoreBatchJobValidationFailedEvent` with related object `v2.core.BatchJob`
* Add support for error code `service_period_coupon_with_metered_tiered_item_unsupported` on `QuotePreviewInvoice.LastFinalizationError`
