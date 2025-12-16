# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.reserve._release_list_params import ReleaseListParams
    from stripe.params.reserve._release_retrieve_params import (
        ReleaseRetrieveParams,
    )
    from stripe.reserve._release import Release


class ReleaseService(StripeService):
    def list(
        self,
        params: Optional["ReleaseListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Release]":
        """
        Returns a list of ReserveReleases previously created. The ReserveReleases are returned in sorted order, with the most recent ReserveReleases appearing first.
        """
        return cast(
            "ListObject[Release]",
            self._request(
                "get",
                "/v1/reserve/releases",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ReleaseListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Release]":
        """
        Returns a list of ReserveReleases previously created. The ReserveReleases are returned in sorted order, with the most recent ReserveReleases appearing first.
        """
        return cast(
            "ListObject[Release]",
            await self._request_async(
                "get",
                "/v1/reserve/releases",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ReleaseRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Release":
        """
        Retrieve a ReserveRelease.
        """
        return cast(
            "Release",
            self._request(
                "get",
                "/v1/reserve/releases/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ReleaseRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Release":
        """
        Retrieve a ReserveRelease.
        """
        return cast(
            "Release",
            await self._request_async(
                "get",
                "/v1/reserve/releases/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
