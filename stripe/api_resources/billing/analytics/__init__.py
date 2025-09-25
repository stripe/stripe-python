# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.billing.analytics package is deprecated, please change your
    imports to import from stripe.billing.analytics directly.
    From:
      from stripe.api_resources.billing.analytics import ...
    To:
      from stripe.billing.analytics import ...
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.api_resources.billing.analytics.meter_usage import MeterUsage
    from stripe.api_resources.billing.analytics.meter_usage_row import (
        MeterUsageRow,
    )
