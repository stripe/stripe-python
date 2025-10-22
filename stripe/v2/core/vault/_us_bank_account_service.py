# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core.vault._us_bank_account_archive_params import (
        UsBankAccountArchiveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_confirm_microdeposits_params import (
        UsBankAccountConfirmMicrodepositsParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_create_params import (
        UsBankAccountCreateParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_list_params import (
        UsBankAccountListParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_retrieve_params import (
        UsBankAccountRetrieveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_send_microdeposits_params import (
        UsBankAccountSendMicrodepositsParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_update_params import (
        UsBankAccountUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core.vault._us_bank_account import UsBankAccount


class UsBankAccountService(StripeService):
    def list(
        self,
        params: Optional["UsBankAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[UsBankAccount]":
        """
        List USBankAccount objects. Optionally filter by verification status.
        """
        return cast(
            "ListObject[UsBankAccount]",
            self._request(
                "get",
                "/v2/core/vault/us_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["UsBankAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[UsBankAccount]":
        """
        List USBankAccount objects. Optionally filter by verification status.
        """
        return cast(
            "ListObject[UsBankAccount]",
            await self._request_async(
                "get",
                "/v2/core/vault/us_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "UsBankAccountCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Create a USBankAccount object.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Create a USBankAccount object.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Retrieve a USBankAccount object.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Retrieve a USBankAccount object.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Update a USBankAccount object. This is limited to supplying a previously empty routing_number field.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Update a USBankAccount object. This is limited to supplying a previously empty routing_number field.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Archive a USBankAccount object. USBankAccount objects will not be automatically archived by Stripe.
        Archived USBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            "UsBankAccount",
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
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Archive a USBankAccount object. USBankAccount objects will not be automatically archived by Stripe.
        Archived USBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            "UsBankAccount",
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

    def confirm_microdeposits(
        self,
        id: str,
        params: Optional["UsBankAccountConfirmMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Confirm microdeposits amounts or descriptor code that you have received from the Send Microdeposits request. Once you correctly confirm this, this US Bank Account will be verified and eligible to transfer funds with.
        """
        return cast(
            "UsBankAccount",
            self._request(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/confirm_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_microdeposits_async(
        self,
        id: str,
        params: Optional["UsBankAccountConfirmMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Confirm microdeposits amounts or descriptor code that you have received from the Send Microdeposits request. Once you correctly confirm this, this US Bank Account will be verified and eligible to transfer funds with.
        """
        return cast(
            "UsBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/confirm_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def send_microdeposits(
        self,
        id: str,
        params: Optional["UsBankAccountSendMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Send microdeposits in order to verify your US Bank Account so it is eligible to transfer funds. This will start the verification process and you must Confirm Microdeposits to successfully verify your US Bank Account.
        """
        return cast(
            "UsBankAccount",
            self._request(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/send_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def send_microdeposits_async(
        self,
        id: str,
        params: Optional["UsBankAccountSendMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "UsBankAccount":
        """
        Send microdeposits in order to verify your US Bank Account so it is eligible to transfer funds. This will start the verification process and you must Confirm Microdeposits to successfully verify your US Bank Account.
        """
        return cast(
            "UsBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/us_bank_accounts/{id}/send_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
