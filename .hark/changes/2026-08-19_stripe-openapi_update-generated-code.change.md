---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1875
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.6.0a2
---

* Add support for new resources `PaymentPlan` and `billing.FeedbackOption`
* ⚠️ Remove support for resource `billing.FeedbackOptions`
* Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentPlan`
* Add support for `modify` method on resource `v2.money_management.Transaction`
* Add support for `wechat_pay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
* ⚠️ Change type of `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason.feedback_options` from `$Billing.FeedbackOptions` to `$Billing.FeedbackOption`
* Change `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason.feedback_options` to be required
* Add support for `subscription_pause` on `BillingPortal.Session.Flow`
* Add support for new value `subscription_pause` on enum `BillingPortal.Session.Flow.type`
* Add support for new value `usdt` on enums `Crypto.OnrampSession.TransactionDetail.destination_currency`, `crypto.OnrampSessionCreateParams.destination_currency`, and `crypto.OnrampSessionListParams.destination_currency`
* Add support for new value `usdt` on enums `Crypto.OnrampSession.TransactionDetail.destination_currencies` and `crypto.OnrampSessionCreateParams.destination_currencies`
* Add support for `active_entitlements` on `CustomerSession.Component`
* Add support for `shared_payment_issued_token` on `delegated_checkout.RequestedSessionConfirmParams`
* Add support for new values `payment_plan.created`, `payment_plan.installment_due`, `payment_plan.installment_paid`, `payment_plan.installment_will_be_due`, and `payment_plan.updated` on enum `Event.type`
* Add support for `managed_payments` on `InvoiceCreateParams`, `InvoiceItemCreateParams`, `InvoiceItem`, `Invoice`, and `QuotePreviewInvoice`
* Add support for `payment_plan` on `Invoice`
* Add support for `estimated_fee_details` and `estimated_fee` on `Issuing.Authorization.PendingRequest.HoldAmountDetail` and `Issuing.Authorization.RequestHistory.HoldAmountDetail`
* ⚠️ Remove support for `cryptogram` on `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure` and `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure`
* ⚠️ Change type of `ProductCatalog.TrialOffer.EndBehavior.Transition.price` from `$Price` to `deletable($Price)`
* ⚠️ Change type of `Subscription.CancellationDetail.feedback_option` from `$Billing.FeedbackOptions` to `$Billing.FeedbackOption`
* Add support for `cancel_at_period_end` on `Subscription.PendingUpdate`
* Change `Subscription.CancellationDetail.feedback_option` to be required
* Add support for `igic` on `Tax.Registration.CountryOption.At`, `Tax.Registration.CountryOption.Be`, `Tax.Registration.CountryOption.Bg`, `Tax.Registration.CountryOption.Cy`, `Tax.Registration.CountryOption.Cz`, `Tax.Registration.CountryOption.De`, `Tax.Registration.CountryOption.Dk`, `Tax.Registration.CountryOption.E`, `Tax.Registration.CountryOption.Ee`, `Tax.Registration.CountryOption.Fi`, `Tax.Registration.CountryOption.Fr`, `Tax.Registration.CountryOption.Gr`, `Tax.Registration.CountryOption.Hr`, `Tax.Registration.CountryOption.Hu`, `Tax.Registration.CountryOption.Ie`, `Tax.Registration.CountryOption.It`, `Tax.Registration.CountryOption.Lt`, `Tax.Registration.CountryOption.Lu`, `Tax.Registration.CountryOption.Lv`, `Tax.Registration.CountryOption.Mt`, `Tax.Registration.CountryOption.Nl`, `Tax.Registration.CountryOption.Pl`, `Tax.Registration.CountryOption.Pt`, `Tax.Registration.CountryOption.Ro`, `Tax.Registration.CountryOption.Se`, `Tax.Registration.CountryOption.Si`, and `Tax.Registration.CountryOption.Sk`
* Add support for `metadata` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`, `V2.Billing.Contract.PricingOverride.Datum`, `V2.MoneyManagement.Transaction`, `v2.billing.ContractCreateParamsPricingOverride`, `v2.billing.ContractModifyParamsPricingLineActionUpdate`, `v2.billing.ContractModifyParamsPricingOverrideActionAdd`, `v2.billing.ContractModifyParamsPricingOverrideActionUpdate`, and `v2.billing.ContractModifyParams`
* Add support for `tax_amount` on `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee`
* Add support for `payout_method_options` on `V2.MoneyManagement.OutboundPaymentQuote.To` and `v2.money_management.OutboundPaymentQuoteCreateParamsTo`
* Change type of `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdate.metadata` from `string` to `emptyable(string)`
* Add support for snapshot events `payment_plan.created`, `payment_plan.installment_due`, `payment_plan.installment_paid`, `payment_plan.installment_will_be_due`, and `payment_plan.updated` with resource `PaymentPlan`
