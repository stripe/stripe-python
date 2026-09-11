---
title: Rename `StripeStreamResponseAsync`'s `.read()` to `read_async()` for consistency
pr_link: https://github.com/stripe/stripe-python/pull/1474
is_breaking: true
section: ⚠️ Other Breaking changes in the SDK
released_in_version: 12.0.0
---

* Rename `StripeStreamResponseAsync.read()` to `.read_async()`
  * This brings the method name in line with the conventions used by every other async method in the package, ensuring consistent `async` usage.
  * You'll need to update your code if you call `Quote.pdf_async().read()` method. A typechecker will alert you to this change.
