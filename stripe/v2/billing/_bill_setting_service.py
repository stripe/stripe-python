# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._bill_setting import BillSetting
from stripe.v2.billing.bill_settings._version_service import VersionService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing._bill_setting_create_params import (
        BillSettingCreateParams,
    )
    from stripe.params.v2.billing._bill_setting_list_params import (
        BillSettingListParams,
    )
    from stripe.params.v2.billing._bill_setting_retrieve_params import (
        BillSettingRetrieveParams,
    )
    from stripe.params.v2.billing._bill_setting_update_params import (
        BillSettingUpdateParams,
    )


class BillSettingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.versions = VersionService(self._requestor)

    def list(
        self,
        params: Optional["BillSettingListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[BillSetting]:
        """
        List all BillSetting objects.
        """
        return cast(
            ListObject[BillSetting],
            self._request(
                "get",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["BillSettingListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[BillSetting]:
        """
        List all BillSetting objects.
        """
        return cast(
            ListObject[BillSetting],
            await self._request_async(
                "get",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: Optional["BillSettingCreateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Create a BillSetting object.
        """
        return cast(
            BillSetting,
            self._request(
                "post",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["BillSettingCreateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Create a BillSetting object.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "post",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["BillSettingRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Retrieve a BillSetting object by ID.
        """
        return cast(
            BillSetting,
            self._request(
                "get",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["BillSettingRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Retrieve a BillSetting object by ID.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "get",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["BillSettingUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Update fields on an existing BillSetting object.
        """
        return cast(
            BillSetting,
            self._request(
                "post",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["BillSettingUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> BillSetting:
        """
        Update fields on an existing BillSetting object.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "post",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
