# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.provisioning import (
        catalog as catalog,
        payment_profile as payment_profile,
    )
    from stripe.v2.provisioning._catalog_service import (
        CatalogService as CatalogService,
    )
    from stripe.v2.provisioning._eligibility import Eligibility as Eligibility
    from stripe.v2.provisioning._eligibility_service import (
        EligibilityService as EligibilityService,
    )
    from stripe.v2.provisioning._payment_method_request import (
        PaymentMethodRequest as PaymentMethodRequest,
    )
    from stripe.v2.provisioning._payment_method_request_service import (
        PaymentMethodRequestService as PaymentMethodRequestService,
    )
    from stripe.v2.provisioning._payment_profile import (
        PaymentProfile as PaymentProfile,
    )
    from stripe.v2.provisioning._payment_profile_service import (
        PaymentProfileService as PaymentProfileService,
    )
    from stripe.v2.provisioning._project import Project as Project
    from stripe.v2.provisioning._project_service import (
        ProjectService as ProjectService,
    )
    from stripe.v2.provisioning._provider import Provider as Provider
    from stripe.v2.provisioning._provider_connection import (
        ProviderConnection as ProviderConnection,
    )
    from stripe.v2.provisioning._provider_connection_request import (
        ProviderConnectionRequest as ProviderConnectionRequest,
    )
    from stripe.v2.provisioning._provider_connection_request_service import (
        ProviderConnectionRequestService as ProviderConnectionRequestService,
    )
    from stripe.v2.provisioning._provider_connection_service import (
        ProviderConnectionService as ProviderConnectionService,
    )
    from stripe.v2.provisioning._provider_service_detail import (
        ProviderServiceDetail as ProviderServiceDetail,
    )
    from stripe.v2.provisioning._resource import Resource as Resource
    from stripe.v2.provisioning._resource_service import (
        ResourceService as ResourceService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "catalog": ("stripe.v2.provisioning.catalog", True),
    "payment_profile": ("stripe.v2.provisioning.payment_profile", True),
    "CatalogService": ("stripe.v2.provisioning._catalog_service", False),
    "Eligibility": ("stripe.v2.provisioning._eligibility", False),
    "EligibilityService": (
        "stripe.v2.provisioning._eligibility_service",
        False,
    ),
    "PaymentMethodRequest": (
        "stripe.v2.provisioning._payment_method_request",
        False,
    ),
    "PaymentMethodRequestService": (
        "stripe.v2.provisioning._payment_method_request_service",
        False,
    ),
    "PaymentProfile": ("stripe.v2.provisioning._payment_profile", False),
    "PaymentProfileService": (
        "stripe.v2.provisioning._payment_profile_service",
        False,
    ),
    "Project": ("stripe.v2.provisioning._project", False),
    "ProjectService": ("stripe.v2.provisioning._project_service", False),
    "Provider": ("stripe.v2.provisioning._provider", False),
    "ProviderConnection": (
        "stripe.v2.provisioning._provider_connection",
        False,
    ),
    "ProviderConnectionRequest": (
        "stripe.v2.provisioning._provider_connection_request",
        False,
    ),
    "ProviderConnectionRequestService": (
        "stripe.v2.provisioning._provider_connection_request_service",
        False,
    ),
    "ProviderConnectionService": (
        "stripe.v2.provisioning._provider_connection_service",
        False,
    ),
    "ProviderServiceDetail": (
        "stripe.v2.provisioning._provider_service_detail",
        False,
    ),
    "Resource": ("stripe.v2.provisioning._resource", False),
    "ResourceService": ("stripe.v2.provisioning._resource_service", False),
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
