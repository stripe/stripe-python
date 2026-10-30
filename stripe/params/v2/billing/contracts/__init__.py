# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing.contracts import (
        pricing_lines as pricing_lines,
        terms as terms,
    )
    from stripe.params.v2.billing.contracts._term_list_contract_terms_params import (
        TermListContractTermsParams as TermListContractTermsParams,
    )
    from stripe.params.v2.billing.contracts._term_retrieve_contract_term_params import (
        TermRetrieveContractTermParams as TermRetrieveContractTermParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "pricing_lines": (
        "stripe.params.v2.billing.contracts.pricing_lines",
        True,
    ),
    "terms": ("stripe.params.v2.billing.contracts.terms", True),
    "TermListContractTermsParams": (
        "stripe.params.v2.billing.contracts._term_list_contract_terms_params",
        False,
    ),
    "TermRetrieveContractTermParams": (
        "stripe.params.v2.billing.contracts._term_retrieve_contract_term_params",
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
