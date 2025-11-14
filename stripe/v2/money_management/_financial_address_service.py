# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._financial_address_create_params import (
        FinancialAddressCreateParams,
    )
    from stripe.params.v2.money_management._financial_address_list_params import (
        FinancialAddressListParams,
    )
    from stripe.params.v2.money_management._financial_address_retrieve_params import (
        FinancialAddressRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._financial_address import FinancialAddress


class FinancialAddressService(StripeService):
    def list(
        self,
        params: Optional["FinancialAddressListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAddress]":
        """
        List all FinancialAddresses for a FinancialAccount.
        """
        return cast(
            "ListObject[FinancialAddress]",
            self._request(
                "get",
                "/v2/money_management/financial_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FinancialAddressListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancialAddress]":
        """
        List all FinancialAddresses for a FinancialAccount.
        """
        return cast(
            "ListObject[FinancialAddress]",
            await self._request_async(
                "get",
                "/v2/money_management/financial_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FinancialAddressCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddress":
        """
        Create a new FinancialAddress for a FinancialAccount.
        """
        return cast(
            "FinancialAddress",
            self._request(
                "post",
                "/v2/money_management/financial_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FinancialAddressCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddress":
        """
        Create a new FinancialAddress for a FinancialAccount.
        """
        return cast(
            "FinancialAddress",
            await self._request_async(
                "post",
                "/v2/money_management/financial_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FinancialAddressRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddress":
        """
        Retrieve a FinancialAddress. By default, the FinancialAddress will be returned in its unexpanded state, revealing only the last 4 digits of the account number.
        """
        return cast(
            "FinancialAddress",
            self._request(
                "get",
                "/v2/money_management/financial_addresses/{id}".format(
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
        params: Optional["FinancialAddressRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddress":
        """
        Retrieve a FinancialAddress. By default, the FinancialAddress will be returned in its unexpanded state, revealing only the last 4 digits of the account number.
        """
        return cast(
            "FinancialAddress",
            await self._request_async(
                "get",
                "/v2/money_management/financial_addresses/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
