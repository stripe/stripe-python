# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.financial_connections._account_inferred_balance import (
        AccountInferredBalance,
    )
    from stripe.params.financial_connections._account_inferred_balance_list_params import (
        AccountInferredBalanceListParams,
    )


class AccountInferredBalanceService(StripeService):
    def list(
        self,
        account: str,
        params: Optional["AccountInferredBalanceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountInferredBalance]":
        """
        Lists the recorded inferred balances for a Financial Connections Account.
        """
        return cast(
            "ListObject[AccountInferredBalance]",
            self._request(
                "get",
                "/v1/financial_connections/accounts/{account}/inferred_balances".format(
                    account=sanitize_id(account),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        account: str,
        params: Optional["AccountInferredBalanceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountInferredBalance]":
        """
        Lists the recorded inferred balances for a Financial Connections Account.
        """
        return cast(
            "ListObject[AccountInferredBalance]",
            await self._request_async(
                "get",
                "/v1/financial_connections/accounts/{account}/inferred_balances".format(
                    account=sanitize_id(account),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
