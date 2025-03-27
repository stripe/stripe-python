# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._financial_account import FinancialAccount
from typing import cast
from typing_extensions import NotRequired, TypedDict


class FinancialAccountService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page limit.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "FinancialAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAccount]:
        """
        Lists FinancialAccounts in this compartment.
        """
        return cast(
            ListObject[FinancialAccount],
            self._request(
                "get",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "FinancialAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAccount]:
        """
        Lists FinancialAccounts in this compartment.
        """
        return cast(
            ListObject[FinancialAccount],
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "FinancialAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            FinancialAccount,
            self._request(
                "get",
                "/v2/money_management/financial_accounts/{id}".format(
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
        params: "FinancialAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
