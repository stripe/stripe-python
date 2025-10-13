# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.entitlements._active_entitlement import (
        ActiveEntitlement as ActiveEntitlement,
    )
    from stripe.entitlements._active_entitlement_service import (
        ActiveEntitlementService as ActiveEntitlementService,
    )
    from stripe.entitlements._active_entitlement_summary import (
        ActiveEntitlementSummary as ActiveEntitlementSummary,
    )
    from stripe.entitlements._feature import Feature as Feature
    from stripe.entitlements._feature_service import (
        FeatureService as FeatureService,
    )

_submodules = {
    "ActiveEntitlement": "stripe.entitlements._active_entitlement",
    "ActiveEntitlementService": "stripe.entitlements._active_entitlement_service",
    "ActiveEntitlementSummary": "stripe.entitlements._active_entitlement_summary",
    "Feature": "stripe.entitlements._feature",
    "FeatureService": "stripe.entitlements._feature_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
