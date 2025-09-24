# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2.money_management._recipient_verification import (
    RecipientVerification,
)
from typing import Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class MoneyManagementService(StripeService):
    class RecipientVerificationsParams(TypedDict):
        match_result: Literal[
            "close_match", "match", "no_match", "unavailable"
        ]
        """
        Expected match level of the RecipientVerification to be created: `match`, `close_match`, `no_match`, `unavailable`.
        """
        payout_method: str
        """
        ID of the payout method.
        """
        recipient: NotRequired[str]
        """
        ID of the recipient account. Required if the recipient distinct from the sender. Leave empty if the recipient and sender are the same entity (i.e. for me-to-me payouts).
        """

    def recipient_verifications(
        self,
        params: "MoneyManagementService.RecipientVerificationsParams",
        options: Optional[RequestOptions] = None,
    ) -> RecipientVerification:
        """
        Creates a RecipientVerification with a specified match result for testing purposes in a Sandbox environment.
        """
        return cast(
            RecipientVerification,
            self._request(
                "post",
                "/v2/test_helpers/money_management/recipient_verifications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def recipient_verifications_async(
        self,
        params: "MoneyManagementService.RecipientVerificationsParams",
        options: Optional[RequestOptions] = None,
    ) -> RecipientVerification:
        """
        Creates a RecipientVerification with a specified match result for testing purposes in a Sandbox environment.
        """
        return cast(
            RecipientVerification,
            await self._request_async(
                "post",
                "/v2/test_helpers/money_management/recipient_verifications",
                base_address="api",
                params=params,
                options=options,
            ),
        )
