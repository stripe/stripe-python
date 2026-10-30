# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing.contracts import (
        pricing_lines as pricing_lines,
        terms as terms,
    )
    from stripe.v2.billing.contracts._pricing_lines_service import (
        PricingLinesService as PricingLinesService,
    )
    from stripe.v2.billing.contracts._term_service import (
        TermService as TermService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "pricing_lines": ("stripe.v2.billing.contracts.pricing_lines", True),
    "terms": ("stripe.v2.billing.contracts.terms", True),
    "PricingLinesService": (
        "stripe.v2.billing.contracts._pricing_lines_service",
        False,
    ),
    "TermService": ("stripe.v2.billing.contracts._term_service", False),
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
