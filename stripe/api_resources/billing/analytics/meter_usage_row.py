# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.billing.analytics.meter_usage_row package is deprecated, please change your
    imports to import from stripe.billing.analytics directly.
    From:
      from stripe.api_resources.billing.analytics.meter_usage_row import MeterUsageRow
    To:
      from stripe.billing.analytics import MeterUsageRow
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing.analytics._meter_usage_row import (  # noqa
        MeterUsageRow,
    )
