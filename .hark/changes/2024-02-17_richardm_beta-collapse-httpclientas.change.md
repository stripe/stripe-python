---
title: "Beta: Collapse HTTPClientAsync into HTTPClient"
pr_url: https://github.com/stripe/stripe-python/pull/1239
is_breaking: true
released_in_version: 8.5.0b1
---

* ⚠️ Removes the `stripe.default_http_client_async` global and the `stripe.HTTPClientAsync` class.
  * To set your own async-enabled http client, set `stripe.default_http_client` to a subclass of `stripe.HTTPClient` such as `stripe.HTTPXClient` that implements `.request_async`, `.sleep_async`, `.request_stream_async`, and `.close_async`.
  * The default http client of the library is still `RequestsClient` for synchronous methods, that "falls back" to a `HTTPXClient` when asynchronous methods are called.
