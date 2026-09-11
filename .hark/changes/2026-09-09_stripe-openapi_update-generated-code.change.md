---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1901
is_stripe_api_change: true
released_in_version: 15.7.0a3
---

* Add support for `customer_tax_exemption` on `Tax.Calculation.ShippingCost.TaxBreakdown`, `Tax.CalculationLineItem.TaxBreakdown`, and `Tax.Transaction.ShippingCost.TaxBreakdown`
* Add support for new value `data_share_only` on enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, and `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.result`
* Add support for `backdate_start_date` on `Checkout.Session.Item.Subscription` and `checkout.SessionCreateParamsItemSubscription`
* Add support for `signals` on `Identity.VerificationReport`
* Add support for `network_response_code` on `Issuing.Authorization.RequestHistory`
* Add support for `unit_cost_precision` on `PaymentIntentAmountDetailsLineItem`, `PaymentIntentCaptureParamsAmountDetailLineItem`, `PaymentIntentConfirmParamsAmountDetailLineItem`, `PaymentIntentCreateParamsAmountDetailLineItem`, `PaymentIntentDecrementAuthorizationParamsAmountDetailLineItem`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItem`, and `PaymentIntentModifyParamsAmountDetailLineItem`
* Change `PaymentIntent.payment_record` to be required
* Add support for `active` on `product_catalog.TrialOfferListParams`
* Change `Subscription.TrialSetting.EndBehavior.billing_cycle_anchor` to be required
* Add support for new value `rtp` on enum `Treasury.FinancialAccount.FinancialAddress.supported_networks`
* Add support for new value `blik_recurring_payments` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
