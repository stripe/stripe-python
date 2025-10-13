# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.financial_connections._account import Account as Account
    from stripe.financial_connections._account_owner import (
        AccountOwner as AccountOwner,
    )
    from stripe.financial_connections._account_owner_service import (
        AccountOwnerService as AccountOwnerService,
    )
    from stripe.financial_connections._account_ownership import (
        AccountOwnership as AccountOwnership,
    )
    from stripe.financial_connections._account_service import (
        AccountService as AccountService,
    )
    from stripe.financial_connections._session import Session as Session
    from stripe.financial_connections._session_service import (
        SessionService as SessionService,
    )
    from stripe.financial_connections._transaction import (
        Transaction as Transaction,
    )
    from stripe.financial_connections._transaction_service import (
        TransactionService as TransactionService,
    )

_submodules = {
    "Account": "stripe.financial_connections._account",
    "AccountOwner": "stripe.financial_connections._account_owner",
    "AccountOwnerService": "stripe.financial_connections._account_owner_service",
    "AccountOwnership": "stripe.financial_connections._account_ownership",
    "AccountService": "stripe.financial_connections._account_service",
    "Session": "stripe.financial_connections._session",
    "SessionService": "stripe.financial_connections._session_service",
    "Transaction": "stripe.financial_connections._transaction",
    "TransactionService": "stripe.financial_connections._transaction_service",
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
