---
title: Dramatically improve performance by lazily loading most imports
pr_url: https://github.com/stripe/stripe-python/pull/1645
released_in_version: 13.1.0
---

- move many type imports behind an `if TYPE_CHECKING` block
- lazily initialize subservices
- add module-level `__getattr__` functions to most `__init__.py` files
