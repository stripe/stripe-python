---
title: Remove unneeded Python resource helpers
semver_level: major
jira_tickets_closed:
- DEVSDK-1704
---

Removed the `SingletonAPIResource` and `nested_resource_class_methods` infrastructure helpers. Concrete resource methods continue to work without changes.
