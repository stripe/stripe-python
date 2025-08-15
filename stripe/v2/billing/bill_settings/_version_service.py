# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._bill_setting_version import BillSettingVersion
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
        bill_setting_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[BillSettingVersion]:
        """
        List all BillSettingVersions by BillSetting ID.
        """
        return cast(
            ListObject[BillSettingVersion],
            self._request(
                "get",
                "/v2/billing/bill_settings/{bill_setting_id}/versions".format(
                    bill_setting_id=sanitize_id(bill_setting_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        bill_setting_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[BillSettingVersion]:
        """
        List all BillSettingVersions by BillSetting ID.
        """
        return cast(
            ListObject[BillSettingVersion],
            await self._request_async(
                "get",
                "/v2/billing/bill_settings/{bill_setting_id}/versions".format(
                    bill_setting_id=sanitize_id(bill_setting_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        bill_setting_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BillSettingVersion:
        """
        Retrieve a BillSettingVersion by ID.
        """
        return cast(
            BillSettingVersion,
            self._request(
                "get",
                "/v2/billing/bill_settings/{bill_setting_id}/versions/{id}".format(
                    bill_setting_id=sanitize_id(bill_setting_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        bill_setting_id: str,
        id: str,
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BillSettingVersion:
        """
        Retrieve a BillSettingVersion by ID.
        """
        return cast(
            BillSettingVersion,
            await self._request_async(
                "get",
                "/v2/billing/bill_settings/{bill_setting_id}/versions/{id}".format(
                    bill_setting_id=sanitize_id(bill_setting_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
