# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._refund import Refund
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class RefundService(StripeService):
    class ExpireParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def expire(
        self,
        refund: str,
        params: "RefundService.ExpireParams" = {},
        options: RequestOptions = {},
    ) -> Refund:
        """
        Expire a refund with a status of requires_action.
        """
        return cast(
            Refund,
            self._requestor.request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=_util.sanitize_id(refund),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
