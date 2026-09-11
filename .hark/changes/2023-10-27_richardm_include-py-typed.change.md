---
title: Include `py.typed` and enable type annotations for the package
pr_link: https://github.com/stripe/stripe-python/pull/1104
released_in_version: 7.1.0
---

* This PR includes `py.typed` and enables inline type annotations for stripe-python package. Inline type annotations will now take precedence over Typeshed for users who use a type checker or IDE.
* See a detailed guide on the [Github Wiki](https://github.com/stripe/stripe-python/wiki/Inline-type-annotations).
