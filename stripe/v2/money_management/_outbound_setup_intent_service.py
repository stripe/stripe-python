# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._outbound_setup_intent import (
    OutboundSetupIntent,
)
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundSetupIntentService(StripeService):
    class CancelParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        payout_method: NotRequired[str]
        """
        If provided, the existing payout method resource to link to this setup intent.
        Any payout_method_data provided is used to update information on this linked payout method resource.
        """
        payout_method_data: NotRequired[
            "OutboundSetupIntentService.CreateParamsPayoutMethodData"
        ]
        """
        If no payout_method provided, used to create the underlying credential that is set up for outbound money movement.
        If a payout_method provided, used to update data on the credential linked to this setup intent.
        """
        usage_intent: NotRequired[Literal["payment", "transfer"]]
        """
        Specify which type of outbound money movement this credential should be set up for (payment | transfer).
        If not provided, defaults to payment.
        """

    class CreateParamsPayoutMethodData(TypedDict):
        type: Literal["bank_account", "card"]
        """
        Closed Enum. The type of payout method to be created.
        """
        bank_account: NotRequired[
            "OutboundSetupIntentService.CreateParamsPayoutMethodDataBankAccount"
        ]
        """
        The type specific details of the bank account payout method.
        """
        card: NotRequired[
            "OutboundSetupIntentService.CreateParamsPayoutMethodDataCard"
        ]
        """
        The type specific details of the card payout method.
        """

    class CreateParamsPayoutMethodDataBankAccount(TypedDict):
        account_number: str
        """
        The account number or IBAN of the bank account.
        """
        bank_account_type: NotRequired[Literal["checking", "savings"]]
        """
        Closed Enum. The type of the bank account (checking or savings).
        """
        branch_number: NotRequired[str]
        """
        The branch number of the bank account, if present.
        """
        country: str
        """
        The country code of the bank account.
        """
        routing_number: NotRequired[str]
        """
        The routing number of the bank account, if present.
        """
        swift_code: NotRequired[str]
        """
        The swift code of the bank account, if present.
        """

    class CreateParamsPayoutMethodDataCard(TypedDict):
        exp_month: str
        """
        The expiration month of the card.
        """
        exp_year: str
        """
        The expiration year of the card.
        """
        number: str
        """
        The card number.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page size.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        payout_method: NotRequired[str]
        """
        If provided, the existing payout method resource to link to this outbound setup intent.
        """
        payout_method_data: NotRequired[
            "OutboundSetupIntentService.UpdateParamsPayoutMethodData"
        ]
        """
        If no payout_method provided, used to create the underlying credential that is set up for outbound money movement.
        If a payout_method provided, used to update data on the credential linked to this setup intent.
        """

    class UpdateParamsPayoutMethodData(TypedDict):
        type: Literal["bank_account", "card"]
        """
        Closed Enum. The type of payout method to be created/updated.
        """
        bank_account: NotRequired[
            "OutboundSetupIntentService.UpdateParamsPayoutMethodDataBankAccount"
        ]
        """
        The type specific details of the bank account payout method.
        """
        card: NotRequired[
            "OutboundSetupIntentService.UpdateParamsPayoutMethodDataCard"
        ]
        """
        The type specific details of the card payout method.
        """

    class UpdateParamsPayoutMethodDataBankAccount(TypedDict):
        account_number: str
        """
        The account number or IBAN of the bank account.
        """
        bank_account_type: NotRequired[Literal["checking", "savings"]]
        """
        Closed Enum. The type of the bank account (checking or savings).
        """
        branch_number: NotRequired[str]
        """
        The branch number of the bank account, if present.
        """
        country: str
        """
        The country code of the bank account.
        """
        routing_number: NotRequired[str]
        """
        The routing number of the bank account, if present.
        """
        swift_code: NotRequired[str]
        """
        The swift code of the bank account, if present.
        """

    class UpdateParamsPayoutMethodDataCard(TypedDict):
        exp_month: NotRequired[str]
        """
        The expiration month of the card.
        """
        exp_year: NotRequired[str]
        """
        The expiration year of the card.
        """
        number: NotRequired[str]
        """
        The card number. This can only be passed when creating a new credential on an outbound setup intent in the requires_payout_method state.
        """

    def list(
        self,
        params: "OutboundSetupIntentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundSetupIntent]:
        """
        List the OutboundSetupIntent objects.
        """
        return cast(
            ListObject[OutboundSetupIntent],
            self._request(
                "get",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "OutboundSetupIntentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundSetupIntent]:
        """
        List the OutboundSetupIntent objects.
        """
        return cast(
            ListObject[OutboundSetupIntent],
            await self._request_async(
                "get",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OutboundSetupIntentService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Create an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundSetupIntentService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Create an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "OutboundSetupIntentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Retrieve an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            self._request(
                "get",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: "OutboundSetupIntentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Retrieve an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            await self._request_async(
                "get",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: "OutboundSetupIntentService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Update an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}".format(
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
        params: "OutboundSetupIntentService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Update an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "OutboundSetupIntentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Cancel an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            self._request(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "OutboundSetupIntentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundSetupIntent:
        """
        Cancel an OutboundSetupIntent object.
        """
        return cast(
            OutboundSetupIntent,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_setup_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
