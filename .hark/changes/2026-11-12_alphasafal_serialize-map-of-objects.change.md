---
title: "Fix `str()`, `repr()` and `to_dict()` on objects with a map-of-objects field (e.g. `PromotionCode.restrictions.currency_options`), which raised `ValueError: Circular reference detected` or left nested objects unconverted, and stop a `null` value for such a field from breaking deserialization"
semver_level: patch
---
