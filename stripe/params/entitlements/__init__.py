# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.entitlements._active_entitlement_list_params import (
        ActiveEntitlementListParams as ActiveEntitlementListParams,
    )
    from stripe.params.entitlements._active_entitlement_retrieve_params import (
        ActiveEntitlementRetrieveParams as ActiveEntitlementRetrieveParams,
    )
    from stripe.params.entitlements._feature_create_params import (
        FeatureCreateParams as FeatureCreateParams,
    )
    from stripe.params.entitlements._feature_list_params import (
        FeatureListParams as FeatureListParams,
    )
    from stripe.params.entitlements._feature_modify_params import (
        FeatureModifyParams as FeatureModifyParams,
    )
    from stripe.params.entitlements._feature_retrieve_params import (
        FeatureRetrieveParams as FeatureRetrieveParams,
    )
    from stripe.params.entitlements._feature_update_params import (
        FeatureUpdateParams as FeatureUpdateParams,
    )

_submodules = {
    "ActiveEntitlementListParams": "stripe.params.entitlements._active_entitlement_list_params",
    "ActiveEntitlementRetrieveParams": "stripe.params.entitlements._active_entitlement_retrieve_params",
    "FeatureCreateParams": "stripe.params.entitlements._feature_create_params",
    "FeatureListParams": "stripe.params.entitlements._feature_list_params",
    "FeatureModifyParams": "stripe.params.entitlements._feature_modify_params",
    "FeatureRetrieveParams": "stripe.params.entitlements._feature_retrieve_params",
    "FeatureUpdateParams": "stripe.params.entitlements._feature_update_params",
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
