# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._collection_setting_version import (
    CollectionSettingVersion,
)
from typing import cast
from typing_extensions import NotRequired, TypedDict


class VersionService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        collection_setting_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CollectionSettingVersion]:
        """
        List all CollectionSettingVersions by CollectionSetting ID.
        """
        return cast(
            ListObject[CollectionSettingVersion],
            self._request(
                "get",
                "/v2/billing/collection_settings/{collection_setting_id}/versions".format(
                    collection_setting_id=sanitize_id(collection_setting_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        collection_setting_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CollectionSettingVersion]:
        """
        List all CollectionSettingVersions by CollectionSetting ID.
        """
        return cast(
            ListObject[CollectionSettingVersion],
            await self._request_async(
                "get",
                "/v2/billing/collection_settings/{collection_setting_id}/versions".format(
                    collection_setting_id=sanitize_id(collection_setting_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        collection_setting_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSettingVersion:
        """
        Retrieve a CollectionSetting Version by ID.
        """
        return cast(
            CollectionSettingVersion,
            self._request(
                "get",
                "/v2/billing/collection_settings/{collection_setting_id}/versions/{id}".format(
                    collection_setting_id=sanitize_id(collection_setting_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        collection_setting_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSettingVersion:
        """
        Retrieve a CollectionSetting Version by ID.
        """
        return cast(
            CollectionSettingVersion,
            await self._request_async(
                "get",
                "/v2/billing/collection_settings/{collection_setting_id}/versions/{id}".format(
                    collection_setting_id=sanitize_id(collection_setting_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
