---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1643
is_stripe_api_change: true
released_in_version: 13.1.0a3
---

* Add support for new resources `delegated_checkout.RequestedSession` and `identity.BlocklistEntry`
* Add support for `confirm`, `create`, `expire`, `modify`, and `retrieve` methods on resource `delegated_checkout.RequestedSession`
* Add support for `create`, `disable`, `list`, and `retrieve` methods on resource `identity.BlocklistEntry`
* Add support for `blocked_by_entry` on `Identity.VerificationReport.Document`, `Identity.VerificationReport.Selfie`, and `identity.VerificationReportListParams`
