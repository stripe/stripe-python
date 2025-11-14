# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._transaction_entry_list_params import (
        TransactionEntryListParams,
    )
    from stripe.params.v2.money_management._transaction_entry_retrieve_params import (
        TransactionEntryRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._transaction_entry import TransactionEntry


class TransactionEntryService(StripeService):
    def list(
        self,
        params: Optional["TransactionEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TransactionEntry]":
        """
        Returns a list of TransactionEntries that match the provided filters.
        """
        return cast(
            "ListObject[TransactionEntry]",
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
        params: Optional["TransactionEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TransactionEntry]":
        """
        Returns a list of TransactionEntries that match the provided filters.
        """
        return cast(
            "ListObject[TransactionEntry]",
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
        params: Optional["TransactionEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TransactionEntry":
        """
        Retrieves the details of a TransactionEntry by ID.
        """
        return cast(
            "TransactionEntry",
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
        params: Optional["TransactionEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TransactionEntry":
        """
        Retrieves the details of a TransactionEntry by ID.
        """
        return cast(
            "TransactionEntry",
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
