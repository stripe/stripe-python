# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_intent import PaymentIntent
    from stripe._request_options import RequestOptions
    from stripe.params.test_helpers._payment_intent_simulate_crypto_deposit_params import (
        PaymentIntentSimulateCryptoDepositParams,
    )


class PaymentIntentService(StripeService):
    def simulate_crypto_deposit(
        self,
        intent: str,
        params: "PaymentIntentSimulateCryptoDepositParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentIntent":
        """
        Simulate an incoming crypto deposit for a testmode PaymentIntent with payment_method_options[crypto][mode]=deposit. The transaction_hash parameter determines whether the simulated deposit succeeds or fails. Learn more about [testing your integration](https://docs.stripe.com/docs/payments/deposit-mode-stablecoin-payments#test-your-integration).
        """
        return cast(
            "PaymentIntent",
            self._request(
                "post",
                "/v1/test_helpers/payment_intents/{intent}/simulate_crypto_deposit".format(
                    intent=sanitize_id(intent),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def simulate_crypto_deposit_async(
        self,
        intent: str,
        params: "PaymentIntentSimulateCryptoDepositParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentIntent":
        """
        Simulate an incoming crypto deposit for a testmode PaymentIntent with payment_method_options[crypto][mode]=deposit. The transaction_hash parameter determines whether the simulated deposit succeeds or fails. Learn more about [testing your integration](https://docs.stripe.com/docs/payments/deposit-mode-stablecoin-payments#test-your-integration).
        """
        return cast(
            "PaymentIntent",
            await self._request_async(
                "post",
                "/v1/test_helpers/payment_intents/{intent}/simulate_crypto_deposit".format(
                    intent=sanitize_id(intent),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
