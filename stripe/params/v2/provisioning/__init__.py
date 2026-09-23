# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.provisioning import catalog as catalog
    from stripe.params.v2.provisioning._eligibility_retrieve_params import (
        EligibilityRetrieveParams as EligibilityRetrieveParams,
    )
    from stripe.params.v2.provisioning._payment_method_request_create_params import (
        PaymentMethodRequestCreateParams as PaymentMethodRequestCreateParams,
        PaymentMethodRequestCreateParamsUsageLimits as PaymentMethodRequestCreateParamsUsageLimits,
    )
    from stripe.params.v2.provisioning._payment_profile_retrieve_params import (
        PaymentProfileRetrieveParams as PaymentProfileRetrieveParams,
    )
    from stripe.params.v2.provisioning._payment_profile_update_limit_params import (
        PaymentProfileUpdateLimitParams as PaymentProfileUpdateLimitParams,
        PaymentProfileUpdateLimitParamsUsageLimits as PaymentProfileUpdateLimitParamsUsageLimits,
    )
    from stripe.params.v2.provisioning._project_create_params import (
        ProjectCreateParams as ProjectCreateParams,
    )
    from stripe.params.v2.provisioning._provider_connection_list_params import (
        ProviderConnectionListParams as ProviderConnectionListParams,
    )
    from stripe.params.v2.provisioning._provider_connection_request_create_params import (
        ProviderConnectionRequestCreateParams as ProviderConnectionRequestCreateParams,
    )
    from stripe.params.v2.provisioning._provider_connection_request_retrieve_params import (
        ProviderConnectionRequestRetrieveParams as ProviderConnectionRequestRetrieveParams,
    )
    from stripe.params.v2.provisioning._provider_connection_request_submit_information_params import (
        ProviderConnectionRequestSubmitInformationParams as ProviderConnectionRequestSubmitInformationParams,
    )
    from stripe.params.v2.provisioning._provider_connection_unlink_params import (
        ProviderConnectionUnlinkParams as ProviderConnectionUnlinkParams,
    )
    from stripe.params.v2.provisioning._resource_create_params import (
        ResourceCreateParams as ResourceCreateParams,
    )
    from stripe.params.v2.provisioning._resource_link_params import (
        ResourceLinkParams as ResourceLinkParams,
    )
    from stripe.params.v2.provisioning._resource_remove_params import (
        ResourceRemoveParams as ResourceRemoveParams,
    )
    from stripe.params.v2.provisioning._resource_retrieve_params import (
        ResourceRetrieveParams as ResourceRetrieveParams,
    )
    from stripe.params.v2.provisioning._resource_rotate_credentials_params import (
        ResourceRotateCredentialsParams as ResourceRotateCredentialsParams,
    )
    from stripe.params.v2.provisioning._resource_submit_information_params import (
        ResourceSubmitInformationParams as ResourceSubmitInformationParams,
    )
    from stripe.params.v2.provisioning._resource_unlink_params import (
        ResourceUnlinkParams as ResourceUnlinkParams,
    )
    from stripe.params.v2.provisioning._resource_update_params import (
        ResourceUpdateParams as ResourceUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "catalog": ("stripe.params.v2.provisioning.catalog", True),
    "EligibilityRetrieveParams": (
        "stripe.params.v2.provisioning._eligibility_retrieve_params",
        False,
    ),
    "PaymentMethodRequestCreateParams": (
        "stripe.params.v2.provisioning._payment_method_request_create_params",
        False,
    ),
    "PaymentMethodRequestCreateParamsUsageLimits": (
        "stripe.params.v2.provisioning._payment_method_request_create_params",
        False,
    ),
    "PaymentProfileRetrieveParams": (
        "stripe.params.v2.provisioning._payment_profile_retrieve_params",
        False,
    ),
    "PaymentProfileUpdateLimitParams": (
        "stripe.params.v2.provisioning._payment_profile_update_limit_params",
        False,
    ),
    "PaymentProfileUpdateLimitParamsUsageLimits": (
        "stripe.params.v2.provisioning._payment_profile_update_limit_params",
        False,
    ),
    "ProjectCreateParams": (
        "stripe.params.v2.provisioning._project_create_params",
        False,
    ),
    "ProviderConnectionListParams": (
        "stripe.params.v2.provisioning._provider_connection_list_params",
        False,
    ),
    "ProviderConnectionRequestCreateParams": (
        "stripe.params.v2.provisioning._provider_connection_request_create_params",
        False,
    ),
    "ProviderConnectionRequestRetrieveParams": (
        "stripe.params.v2.provisioning._provider_connection_request_retrieve_params",
        False,
    ),
    "ProviderConnectionRequestSubmitInformationParams": (
        "stripe.params.v2.provisioning._provider_connection_request_submit_information_params",
        False,
    ),
    "ProviderConnectionUnlinkParams": (
        "stripe.params.v2.provisioning._provider_connection_unlink_params",
        False,
    ),
    "ResourceCreateParams": (
        "stripe.params.v2.provisioning._resource_create_params",
        False,
    ),
    "ResourceLinkParams": (
        "stripe.params.v2.provisioning._resource_link_params",
        False,
    ),
    "ResourceRemoveParams": (
        "stripe.params.v2.provisioning._resource_remove_params",
        False,
    ),
    "ResourceRetrieveParams": (
        "stripe.params.v2.provisioning._resource_retrieve_params",
        False,
    ),
    "ResourceRotateCredentialsParams": (
        "stripe.params.v2.provisioning._resource_rotate_credentials_params",
        False,
    ),
    "ResourceSubmitInformationParams": (
        "stripe.params.v2.provisioning._resource_submit_information_params",
        False,
    ),
    "ResourceUnlinkParams": (
        "stripe.params.v2.provisioning._resource_unlink_params",
        False,
    ),
    "ResourceUpdateParams": (
        "stripe.params.v2.provisioning._resource_update_params",
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
