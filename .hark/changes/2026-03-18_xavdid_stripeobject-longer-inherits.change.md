---
title: "`StripeObject` no longer inherits from `dict`"
pr_link: https://github.com/stripe/stripe-python/pull/1762
is_breaking: true
released_in_version: 15.0.0
---

- `StripeObject` no longer inherits from `dict`, so any `dict` methods will no longer exist, including `.get()` and notably, `.items()`.
  - For convenience, it's still possible to check key presence with `'some_key' in some_obj`. To replicate `.get()` behavior, use `getattr(obj, 'some_key', None)` for now. We've got some improvements around accessing properties that may not be present planned, but `getattr` works for now.
  - `.update()` has been retained for easier interaction with `metadata`, but it's not really intended for use on full objects.
  - Equality between `StripeObject`s still works: it checks for equality between the same class and underlying data.
- To access the underlying data as a `dict`, call `some_obj.to_dict()`, which recursively dumps all stripe-provided classes into native Python types. This is a read-only view; changes to the output of `to_dict()` won't affect the original object.
- Write operations can still be done with dot notation (`some_obj.val = 123`) or bracket notation (`some_obj["val"] = 123`). Do that instead of trying to interact with the underlying data store, as the implementation is considered private and may change without warning in the future.
