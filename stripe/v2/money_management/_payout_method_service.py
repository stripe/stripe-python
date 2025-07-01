# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._payout_method import PayoutMethod
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class PayoutMethodService(StripeService):
    class ArchiveParams(TypedDict):
        pass

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page size.
        """
        usage_status: NotRequired["PayoutMethodService.ListParamsUsageStatus"]
        """
        Usage status filter.
        """

    class ListParamsUsageStatus(TypedDict):
        payments: NotRequired[
            List[Literal["eligible", "invalid", "requires_action"]]
        ]
        """
        List of payments status to filter by.
        """
        transfers: NotRequired[
            List[Literal["eligible", "invalid", "requires_action"]]
        ]
        """
        List of transfers status to filter by.
        """

    class RetrieveParams(TypedDict):
        pass

    class UnarchiveParams(TypedDict):
        pass

    def list(
        self,
        params: "PayoutMethodService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PayoutMethod]:
        """
        List objects that adhere to the PayoutMethod interface.
        """
        return cast(
            ListObject[PayoutMethod],
            self._request(
                "get",
                "/v2/money_management/payout_methods",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "PayoutMethodService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[PayoutMethod]:
        """
        List objects that adhere to the PayoutMethod interface.
        """
        return cast(
            ListObject[PayoutMethod],
            await self._request_async(
                "get",
                "/v2/money_management/payout_methods",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "PayoutMethodService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Retrieve a PayoutMethod object.
        """
        return cast(
            PayoutMethod,
            self._request(
                "get",
                "/v2/money_management/payout_methods/{id}".format(
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
        params: "PayoutMethodService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Retrieve a PayoutMethod object.
        """
        return cast(
            PayoutMethod,
            await self._request_async(
                "get",
                "/v2/money_management/payout_methods/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def archive(
        self,
        id: str,
        params: "PayoutMethodService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Archive a PayoutMethod object. Archived objects cannot be used as payout methods
        and will not appear in the payout method list.
        """
        return cast(
            PayoutMethod,
            self._request(
                "post",
                "/v2/money_management/payout_methods/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def archive_async(
        self,
        id: str,
        params: "PayoutMethodService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Archive a PayoutMethod object. Archived objects cannot be used as payout methods
        and will not appear in the payout method list.
        """
        return cast(
            PayoutMethod,
            await self._request_async(
                "post",
                "/v2/money_management/payout_methods/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def unarchive(
        self,
        id: str,
        params: "PayoutMethodService.UnarchiveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Unarchive an PayoutMethod object.
        """
        return cast(
            PayoutMethod,
            self._request(
                "post",
                "/v2/money_management/payout_methods/{id}/unarchive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def unarchive_async(
        self,
        id: str,
        params: "PayoutMethodService.UnarchiveParams" = {},
        options: RequestOptions = {},
    ) -> PayoutMethod:
        """
        Unarchive an PayoutMethod object.
        """
        return cast(
            PayoutMethod,
            await self._request_async(
                "post",
                "/v2/money_management/payout_methods/{id}/unarchive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
