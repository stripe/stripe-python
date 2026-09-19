# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.orchestration._payment_attempt import PaymentAttempt
    from stripe.params.orchestration._payment_attempt_retrieve_params import (
        PaymentAttemptRetrieveParams,
    )


class PaymentAttemptService(StripeService):
    def retrieve(
        self,
        id: str,
        /,
        params: Optional["PaymentAttemptRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttempt":
        """
        Retrieves orchestration information for the given payment attempt record (e.g. return url).
        """
        return cast(
            "PaymentAttempt",
            self._request(
                "get",
                "/v1/orchestration/payment_attempts/{id}".format(
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
        /,
        params: Optional["PaymentAttemptRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttempt":
        """
        Retrieves orchestration information for the given payment attempt record (e.g. return url).
        """
        return cast(
            "PaymentAttempt",
            await self._request_async(
                "get",
                "/v1/orchestration/payment_attempts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
