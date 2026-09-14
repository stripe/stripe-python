---
title: API Updates for beta branch
pr_url: https://github.com/stripe/stripe-python/pull/914
is_stripe_api_change: true
released_in_version: 5.1.0b5
---

* Updated stable APIs to the latest version
* Change `quote.draft_quote` implementation to from calling `POST /v1/quotes/{quote}/draft` to `POST /v1/quotes/{quote}/mark_draft`
* Add support for `tax.Registration` resource
