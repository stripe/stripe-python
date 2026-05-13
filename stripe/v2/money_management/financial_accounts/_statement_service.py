# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management.financial_accounts._statement_list_params import (
        StatementListParams,
    )
    from stripe.params.v2.money_management.financial_accounts._statement_retrieve_params import (
        StatementRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._financial_account_statement import (
        FinancialAccountStatement,
    )


class StatementService(StripeService):
    def list(
        self,
        financial_account_id: str,
        params: Optional["StatementListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAccountStatement]":
        """
        Returns a list of statements for a Financial Account.
        """
        return cast(
            "ListObject[FinancialAccountStatement]",
            self._request(
                "get",
                "/v2/money_management/financial_accounts/{financial_account_id}/statements".format(
                    financial_account_id=sanitize_id(financial_account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        financial_account_id: str,
        params: Optional["StatementListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAccountStatement]":
        """
        Returns a list of statements for a Financial Account.
        """
        return cast(
            "ListObject[FinancialAccountStatement]",
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts/{financial_account_id}/statements".format(
                    financial_account_id=sanitize_id(financial_account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        financial_account_id: str,
        id: str,
        params: Optional["StatementRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountStatement":
        """
        Retrieves the details of a Financial Account Statement.
        """
        return cast(
            "FinancialAccountStatement",
            self._request(
                "get",
                "/v2/money_management/financial_accounts/{financial_account_id}/statements/{id}".format(
                    financial_account_id=sanitize_id(financial_account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        financial_account_id: str,
        id: str,
        params: Optional["StatementRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountStatement":
        """
        Retrieves the details of a Financial Account Statement.
        """
        return cast(
            "FinancialAccountStatement",
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts/{financial_account_id}/statements/{id}".format(
                    financial_account_id=sanitize_id(financial_account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
