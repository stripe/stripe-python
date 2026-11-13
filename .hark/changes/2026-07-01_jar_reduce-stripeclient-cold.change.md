---
title: Reduce StripeClient() cold start latency for serverless environments
pr_url: https://github.com/stripe/stripe-python/pull/1834
released_in_version: 15.3.1
---

- Moves HTTP library imports to module load time to better accommodate AWS Lambda and other serverless environments that have separate Init phase and Invoke phase time budgets.
