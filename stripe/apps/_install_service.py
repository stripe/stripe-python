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
        Returns a list of app installs. An app developer filtering by its own app with its own key sees that app's installs across the accounts that installed it. An app developer acting on a connected account through Stripe-Account and filtering by its app sees that account's installs of the app, and an embedding platform acting on a connected account sees only the installs it created there. Other callers see the installs on their own account. A live key lists live installs and a test key lists test installs; the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox.
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
        Returns a list of app installs. An app developer filtering by its own app with its own key sees that app's installs across the accounts that installed it. An app developer acting on a connected account through Stripe-Account and filtering by its app sees that account's installs of the app, and an embedding platform acting on a connected account sees only the installs it created there. Other callers see the installs on their own account. A live key lists live installs and a test key lists test installs; the key of an app's managed sandbox filtering by app lists that app's installs across every sandbox.
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
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer acting on a connected account through Stripe-Account installs or reinstalls its app there, and an embedding platform can do the same once the app's developer approves its request to embed the app. For a private app, creating an install installs the newest completed upload; when that version is already installed with nothing pending, the existing install is returned.
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
        Creates an app install. An account installs its own private app with its own key; public and testing installs are made from the Dashboard. An app developer acting on a connected account through Stripe-Account installs or reinstalls its app there, and an embedding platform can do the same once the app's developer approves its request to embed the app. For a private app, creating an install installs the newest completed upload; when that version is already installed with nothing pending, the existing install is returned.
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
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the version being installed requests. An account reauthorizes its own installs on any channel with its own key, which grants all of that access, so only give app_install_write to keys that may approve an app's access. App developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. An app developer can't grant new access. An embedding platform can grant new access only once the app's developer approves its request to embed the app. For private apps, the version being installed is the newest completed upload.
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
        Reauthorizes an app install. The installer grants the permissions, content security policy entries, and endpoints that the version being installed requests. An account reauthorizes its own installs on any channel with its own key, which grants all of that access, so only give app_install_write to keys that may approve an app's access. App developers and embedding platforms reauthorize installs on connected accounts through Stripe-Account. An app developer can't grant new access. An embedding platform can grant new access only once the app's developer approves its request to embed the app. For private apps, the version being installed is the newest completed upload.
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
