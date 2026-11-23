---
title: Encode `decimal_string` values in fixed-point notation
semver_level: patch
---

- `Decimal` and `float` values for `decimal_string` fields are now sent in fixed-point notation. Previously, small and large values used exponent notation, which V2 endpoints reject: `0.00001` was sent as `"1e-05"`, `1e16` as `"1e+16"`, and `Decimal("0.0000001")` as `"1E-7"`. Now they are sent as `"0.00001"`, `"10000000000000000"`, and `"0.0000001"`.
- `Decimal` values in `StripeObject` JSON output use fixed-point notation as well.
