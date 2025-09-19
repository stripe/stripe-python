# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._financial_account import FinancialAccount
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountService(StripeService):
    class CloseParams(TypedDict):
        forwarding_settings: NotRequired[
            "FinancialAccountService.CloseParamsForwardingSettings"
        ]
        """
        The addresses to forward any incoming transactions to.
        """

    class CloseParamsForwardingSettings(TypedDict):
        payment_method: NotRequired[str]
        """
        The address to send forwarded payments to.
        """
        payout_method: NotRequired[str]
        """
        The address to send forwarded payouts to.
        """

    class CreateParams(TypedDict):
        display_name: NotRequired[str]
        """
        A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Metadata associated with the FinancialAccount.
        """
        storage: NotRequired["FinancialAccountService.CreateParamsStorage"]
        """
        Parameters specific to creating `storage` type FinancialAccounts.
        """
        type: Literal["storage"]
        """
        The type of FinancialAccount to create.
        """

    class CreateParamsStorage(TypedDict):
        holds_currencies: List[str]
        """
        The currencies that this FinancialAccount can hold.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page limit.
        """
        status: NotRequired[Literal["closed", "open", "pending"]]
        """
        The status of the FinancialAccount to filter by. By default, closed FinancialAccounts are not returned.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: Optional["FinancialAccountService.ListParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["FinancialAccountService.ListParams"] = None,
        options: Optional[RequestOptions] = None,
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

    def create(
        self,
        params: "FinancialAccountService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> FinancialAccount:
        """
        Creates a new FinancialAccount.
        """
        return cast(
            FinancialAccount,
            self._request(
                "post",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FinancialAccountService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> FinancialAccount:
        """
        Creates a new FinancialAccount.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FinancialAccountService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["FinancialAccountService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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

    def close(
        self,
        id: str,
        params: Optional["FinancialAccountService.CloseParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> FinancialAccount:
        """
        Closes a FinancialAccount with or without forwarding settings.
        """
        return cast(
            FinancialAccount,
            self._request(
                "post",
                "/v2/money_management/financial_accounts/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def close_async(
        self,
        id: str,
        params: Optional["FinancialAccountService.CloseParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> FinancialAccount:
        """
        Closes a FinancialAccount with or without forwarding settings.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
