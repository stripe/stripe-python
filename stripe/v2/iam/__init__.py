# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.iam._activity_log import ActivityLog as ActivityLog
    from stripe.v2.iam._activity_log_service import (
        ActivityLogService as ActivityLogService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ActivityLog": ("stripe.v2.iam._activity_log", False),
    "ActivityLogService": ("stripe.v2.iam._activity_log_service", False),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
