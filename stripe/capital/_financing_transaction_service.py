# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.capital._financing_transaction import FinancingTransaction
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class FinancingTransactionService(StripeService):
    class ListParams(TypedDict):
        charge: NotRequired[str]
        """
        For transactions of type `paydown` and reason `automatic_withholding` only, only returns transactions that were created as a result of this charge.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        financing_offer: NotRequired[str]
        """
        Returns transactions that were created that apply to this financing offer ID.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        reversed_transaction: NotRequired[str]
        """
        Only returns transactions that are responsible for reversing this financing transaction ID.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        treasury_transaction: NotRequired[str]
        """
        For transactions of type `paydown` and reason `automatic_withholding` only, only returns transactions that were created as a result of this Treasury Transaction.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "FinancingTransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancingTransaction]:
        """
        Returns a list of financing transactions. The transactions are returned in sorted order,
        with the most recent transactions appearing first.
        """
        return cast(
            ListObject[FinancingTransaction],
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
        params: "FinancingTransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancingTransaction]:
        """
        Returns a list of financing transactions. The transactions are returned in sorted order,
        with the most recent transactions appearing first.
        """
        return cast(
            ListObject[FinancingTransaction],
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
        params: "FinancingTransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingTransaction:
        """
        Retrieves a financing transaction for a financing offer.
        """
        return cast(
            FinancingTransaction,
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
        params: "FinancingTransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingTransaction:
        """
        Retrieves a financing transaction for a financing offer.
        """
        return cast(
            FinancingTransaction,
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
