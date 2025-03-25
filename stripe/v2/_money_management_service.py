# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.money_management._outbound_setup_intent_service import (
    OutboundSetupIntentService,
)
from stripe.v2.money_management._payout_method_service import (
    PayoutMethodService,
)
from stripe.v2.money_management._payout_methods_bank_account_spec_service import (
    PayoutMethodsBankAccountSpecService,
)


class MoneyManagementService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.outbound_setup_intents = OutboundSetupIntentService(
            self._requestor,
        )
        self.payout_methods = PayoutMethodService(self._requestor)
        self.payout_methods_bank_account_spec = (
            PayoutMethodsBankAccountSpecService(
                self._requestor,
            )
        )
