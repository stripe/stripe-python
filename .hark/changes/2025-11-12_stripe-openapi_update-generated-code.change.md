---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1666
is_stripe_api_change: true
released_in_version: 13.3.0a2
---

* Remove support for resource `v2.tax.AutomaticRule`
* Remove support for `create`, `deactivate`, `find`, `modify`, and `retrieve` methods on resource `v2.tax.AutomaticRule`
* Add support for `self_reported_income` and `self_reported_monthly_housing_payment` on `AccountCreateParamsIndividual`, `AccountCreatePersonParams`, `AccountModifyParamsIndividual`, `AccountModifyPersonParams`, `Person`, `TokenCreateParamsAccountIndividual`, and `TokenCreateParamsPerson`
* Add support for new values `amendment_end`, `line_ends_at`, `schedule_end`, and `upcoming_invoice` on enums `InvoiceCreatePreviewParamsSubscriptionDetailBillingScheduleBillUntil.type`, `Subscription.BillingSchedule.BillUntil.type`, `SubscriptionCreateParamsBillingScheduleBillUntil.type`, and `SubscriptionModifyParamsBillingScheduleBillUntil.type`
* Add support for `billing_schedules` and `phase_effective_at` on `Quote.SubscriptionDataOverride`, `Quote.SubscriptionDatum`, `QuoteCreateParamsSubscriptionDataOverride`, `QuoteCreateParamsSubscriptionDatum`, `QuoteModifyParamsSubscriptionDataOverride`, and `QuoteModifyParamsSubscriptionDatum`
* Add support for `bill_from` on `Subscription.BillingSchedule`
* Add support for `amendment_end` and `line_ends_at` on `Subscription.BillingSchedule.BillUntil`
* Remove support for `data` and `related_object` on `V2.Core.Event`
