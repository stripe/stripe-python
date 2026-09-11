---
title: Update generated code.
pr_link: https://github.com/stripe/stripe-python/pull/1544
is_stripe_api_change: true
released_in_version: 12.5.0
---

* Add support for `balance_report`, `payout_details`, and `payout_reconciliation_report` on `AccountSession.Component` and `AccountSession.CreateParamsComponent`
* Add support for `name` on `BillingPortal.Configuration`, `billing_portal.Configuration.CreateParams`, and `billing_portal.Configuration.ModifyParams`
* Add support for `installments` on `Charge.PaymentMethodDetail.Alma`
* Add support for `transaction_id` on `Charge.PaymentMethodDetail.Alma`, `Charge.PaymentMethodDetail.AmazonPay`, `Charge.PaymentMethodDetail.Billie`, `Charge.PaymentMethodDetail.KakaoPay`, `Charge.PaymentMethodDetail.KrCard`, `Charge.PaymentMethodDetail.NaverPay`, `Charge.PaymentMethodDetail.Payco`, `Charge.PaymentMethodDetail.RevolutPay`, `Charge.PaymentMethodDetail.SamsungPay`, and `Charge.PaymentMethodDetail.Satispay`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Paynow`
* Add support for `amount_includes_iof` on `Checkout.Session.PaymentMethodOption.Pix`, `PaymentIntent.ConfirmParamsPaymentMethodOptionPix`, `PaymentIntent.CreateParamsPaymentMethodOptionPix`, `PaymentIntent.ModifyParamsPaymentMethodOptionPix`, `PaymentIntent.PaymentMethodOption.Pix`, and `checkout.Session.CreateParamsPaymentMethodOptionPix`
* Add support for new values `block` and `resolution` on enum `Dispute.PaymentMethodDetail.Card.case_type`
* Add support for new value `terminal_android_apk` on enums `File.ListParams.purpose` and `File.purpose`
* Add support for new value `terminal_android_apk` on enum `File.CreateParams.purpose`
* Add support for `metadata` and `period` on `Invoice.CreatePreviewParamsScheduleDetailPhaseAddInvoiceItem`, `Subscription.CreateParamsAddInvoiceItem`, `Subscription.ModifyParamsAddInvoiceItem`, `SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem`, `SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem`, and `SubscriptionSchedule.Phase.AddInvoiceItem`
* Add support for `exp_month` and `exp_year` on `issuing.Card.CreateParams`
* Add support for `excluded_payment_method_types` on `PaymentIntent.CreateParams` and `PaymentIntent`
* Add support for `payout_method` on `Payout.CreateParams` and `Payout`
* Add support for `mxn` on `Terminal.Configuration.Tipping`, `terminal.Configuration.CreateParamsTipping`, and `terminal.Configuration.ModifyParamsTipping`
* Add support for `card` on `terminal.Reader.PresentPaymentMethodParams`
* Add support for new value `card` on enum `terminal.Reader.PresentPaymentMethodParams.type`
* Add support for new value `2025-08-27.basil` on enum `WebhookEndpoint.CreateParams.api_version`
* Add support for error codes `customer_session_expired` and `india_recurring_payment_mandate_canceled` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
