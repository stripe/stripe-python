# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.collection_settings._version_list_params import (
        VersionListParams,
    )
    from stripe.params.v2.billing.collection_settings._version_retrieve_params import (
        VersionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._collection_setting_version import (
        CollectionSettingVersion,
    )


class VersionService(StripeService):
    def list(
        self,
        collection_setting_id: str,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CollectionSettingVersion]":
        """
        List all CollectionSettingVersions by CollectionSetting ID.
        """
        return cast(
            "ListObject[CollectionSettingVersion]",
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
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CollectionSettingVersion]":
        """
        List all CollectionSettingVersions by CollectionSetting ID.
        """
        return cast(
            "ListObject[CollectionSettingVersion]",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSettingVersion":
        """
        Retrieve a CollectionSetting Version by ID.
        """
        return cast(
            "CollectionSettingVersion",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CollectionSettingVersion":
        """
        Retrieve a CollectionSetting Version by ID.
        """
        return cast(
            "CollectionSettingVersion",
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
