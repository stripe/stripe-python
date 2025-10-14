# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.entitlements._active_entitlement_service import (
    ActiveEntitlementService,
)
from stripe.entitlements._feature_service import FeatureService
from importlib import import_module

_subservices = {
    "active_entitlements": ["stripe._account_service", "AccountService"],
    "features": ["stripe._account_service", "AccountService"],
}


class EntitlementsService(StripeService):
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
