# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._received_debit import ReceivedDebit
from typing import cast
from typing_extensions import NotRequired, TypedDict


class ReceivedDebitService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page limit.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "ReceivedDebitService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[ReceivedDebit]:
        """
        Retrieves a list of ReceivedDebits, given the selected filters.
        """
        return cast(
            ListObject[ReceivedDebit],
            self._request(
                "get",
                "/v2/money_management/received_debits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ReceivedDebitService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[ReceivedDebit]:
        """
        Retrieves a list of ReceivedDebits, given the selected filters.
        """
        return cast(
            ListObject[ReceivedDebit],
            await self._request_async(
                "get",
                "/v2/money_management/received_debits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ReceivedDebitService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReceivedDebit:
        """
        Retrieves a single ReceivedDebit by ID.
        """
        return cast(
            ReceivedDebit,
            self._request(
                "get",
                "/v2/money_management/received_debits/{id}".format(
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
        params: "ReceivedDebitService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReceivedDebit:
        """
        Retrieves a single ReceivedDebit by ID.
        """
        return cast(
            ReceivedDebit,
            await self._request_async(
                "get",
                "/v2/money_management/received_debits/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
