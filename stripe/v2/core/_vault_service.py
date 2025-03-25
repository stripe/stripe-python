# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.core.vault._gb_bank_account_service import GbBankAccountService
from stripe.v2.core.vault._us_bank_account_service import UsBankAccountService


class VaultService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.gb_bank_accounts = GbBankAccountService(self._requestor)
        self.us_bank_accounts = UsBankAccountService(self._requestor)
