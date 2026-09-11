---
title: Fix incorrect property name on `ThinEvent.related_object.type`
pr_link: https://github.com/stripe/stripe-python/pull/1471
is_breaking: true
section: ⚠️ Other Breaking changes in the SDK
released_in_version: 12.0.0
---

* Rename `ThinEvent.related_object.type_` to `ThinEvent.related_object.type`
  * This was an unintentional typo before. The property name now correctly matches the value you get back from the API
