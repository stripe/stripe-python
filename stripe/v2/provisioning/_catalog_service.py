# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.provisioning.catalog._provider_service import (
        ProviderService,
    )
    from stripe.v2.provisioning.catalog._service_service import ServiceService

_subservices = {
    "providers": [
        "stripe.v2.provisioning.catalog._provider_service",
        "ProviderService",
    ],
    "services": [
        "stripe.v2.provisioning.catalog._service_service",
        "ServiceService",
    ],
}


class CatalogService(StripeService):
    providers: "ProviderService"
    services: "ServiceService"

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
