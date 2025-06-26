# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.core.vault._us_bank_account import UsBankAccount
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class UsBankAccountService(StripeService):
    class ArchiveParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        account_number: str
        """
        The account number of the bank account.
        """
        bank_account_type: NotRequired[Literal["checking", "savings"]]
        """
        Closed Enum. The type of the bank account (checking or savings).
        """
        fedwire_routing_number: NotRequired[str]
        """
        The fedwire routing number of the bank account. Note that certain banks have the same ACH and wire routing number.
        """
        routing_number: NotRequired[str]
        """
        The ACH routing number of the bank account. Note that certain banks have the same ACH and wire routing number.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        fedwire_routing_number: NotRequired[str]
        """
        The bank account's fedwire routing number can be provided for update it was were empty previously.
        """
        routing_number: NotRequired[str]
        """
        The bank account's ACH routing number can be provided for update if it was empty previously.
        """

    def create(
        self,
        params: "UsBankAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Create a USBankAccount object.
        """
        return cast(
            UsBankAccount,
            self._request(
                "post",
                "/v2/core/vault/us_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "UsBankAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Create a USBankAccount object.
        """
        return cast(
            UsBankAccount,
            await self._request_async(
                "post",
                "/v2/core/vault/us_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "UsBankAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Retrieve a USBankAccount object.
        """
        return cast(
            UsBankAccount,
            self._request(
                "get",
                "/v2/core/vault/us_bank_accounts/{id}".format(
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
        params: "UsBankAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Retrieve a USBankAccount object.
        """
        return cast(
            UsBankAccount,
            await self._request_async(
                "get",
                "/v2/core/vault/us_bank_accounts/{id}".format(
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
        params: "UsBankAccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Update a USBankAccount object. This is limited to supplying a previously empty routing_number field.
        """
        return cast(
            UsBankAccount,
            self._request(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}".format(
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
        params: "UsBankAccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Update a USBankAccount object. This is limited to supplying a previously empty routing_number field.
        """
        return cast(
            UsBankAccount,
            await self._request_async(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def archive(
        self,
        id: str,
        params: "UsBankAccountService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Archive a USBankAccount object. USBankAccount objects will not be automatically archived by Stripe.
        Archived USBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            UsBankAccount,
            self._request(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def archive_async(
        self,
        id: str,
        params: "UsBankAccountService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> UsBankAccount:
        """
        Archive a USBankAccount object. USBankAccount objects will not be automatically archived by Stripe.
        Archived USBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            UsBankAccount,
            await self._request_async(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
