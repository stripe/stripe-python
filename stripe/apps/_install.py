# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.apps._install_create_params import InstallCreateParams
    from stripe.params.apps._install_list_params import InstallListParams
    from stripe.params.apps._install_modify_params import InstallModifyParams
    from stripe.params.apps._install_retrieve_params import (
        InstallRetrieveParams,
    )
    from stripe.params.apps._install_uninstall_params import (
        InstallUninstallParams,
    )


class Install(
    CreateableAPIResource["Install"],
    ListableAPIResource["Install"],
    UpdateableAPIResource["Install"],
):
    """
    An app install represents a Stripe App that is installed on an account. It reports the permissions,
    content security policy entries, and endpoints that the installing account has authorized, along with any
    that the app's latest version requests but the account has not authorized yet. Use the Install API to
    install, reauthorize, and uninstall apps, and to check the state of existing installs.
    """

    OBJECT_NAME: ClassVar[Literal["apps.install"]] = "apps.install"

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
    channel: Union[
        Literal["private_live", "private_test", "public", "review", "testing"],
        str,
    ]
    """
    The distribution channel associated with the app install.
    """
    content_security_policy_granted: ContentSecurityPolicyGranted
    content_security_policy_pending: ContentSecurityPolicyPending
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: Optional[str]
    """
    The ID of the embedding platform that created the install, if applicable.
    """
    endpoints_granted: List[str]
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
    permissions_granted: List[str]
    """
    The permissions authorized by the installer.
    """
    permissions_pending: List[str]
    """
    The permissions requested by the latest app version that the installer has not authorized.
    """
    status: Union[
        Literal[
            "install_failed",
            "installed",
            "installing",
            "uninstall_failed",
            "uninstalling",
        ],
        str,
    ]
    """
    The status of the app install.
    """

    @classmethod
    def create(cls, **params: Unpack["InstallCreateParams"]) -> "Install":
        """
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer or embedding platform acting on a connected account through Stripe-Account installs or reinstalls its app there. Creating an install for a private app that is already installed at the channel's current version with nothing pending returns the existing install.
        """
        return cast(
            "Install",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["InstallCreateParams"]
    ) -> "Install":
        """
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer or embedding platform acting on a connected account through Stripe-Account installs or reinstalls its app there. Creating an install for a private app that is already installed at the channel's current version with nothing pending returns the existing install.
        """
        return cast(
            "Install",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["InstallListParams"]
    ) -> ListObject["Install"]:
        """
        Returns a list of app installs. An app developer or embedding platform filtering by its own app sees the installs across the accounts that installed it; other callers see the installs on their own account. The key selects the environment: a live key lists live installs, a sandbox API key lists the installs on that sandbox, and the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox. For existing accounts that still use legacy test mode, a test mode key lists legacy test mode installs.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["InstallListParams"]
    ) -> ListObject["Install"]:
        """
        Returns a list of app installs. An app developer or embedding platform filtering by its own app sees the installs across the accounts that installed it; other callers see the installs on their own account. The key selects the environment: a live key lists live installs, a sandbox API key lists the installs on that sandbox, and the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox. For existing accounts that still use legacy test mode, a test mode key lists legacy test mode installs.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["InstallModifyParams"]
    ) -> "Install":
        """
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the latest published version of the app requests. An account reauthorizes its own installs on any channel with its own key; app developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. For private apps, install a new version from the Dashboard to grant its permissions.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Install",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["InstallModifyParams"]
    ) -> "Install":
        """
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the latest published version of the app requests. An account reauthorizes its own installs on any channel with its own key; app developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. For private apps, install a new version from the Dashboard to grant its permissions.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Install",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["InstallRetrieveParams"]
    ) -> "Install":
        """
        Retrieves an app install. The installing account, the app's developer (with the keys of the account that owns the app or of the app's managed sandbox), and the embedding platform that created the install can retrieve it.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["InstallRetrieveParams"]
    ) -> "Install":
        """
        Retrieves an app install. The installing account, the app's developer (with the keys of the account that owns the app or of the app's managed sandbox), and the embedding platform that created the install can retrieve it.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_uninstall(
        cls, id: str, /, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            cls._static_request(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def uninstall(
        id: str, /, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        ...

    @overload
    def uninstall(
        self, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        ...

    @class_method_variant("_cls_uninstall")
    def uninstall(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            self._request(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_uninstall_async(
        cls, id: str, /, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            await cls._static_request_async(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def uninstall_async(
        id: str, /, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        ...

    @overload
    async def uninstall_async(
        self, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        ...

    @class_method_variant("_cls_uninstall_async")
    async def uninstall_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["InstallUninstallParams"]
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            await self._request_async(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "content_security_policy_granted": ContentSecurityPolicyGranted,
        "content_security_policy_pending": ContentSecurityPolicyPending,
    }
