# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.shared_payment._granted_token_service import (
        GrantedTokenService,
    )
    from stripe.shared_payment._issued_token_service import IssuedTokenService

_subservices = {
    "granted_tokens": [
        "stripe.shared_payment._granted_token_service",
        "GrantedTokenService",
    ],
    "issued_tokens": [
        "stripe.shared_payment._issued_token_service",
        "IssuedTokenService",
    ],
}


class SharedPaymentService(StripeService):
    granted_tokens: "GrantedTokenService"
    issued_tokens: "IssuedTokenService"

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
