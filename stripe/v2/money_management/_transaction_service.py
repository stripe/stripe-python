# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._transaction_list_params import (
        TransactionListParams,
    )
    from stripe.params.v2.money_management._transaction_retrieve_params import (
        TransactionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._transaction import Transaction


class TransactionService(StripeService):
    def list(
        self,
        params: Optional["TransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Transaction]":
        """
        Returns a list of Transactions that match the provided filters.
        """
        return cast(
            "ListObject[Transaction]",
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
        params: Optional["TransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Transaction]":
        """
        Returns a list of Transactions that match the provided filters.
        """
        return cast(
            "ListObject[Transaction]",
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
        params: Optional["TransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Retrieves the details of a Transaction by ID.
        """
        return cast(
            "Transaction",
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
        params: Optional["TransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Retrieves the details of a Transaction by ID.
        """
        return cast(
            "Transaction",
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
