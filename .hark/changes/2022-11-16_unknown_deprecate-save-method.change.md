---
title: "Deprecate `save` method on resources (#887). Use `modify` instead."
section: Deprecated
released_in_version: 5.0.0
---

 ```python
# Before
customer = stripe.Customer.retrieve("cus_123")
customer.email = "example@test.com"
customer.save()

# After
stripe.Customer.modify("cus_123", email="example@test.com")
 ```
