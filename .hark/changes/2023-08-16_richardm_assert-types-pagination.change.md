---
title: Assert types of pagination responses
pr_url: https://github.com/stripe/stripe-python/pull/1015
is_breaking: true
released_in_version: 6.0.0
---

* Pagination will raise an exception if the API response is not of the correct type. This should never happen in production use but may break tests that use mock data.
