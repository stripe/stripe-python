# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.entitlements.event package is deprecated, please change your
    imports to import from stripe.entitlements directly.
    From:
      from stripe.api_resources.entitlements.event import Event
    To:
      from stripe.entitlements import Event
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.entitlements._event import (  # noqa
        Event,
    )
