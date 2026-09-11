---
title: Remove deprecated compatibility exports
pr_link: https://github.com/stripe/stripe-python/pull/1603
is_breaking: true
released_in_version: 13.0.0
---

- ⚠️ Removed deprecated module shims. They've long been available in the `stripe` module directly; now that's the only place to import them. Specifically, we removed:
  - `stripe.stripe_response`
  - `stripe.stripe_object`
  - `stripe.error_object`
  - `stripe.error`
  - `stripe.http_client`
  - `stripe.util`
  - `stripe.oauth`
  - `stripe.webhook`
  - `stripe.multipart_data_generator`
  - `stripe.request_metrics`
  - `stripe.api_resources.abstract`
  - `stripe.api_resources`


To update your code, follow this pattern:

```diff
-from stripe.<MODULE> import SomeClass
+from stripe import SomeClass

-stripe.<MODULE>.SomeClass
+stripe.SomeClass
```

- ⚠️ Removed the `FileUpload` alias

To update your code:

```diff
-from stripe import FileUpload
-from stripe.api_resources import FileUpload
+from stripe import File
```

- ⚠️ Removed the `io` import from `stripe._util`. If you had code relying on `stripe.util.io`, you'll need to import the `io` package directly yourself.
- added `UrllibClient` to `stripe` to make creating your own HTTP client easier.
