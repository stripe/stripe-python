# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._outbound_payment import OutboundPayment
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundPaymentService(StripeService):
    class CancelParams(TypedDict):
        pass

    _CreateParamsBase = TypedDict(
        "CreateParams",
        {"from": "OutboundPaymentService.CreateParamsFrom"},
    )

    class CreateParams(_CreateParamsBase):
        amount: AmountParam
        """
        The "presentment amount" to be sent to the recipient.
        """
        delivery_options: NotRequired[
            "OutboundPaymentService.CreateParamsDeliveryOptions"
        ]
        """
        Delivery options to be used to send the OutboundPayment.
        """
        description: NotRequired[str]
        """
        An arbitrary string attached to the OutboundPayment. Often useful for displaying to users.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        outbound_payment_quote: NotRequired[str]
        """
        The quote for this OutboundPayment. Only required for countries with regulatory mandates to display fee estimates before OutboundPayment creation.
        """
        recipient_notification: NotRequired[
            "OutboundPaymentService.CreateParamsRecipientNotification"
        ]
        """
        Details about the notification settings for the OutboundPayment recipient.
        """
        to: "OutboundPaymentService.CreateParamsTo"
        """
        To which payout method to send the OutboundPayment.
        """

    class CreateParamsDeliveryOptions(TypedDict):
        bank_account: NotRequired[Literal["automatic", "local", "wire"]]
        """
        Open Enum. Method for bank account.
        """

    class CreateParamsFrom(TypedDict):
        currency: str
        """
        Describes the FinancialAmount's currency drawn from.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """

    class CreateParamsRecipientNotification(TypedDict):
        setting: Literal["configured", "none"]
        """
        Closed Enum. Configuration option to enable or disable notifications to recipients.
        Do not send notifications when setting is NONE. Default to account setting when setting is CONFIGURED or not set.
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

    class ListParams(TypedDict):
        created: NotRequired[str]
        """
        Filter for objects created at the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_gt: NotRequired[str]
        """
        Filter for objects created after the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_gte: NotRequired[str]
        """
        Filter for objects created on or after the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_lt: NotRequired[str]
        """
        Filter for objects created before the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        created_lte: NotRequired[str]
        """
        Filter for objects created on or before the specified timestamp.
        Must be an RFC 3339 date & time value, for example: 2022-09-18T13:22:00Z.
        """
        limit: NotRequired[int]
        """
        The maximum number of results to return.
        """
        recipient: NotRequired[str]
        """
        Only return OutboundPayments sent to this recipient.
        """
        status: NotRequired[
            List[
                Literal[
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ]
        ]
        """
        Closed Enum. Only return OutboundPayments with this status.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "OutboundPaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundPayment]:
        """
        Returns a list of OutboundPayments that match the provided filters.
        """
        return cast(
            ListObject[OutboundPayment],
            self._request(
                "get",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "OutboundPaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundPayment]:
        """
        Returns a list of OutboundPayments that match the provided filters.
        """
        return cast(
            ListObject[OutboundPayment],
            await self._request_async(
                "get",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OutboundPaymentService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Creates an OutboundPayment.
        """
        return cast(
            OutboundPayment,
            self._request(
                "post",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundPaymentService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Creates an OutboundPayment.
        """
        return cast(
            OutboundPayment,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "OutboundPaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment create or list response.
        """
        return cast(
            OutboundPayment,
            self._request(
                "get",
                "/v2/money_management/outbound_payments/{id}".format(
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
        params: "OutboundPaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment create or list response.
        """
        return cast(
            OutboundPayment,
            await self._request_async(
                "get",
                "/v2/money_management/outbound_payments/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "OutboundPaymentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Cancels an OutboundPayment. Only processing OutboundPayments can be canceled.
        """
        return cast(
            OutboundPayment,
            self._request(
                "post",
                "/v2/money_management/outbound_payments/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "OutboundPaymentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Cancels an OutboundPayment. Only processing OutboundPayments can be canceled.
        """
        return cast(
            OutboundPayment,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payments/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
