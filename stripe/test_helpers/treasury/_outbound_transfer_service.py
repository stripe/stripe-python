# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.treasury._outbound_transfer import OutboundTransfer
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundTransferService(StripeService):
    class FailParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class PostParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReturnOutboundTransferParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        returned_details: NotRequired[
            "OutboundTransferService.ReturnOutboundTransferParamsReturnedDetails"
        ]
        """
        Details about a returned OutboundTransfer.
        """

    class ReturnOutboundTransferParamsReturnedDetails(TypedDict):
        code: NotRequired[
            Literal[
                "account_closed",
                "account_frozen",
                "bank_account_restricted",
                "bank_ownership_changed",
                "declined",
                "incorrect_account_holder_name",
                "invalid_account_number",
                "invalid_currency",
                "no_account",
                "other",
            ]
        ]
        """
        Reason for the return.
        """

    def fail(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.FailParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def fail_async(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.FailParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def post(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.PostParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def post_async(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.PostParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def return_outbound_transfer(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.ReturnOutboundTransferParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            self._request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def return_outbound_transfer_async(
        self,
        outbound_transfer: str,
        params: "OutboundTransferService.ReturnOutboundTransferParams" = {},
        options: RequestOptions = {},
    ) -> OutboundTransfer:
        """
        Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
        """
        return cast(
            OutboundTransfer,
            await self._request_async(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                    outbound_transfer=sanitize_id(outbound_transfer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
