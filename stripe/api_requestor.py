# -*- coding: utf-8 -*-
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_requestor package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_requestor import APIRequestor
    To:
      from stripe import APIRequestor
    """,
    DeprecationWarning,
)

if not TYPE_CHECKING:
    from stripe._api_requestor import (  # noqa
        APIRequestor,
    )
