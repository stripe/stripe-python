# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.apps._install import Install
    from stripe.params.apps._install_create_params import InstallCreateParams
    from stripe.params.apps._install_list_params import InstallListParams
    from stripe.params.apps._install_retrieve_params import (
        InstallRetrieveParams,
    )
    from stripe.params.apps._install_uninstall_params import (
        InstallUninstallParams,
    )
    from stripe.params.apps._install_update_params import InstallUpdateParams


class InstallService(StripeService):
    def list(
        self,
        params: Optional["InstallListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Install]":
        """
        Returns a list of app installs. An app developer or embedding platform filtering by its own app sees the installs across the accounts that installed it; other callers see the installs on their own account. The key selects the environment: a live key lists live installs, a sandbox API key lists the installs on that sandbox, and the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox. For existing accounts that still use legacy test mode, a test mode key lists legacy test mode installs.
        """
        return cast(
            "ListObject[Install]",
            self._request(
                "get",
                "/v1/apps/installs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["InstallListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Install]":
        """
        Returns a list of app installs. An app developer or embedding platform filtering by its own app sees the installs across the accounts that installed it; other callers see the installs on their own account. The key selects the environment: a live key lists live installs, a sandbox API key lists the installs on that sandbox, and the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox. For existing accounts that still use legacy test mode, a test mode key lists legacy test mode installs.
        """
        return cast(
            "ListObject[Install]",
            await self._request_async(
                "get",
                "/v1/apps/installs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "InstallCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer or embedding platform acting on a connected account through Stripe-Account installs or reinstalls its app there. Creating an install for a private app that is already installed at the channel's current version with nothing pending returns the existing install.
        """
        return cast(
            "Install",
            self._request(
                "post",
                "/v1/apps/installs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "InstallCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer or embedding platform acting on a connected account through Stripe-Account installs or reinstalls its app there. Creating an install for a private app that is already installed at the channel's current version with nothing pending returns the existing install.
        """
        return cast(
            "Install",
            await self._request_async(
                "post",
                "/v1/apps/installs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["InstallRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Retrieves an app install. The installing account, the app's developer (with the keys of the account that owns the app or of the app's managed sandbox), and the embedding platform that created the install can retrieve it.
        """
        return cast(
            "Install",
            self._request(
                "get",
                "/v1/apps/installs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["InstallRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Retrieves an app install. The installing account, the app's developer (with the keys of the account that owns the app or of the app's managed sandbox), and the embedding platform that created the install can retrieve it.
        """
        return cast(
            "Install",
            await self._request_async(
                "get",
                "/v1/apps/installs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["InstallUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the latest published version of the app requests. An account reauthorizes its own installs on any channel with its own key; app developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. For private apps, install a new version from the Dashboard to grant its permissions.
        """
        return cast(
            "Install",
            self._request(
                "post",
                "/v1/apps/installs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["InstallUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the latest published version of the app requests. An account reauthorizes its own installs on any channel with its own key; app developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. For private apps, install a new version from the Dashboard to grant its permissions.
        """
        return cast(
            "Install",
            await self._request_async(
                "post",
                "/v1/apps/installs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def uninstall(
        self,
        id: str,
        /,
        params: Optional["InstallUninstallParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            self._request(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def uninstall_async(
        self,
        id: str,
        /,
        params: Optional["InstallUninstallParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Install":
        """
        Uninstalls an app from the account that installed it.
        """
        return cast(
            "Install",
            await self._request_async(
                "post",
                "/v1/apps/installs/{id}/uninstall".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
