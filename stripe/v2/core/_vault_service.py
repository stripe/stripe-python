# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.core.vault._gb_bank_account_service import (
        GbBankAccountService,
    )
    from stripe.v2.core.vault._us_bank_account_service import (
        UsBankAccountService,
    )

_subservices = {
    "gb_bank_accounts": [
        "stripe.v2.core.vault._gb_bank_account_service",
        "GbBankAccountService",
    ],
    "us_bank_accounts": [
        "stripe.v2.core.vault._us_bank_account_service",
        "UsBankAccountService",
    ],
}


class VaultService(StripeService):
    gb_bank_accounts: "GbBankAccountService"
    us_bank_accounts: "UsBankAccountService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
