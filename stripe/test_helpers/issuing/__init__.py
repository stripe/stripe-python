# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.test_helpers.issuing._authorization_service import (
        AuthorizationService as AuthorizationService,
    )
    from stripe.test_helpers.issuing._card_service import (
        CardService as CardService,
    )
    from stripe.test_helpers.issuing._personalization_design_service import (
        PersonalizationDesignService as PersonalizationDesignService,
    )
    from stripe.test_helpers.issuing._transaction_service import (
        TransactionService as TransactionService,
    )

_submodules = {
    "AuthorizationService": "stripe.test_helpers.issuing._authorization_service",
    "CardService": "stripe.test_helpers.issuing._card_service",
    "PersonalizationDesignService": "stripe.test_helpers.issuing._personalization_design_service",
    "TransactionService": "stripe.test_helpers.issuing._transaction_service",
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
