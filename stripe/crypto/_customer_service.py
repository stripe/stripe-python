# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.crypto._customer import Customer
    from stripe.crypto._customer_consumer_wallet_service import (
        CustomerConsumerWalletService,
    )
    from stripe.crypto._customer_payment_token_service import (
        CustomerPaymentTokenService,
    )
    from stripe.params.crypto._customer_retrieve_params import (
        CustomerRetrieveParams,
    )

_subservices = {
    "consumer_wallets": [
        "stripe.crypto._customer_consumer_wallet_service",
        "CustomerConsumerWalletService",
    ],
    "payment_tokens": [
        "stripe.crypto._customer_payment_token_service",
        "CustomerPaymentTokenService",
    ],
}


class CustomerService(StripeService):
    consumer_wallets: "CustomerConsumerWalletService"
    payment_tokens: "CustomerPaymentTokenService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def retrieve(
        self,
        id: str,
        params: Optional["CustomerRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Customer":
        """
        Retrieves the details of a Crypto Customer.
        """
        return cast(
            "Customer",
            self._request(
                "get",
                "/v1/crypto/customers/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["CustomerRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Customer":
        """
        Retrieves the details of a Crypto Customer.
        """
        return cast(
            "Customer",
            await self._request_async(
                "get",
                "/v1/crypto/customers/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
