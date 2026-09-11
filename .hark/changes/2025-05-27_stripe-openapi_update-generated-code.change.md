---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1509
is_stripe_api_change: true
released_in_version: 12.3.0b1
---

### Breaking changes
* Remove support for deprecated previews
  * Remove support for resources `billing.MeterErrorReport`, `gift_cards.Card`, `gift_cards.Transaction`, and `privacy.RedactionJobRootObjects`
  * Remove support for `create`, `list`, `modify`, `retrieve`, and `validate` methods on resource `gift_cards.Card`
  * Remove support for `cancel`, `confirm`, `create`, `list`, `modify`, and `retrieve` methods on resource `gift_cards.Transaction`
  * Remove support for `provisioning` on `Product.CreateParams` and `Product`
  * Remove support for snapshot event `billing.meter_error_report.triggered` with resource `billing.MeterErrorReport`
  * Remove support for error codes `gift_card_balance_insufficient`, `gift_card_code_exists`, and `gift_card_inactive` on `QuotePreviewInvoice.LastFinalizationError` and `StripeError`
* Remove support for values `credits_attributed_to_debits` and `legacy_prorations` from enums `Invoice.CreatePreviewParamsScheduleDetail.billing_mode`, `Invoice.CreatePreviewParamsSubscriptionDetail.billing_mode`, `Quote.CreateParamsSubscriptionDatum.billing_mode`, `Quote.SubscriptionDatum.billing_mode`, `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.CreateParams.billing_mode`, `Subscription.billing_mode`, `SubscriptionSchedule.CreateParams.billing_mode`, `SubscriptionSchedule.billing_mode`, and `checkout.Session.CreateParamsSubscriptionDatum.billing_mode`
* Change type of `checkout.Session.ModifyParamsLineItem.quantity` from `emptyable(longInteger)` to `longInteger`
* Change `CreditNote.post_payment_amount` to be required
* Change `CreditNote.pre_payment_amount` to be required
* Remove support for `credits` on `Order.CreateParams`, `Order.ModifyParams`, and `Order`
* Remove support for `amount_remaining` on `Order`
* Remove support for `amount_credit` on `Order.TotalDetail`
* Change type of `PaymentAttemptRecord.metadata` and `PaymentRecord.metadata` from `nullable(map(string: string))` to `map(string: string)`
* Remove support for `async_workflows` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.DecrementAuthorizationParams`, `PaymentIntent.IncrementAuthorizationParams`, `PaymentIntent.ModifyParams`, and `PaymentIntent`
* Change type of `PaymentRecord.ReportPaymentAttemptCanceledParams.metadata`, `PaymentRecord.ReportPaymentAttemptFailedParams.metadata`, `PaymentRecord.ReportPaymentAttemptGuaranteedParams.metadata`, `PaymentRecord.ReportPaymentAttemptParams.metadata`, and `PaymentRecord.ReportPaymentParams.metadata` from `map(string: string)` to `emptyable(map(string: string))`
* Change type of `Privacy.RedactionJob.objects` from `$Privacy.RedactionJobRootObjects` to `RedactionResourceRootObjects`
* Change type of `Privacy.RedactionJob.status` from `string` to `enum`
* Change type of `Privacy.RedactionJob.validation_behavior` from `string` to `enum('error'|'fix')`
* Change type of `Privacy.RedactionJobValidationError.code` from `string` to `enum`
* Change type of `Privacy.RedactionJobValidationError.erroring_object` from `map(string: string)` to `RedactionResourceErroringObject`
* Remove support for `status_details` and `status` on `Tax.Association`

### Other changes
* Add support for `migrate` method on resource `Subscription`
* Add support for `distance`, `pickup_location_name`, `return_location_name`, and `vehicle_identification_number` on `Charge.CaptureParamsPaymentDetailCarRental`, `Charge.ModifyParamsPaymentDetailCarRental`, `PaymentIntent.CaptureParamsPaymentDetailCarRental`, `PaymentIntent.ConfirmParamsPaymentDetailCarRental`, `PaymentIntent.CreateParamsPaymentDetailCarRental`, `PaymentIntent.ModifyParamsPaymentDetailCarRental`, and `PaymentIntent.PaymentDetail.CarRental`
* Add support for `driver_identification_number` and `driver_tax_number` on `Charge.CaptureParamsPaymentDetailCarRentalDriver`, `Charge.ModifyParamsPaymentDetailCarRentalDriver`, `PaymentIntent.CaptureParamsPaymentDetailCarRentalDriver`, `PaymentIntent.ConfirmParamsPaymentDetailCarRentalDriver`, `PaymentIntent.CreateParamsPaymentDetailCarRentalDriver`, `PaymentIntent.ModifyParamsPaymentDetailCarRentalDriver`, and `PaymentIntent.PaymentDetail.CarRental.Driver`
* Add support for new values `classic` and `flexible` on enums `Invoice.CreatePreviewParamsScheduleDetail.billing_mode`, `Invoice.CreatePreviewParamsSubscriptionDetail.billing_mode`, `Quote.CreateParamsSubscriptionDatum.billing_mode`, `Quote.SubscriptionDatum.billing_mode`, `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.CreateParams.billing_mode`, `Subscription.billing_mode`, `SubscriptionSchedule.CreateParams.billing_mode`, `SubscriptionSchedule.billing_mode`, and `checkout.Session.CreateParamsSubscriptionDatum.billing_mode`
* Add support for `institution` on `FinancialConnections.Account`
* Add support for `countries` on `FinancialConnections.Institution`
* Change type of `Invoice.CreatePreviewParamsSubscriptionDetail.cancel_at`, `Subscription.CreateParams.cancel_at`, and `Subscription.ModifyParams.cancel_at` from `DateTime` to `DateTime | enum('max_period_end'|'min_period_end')`
* Add support for `location` and `reader` on `PaymentAttemptRecord.PaymentMethodDetail.Affirm`, `PaymentAttemptRecord.PaymentMethodDetail.WechatPay`, `PaymentRecord.PaymentMethodDetail.Affirm`, and `PaymentRecord.PaymentMethodDetail.WechatPay`
* Add support for `hooks` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.DecrementAuthorizationParams`, `PaymentIntent.IncrementAuthorizationParams`, `PaymentIntent.ModifyParams`, and `PaymentIntent`
* Add support for `card_present` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption`
* Add support for `livemode` on `Privacy.RedactionJob`
* Add support for `billing_thresholds` on `QuotePreviewSubscriptionSchedule.DefaultSetting`, `QuotePreviewSubscriptionSchedule.Phase.Item`, and `QuotePreviewSubscriptionSchedule.Phase`
* Add support for `billing_mode_details` on `Subscription`
* Add support for `tax_transaction_attempts` on `Tax.Association`
* Add support for `confirm_config` on `Terminal.Reader.Action.ConfirmPaymentIntent` and `terminal.Reader.ConfirmPaymentIntentParams`  
* Add support for error code `forwarding_api_upstream_error` on `QuotePreviewInvoice.LastFinalizationError`
