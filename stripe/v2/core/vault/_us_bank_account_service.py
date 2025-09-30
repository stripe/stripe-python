# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.core.vault._us_bank_account import UsBankAccount
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core.vault._us_bank_account_archive_params import (
        UsBankAccountArchiveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_create_params import (
        UsBankAccountCreateParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_retrieve_params import (
        UsBankAccountRetrieveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_update_params import (
        UsBankAccountUpdateParams,
    )


class UsBankAccountService(StripeService):
    def create(
        self,
        params: "UsBankAccountCreateParams",
        options: Optional[RequestOptions] = None,
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
        params: "UsBankAccountCreateParams",
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountArchiveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["UsBankAccountArchiveParams"] = None,
        options: Optional[RequestOptions] = None,
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
