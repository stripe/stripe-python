# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2.money_management._outbound_payment_quote import (
    OutboundPaymentQuote,
)
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundPaymentQuoteService(StripeService):
    _CreateParamsBase = TypedDict(
        "CreateParams",
        {"from": "OutboundPaymentQuoteService.CreateParamsFrom"},
    )

    class CreateParams(_CreateParamsBase):
        amount: AmountParam
        """
        The "presentment amount" to be sent to the recipient.
        """
        delivery_options: NotRequired[
            "OutboundPaymentQuoteService.CreateParamsDeliveryOptions"
        ]
        """
        Method to be used to send the OutboundPayment.
        """
        to: "OutboundPaymentQuoteService.CreateParamsTo"
        """
        Request details about the recipient of an OutboundPaymentQuote.
        """

    class CreateParamsDeliveryOptions(TypedDict):
        bank_account: NotRequired[Literal["automatic", "local", "wire"]]
        """
        Open Enum. Method for bank account.
        """

    class CreateParamsFrom(TypedDict):
        currency: str
        """
        Describes the FinancialAccount's currency drawn from.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """

    class CreateParamsTo(TypedDict):
        currency: NotRequired[str]
        """
        Describes the currency to send to the recipient.
        If included, this currency must match a currency supported by the destination.
        Can be omitted in the following cases:
        - destination only supports one currency
        - destination supports multiple currencies and one of the currencies matches the FA currency
        - destination supports multiple currencies and one of the currencies matches the presentment currency
        Note - when both FA currency and presentment currency are supported, we pick the FA currency to minimize FX.
        """
        payout_method: NotRequired[str]
        """
        The payout method which the OutboundPayment uses to send payout.
        """
        recipient: str
        """
        To which account the OutboundPayment is sent.
        """

    class RetrieveParams(TypedDict):
        pass

    def create(
        self,
        params: "OutboundPaymentQuoteService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundPaymentQuote:
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            OutboundPaymentQuote,
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
        params: "OutboundPaymentQuoteService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundPaymentQuote:
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            OutboundPaymentQuote,
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
        params: "OutboundPaymentQuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPaymentQuote:
        """
        Retrieves the details of an existing OutboundPaymentQuote by passing the unique OutboundPaymentQuote ID.
        """
        return cast(
            OutboundPaymentQuote,
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
        params: "OutboundPaymentQuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPaymentQuote:
        """
        Retrieves the details of an existing OutboundPaymentQuote by passing the unique OutboundPaymentQuote ID.
        """
        return cast(
            OutboundPaymentQuote,
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
