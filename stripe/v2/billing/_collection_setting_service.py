# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._collection_setting_create_params import (
        CollectionSettingCreateParams,
    )
    from stripe.params.v2.billing._collection_setting_list_params import (
        CollectionSettingListParams,
    )
    from stripe.params.v2.billing._collection_setting_retrieve_params import (
        CollectionSettingRetrieveParams,
    )
    from stripe.params.v2.billing._collection_setting_update_params import (
        CollectionSettingUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._collection_setting import CollectionSetting
    from stripe.v2.billing.collection_settings._version_service import (
        VersionService,
    )

_subservices = {
    "versions": [
        "stripe.v2.billing.collection_settings._version_service",
        "VersionService",
    ],
}


class CollectionSettingService(StripeService):
    versions: "VersionService"

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

    def list(
        self,
        params: Optional["CollectionSettingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CollectionSetting]":
        """
        List all CollectionSetting objects.
        """
        return cast(
            "ListObject[CollectionSetting]",
            self._request(
                "get",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["CollectionSettingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CollectionSetting]":
        """
        List all CollectionSetting objects.
        """
        return cast(
            "ListObject[CollectionSetting]",
            await self._request_async(
                "get",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: Optional["CollectionSettingCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Create a CollectionSetting object.
        """
        return cast(
            "CollectionSetting",
            self._request(
                "post",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["CollectionSettingCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Create a CollectionSetting object.
        """
        return cast(
            "CollectionSetting",
            await self._request_async(
                "post",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["CollectionSettingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Retrieve a CollectionSetting by ID.
        """
        return cast(
            "CollectionSetting",
            self._request(
                "get",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["CollectionSettingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Retrieve a CollectionSetting by ID.
        """
        return cast(
            "CollectionSetting",
            await self._request_async(
                "get",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["CollectionSettingUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Update fields on an existing CollectionSetting.
        """
        return cast(
            "CollectionSetting",
            self._request(
                "post",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["CollectionSettingUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSetting":
        """
        Update fields on an existing CollectionSetting.
        """
        return cast(
            "CollectionSetting",
            await self._request_async(
                "post",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
