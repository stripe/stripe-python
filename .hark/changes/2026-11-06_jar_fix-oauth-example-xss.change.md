---
title: Fixed reflected XSS in the OAuth example app
pr_url: https://github.com/stripe/stripe-python/pull/1970
semver_level: patch
jira_tickets_closed:
- RUN_DEVSDK-1345
---

Escaped the `OAuthError` message before including it in the HTTP response in `examples/oauth.py`'s `/oauth/callback` and `/deauthorize` routes.
