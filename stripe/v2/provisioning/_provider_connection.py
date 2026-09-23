# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ProviderConnection(StripeObject):
    """
    A ProviderConnection represents a link between a project and a provider account that
    resources can be created against; unlinking it prevents further resource creation.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.provider_connection"]] = (
        "v2.provisioning.provider_connection"
    )

    class ProviderAccountDetails(StripeObject):
        class ActiveService(StripeObject):
            display_name: Optional[str]
            """
            Display name of the service.
            """
            provider_resource_id: Optional[str]
            """
            Identifier of the resource at the provider that backs this service, if any.
            """
            service_id: str
            """
            Identifier of the service at the provider.
            """
            status: Literal["active", "inactive", "pending"]
            """
            Current status of the service.
            """

        active_services: List[ActiveService]
        """
        Services active for the connected account.
        """
        active_services_provided: bool
        """
        True when the provider explicitly supplied active_services, including an empty array.
        """
        display_name: Optional[str]
        """
        Display name of the connected account.
        """
        id: str
        """
        Identifier of the connected account at the provider.
        """
        link_action: Optional[Literal["created", "linked_existing"]]
        """
        Action taken when the account was linked.
        """
        primary_email: Optional[str]
        """
        Primary email address of the connected account.
        """
        _inner_class_types = {"active_services": ActiveService}

    created: Optional[str]
    """
    Time at which the provider connection was created.
    """
    id: str
    """
    Unique identifier for the provider connection.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.provisioning.provider_connection"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    provider: str
    """
    Identifier of the provider this connection is linked to.
    """
    provider_account: Optional[str]
    """
    Identifier of the connected account at the provider, if one has been established.
    """
    provider_account_details: Optional[ProviderAccountDetails]
    """
    Details about the connected provider account.
    """
    status: Literal["active", "expired", "unknown"]
    """
    Current status of the provider connection.
    """
    _inner_class_types = {"provider_account_details": ProviderAccountDetails}
