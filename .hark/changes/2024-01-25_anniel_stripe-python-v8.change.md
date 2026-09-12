---
title: stripe-python v8 release
pr_url: https://github.com/stripe/stripe-python/pull/1206
is_breaking: true
released_in_version: 8.0.0
---

This release introduces `StripeClient` and a service-based call pattern. This new interface allows you to easily call Stripe APIs and has several benefits over the existing resource-based pattern:

* No global config: you can simultaneously use multiple clients with different configuration options (such as API keys)
* No static methods for easier mocking

For full migration instructions, please refer to the [v8 migration guide](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient)).

"⚠️" symbol highlights breaking changes

### ⚠️ Changed
* ⚠️ **Request options like `api_key`, `stripe_account`, `stripe_version`, and `idempotency_key` can no longer be passed in positionally on resource methods. Please pass these in as keyword arguments.**

**BEFORE**
```python
stripe.Customer.create(
  "sk_test_123",  # api key
  "KG5LxwFBepaKHyUD",  # idempotency key
  "2022-11-15",  # stripe version
  "acct_123",  # stripe account
)
```

**AFTER**
```python
stripe.Customer.create(
  api_key="sk_test_123",
  idempotency_key="KG5LxwFBepaKHyUD",
  stripe_version="2022-11-15",
  stripe_account="acct_123",
)
```
* ⚠️ Methods that turn a response stream (`Quote.pdf`) now returns a single value of type `StripeResponseStream` instead of a tuple containing `(StripeResponseStream, api_key)`.
* ⚠️ Removed public access to `APIRequestor`. `APIRequestor`'s main use is internal, and we don't have a good understanding of its external use cases. We had to make several breaking changes to its interface as part of this update, so rather than leaving it public we made it private. If you have a use case for `APIRequestor`, please open up a Github issue describing it. We'd rather you rely on something specifically designed for your use case than having to reach into the library's internals.


### ⚠️ Removed
* ⚠️ Remove `api_version` from `File.create` parameters. Please use `stripe_version` instead.
* ⚠️ Remove `util.read_special_variable()` utility method (importing directly from `stripe.util` is deprecated as of [v7.8.0](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#780---2023-12-07))
* ⚠️ Remove `StripeError.construct_error_object()`. This method was intended for internal stripe-python use only.
* ⚠️ Remove `ListObject.empty_list()`. This method was intended for internal stripe-python use only.
* ⚠️ Remove `SearchResultObject.empty_search_result()`. This method was intended for internal stripe-python use only.
* ⚠️ Remove `StripeObject.ReprJSONEncoder`. This class was intended for internal stripe-python use only.
* ⚠️ Remove `StripeObject.api_base`. This property was defunct and returned `None`.
