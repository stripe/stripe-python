---
title: Remove unneeded Python resource helpers
pr_url: https://github.com/stripe/stripe-python/pull/1922
semver_level: major
jira_tickets_closed:
- DEVSDK-1704
---

Removed the `SingletonAPIResource` and `nested_resource_class_methods` infrastructure helpers. Concrete resource methods continue to work without changes. Users who imported either helper directly should follow the v16 migration guide.
