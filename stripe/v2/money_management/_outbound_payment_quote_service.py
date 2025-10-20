# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._outbound_payment_quote_create_params import (
        OutboundPaymentQuoteCreateParams,
    )
    from stripe.params.v2.money_management._outbound_payment_quote_retrieve_params import (
        OutboundPaymentQuoteRetrieveParams,
    )
    from stripe.v2.money_management._outbound_payment_quote import (
        OutboundPaymentQuote,
    )


class OutboundPaymentQuoteService(StripeService):
    def create(
        self,
        params: "OutboundPaymentQuoteCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPaymentQuote":
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            "OutboundPaymentQuote",
            self._request(
                "post",
                "/v2/money_management/outbound_payment_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundPaymentQuoteCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPaymentQuote":
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            "OutboundPaymentQuote",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payment_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OutboundPaymentQuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPaymentQuote":
        """
        Retrieves the details of an existing OutboundPaymentQuote by passing the unique OutboundPaymentQuote ID.
        """
        return cast(
            "OutboundPaymentQuote",
            self._request(
                "get",
                "/v2/money_management/outbound_payment_quotes/{id}".format(
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
        params: Optional["OutboundPaymentQuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPaymentQuote":
        """
        Retrieves the details of an existing OutboundPaymentQuote by passing the unique OutboundPaymentQuote ID.
        """
        return cast(
            "OutboundPaymentQuote",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_payment_quotes/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
