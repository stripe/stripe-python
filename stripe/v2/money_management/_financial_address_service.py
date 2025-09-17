# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._financial_address import FinancialAddress
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressService(StripeService):
    class CreateParams(TypedDict):
        currency: str
        """
        Open Enum. The currency the FinancialAddress should support. Currently, only the `usd` and `gbp` values are supported.
        """
        financial_account: str
        """
        The ID of the FinancialAccount the new FinancialAddress should be associated with.
        """

    class ListParams(TypedDict):
        financial_account: NotRequired[str]
        """
        The ID of the FinancialAccount for which FinancialAddresses are to be returned.
        """
        include: NotRequired[
            List[
                Literal[
                    "credentials.gb_bank_account.account_number",
                    "credentials.us_bank_account.account_number",
                ]
            ]
        ]
        """
        Open Enum. A list of fields to reveal in the FinancialAddresses returned.
        """
        limit: NotRequired[int]
        """
        The page limit.
        """

    class RetrieveParams(TypedDict):
        include: NotRequired[
            List[
                Literal[
                    "credentials.gb_bank_account.account_number",
                    "credentials.us_bank_account.account_number",
                ]
            ]
        ]
        """
        Open Enum. A list of fields to reveal in the FinancialAddresses returned.
        """

    def list(
        self,
        params: "FinancialAddressService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAddress]:
        """
        List all FinancialAddresses for a FinancialAccount.
        """
        return cast(
            ListObject[FinancialAddress],
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
        params: "FinancialAddressService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAddress]:
        """
        List all FinancialAddresses for a FinancialAccount.
        """
        return cast(
            ListObject[FinancialAddress],
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
        params: "FinancialAddressService.CreateParams",
        options: RequestOptions = {},
    ) -> FinancialAddress:
        """
        Create a new FinancialAddress for a FinancialAccount.
        """
        return cast(
            FinancialAddress,
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
        params: "FinancialAddressService.CreateParams",
        options: RequestOptions = {},
    ) -> FinancialAddress:
        """
        Create a new FinancialAddress for a FinancialAccount.
        """
        return cast(
            FinancialAddress,
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
        params: "FinancialAddressService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAddress:
        """
        Retrieve a FinancialAddress. By default, the FinancialAddress will be returned in its unexpanded state, revealing only the last 4 digits of the account number.
        """
        return cast(
            FinancialAddress,
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
        params: "FinancialAddressService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAddress:
        """
        Retrieve a FinancialAddress. By default, the FinancialAddress will be returned in its unexpanded state, revealing only the last 4 digits of the account number.
        """
        return cast(
            FinancialAddress,
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
