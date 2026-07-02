# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.crypto._onramp_transaction_limits import (
        OnrampTransactionLimits,
    )
    from stripe.params.crypto._onramp_transaction_limits_retrieve_params import (
        OnrampTransactionLimitsRetrieveParams,
    )


class OnrampTransactionLimitsService(StripeService):
    def retrieve(
        self,
        params: Optional["OnrampTransactionLimitsRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampTransactionLimits":
        """
        Retrieves the remaining onramp limit for a crypto customer.
        """
        return cast(
            "OnrampTransactionLimits",
            self._request(
                "get",
                "/v1/crypto/onramp_transaction_limits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: Optional["OnrampTransactionLimitsRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampTransactionLimits":
        """
        Retrieves the remaining onramp limit for a crypto customer.
        """
        return cast(
            "OnrampTransactionLimits",
            await self._request_async(
                "get",
                "/v1/crypto/onramp_transaction_limits",
                base_address="api",
                params=params,
                options=options,
            ),
        )
