# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.product_catalog._trial_offer import TrialOffer as TrialOffer
    from stripe.product_catalog._trial_offer_service import (
        TrialOfferService as TrialOfferService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "TrialOffer": ("stripe.product_catalog._trial_offer", False),
    "TrialOfferService": (
        "stripe.product_catalog._trial_offer_service",
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
