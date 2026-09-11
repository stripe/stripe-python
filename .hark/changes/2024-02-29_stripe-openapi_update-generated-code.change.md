---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1255
is_stripe_api_change: true
released_in_version: 8.5.0
---

* Change `identity.VerificationReport.type` to be required
* Change type of `identity.VerificationSession.type` from `Optional[Literal["document", "id_number"]]` to `Literal["document", "id_number"]`
* Add support for `number` on `Invoice.CreateParams` and `Invoice.ModifyParams`
* Add support for `enable_customer_cancellation` on `terminal.Reader.Action.ProcessPaymentIntent.process_config`, `Terminal.Reader.Action.ProcessSetupIntent.process_config`, `Terminal.Reader.ProcessPaymentIntentParams.process_config`, and `Terminal.Reader.ProcessSetupIntentParams.process_config`
* Add support for `refund_payment_config` on `Terminal.Reader.Action.refund_payment` and `Terminal.Reader.RefundPaymentParams`
* Add support for `payment_method` on `Token.CreateParams.bank_account`
* Add `list_refunds` and `retrieve_refund` methods on resource `Charge`.
