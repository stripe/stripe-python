# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_create_params import (
        CustomPricingUnitOverageRateCreateParams as CustomPricingUnitOverageRateCreateParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_delete_params import (
        CustomPricingUnitOverageRateDeleteParams as CustomPricingUnitOverageRateDeleteParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_list_params import (
        CustomPricingUnitOverageRateListParams as CustomPricingUnitOverageRateListParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_retrieve_params import (
        CustomPricingUnitOverageRateRetrieveParams as CustomPricingUnitOverageRateRetrieveParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_create_params import (
        RateCreateParams as RateCreateParams,
        RateCreateParamsCustomPricingUnitAmount as RateCreateParamsCustomPricingUnitAmount,
        RateCreateParamsTier as RateCreateParamsTier,
        RateCreateParamsTransformQuantity as RateCreateParamsTransformQuantity,
    )
    from stripe.params.v2.billing.rate_cards._rate_delete_params import (
        RateDeleteParams as RateDeleteParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_list_params import (
        RateListParams as RateListParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_retrieve_params import (
        RateRetrieveParams as RateRetrieveParams,
    )
    from stripe.params.v2.billing.rate_cards._version_list_params import (
        VersionListParams as VersionListParams,
    )
    from stripe.params.v2.billing.rate_cards._version_retrieve_params import (
        VersionRetrieveParams as VersionRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "CustomPricingUnitOverageRateCreateParams": (
        "stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_create_params",
        False,
    ),
    "CustomPricingUnitOverageRateDeleteParams": (
        "stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_delete_params",
        False,
    ),
    "CustomPricingUnitOverageRateListParams": (
        "stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_list_params",
        False,
    ),
    "CustomPricingUnitOverageRateRetrieveParams": (
        "stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_retrieve_params",
        False,
    ),
    "RateCreateParams": (
        "stripe.params.v2.billing.rate_cards._rate_create_params",
        False,
    ),
    "RateCreateParamsCustomPricingUnitAmount": (
        "stripe.params.v2.billing.rate_cards._rate_create_params",
        False,
    ),
    "RateCreateParamsTier": (
        "stripe.params.v2.billing.rate_cards._rate_create_params",
        False,
    ),
    "RateCreateParamsTransformQuantity": (
        "stripe.params.v2.billing.rate_cards._rate_create_params",
        False,
    ),
    "RateDeleteParams": (
        "stripe.params.v2.billing.rate_cards._rate_delete_params",
        False,
    ),
    "RateListParams": (
        "stripe.params.v2.billing.rate_cards._rate_list_params",
        False,
    ),
    "RateRetrieveParams": (
        "stripe.params.v2.billing.rate_cards._rate_retrieve_params",
        False,
    ),
    "VersionListParams": (
        "stripe.params.v2.billing.rate_cards._version_list_params",
        False,
    ),
    "VersionRetrieveParams": (
        "stripe.params.v2.billing.rate_cards._version_retrieve_params",
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
