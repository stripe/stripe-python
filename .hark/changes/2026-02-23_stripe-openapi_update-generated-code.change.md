---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1735
is_stripe_api_change: true
released_in_version: 14.5.0a1
---

* Add support for new resource `AccountSignals`
* Add support for `retrieve` method on resource `AccountSignals`
* Add support for `aggregation_period`, `group_by`, and `triggered_at` on `Billing.AlertTriggered`
* Add support for `external_account_collection` on `AccountLinkCreateParamsCollectionOption`
* Add support for `funding_source` on `ApplicationFee`
* Change `delegated_checkout.RequestedSessionConfirmParamsPaymentMethodDatumBillingDetailAddress.line1`, `delegated_checkout.RequestedSessionCreateParamsFulfillmentDetailAddress.line1`, `delegated_checkout.RequestedSessionCreateParamsPaymentMethodDatumBillingDetailAddress.line1`, `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetailAddress.line1`, and `delegated_checkout.RequestedSessionModifyParamsPaymentMethodDatumBillingDetailAddress.line1` to be optional
* Add support for `hosted` and `ui_mode` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
* Add support for `url` on `FinancialConnections.Session`
* Add support for `billing_cycle_anchor` on `SubscriptionCreateParamsTrialSettingEndBehavior` and `SubscriptionModifyParamsTrialSettingEndBehavior`
