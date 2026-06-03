# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing.contracts import license_pricing as license_pricing
    from stripe.v2.billing.contracts._license_pricing_service import (
        LicensePricingService as LicensePricingService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "license_pricing": ("stripe.v2.billing.contracts.license_pricing", True),
    "LicensePricingService": (
        "stripe.v2.billing.contracts._license_pricing_service",
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
