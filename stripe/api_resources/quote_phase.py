# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.quote_phase package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.quote_phase import QuotePhase
    To:
      from stripe import QuotePhase
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._quote_phase import (  # noqa
        QuotePhase,
    )
