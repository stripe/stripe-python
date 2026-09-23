# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Install(StripeObject):
    """
    An app install represents a Stripe App that is installed on an account. It reports the permissions,
    content security policy entries, and endpoints that the installing account has authorized, along with any
    that the app's latest version requests but the account has not authorized yet. Use the Install API to
    install, reauthorize, and uninstall apps, and to check the state of existing installs.
    """

    OBJECT_NAME: ClassVar[Literal["apps.install"]] = "apps.install"

    class AuthorizedContentSecurityPolicy(StripeObject):
        connect_src: Optional[List[str]]
        image_src: Optional[List[str]]
        purpose: Optional[str]

    class ContentSecurityPolicyGranted(StripeObject):
        connect_src: List[str]
        """
        The URLs that the app can make network requests to.
        """
        image_src: List[str]
        """
        The URLs that the app can load images from.
        """

    class ContentSecurityPolicyPending(StripeObject):
        connect_src: List[str]
        """
        The URLs that the app can make network requests to.
        """
        image_src: List[str]
        """
        The URLs that the app can load images from.
        """

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
    Whether the installer must authorize pending permissions, content security policy entries, or endpoints. For private apps, `approval_required` stays `false`. Install a new version from the Dashboard to grant its permissions.
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
