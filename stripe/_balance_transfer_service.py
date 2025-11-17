# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._balance_transfer import BalanceTransfer
    from stripe._request_options import RequestOptions
    from stripe.params._balance_transfer_create_params import (
        BalanceTransferCreateParams,
    )


class BalanceTransferService(StripeService):
    def create(
        self,
        params: "BalanceTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BalanceTransfer":
        """
        Creates a balance transfer. For Issuing use cases, funds will be debited immediately from the source balance and credited to the destination balance immediately (if your account is based in the US) or next-business-day (if your account is based in the EU). For Segregated Separate Charges and Transfers use cases, funds will be debited immediately from the source balance and credited immediately to the destination balance.
        """
        return cast(
            "BalanceTransfer",
            self._request(
                "post",
                "/v1/balance_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "BalanceTransferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BalanceTransfer":
        """
        Creates a balance transfer. For Issuing use cases, funds will be debited immediately from the source balance and credited to the destination balance immediately (if your account is based in the US) or next-business-day (if your account is based in the EU). For Segregated Separate Charges and Transfers use cases, funds will be debited immediately from the source balance and credited immediately to the destination balance.
        """
        return cast(
            "BalanceTransfer",
            await self._request_async(
                "post",
                "/v1/balance_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )
