# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._transaction import Transaction
from typing import cast
from typing_extensions import NotRequired, TypedDict


class TransactionService(StripeService):
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
        financial_account: NotRequired[str]
        """
        Filter for Transactions belonging to a FinancialAccount.
        """
        flow: NotRequired[str]
        """
        Filter for Transactions corresponding to a Flow.
        """
        limit: NotRequired[int]
        """
        The page limit.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "TransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Transaction]:
        """
        Returns a list of Transactions that match the provided filters.
        """
        return cast(
            ListObject[Transaction],
            self._request(
                "get",
                "/v2/money_management/transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "TransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Transaction]:
        """
        Returns a list of Transactions that match the provided filters.
        """
        return cast(
            ListObject[Transaction],
            await self._request_async(
                "get",
                "/v2/money_management/transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "TransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Retrieves the details of a Transaction by ID.
        """
        return cast(
            Transaction,
            self._request(
                "get",
                "/v2/money_management/transactions/{id}".format(
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
        params: "TransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Retrieves the details of a Transaction by ID.
        """
        return cast(
            Transaction,
            await self._request_async(
                "get",
                "/v2/money_management/transactions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
