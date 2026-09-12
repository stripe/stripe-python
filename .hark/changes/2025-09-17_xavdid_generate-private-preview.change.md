---
title: generate private-preview SDK w/ mid Sept changes
pr_url: https://github.com/stripe/stripe-python/pull/1571
is_stripe_api_change: true
released_in_version: 12.6.0a2
---

* Add support for `retrieve` method on resource `v2.core.ClaimableSandbox`
* Add support for `month_of_year` on `V2.Billing.Cadence.BillingCycle.Month` and `v2.billing.Cadence.CreateParamsBillingCycleMonth`
* Add support for `claimed_at`, `expires_at`, `sandbox_details`, and `status` on `V2.Core.ClaimableSandbox`
* Remove support for `api_keys` on `V2.Core.ClaimableSandbox`
* Change type of `V2.Core.ClaimableSandbox.claim_url` from `string` to `nullable(string)`
* Add support for new value `current_billing_period_end` on enums `V2.Billing.IntentAction.Deactivate.EffectiveAt.type` and `v2.billing.Intent.CreateParamsActionDeactivateEffectiveAt.type`
* Add support for `will_activate_at` and `will_cancel_at` on `V2.Billing.PricingPlanSubscription.ServicingStatusTransition` and `V2.Billing.RateCardSubscription.ServicingStatusTransition`
* Add support for `category` and `priority` on `V2.Billing.ServiceAction.CreditGrantPerTenant`, `V2.Billing.ServiceAction.CreditGrant`, `v2.billing.ServiceAction.CreateParamsCreditGrantPerTenant`, and `v2.billing.ServiceAction.CreateParamsCreditGrant`
* Change `v2.billing.LicenseFee.ModifyParams.display_name` to be optional
* Add support for `invoices` on `EventsV2BillingCadenceBilledEvent`
* Add support for thin events `V2CoreClaimableSandboxClaimedEvent`, `V2CoreClaimableSandboxExpiredEvent`, `V2CoreClaimableSandboxExpiringEvent`, and `V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent` with related object `V2.core.ClaimableSandbox`
* Remove support for thin event `V2BillingCadenceErroredEvent` with related object `V2.billing.Cadence`
