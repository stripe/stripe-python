---
title: Make Stripe errors serializable
pr_url: https://github.com/stripe/stripe-python/pull/1944
semver_level: patch
jira_tickets_closed:
- RUN_DEVSDK-3443
github_issues_resolved:
- https://github.com/stripe/stripe-python/issues/1941
released_in_version: 16.1.0
---

Stripe exceptions can now be serialized and deserialized with Python `pickle` and Celery JSON result serialization without losing their type or attributes.
