# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.tax.association package is deprecated, please change your
    imports to import from stripe.tax directly.
    From:
      from stripe.api_resources.tax.association import Association
    To:
      from stripe.tax import Association
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.tax._association import (  # noqa
        Association,
    )
