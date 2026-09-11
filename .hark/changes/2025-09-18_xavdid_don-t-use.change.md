---
title: Don't use mutable default arguments
pr_link: https://github.com/stripe/stripe-python/pull/1570
released_in_version: 13.0.0
---

- Service methods now correctly set `None` as the default function argument instead of `{}`
