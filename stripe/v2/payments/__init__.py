# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.payments import (
        settlement_allocation_intents as settlement_allocation_intents,
    )
    from stripe.v2.payments._off_session_payment import (
        OffSessionPayment as OffSessionPayment,
    )
    from stripe.v2.payments._off_session_payment_service import (
        OffSessionPaymentService as OffSessionPaymentService,
    )
    from stripe.v2.payments._settlement_allocation_intent import (
        SettlementAllocationIntent as SettlementAllocationIntent,
    )
    from stripe.v2.payments._settlement_allocation_intent_service import (
        SettlementAllocationIntentService as SettlementAllocationIntentService,
    )
    from stripe.v2.payments._settlement_allocation_intent_split import (
        SettlementAllocationIntentSplit as SettlementAllocationIntentSplit,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "settlement_allocation_intents": (
        "stripe.v2.payments.settlement_allocation_intents",
        True,
    ),
    "OffSessionPayment": ("stripe.v2.payments._off_session_payment", False),
    "OffSessionPaymentService": (
        "stripe.v2.payments._off_session_payment_service",
        False,
    ),
    "SettlementAllocationIntent": (
        "stripe.v2.payments._settlement_allocation_intent",
        False,
    ),
    "SettlementAllocationIntentService": (
        "stripe.v2.payments._settlement_allocation_intent_service",
        False,
    ),
    "SettlementAllocationIntentSplit": (
        "stripe.v2.payments._settlement_allocation_intent_split",
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
