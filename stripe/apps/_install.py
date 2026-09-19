# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Install(StripeObject):
    """
    An object representing an app installation.
    """

    OBJECT_NAME: ClassVar[Literal["apps.install"]] = "apps.install"

    class AuthorizedContentSecurityPolicy(StripeObject):
        connect_src: Optional[List[str]]
        image_src: Optional[List[str]]
        purpose: Optional[str]

    class ContentSecurityPolicyGranted(StripeObject):
        connect_src: List[str]
        image_src: List[str]

    class ContentSecurityPolicyPending(StripeObject):
        connect_src: List[str]
        image_src: List[str]

    account: str
    """
    The ID of the account that the app install belongs to.
    """
    app: str
    """
    The ID of the app installed.
    """
    approval_required: bool
    """
    Whether the installer must authorize pending permissions, content security policy entries, or endpoints.
    """
    auth_code: Optional[str]
    """
    The authorization code for an oauth app install.
    """
    authorized_content_security_policy: AuthorizedContentSecurityPolicy
    authorized_endpoints: List[str]
    """
    The endpoint URLs authorized by the installer.
    """
    authorized_permissions: List[str]
    """
    The permissions authorized by the installer.
    """
    channel: str
    """
    The distribution channel associated with the app install.
    """
    content_security_policy_granted: Optional[ContentSecurityPolicyGranted]
    """
    The content security policy entries authorized by the installer.
    """
    content_security_policy_pending: ContentSecurityPolicyPending
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: Optional[str]
    """
    The ID of the embedding platform that created the install, if applicable.
    """
    endpoints_granted: Optional[List[str]]
    """
    The endpoint URLs authorized by the installer.
    """
    endpoints_pending: List[str]
    """
    The endpoint URLs requested by the latest app version that the installer has not authorized.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["apps.install"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    permissions_granted: Optional[List[str]]
    """
    The permissions authorized by the installer.
    """
    permissions_pending: List[str]
    """
    The permissions requested by the latest app version that the installer has not authorized.
    """
    state: str
    """
    The status of the app install.
    """
    status: Optional[
        Union[
            Literal[
                "install_failed",
                "installed",
                "installing",
                "uninstall_failed",
                "uninstalling",
            ],
            str,
        ]
    ]
    """
    The status of the app install.
    """
    _inner_class_types = {
        "authorized_content_security_policy": AuthorizedContentSecurityPolicy,
        "content_security_policy_granted": ContentSecurityPolicyGranted,
        "content_security_policy_pending": ContentSecurityPolicyPending,
    }
