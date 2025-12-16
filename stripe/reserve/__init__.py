# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.reserve._hold import Hold as Hold
    from stripe.reserve._hold_service import HoldService as HoldService
    from stripe.reserve._plan import Plan as Plan
    from stripe.reserve._plan_service import PlanService as PlanService
    from stripe.reserve._release import Release as Release
    from stripe.reserve._release_service import (
        ReleaseService as ReleaseService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Hold": ("stripe.reserve._hold", False),
    "HoldService": ("stripe.reserve._hold_service", False),
    "Plan": ("stripe.reserve._plan", False),
    "PlanService": ("stripe.reserve._plan_service", False),
    "Release": ("stripe.reserve._release", False),
    "ReleaseService": ("stripe.reserve._release_service", False),
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
