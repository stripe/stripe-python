# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.platform_tax_fee package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.platform_tax_fee import PlatformTaxFee
    To:
      from stripe import PlatformTaxFee
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._platform_tax_fee import (  # noqa
        PlatformTaxFee,
    )
