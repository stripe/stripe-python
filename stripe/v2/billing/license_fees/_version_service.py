# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.license_fees._version_list_params import (
        VersionListParams,
    )
    from stripe.params.v2.billing.license_fees._version_retrieve_params import (
        VersionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._license_fee_version import LicenseFeeVersion


class VersionService(StripeService):
    def list(
        self,
        license_fee_id: str,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicenseFeeVersion]":
        """
        List all versions of a License Fee object.
        """
        return cast(
            "ListObject[LicenseFeeVersion]",
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
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicenseFeeVersion]":
        """
        List all versions of a License Fee object.
        """
        return cast(
            "ListObject[LicenseFeeVersion]",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFeeVersion":
        """
        Retrieve a License Fee Version object.
        """
        return cast(
            "LicenseFeeVersion",
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
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFeeVersion":
        """
        Retrieve a License Fee Version object.
        """
        return cast(
            "LicenseFeeVersion",
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
