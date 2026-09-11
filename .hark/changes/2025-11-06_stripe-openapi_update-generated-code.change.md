---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1664
is_stripe_api_change: true
released_in_version: 13.3.0a1
---

* Add support for new resources `TransitBalance`, `v2.reporting.ReportRun`, `v2.reporting.Report`
* Add support for `create` and `retrieve` methods on resource `v2.reporting.ReportRun`
* Add support for `retrieve` method on resource `v2.reporting.Report`
* Add support for `create` and `refill` test helper methods on resource `capital.FinancingOffer`
* Add support for `allocated_funds` on `Charge`, `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, and `PaymentIntentModifyParams`
* Add support for thin events `V2ReportingReportRunCreatedEvent`, `V2ReportingReportRunFailedEvent`, `V2ReportingReportRunSucceededEvent`, and `V2ReportingReportRunUpdatedEvent` with related object `v2.reporting.ReportRun`
