---
title: migrate from `setup.py` to `pyproject.toml`
pr_link: https://github.com/stripe/stripe-python/pull/1572
is_breaking: true
released_in_version: 13.0.0
---

- ⚠️ The package has swapped from `setup.py` to `pyproject.toml`. As a result, we're dropping support for `pip < 10.0.0` (released April 2018).
- Additionally, we're no longer shipping tests or examples in our sdist now, which should offer a small size reduction for the package if installed without the wheel (approx. 2.5MB unzipped)
