# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2._amount import AmountParam
from stripe.v2._outbound_payment_quote import OutboundPaymentQuote
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class QuoteService(StripeService):
    _CreateParamsBase = TypedDict(
        "CreateParams",
        {"from": "QuoteService.CreateParamsFrom"},
    )

    class CreateParams(_CreateParamsBase):
        amount: AmountParam
        """
        The "presentment amount" to be sent to the recipient.
        """
        delivery_options: NotRequired[
            "QuoteService.CreateParamsDeliveryOptions"
        ]
        """
        Method to be used to send the OutboundPayment.
        """
        to: "QuoteService.CreateParamsTo"
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

    def create(
        self, params: "QuoteService.CreateParams", options: RequestOptions = {}
    ) -> OutboundPaymentQuote:
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            OutboundPaymentQuote,
            self._request(
                "post",
                "/v2/money_management/outbound_payments/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self, params: "QuoteService.CreateParams", options: RequestOptions = {}
    ) -> OutboundPaymentQuote:
        """
        Creates an OutboundPaymentQuote usable in an OutboundPayment.
        """
        return cast(
            OutboundPaymentQuote,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payments/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )
