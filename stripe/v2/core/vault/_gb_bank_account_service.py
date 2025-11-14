# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core.vault._gb_bank_account_acknowledge_confirmation_of_payee_params import (
        GbBankAccountAcknowledgeConfirmationOfPayeeParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_archive_params import (
        GbBankAccountArchiveParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_create_params import (
        GbBankAccountCreateParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_initiate_confirmation_of_payee_params import (
        GbBankAccountInitiateConfirmationOfPayeeParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_list_params import (
        GbBankAccountListParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_retrieve_params import (
        GbBankAccountRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core.vault._gb_bank_account import GbBankAccount


class GbBankAccountService(StripeService):
    def list(
        self,
        params: Optional["GbBankAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[GbBankAccount]":
        """
        List objects that can be used as destinations for outbound money movement via OutboundPayment.
        """
        return cast(
            "ListObject[GbBankAccount]",
            self._request(
                "get",
                "/v2/core/vault/gb_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["GbBankAccountListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[GbBankAccount]":
        """
        List objects that can be used as destinations for outbound money movement via OutboundPayment.
        """
        return cast(
            "ListObject[GbBankAccount]",
            await self._request_async(
                "get",
                "/v2/core/vault/gb_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "GbBankAccountCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Create a GB bank account.
        """
        return cast(
            "GbBankAccount",
            self._request(
                "post",
                "/v2/core/vault/gb_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "GbBankAccountCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Create a GB bank account.
        """
        return cast(
            "GbBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/gb_bank_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["GbBankAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Retrieve a GB bank account.
        """
        return cast(
            "GbBankAccount",
            self._request(
                "get",
                "/v2/core/vault/gb_bank_accounts/{id}".format(
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
        params: Optional["GbBankAccountRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Retrieve a GB bank account.
        """
        return cast(
            "GbBankAccount",
            await self._request_async(
                "get",
                "/v2/core/vault/gb_bank_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def acknowledge_confirmation_of_payee(
        self,
        id: str,
        params: Optional[
            "GbBankAccountAcknowledgeConfirmationOfPayeeParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Confirm that you have received the result of the Confirmation of Payee request, and that you are okay with
        proceeding to pay out to this bank account despite the account not matching, partially matching, or the service
        being unavailable. Once you confirm this, you will be able to send OutboundPayments, but this may lead to
        funds being sent to the wrong account, which we might not be able to recover.
        """
        return cast(
            "GbBankAccount",
            self._request(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/acknowledge_confirmation_of_payee".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def acknowledge_confirmation_of_payee_async(
        self,
        id: str,
        params: Optional[
            "GbBankAccountAcknowledgeConfirmationOfPayeeParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Confirm that you have received the result of the Confirmation of Payee request, and that you are okay with
        proceeding to pay out to this bank account despite the account not matching, partially matching, or the service
        being unavailable. Once you confirm this, you will be able to send OutboundPayments, but this may lead to
        funds being sent to the wrong account, which we might not be able to recover.
        """
        return cast(
            "GbBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/acknowledge_confirmation_of_payee".format(
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
        params: Optional["GbBankAccountArchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Archive a GBBankAccount object. Archived GBBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            "GbBankAccount",
            self._request(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/archive".format(
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
        params: Optional["GbBankAccountArchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Archive a GBBankAccount object. Archived GBBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            "GbBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def initiate_confirmation_of_payee(
        self,
        id: str,
        params: Optional[
            "GbBankAccountInitiateConfirmationOfPayeeParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Initiate Confirmation of Payee (CoP) in order to verify that the owner of a UK bank account matches
        who you expect. This must be done on all UK bank accounts before sending domestic OutboundPayments. If
        the result is a partial match or a non match, explicit acknowledgement using AcknowledgeConfirmationOfPayee
        is required before sending funds.
        """
        return cast(
            "GbBankAccount",
            self._request(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/initiate_confirmation_of_payee".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def initiate_confirmation_of_payee_async(
        self,
        id: str,
        params: Optional[
            "GbBankAccountInitiateConfirmationOfPayeeParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GbBankAccount":
        """
        Initiate Confirmation of Payee (CoP) in order to verify that the owner of a UK bank account matches
        who you expect. This must be done on all UK bank accounts before sending domestic OutboundPayments. If
        the result is a partial match or a non match, explicit acknowledgement using AcknowledgeConfirmationOfPayee
        is required before sending funds.
        """
        return cast(
            "GbBankAccount",
            await self._request_async(
                "post",
                "/v2/core/vault/gb_bank_accounts/{id}/initiate_confirmation_of_payee".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
