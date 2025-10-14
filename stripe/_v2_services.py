# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2._billing_service import BillingService
from stripe.v2._core_service import CoreService
from importlib import import_module

_subservices = {
    "billing": ["stripe._account_service", "AccountService"],
    "core": ["stripe._account_service", "AccountService"],
}


class V2Services(StripeService):
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
            raise AttributeError(f"unable to find service '{name}'")
