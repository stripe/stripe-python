# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.capital._financing_transaction import FinancingTransaction
    from stripe.params.capital._financing_transaction_list_params import (
        FinancingTransactionListParams,
    )
    from stripe.params.capital._financing_transaction_retrieve_params import (
        FinancingTransactionRetrieveParams,
    )


class FinancingTransactionService(StripeService):
    def list(
        self,
        params: Optional["FinancingTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancingTransaction]":
        """
        Returns a list of financing transactions. The transactions are returned in sorted order,
        with the most recent transactions appearing first.
        """
        return cast(
            "ListObject[FinancingTransaction]",
            self._request(
                "get",
                "/v1/capital/financing_transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FinancingTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancingTransaction]":
        """
        Returns a list of financing transactions. The transactions are returned in sorted order,
        with the most recent transactions appearing first.
        """
        return cast(
            "ListObject[FinancingTransaction]",
            await self._request_async(
                "get",
                "/v1/capital/financing_transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        financing_transaction: str,
        params: Optional["FinancingTransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingTransaction":
        """
        Retrieves a financing transaction for a financing offer.
        """
        return cast(
            "FinancingTransaction",
            self._request(
                "get",
                "/v1/capital/financing_transactions/{financing_transaction}".format(
                    financing_transaction=sanitize_id(financing_transaction),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        financing_transaction: str,
        params: Optional["FinancingTransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingTransaction":
        """
        Retrieves a financing transaction for a financing offer.
        """
        return cast(
            "FinancingTransaction",
            await self._request_async(
                "get",
                "/v1/capital/financing_transactions/{financing_transaction}".format(
                    financing_transaction=sanitize_id(financing_transaction),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
