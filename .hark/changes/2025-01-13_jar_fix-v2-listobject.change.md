---
title: Fix V2 ListObject.data type hint
pr_link: https://github.com/stripe/stripe-python/pull/1442
released_in_version: 11.6.0
---

- Change `stripe.v2.ListObject.data` type hint from `List[StripeObject]` to `List[T]` where T is the specific stripe object contained within the list
