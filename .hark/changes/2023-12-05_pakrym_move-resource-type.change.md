---
title: Move resource type exports to stripe.___
pr_link: https://github.com/stripe/stripe-python/pull/1142
released_in_version: 7.8.0
---

- `stripe.error`, `stripe.stripe_object`, `stripe.api_requestor`, `stripe.stripe_response`, `stripe.request_options`, `stripe.api_resources.*`,  `stripe.api_resources.abstract.*` modules are deprecated. All types are available directly from `stripe` module now.
   Before:
   ```python
   from stripe.error import APIError
   # or
   stripe.error.APIError
   ````
   After:
   ```python
   from stripe import APIError
   # or
   stripe.APIError
   ```
