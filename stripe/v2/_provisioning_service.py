# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.provisioning._catalog_service import CatalogService
    from stripe.v2.provisioning._eligibility_service import EligibilityService
    from stripe.v2.provisioning._payment_method_request_service import (
        PaymentMethodRequestService,
    )
    from stripe.v2.provisioning._payment_profile_service import (
        PaymentProfileService,
    )
    from stripe.v2.provisioning._project_service import ProjectService
    from stripe.v2.provisioning._provider_connection_request_service import (
        ProviderConnectionRequestService,
    )
    from stripe.v2.provisioning._provider_connection_service import (
        ProviderConnectionService,
    )
    from stripe.v2.provisioning._resource_service import ResourceService

_subservices = {
    "catalog": ["stripe.v2.provisioning._catalog_service", "CatalogService"],
    "eligibility": [
        "stripe.v2.provisioning._eligibility_service",
        "EligibilityService",
    ],
    "payment_method_requests": [
        "stripe.v2.provisioning._payment_method_request_service",
        "PaymentMethodRequestService",
    ],
    "payment_profile": [
        "stripe.v2.provisioning._payment_profile_service",
        "PaymentProfileService",
    ],
    "projects": ["stripe.v2.provisioning._project_service", "ProjectService"],
    "provider_connections": [
        "stripe.v2.provisioning._provider_connection_service",
        "ProviderConnectionService",
    ],
    "provider_connection_requests": [
        "stripe.v2.provisioning._provider_connection_request_service",
        "ProviderConnectionRequestService",
    ],
    "resources": [
        "stripe.v2.provisioning._resource_service",
        "ResourceService",
    ],
}


class ProvisioningService(StripeService):
    catalog: "CatalogService"
    eligibility: "EligibilityService"
    payment_method_requests: "PaymentMethodRequestService"
    payment_profile: "PaymentProfileService"
    projects: "ProjectService"
    provider_connections: "ProviderConnectionService"
    provider_connection_requests: "ProviderConnectionRequestService"
    resources: "ResourceService"

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
