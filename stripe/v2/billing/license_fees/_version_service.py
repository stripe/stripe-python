# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._license_fee_version import LicenseFeeVersion
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
        license_fee_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[LicenseFeeVersion]:
        """
        List all versions of a License Fee object.
        """
        return cast(
            ListObject[LicenseFeeVersion],
            self._request(
                "get",
                "/v2/billing/license_fees/{license_fee_id}/versions".format(
                    license_fee_id=sanitize_id(license_fee_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        license_fee_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[LicenseFeeVersion]:
        """
        List all versions of a License Fee object.
        """
        return cast(
            ListObject[LicenseFeeVersion],
            await self._request_async(
                "get",
                "/v2/billing/license_fees/{license_fee_id}/versions".format(
                    license_fee_id=sanitize_id(license_fee_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        license_fee_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFeeVersion:
        """
        Retrieve a License Fee Version object.
        """
        return cast(
            LicenseFeeVersion,
            self._request(
                "get",
                "/v2/billing/license_fees/{license_fee_id}/versions/{id}".format(
                    license_fee_id=sanitize_id(license_fee_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        license_fee_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFeeVersion:
        """
        Retrieve a License Fee Version object.
        """
        return cast(
            LicenseFeeVersion,
            await self._request_async(
                "get",
                "/v2/billing/license_fees/{license_fee_id}/versions/{id}".format(
                    license_fee_id=sanitize_id(license_fee_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
