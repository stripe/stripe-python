# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.orchestrated_commerce._agreement import (
        Agreement as Agreement,
    )
    from stripe.v2.orchestrated_commerce._agreement_service import (
        AgreementService as AgreementService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Agreement": ("stripe.v2.orchestrated_commerce._agreement", False),
    "AgreementService": (
        "stripe.v2.orchestrated_commerce._agreement_service",
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
