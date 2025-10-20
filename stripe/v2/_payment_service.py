# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.payments._off_session_payment_service import (
        OffSessionPaymentService,
    )

_subservices = {
    "off_session_payments": [
        "stripe.v2.payments._off_session_payment_service",
        "OffSessionPaymentService",
    ],
}


class PaymentService(StripeService):
    off_session_payments: "OffSessionPaymentService"

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
