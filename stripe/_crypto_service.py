# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.crypto._customer_service import CustomerService
    from stripe.crypto._onramp_session_service import OnrampSessionService
    from stripe.crypto._onramp_transaction_limits_service import (
        OnrampTransactionLimitsService,
    )

_subservices = {
    "customers": ["stripe.crypto._customer_service", "CustomerService"],
    "onramp_sessions": [
        "stripe.crypto._onramp_session_service",
        "OnrampSessionService",
    ],
    "onramp_transaction_limits": [
        "stripe.crypto._onramp_transaction_limits_service",
        "OnrampTransactionLimitsService",
    ],
}


class CryptoService(StripeService):
    customers: "CustomerService"
    onramp_sessions: "OnrampSessionService"
    onramp_transaction_limits: "OnrampTransactionLimitsService"

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
