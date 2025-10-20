# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.pricing_plans._component_create_params import (
        ComponentCreateParams as ComponentCreateParams,
        ComponentCreateParamsLicenseFee as ComponentCreateParamsLicenseFee,
        ComponentCreateParamsRateCard as ComponentCreateParamsRateCard,
        ComponentCreateParamsServiceAction as ComponentCreateParamsServiceAction,
    )
    from stripe.params.v2.billing.pricing_plans._component_delete_params import (
        ComponentDeleteParams as ComponentDeleteParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_list_params import (
        ComponentListParams as ComponentListParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_retrieve_params import (
        ComponentRetrieveParams as ComponentRetrieveParams,
    )
    from stripe.params.v2.billing.pricing_plans._component_update_params import (
        ComponentUpdateParams as ComponentUpdateParams,
    )
    from stripe.params.v2.billing.pricing_plans._version_list_params import (
        VersionListParams as VersionListParams,
    )
    from stripe.params.v2.billing.pricing_plans._version_retrieve_params import (
        VersionRetrieveParams as VersionRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ComponentCreateParams": (
        "stripe.params.v2.billing.pricing_plans._component_create_params",
        False,
    ),
    "ComponentCreateParamsLicenseFee": (
        "stripe.params.v2.billing.pricing_plans._component_create_params",
        False,
    ),
    "ComponentCreateParamsRateCard": (
        "stripe.params.v2.billing.pricing_plans._component_create_params",
        False,
    ),
    "ComponentCreateParamsServiceAction": (
        "stripe.params.v2.billing.pricing_plans._component_create_params",
        False,
    ),
    "ComponentDeleteParams": (
        "stripe.params.v2.billing.pricing_plans._component_delete_params",
        False,
    ),
    "ComponentListParams": (
        "stripe.params.v2.billing.pricing_plans._component_list_params",
        False,
    ),
    "ComponentRetrieveParams": (
        "stripe.params.v2.billing.pricing_plans._component_retrieve_params",
        False,
    ),
    "ComponentUpdateParams": (
        "stripe.params.v2.billing.pricing_plans._component_update_params",
        False,
    ),
    "VersionListParams": (
        "stripe.params.v2.billing.pricing_plans._version_list_params",
        False,
    ),
    "VersionRetrieveParams": (
        "stripe.params.v2.billing.pricing_plans._version_retrieve_params",
        False,
    ),
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
