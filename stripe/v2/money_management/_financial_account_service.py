# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._financial_account_list_params import (
        FinancialAccountListParams,
    )
    from stripe.params.v2.money_management._financial_account_retrieve_params import (
        FinancialAccountRetrieveParams,
    )
    from stripe.params.v2.money_management._financial_account_update_params import (
        FinancialAccountUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._financial_account import FinancialAccount


class FinancialAccountService(StripeService):
    def list(
        self,
        params: Optional["FinancialAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAccount]":
        """
        Returns a list of FinancialAccounts in your account that match the provided filters.
        """
        return cast(
            "ListObject[FinancialAccount]",
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
        params: Optional["FinancialAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAccount]":
        """
        Returns a list of FinancialAccounts in your account that match the provided filters.
        """
        return cast(
            "ListObject[FinancialAccount]",
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
        /,
        params: Optional["FinancialAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccount":
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            "FinancialAccount",
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
        /,
        params: Optional["FinancialAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccount":
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            "FinancialAccount",
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

    def update(
        self,
        id: str,
        /,
        params: Optional["FinancialAccountUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccount":
        """
        Updates an existing FinancialAccount using the provided parameters.
        """
        return cast(
            "FinancialAccount",
            self._request(
                "post",
                "/v2/money_management/financial_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["FinancialAccountUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccount":
        """
        Updates an existing FinancialAccount using the provided parameters.
        """
        return cast(
            "FinancialAccount",
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
