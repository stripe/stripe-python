# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.billing._credit_balance_transaction import CreditBalanceTransaction
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class CreditBalanceTransactionService(StripeService):
    class ListParams(TypedDict):
        credit_grant: NotRequired[str]
        """
        The credit grant for which to fetch credit balance transactions.
        """
        customer: str
        """
        The customer for which to fetch credit balance transactions.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "CreditBalanceTransactionService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[CreditBalanceTransaction]:
        """
        Retrieve a list of credit balance transactions
        """
        return cast(
            ListObject[CreditBalanceTransaction],
            self._request(
                "get",
                "/v1/billing/credit_balance_transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CreditBalanceTransactionService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[CreditBalanceTransaction]:
        """
        Retrieve a list of credit balance transactions
        """
        return cast(
            ListObject[CreditBalanceTransaction],
            await self._request_async(
                "get",
                "/v1/billing/credit_balance_transactions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CreditBalanceTransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditBalanceTransaction:
        """
        Retrieves a credit balance transaction
        """
        return cast(
            CreditBalanceTransaction,
            self._request(
                "get",
                "/v1/billing/credit_balance_transactions/{id}".format(
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
        params: "CreditBalanceTransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditBalanceTransaction:
        """
        Retrieves a credit balance transaction
        """
        return cast(
            CreditBalanceTransaction,
            await self._request_async(
                "get",
                "/v1/billing/credit_balance_transactions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
