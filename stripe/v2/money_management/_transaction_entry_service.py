# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._transaction_entry import TransactionEntry
from typing import cast
from typing_extensions import NotRequired, TypedDict


class TransactionEntryService(StripeService):
    class ListParams(TypedDict):
        created: NotRequired[str]
        """
        Filter for Transactions created at an exact time.
        """
        created_gt: NotRequired[str]
        """
        Filter for Transactions created after the specified timestamp.
        """
        created_gte: NotRequired[str]
        """
        Filter for Transactions created at or after the specified timestamp.
        """
        created_lt: NotRequired[str]
        """
        Filter for Transactions created before the specified timestamp.
        """
        created_lte: NotRequired[str]
        """
        Filter for Transactions created at or before the specified timestamp.
        """
        limit: NotRequired[int]
        """
        The page limit.
        """
        transaction: NotRequired[str]
        """
        Filter for TransactionEntries belonging to a Transaction.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "TransactionEntryService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[TransactionEntry]:
        """
        Returns a list of TransactionEntries that match the provided filters.
        """
        return cast(
            ListObject[TransactionEntry],
            self._request(
                "get",
                "/v2/money_management/transaction_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "TransactionEntryService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[TransactionEntry]:
        """
        Returns a list of TransactionEntries that match the provided filters.
        """
        return cast(
            ListObject[TransactionEntry],
            await self._request_async(
                "get",
                "/v2/money_management/transaction_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "TransactionEntryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> TransactionEntry:
        """
        Retrieves the details of a TransactionEntry by ID.
        """
        return cast(
            TransactionEntry,
            self._request(
                "get",
                "/v2/money_management/transaction_entries/{id}".format(
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
        params: "TransactionEntryService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> TransactionEntry:
        """
        Retrieves the details of a TransactionEntry by ID.
        """
        return cast(
            TransactionEntry,
            await self._request_async(
                "get",
                "/v2/money_management/transaction_entries/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
