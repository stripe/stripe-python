# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._received_credit import ReceivedCredit
from typing import cast
from typing_extensions import NotRequired, TypedDict


class ReceivedCreditService(StripeService):
    class ListParams(TypedDict):
        created: NotRequired[str]
        """
        Filter for objects created at the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_gt: NotRequired[str]
        """
        Filter for objects created after the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_gte: NotRequired[str]
        """
        Filter for objects created on or after the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_lt: NotRequired[str]
        """
        Filter for objects created before the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_lte: NotRequired[str]
        """
        Filter for objects created on or before the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        limit: NotRequired[int]
        """
        The page limit.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "ReceivedCreditService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[ReceivedCredit]:
        """
        Retrieves a list of ReceivedCredits.
        """
        return cast(
            ListObject[ReceivedCredit],
            self._request(
                "get",
                "/v2/money_management/received_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ReceivedCreditService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[ReceivedCredit]:
        """
        Retrieves a list of ReceivedCredits.
        """
        return cast(
            ListObject[ReceivedCredit],
            await self._request_async(
                "get",
                "/v2/money_management/received_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ReceivedCreditService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReceivedCredit:
        """
        Retrieve a ReceivedCredit by ID.
        """
        return cast(
            ReceivedCredit,
            self._request(
                "get",
                "/v2/money_management/received_credits/{id}".format(
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
        params: "ReceivedCreditService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReceivedCredit:
        """
        Retrieve a ReceivedCredit by ID.
        """
        return cast(
            ReceivedCredit,
            await self._request_async(
                "get",
                "/v2/money_management/received_credits/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
