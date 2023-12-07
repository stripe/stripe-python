# -*- coding: utf-8 -*-
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.app_info package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.app_info import AppInfo
    To:
      from stripe import AppInfo
    """,
    DeprecationWarning,
)

if not TYPE_CHECKING:
    from stripe._app_info import (  # noqa
        AppInfo,
    )
