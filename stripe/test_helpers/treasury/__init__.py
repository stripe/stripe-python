# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.test_helpers.treasury._inbound_transfer_service import (
        InboundTransferService as InboundTransferService,
    )
    from stripe.test_helpers.treasury._outbound_payment_service import (
        OutboundPaymentService as OutboundPaymentService,
    )
    from stripe.test_helpers.treasury._outbound_transfer_service import (
        OutboundTransferService as OutboundTransferService,
    )
    from stripe.test_helpers.treasury._received_credit_service import (
        ReceivedCreditService as ReceivedCreditService,
    )
    from stripe.test_helpers.treasury._received_debit_service import (
        ReceivedDebitService as ReceivedDebitService,
    )

_submodules = {
    "InboundTransferService": "stripe.test_helpers.treasury._inbound_transfer_service",
    "OutboundPaymentService": "stripe.test_helpers.treasury._outbound_payment_service",
    "OutboundTransferService": "stripe.test_helpers.treasury._outbound_transfer_service",
    "ReceivedCreditService": "stripe.test_helpers.treasury._received_credit_service",
    "ReceivedDebitService": "stripe.test_helpers.treasury._received_debit_service",
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
