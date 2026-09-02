# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.signals._payment_retry_signal_retrieve_params import (
        PaymentRetrySignalRetrieveParams,
    )
    from stripe.v2.signals._payment_retry_signal import PaymentRetrySignal


class PaymentRetrySignalService(StripeService):
    def retrieve(
        self,
        id: str,
        params: Optional["PaymentRetrySignalRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetrySignal":
        """
        Retrieves a payment retry signal by ID.
        """
        return cast(
            "PaymentRetrySignal",
            self._request(
                "get",
                "/v2/signals/payment_retry_signals/{id}".format(
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
        params: Optional["PaymentRetrySignalRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetrySignal":
        """
        Retrieves a payment retry signal by ID.
        """
        return cast(
            "PaymentRetrySignal",
            await self._request_async(
                "get",
                "/v2/signals/payment_retry_signals/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
