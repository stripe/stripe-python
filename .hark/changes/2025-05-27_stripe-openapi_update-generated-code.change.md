---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1517
is_stripe_api_change: true
released_in_version: 12.2.0
---

* Add support for `attach_payment` method on resource `Invoice`
* Add support for `collect_inputs` method on resource `terminal.Reader`
* Add support for `succeed_input_collection` and `timeout_input_collection` test helper methods on resource `terminal.Reader`
* Add support for `pix_payments` on `Account.Capability`, `Account.CreateParamsCapability`, and `Account.ModifyParamsCapability`
* Add support for `disputes_list` and `payment_disputes` on `AccountSession.Component` and `AccountSession.CreateParamsComponent`
* Add support for `refund_and_dispute_prefunding` on `Balance`
* Add support for `balance_type` on `BalanceTransaction`
* Change `billing.Alert.CreateParamsUsageThreshold.meter` to be required
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Affirm` and `Charge.PaymentMethodDetail.WechatPay`
* Add support for `payment_method_remove` on `checkout.Session.CreateParamsSavedPaymentMethodOption`
* Add support for `setup_future_usage` on `Checkout.Session.PaymentMethodOption.NaverPay`
* Change `ConfirmationToken.PaymentMethodPreview.NaverPay.buyer_id` and `PaymentMethod.NaverPay.buyer_id` to be required
* Add support for `post_payment_amount` and `pre_payment_amount` on `CreditNote`
* Add support for new value `mixed` on enum `CreditNote.type`
* Add support for new value `invoice_payment.paid` on enum `Event.type`
* Add support for `sex`, `unparsed_place_of_birth`, and `unparsed_sex` on `Identity.VerificationReport.Document` and `Identity.VerificationSession.VerifiedOutput`
* Add support for `billing_thresholds` on `Invoice.CreatePreviewParamsScheduleDetailPhaseItem`, `Invoice.CreatePreviewParamsScheduleDetailPhase`, `Invoice.CreatePreviewParamsSubscriptionDetailItem`, `Subscription.CreateParamsItem`, `Subscription.CreateParams`, `Subscription.ModifyParamsItem`, `Subscription.ModifyParams`, `SubscriptionItem.CreateParams`, `SubscriptionItem.ModifyParams`, `SubscriptionItem`, `SubscriptionSchedule.CreateParamsDefaultSetting`, `SubscriptionSchedule.CreateParamsPhaseItem`, `SubscriptionSchedule.CreateParamsPhase`, `SubscriptionSchedule.DefaultSetting`, `SubscriptionSchedule.ModifyParamsDefaultSetting`, `SubscriptionSchedule.ModifyParamsPhaseItem`, `SubscriptionSchedule.ModifyParamsPhase`, `SubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase`, and `Subscription`
* Add support for `satispay` on `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.ModifyParamsPaymentMethodOption`, and `PaymentIntent.PaymentMethodOption`
* Add support for `capture_method` on `PaymentIntent.PaymentMethodOption.Billie`
* Add support for `kakao_pay`, `kr_card`, `naver_pay`, `payco`, and `samsung_pay` on `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.ModifyParams`, and `PaymentMethodConfiguration`
* Add support for `network_decline_code` on `Refund.DestinationDetail.Paypal`
* Add support for `metadata` on `Tax.CalculationLineItem` and `tax.Calculation.CreateParamsLineItem`
* Add support for new value `simulated_stripe_s700` on enums `Terminal.Reader.device_type` and `terminal.Reader.ListParams.device_type`
* Add support for `return_url` on `Terminal.Reader.Action.ProcessPaymentIntent.ProcessConfig` and `terminal.Reader.ProcessPaymentIntentParamsProcessConfig`
* Add support for `collect_inputs` on `Terminal.Reader.Action`
* Add support for new value `collect_inputs` on enum `Terminal.Reader.Action.type`
* Add support for new value `invoice_payment.paid` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.ModifyParams.enabled_events`
* Add support for new value `2025-05-28.basil` on enum `WebhookEndpoint.CreateParams.api_version`
* Add support for snapshot event `invoice_payment.paid` with resource `InvoicePayment`
* Add support for error code `forwarding_api_upstream_error` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
