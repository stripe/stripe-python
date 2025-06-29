# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.core.vault._gb_bank_account import GbBankAccount
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class GbBankAccountService(StripeService):
    class AcknowledgeConfirmationOfPayeeParams(TypedDict):
        pass

    class ArchiveParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        account_number: str
        """
        The Account Number of the bank account.
        """
        bank_account_type: NotRequired[Literal["checking", "savings"]]
        """
        Closed Enum. The type of the bank account (checking or savings).
        """
        confirmation_of_payee: NotRequired[
            "GbBankAccountService.CreateParamsConfirmationOfPayee"
        ]
        """
        Whether or not to automatically perform Confirmation of Payee to verify the users information
        against what was provided by the bank. Doing so is required for all bank accounts not owned
        by you before making domestic UK OutboundPayments.
        """
        sort_code: str
        """
        The Sort Code of the bank account.
        """

    class CreateParamsConfirmationOfPayee(TypedDict):
        business_type: NotRequired[Literal["business", "personal"]]
        """
        The business type to be checked against. Legal entity information will be used if unspecified.
        Closed enum.
        """
        initiate: bool
        """
        User specifies whether Confirmation of Payee is automatically initiated when creating the bank account.
        """
        name: NotRequired[str]
        """
        The name to be checked against. Legal entity information will be used if unspecified.
        """

    class InitiateConfirmationOfPayeeParams(TypedDict):
        business_type: NotRequired[Literal["business", "personal"]]
        """
        The business type to be checked against. Legal entity information will be used if unspecified.
        """
        name: NotRequired[str]
        """
        The name of the user to be checked against. Legal entity information will be used if unspecified.
        """

    class RetrieveParams(TypedDict):
        pass

    def create(
        self,
        params: "GbBankAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Create a GB bank account.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Create a GB bank account.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Retrieve a GB bank account.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Retrieve a GB bank account.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.AcknowledgeConfirmationOfPayeeParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Confirm that you have received the result of the Confirmation of Payee request, and that you are okay with
        proceeding to pay out to this bank account despite the account not matching, partially matching, or the service
        being unavailable. Once you confirm this, you will be able to send OutboundPayments, but this may lead to
        funds being sent to the wrong account, which we might not be able to recover.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.AcknowledgeConfirmationOfPayeeParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Confirm that you have received the result of the Confirmation of Payee request, and that you are okay with
        proceeding to pay out to this bank account despite the account not matching, partially matching, or the service
        being unavailable. Once you confirm this, you will be able to send OutboundPayments, but this may lead to
        funds being sent to the wrong account, which we might not be able to recover.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Archive a GBBankAccount object. Archived GBBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Archive a GBBankAccount object. Archived GBBankAccount objects cannot be used as outbound destinations
        and will not appear in the outbound destination list.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.InitiateConfirmationOfPayeeParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Initiate Confirmation of Payee (CoP) in order to verify that the owner of a UK bank account matches
        who you expect. This must be done on all UK bank accounts before sending domestic OutboundPayments. If
        the result is a partial match or a non match, explicit acknowledgement using AcknowledgeConfirmationOfPayee
        is required before sending funds.
        """
        return cast(
            GbBankAccount,
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
        params: "GbBankAccountService.InitiateConfirmationOfPayeeParams" = {},
        options: RequestOptions = {},
    ) -> GbBankAccount:
        """
        Initiate Confirmation of Payee (CoP) in order to verify that the owner of a UK bank account matches
        who you expect. This must be done on all UK bank accounts before sending domestic OutboundPayments. If
        the result is a partial match or a non match, explicit acknowledgement using AcknowledgeConfirmationOfPayee
        is required before sending funds.
        """
        return cast(
            GbBankAccount,
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
