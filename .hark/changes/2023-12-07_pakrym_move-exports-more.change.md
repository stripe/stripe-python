---
title: Move exports for more modules
pr_url: https://github.com/stripe/stripe-python/pull/1153
released_in_version: 7.8.0
---

-  `stripe.app_info`, `stripe.http_client`, `stripe.oauth`, `stripe.util`, `stripe.version`, `stripe.webhook`,  modules are deprecated. All types are available directly from `stripe` module now.
   Before:
   ```python
   from stripe.util import convert_to_stripe_object
   # or
   stripe.util.convert_to_stripe_object
   ````
   After:
   ```python
   from stripe import convert_to_stripe_object
   # or
   stripe.convert_to_stripe_object
   ```
- `stripe.api_version`, `stripe.multipart_data_generator`, `stripe.request_metrics` are deprecated and will be fully removed in the future.
