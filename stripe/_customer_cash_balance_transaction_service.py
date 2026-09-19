# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer_cash_balance_transaction import (
        CustomerCashBalanceTransaction,
    )
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._customer_cash_balance_transaction_list_params import (
        CustomerCashBalanceTransactionListParams,
    )
    from stripe.params._customer_cash_balance_transaction_retrieve_params import (
        CustomerCashBalanceTransactionRetrieveParams,
    )


class CustomerCashBalanceTransactionService(StripeService):
    def list(
        self,
        id: str,
        /,
        params: Optional["CustomerCashBalanceTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerCashBalanceTransaction]":
        """
        Returns a list of transactions that modified the customer's [cash balance](https://docs.stripe.com/docs/payments/customer-balance).
        """
        return cast(
            "ListObject[CustomerCashBalanceTransaction]",
            self._request(
                "get",
                "/v1/customers/{id}/cash_balance_transactions".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        /,
        params: Optional["CustomerCashBalanceTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerCashBalanceTransaction]":
        """
        Returns a list of transactions that modified the customer's [cash balance](https://docs.stripe.com/docs/payments/customer-balance).
        """
        return cast(
            "ListObject[CustomerCashBalanceTransaction]",
            await self._request_async(
                "get",
                "/v1/customers/{id}/cash_balance_transactions".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        customer_id: str,
        id: str,
        /,
        params: Optional[
            "CustomerCashBalanceTransactionRetrieveParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerCashBalanceTransaction":
        """
        Retrieves a specific cash balance transaction, which updated the customer's [cash balance](https://docs.stripe.com/docs/payments/customer-balance).
        """
        return cast(
            "CustomerCashBalanceTransaction",
            self._request(
                "get",
                "/v1/customers/{customer_id}/cash_balance_transactions/{id}".format(
                    customer_id=sanitize_id(customer_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        customer_id: str,
        id: str,
        /,
        params: Optional[
            "CustomerCashBalanceTransactionRetrieveParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerCashBalanceTransaction":
        """
        Retrieves a specific cash balance transaction, which updated the customer's [cash balance](https://docs.stripe.com/docs/payments/customer-balance).
        """
        return cast(
            "CustomerCashBalanceTransaction",
            await self._request_async(
                "get",
                "/v1/customers/{customer_id}/cash_balance_transactions/{id}".format(
                    customer_id=sanitize_id(customer_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
