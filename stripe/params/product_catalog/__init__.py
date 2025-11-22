# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.product_catalog._trial_offer_create_params import (
        TrialOfferCreateParams as TrialOfferCreateParams,
        TrialOfferCreateParamsDuration as TrialOfferCreateParamsDuration,
        TrialOfferCreateParamsDurationRelative as TrialOfferCreateParamsDurationRelative,
        TrialOfferCreateParamsEndBehavior as TrialOfferCreateParamsEndBehavior,
        TrialOfferCreateParamsEndBehaviorTransition as TrialOfferCreateParamsEndBehaviorTransition,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "TrialOfferCreateParams": (
        "stripe.params.product_catalog._trial_offer_create_params",
        False,
    ),
    "TrialOfferCreateParamsDuration": (
        "stripe.params.product_catalog._trial_offer_create_params",
        False,
    ),
    "TrialOfferCreateParamsDurationRelative": (
        "stripe.params.product_catalog._trial_offer_create_params",
        False,
    ),
    "TrialOfferCreateParamsEndBehavior": (
        "stripe.params.product_catalog._trial_offer_create_params",
        False,
    ),
    "TrialOfferCreateParamsEndBehaviorTransition": (
        "stripe.params.product_catalog._trial_offer_create_params",
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
