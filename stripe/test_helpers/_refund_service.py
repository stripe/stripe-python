# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._refund import Refund
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, Optional, cast
from typing_extensions import NotRequired, TypedDict


class RefundService(StripeService):
    class ExpireParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def expire(
        self,
        refund: str,
        params: "RefundService.ExpireParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Refund:
        """
        Expire a refund with a status of requires_action.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Refund,
            self._request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=sanitize_id(refund),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def expire_async(
        self,
        refund: str,
        params: "RefundService.ExpireParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Refund:
        """
        Expire a refund with a status of requires_action.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Refund,
            await self._request_async(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=sanitize_id(refund),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
