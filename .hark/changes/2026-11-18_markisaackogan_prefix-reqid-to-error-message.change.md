---
title: Prefix request ID to the error message as `[req_xxx]` if a request ID exists
---

`str(error)` is now `[req_xxx] message` instead of `Request req_xxx: message`. Use `error.user_message` for the message without the prefix.
