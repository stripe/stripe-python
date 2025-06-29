# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._inbound_transfer import InboundTransfer
from typing import cast
from typing_extensions import NotRequired, TypedDict


class InboundTransferService(StripeService):
    _CreateParamsBase = TypedDict(
        "CreateParams",
        {"from": "InboundTransferService.CreateParamsFrom"},
    )

    class CreateParams(_CreateParamsBase):
        amount: AmountParam
        """
        The amount, in specified currency, by which the FinancialAccount balance will increase due to the InboundTransfer.
        """
        description: NotRequired[str]
        """
        An optional, freeform description field intended to store metadata.
        """
        to: "InboundTransferService.CreateParamsTo"
        """
        Object containing details about where the funds will land.
        """

    class CreateParamsFrom(TypedDict):
        currency: NotRequired[str]
        """
        An optional currency field used to specify which currency is debited from the Payment Method.
        Since many Payment Methods support only one currency, this field is optional.
        """
        payment_method: str
        """
        ID of the Payment Method using which IBT will be made.
        """

    class CreateParamsTo(TypedDict):
        currency: str
        """
        The currency in which funds will land in.
        """
        financial_account: str
        """
        The FinancialAccount that funds will land in.
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
        The page limit.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "InboundTransferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InboundTransfer]:
        """
        Retrieves a list of InboundTransfers.
        """
        return cast(
            ListObject[InboundTransfer],
            self._request(
                "get",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InboundTransferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InboundTransfer]:
        """
        Retrieves a list of InboundTransfers.
        """
        return cast(
            ListObject[InboundTransfer],
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "InboundTransferService.CreateParams",
        options: RequestOptions = {},
    ) -> InboundTransfer:
        """
        InboundTransfers APIs are used to create, retrieve or list InboundTransfers.
        """
        return cast(
            InboundTransfer,
            self._request(
                "post",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "InboundTransferService.CreateParams",
        options: RequestOptions = {},
    ) -> InboundTransfer:
        """
        InboundTransfers APIs are used to create, retrieve or list InboundTransfers.
        """
        return cast(
            InboundTransfer,
            await self._request_async(
                "post",
                "/v2/money_management/inbound_transfers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "InboundTransferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InboundTransfer:
        """
        Retrieve an InboundTransfer by ID.
        """
        return cast(
            InboundTransfer,
            self._request(
                "get",
                "/v2/money_management/inbound_transfers/{id}".format(
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
        params: "InboundTransferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InboundTransfer:
        """
        Retrieve an InboundTransfer by ID.
        """
        return cast(
            InboundTransfer,
            await self._request_async(
                "get",
                "/v2/money_management/inbound_transfers/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
