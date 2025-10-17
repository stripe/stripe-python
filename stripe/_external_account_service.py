# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._bank_account import BankAccount
    from stripe._card import Card
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._external_account_create_params import (
        ExternalAccountCreateParams,
    )
    from stripe.params._external_account_delete_params import (
        ExternalAccountDeleteParams,
    )
    from stripe.params._external_account_list_params import (
        ExternalAccountListParams,
    )
    from stripe.params._external_account_retrieve_params import (
        ExternalAccountRetrieveParams,
    )
    from stripe.params._external_account_update_params import (
        ExternalAccountUpdateParams,
    )
    from typing import Union


class ExternalAccountService(StripeService):
    def delete(
        self,
        id: str,
        params: Optional["ExternalAccountDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Delete a specified external account for a given account.
        """
        return cast(
            "Union[BankAccount, Card]",
            self._request(
                "delete",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: Optional["ExternalAccountDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Delete a specified external account for a given account.
        """
        return cast(
            "Union[BankAccount, Card]",
            await self._request_async(
                "delete",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ExternalAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Retrieve a specified external account for a given account.
        """
        return cast(
            "Union[BankAccount, Card]",
            self._request(
                "get",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ExternalAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Retrieve a specified external account for a given account.
        """
        return cast(
            "Union[BankAccount, Card]",
            await self._request_async(
                "get",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["ExternalAccountUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.

        You can only update bank accounts when [account.controller.requirement_collection is application, which includes <a href="/connect/custom-accounts">Custom accounts](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection).

        You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.
        """
        return cast(
            "Union[BankAccount, Card]",
            self._request(
                "post",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["ExternalAccountUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.

        You can only update bank accounts when [account.controller.requirement_collection is application, which includes <a href="/connect/custom-accounts">Custom accounts](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection).

        You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.
        """
        return cast(
            "Union[BankAccount, Card]",
            await self._request_async(
                "post",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: Optional["ExternalAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Union[BankAccount, Card]]":
        """
        List external accounts for an account.
        """
        return cast(
            "ListObject[Union[BankAccount, Card]]",
            self._request(
                "get",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ExternalAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Union[BankAccount, Card]]":
        """
        List external accounts for an account.
        """
        return cast(
            "ListObject[Union[BankAccount, Card]]",
            await self._request_async(
                "get",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ExternalAccountCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Create an external account for a given connected account.
        """
        return cast(
            "Union[BankAccount, Card]",
            self._request(
                "post",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ExternalAccountCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Union[BankAccount, Card]":
        """
        Create an external account for a given connected account.
        """
        return cast(
            "Union[BankAccount, Card]",
            await self._request_async(
                "post",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )
