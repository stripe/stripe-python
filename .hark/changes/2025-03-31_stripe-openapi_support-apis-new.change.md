---
title: Support for APIs in the new API version 2025-03-31.basil
pr_url: https://github.com/stripe/stripe-python/pull/1463
is_stripe_api_change: true
released_in_version: 12.0.0
---

This release changes the pinned API version to `2025-03-31.basil`.

### ⚠️ Breaking changes  due to changes in the Stripe API

Please review details for the breaking changes and alternatives in the [Stripe API changelog](https://docs.stripe.com/changelog/basil) before upgrading.

* Remove support for resources `SubscriptionItemUsageRecordSummary` and `SubscriptionItemUsageRecord`
* Remove support for `create` method on resource `SubscriptionItemUsageRecord`
* Remove support for `list` method on resource `SubscriptionItemUsageRecordSummary`
* Remove support for `upcomingLines` and `upcoming` methods on resource `Invoice`
* Remove support for `invoice` on `Charge` and `PaymentIntent`
* Remove support for `shipping_details` on `CheckoutSession`
* Remove support for `carrier`, `phone`, and `tracking_number` on `CheckoutSession.CollectedInformation.ShippingDetail`
* Remove support for `refund` on `CreditNote.CreateParams`, `CreditNote.PreviewParams`, `CreditNotePreviewLines.ListParams`, and `CreditNote`
* Remove support for `tax_amounts` on `CreditNoteLineItem`, `CreditNote`, and `InvoiceLineItem`
* Remove support for `amount_excluding_tax` and `unit_amount_excluding_tax` on `CreditNoteLineItem` and `InvoiceLineItem`
* Remove support for `coupon` on `Customer.CreateParams`, `Customer.UpdateParams`, `Invoice.CreatePreviewParamsScheduleDetailPhase`, `Invoice.CreatePreviewParams`, `Subscription.CreateParams`, `Subscription.UpdateParams`, `SubscriptionSchedule.CreateParamsPhase`, `SubscriptionSchedule.Phase`, and `SubscriptionSchedule.UpdateParamsPhase`
* Remove support for `promotion_code` on `Customer.CreateParams`, `Customer.UpdateParams`, `Subscription.CreateParams`, and `Subscription.UpdateParams`
* Remove support for `price` on `Invoice.AddLinesParamsLine`, `Invoice.UpdateLinesParamsLine`, `InvoiceItem.CreateParams`, `InvoiceItem.UpdateParams`, `InvoiceItem`, `InvoiceLineItem.UpdateParams`, and `InvoiceLineItem`
* Remove support for `billing_thresholds` on `Invoice.CreatePreviewParamsScheduleDetailPhaseItem`, `Invoice.CreatePreviewParamsScheduleDetailPhase`, `Invoice.CreatePreviewParamsSubscriptionDetailItem`, `Subscription.CreateParamsItem`, `Subscription.CreateParams`, `Subscription.UpdateParamsItem`, `Subscription.UpdateParams`, `SubscriptionItem.CreateParams`, `SubscriptionItem.UpdateParams`, `SubscriptionItem`, `SubscriptionSchedule.CreateParamsDefaultSetting`, `SubscriptionSchedule.CreateParamsPhaseItem`, `SubscriptionSchedule.CreateParamsPhase`, `SubscriptionSchedule.DefaultSetting`, `SubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase`, `SubscriptionSchedule.UpdateParamsDefaultSetting`, `SubscriptionSchedule.UpdateParamsPhaseItem`, `SubscriptionSchedule.UpdateParamsPhase`, and `Subscription`
* Remove support for `application_fee_amount`, `charge`, `paid_out_of_band`, `paid`, `payment_intent`, `quote`, `subscription`, `subscription_details`, `subscription_proration_date`, `tax`, `total_tax_amounts`, and `transfer_data` on `Invoice`
* Remove support for `discount` on `Invoice` and `Subscription`
* Remove support for `invoice_item`, `proration_details`, `proration`, `tax_rates`, and `type` on `InvoiceLineItem`
* Remove support for `plan` and `subscription_item` on `InvoiceItem` and `InvoiceLineItem`
* Remove support for `unit_amount` on `InvoiceItem.CreateParams`, `InvoiceItem.UpdateParams`, and `InvoiceItem`
* Remove support for `subscription` and `unit_amount_decimal` on `InvoiceItem`
* Remove support for `naver_pay` on `PaymentMethod.UpdateParams`
* Remove support for `aggregate_usage` on `Plan.CreateParams`, `Plan`, `Price.CreateParamsRecurring`, and `Price.Recurring`
* Remove support for `current_period_end` and `current_period_start` on `Subscription`
* Remove support for page on `v2.Event.ListParams` and `v2.EventDestination.ListParams`

### Changes
* Change `CheckoutSession.collected_information` to be required
* Change `CheckoutSession.CollectedInformation.shipping_details` to be required
* Change `CheckoutSession.CollectedInformation.ShippingDetail.address` to be required
* Change `CheckoutSession.CollectedInformation.ShippingDetail.name` to be required
* Change `PaymentIntent.ConfirmParamsPaymentMethodOptionWechatPay.client`, `PaymentIntent.CreateParamsPaymentMethodOptionWechatPay.client`, and `PaymentIntent.UpdateParamsPaymentMethodOptionWechatPay.client` to be optional
* Change `political_exposure` on resources `Person` and `Token` and params `Token.CreateParams` from string to `enum("existing" | "none")`

### Additions

* Add support for new resource `InvoicePayment`
* Add support for `list` and `retrieve` methods on resource `InvoicePayment`
* Add support for `billie_payments`, `nz_bank_account_becs_debit_payments`, and `satispay_payments` on `Account.Capability`, `Account.CreateParamsCapability`, and `Account.UpdateParamsCapability`
* Add support for `hosted_payment_method_save` on `Account.Setting.Invoice` and `Account.UpdateParamsSettingInvoice`
* Add support for `invoices` on `Account.CreateParamsSetting`
* Add support for new values `information_missing`, `invalid_signator`, `verification_failed_authorizer_authority`, and `verification_rejected_ownership_exemption_reason` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `AccountCapability.FutureRequirement.Error.code`, `AccountCapability.Requirement.Error.code`, `AccountPerson.FutureRequirement.Error.code`, `AccountPerson.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, and `BankAccount.Requirement.Error.code`
* Add support for new values `forwarding_api_retryable_upstream_error` and `setup_intent_mobile_wallet_unsupported` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `SetupAttempt.SetupError.code`, `SetupIntent.LastSetupError.code`, and `StripeError.code`
* Add support for new values `stripe_balance_payment_debit_reversal` and `stripe_balance_payment_debit` on enum `BalanceTransaction.type`
* Add support for new value `last` on enums `BillingMeter.DefaultAggregation.formula` and `billing.Meter.CreateParamsDefaultAggregation.formula`
* Add support for `presentment_details` on `Charge`, `CheckoutSession`, `PaymentIntent`, and `Refund`
* Add support for `billie` and `satispay` on `Charge.PaymentMethodDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatum`, `ConfirmationToken.PaymentMethodPreview`, `CustomerPaymentMethod`, `PaymentIntent.ConfirmParamsPaymentMethodDatum`, `PaymentIntent.CreateParamsPaymentMethodDatum`, `PaymentIntent.UpdateParamsPaymentMethodDatum`, `PaymentMethod.CreateParams`, `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, `PaymentMethodConfiguration`, `PaymentMethod`, `SetupIntent.ConfirmParamsPaymentMethodDatum`, `SetupIntent.CreateParamsPaymentMethodDatum`, and `SetupIntent.UpdateParamsPaymentMethodDatum`
* Add support for `nz_bank_account` on `Charge.PaymentMethodDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatum`, `ConfirmationToken.PaymentMethodPreview`, `CustomerPaymentMethod`, `Mandate.PaymentMethodDetail`, `PaymentIntent.ConfirmParamsPaymentMethodDatum`, `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodDatum`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, `PaymentIntent.UpdateParamsPaymentMethodDatum`, `PaymentIntent.UpdateParamsPaymentMethodOption`, `PaymentMethod.CreateParams`, `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, `PaymentMethodConfiguration`, `PaymentMethod`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.ConfirmParamsPaymentMethodDatum`, `SetupIntent.CreateParamsPaymentMethodDatum`, and `SetupIntent.UpdateParamsPaymentMethodDatum`
* Add support for `optional_items` on `CheckoutSession`, `PaymentLink.CreateParams`, `PaymentLink`, and `checkout.Session.CreateParams`
* Add support for `permissions` on `CheckoutSession` and `checkout.Session.CreateParams`
* Add support for new values `billie` and `satispay` on enum `checkout.Session.CreateParams.payment_method_types`
* Add support for new value `custom` on enums `CheckoutSession.ui_mode` and `checkout.Session.CreateParams.ui_mode`
* Add support for `shipping_options` on `checkout.Session.UpdateParams`
* Add support for new values `billie`, `nz_bank_account`, and `satispay` on enums `ConfirmationToken.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.ConfirmParamsPaymentMethodDatum.type`, `PaymentIntent.CreateParamsPaymentMethodDatum.type`, `PaymentIntent.UpdateParamsPaymentMethodDatum.type`, `SetupIntent.ConfirmParamsPaymentMethodDatum.type`, `SetupIntent.CreateParamsPaymentMethodDatum.type`, and `SetupIntent.UpdateParamsPaymentMethodDatum.type`
* Add support for `buyer_id` on `ConfirmationToken.PaymentMethodPreview.NaverPay`, `CustomerPaymentMethod.NaverPay`, and `PaymentMethod.NaverPay`
* Add support for new values `billie`, `nz_bank_account`, and `satispay` on enums `ConfirmationToken.PaymentMethodPreview.type`, `CustomerPaymentMethod.type`, and `PaymentMethod.type`
* Add support for `refunds` on `CreditNote.CreateParams`, `CreditNote.PreviewParams`, `CreditNotePreviewLines.ListParams`, and `CreditNote`
* Add support for `total_taxes` on `CreditNote` and `Invoice`
* Add support for `taxes` on `CreditNoteLineItem` and `InvoiceLineItem`
* Add support for `checkout_session` on `CustomerBalanceTransaction`
* Add support for new values `checkout_session_subscription_payment_canceled` and `checkout_session_subscription_payment` on enum `CustomerBalanceTransaction.type`
* Add support for new values `billie`, `nz_bank_account`, and `satispay` on enums `CustomerPaymentMethod.ListParams.type`, `PaymentMethod.CreateParams.type`, and `PaymentMethod.ListParams.type`
* Add support for new value `invoice.overpaid` on enum `Event.type`
* Add support for new values `klarna` and `nz_bank_account` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `Invoice.UpdateParamsPaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, and `Subscription.UpdateParamsPaymentSetting.payment_method_types`
* Add support for `pricing` on `Invoice.AddLinesParamsLine`, `Invoice.UpdateLinesParamsLine`, `InvoiceItem.CreateParams`, `InvoiceItem.UpdateParams`, `InvoiceItem`, `InvoiceLineItem.UpdateParams`, and `InvoiceLineItem`
* Add support for `taxability_reason` on `Invoice.AddLinesParamsLineTaxAmount`, `Invoice.UpdateLinesParamsLineTaxAmount`, and `InvoiceLineItem.UpdateParamsTaxAmount`
* Add support for `jurisdiction_level` on `Invoice.AddLinesParamsLineTaxAmountTaxRateDatum`, `Invoice.UpdateLinesParamsLineTaxAmountTaxRateDatum`, and `InvoiceLineItem.UpdateParamsTaxAmountTaxRateDatum`
* Add support for `amount_overpaid`, `confirmation_secret`, and `payments` on `Invoice`
* Add support for `parent` on `InvoiceItem`, `InvoiceLineItem`, and `Invoice`
* Add support for new value `expired` on enums `IssuingAuthorization.status` and `issuing.Authorization.ListParams.status`
* Add support for new value `network_fallback` on enum `IssuingAuthorization.RequestHistory.reason`
* Add support for `naver_pay` on `Mandate.PaymentMethodDetail` and `SetupAttempt.PaymentMethodDetail`
* Add support for `setup_future_usage` on `PaymentIntent.ConfirmParamsPaymentMethodOptionNaverPay`, `PaymentIntent.CreateParamsPaymentMethodOptionNaverPay`, `PaymentIntent.PaymentMethodOption.NaverPay`, and `PaymentIntent.UpdateParamsPaymentMethodOptionNaverPay`
* Add support for `default_value` on `PaymentLink.CreateParamsCustomFieldDropdown`, `PaymentLink.CreateParamsCustomFieldNumeric`, `PaymentLink.CreateParamsCustomFieldText`, `PaymentLink.CustomField.Dropdown`, `PaymentLink.CustomField.Numeric`, `PaymentLink.CustomField.Text`, `PaymentLink.UpdateParamsCustomFieldDropdown`, `PaymentLink.UpdateParamsCustomFieldNumeric`, and `PaymentLink.UpdateParamsCustomFieldText`
* Add support for new values `billie` and `satispay` on enums `PaymentLink.CreateParams.payment_method_types`, `PaymentLink.UpdateParams.payment_method_types`, and `PaymentLink.payment_method_types`
* Add support for `nz_bank_transfer` on `Refund.DestinationDetail`
* Add support for new value `canceled` on enum `Review.closed_reason`
* Add support for `current_period_end` and `current_period_start` on `SubscriptionItem`
* Add support for `wifi` on `TerminalConfiguration`, `terminal.Configuration.CreateParams`, and `terminal.Configuration.UpdateParams`
* Add support for new value `invoice.overpaid` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.UpdateParams.enabled_events`
* Add support for new values `2025-03-01.dashboard` and `2025-03-31.basil` on enum `WebhookEndpoint.CreateParams.api_version`
