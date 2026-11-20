# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.test_helpers._money_management_recipient_verifications_params import (
        MoneyManagementRecipientVerificationsParams,
    )
    from stripe.v2.money_management._recipient_verification import (
        RecipientVerification,
    )


class MoneyManagementService(StripeService):
    def recipient_verifications(
        self,
        params: "MoneyManagementRecipientVerificationsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Creates a RecipientVerification with a specified match result for testing purposes in a Sandbox environment.
        """
        return cast(
            "RecipientVerification",
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
        params: "MoneyManagementRecipientVerificationsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Creates a RecipientVerification with a specified match result for testing purposes in a Sandbox environment.
        """
        return cast(
            "RecipientVerification",
            await self._request_async(
                "post",
                "/v2/test_helpers/money_management/recipient_verifications",
                base_address="api",
                params=params,
                options=options,
            ),
        )
