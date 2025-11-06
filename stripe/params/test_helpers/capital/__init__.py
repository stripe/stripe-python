# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.test_helpers.capital._financing_offer_create_params import (
        FinancingOfferCreateParams as FinancingOfferCreateParams,
    )
    from stripe.params.test_helpers.capital._financing_offer_refill_params import (
        FinancingOfferRefillParams as FinancingOfferRefillParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FinancingOfferCreateParams": (
        "stripe.params.test_helpers.capital._financing_offer_create_params",
        False,
    ),
    "FinancingOfferRefillParams": (
        "stripe.params.test_helpers.capital._financing_offer_refill_params",
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
