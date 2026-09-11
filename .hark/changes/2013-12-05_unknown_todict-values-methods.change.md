---
title: The `to_dict` and `values` methods on resources no longer recursively convert objects to plain `dict`s.  All resources now inherit from `dict` but are functionally different in that you cannot set a value to an empty string and cannot delete items.
is_breaking: true
section: Backwards incompatible changes
released_in_version: 1.11.0
---
