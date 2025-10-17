# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.core.vault._gb_bank_account import (
        GbBankAccount as GbBankAccount,
    )
    from stripe.v2.core.vault._gb_bank_account_service import (
        GbBankAccountService as GbBankAccountService,
    )
    from stripe.v2.core.vault._us_bank_account import (
        UsBankAccount as UsBankAccount,
    )
    from stripe.v2.core.vault._us_bank_account_service import (
        UsBankAccountService as UsBankAccountService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "GbBankAccount": ("stripe.v2.core.vault._gb_bank_account", False),
    "GbBankAccountService": (
        "stripe.v2.core.vault._gb_bank_account_service",
        False,
    ),
    "UsBankAccount": ("stripe.v2.core.vault._us_bank_account", False),
    "UsBankAccountService": (
        "stripe.v2.core.vault._us_bank_account_service",
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
