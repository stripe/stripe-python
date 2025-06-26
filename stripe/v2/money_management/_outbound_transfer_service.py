# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._outbound_transfer import OutboundTransfer
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundTransferService(StripeService):
    class CancelParams(TypedDict):
        pass

    _CreateParamsBase = TypedDict(
        "CreateParams",
        {"from": "OutboundTransferService.CreateParamsFrom"},
    )

    class CreateParams(_CreateParamsBase):
        amount: AmountParam
        """
        The "presentment amount" for the OutboundPayment.
        """
        delivery_options: NotRequired[
            "OutboundTransferService.CreateParamsDeliveryOptions"
        ]
        """
        Delivery options to be used to send the OutboundTransfer.
        """
        description: NotRequired[str]
        """
        An arbitrary string attached to the OutboundTransfer. Often useful for displaying to users.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        to: "OutboundTransferService.CreateParamsTo"
        """
        To which payout method to send the OutboundTransfer.
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
        payout_method: str
        """
        The payout method which the OutboundTransfer uses to send payout.
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
        status: NotRequired[
            List[
                Literal[
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ]
        ]
        """
        Closed Enum. Only return OutboundTransfers with this status.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "OutboundTransferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundTransfer]:
        """
        Returns a list of OutboundTransfers that match the provided filters.
        """
        return cast(
            ListObject[OutboundTransfer],
            self._request(
                "get",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "OutboundTransferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OutboundTransfer]:
        """
        Returns a list of OutboundTransfers that match the provided filters.
        """
        return cast(
            ListObject[OutboundTransfer],
            await self._request_async(
                "get",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OutboundTransferService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Creates an OutboundTransfer.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "post",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundTransferService.CreateParams",
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Creates an OutboundTransfer.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "OutboundTransferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundPayment create or list response.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "get",
                "/v2/money_management/outbound_transfers/{id}".format(
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
        params: "OutboundTransferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundPayment create or list response.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "get",
                "/v2/money_management/outbound_transfers/{id}".format(
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
        params: "OutboundTransferService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Cancels an OutboundTransfer. Only processing OutboundTransfers can be canceled.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "post",
                "/v2/money_management/outbound_transfers/{id}/cancel".format(
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
        params: "OutboundTransferService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Cancels an OutboundTransfer. Only processing OutboundTransfers can be canceled.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "post",
                "/v2/money_management/outbound_transfers/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
