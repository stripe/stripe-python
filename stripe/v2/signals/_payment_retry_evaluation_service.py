# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.signals._payment_retry_evaluation_cancel_params import (
        PaymentRetryEvaluationCancelParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_create_params import (
        PaymentRetryEvaluationCreateParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_retrieve_params import (
        PaymentRetryEvaluationRetrieveParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_update_params import (
        PaymentRetryEvaluationUpdateParams,
    )
    from stripe.v2.signals._payment_retry_evaluation import (
        PaymentRetryEvaluation,
    )


class PaymentRetryEvaluationService(StripeService):
    def create(
        self,
        params: Optional["PaymentRetryEvaluationCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Creates a new payment retry evaluation for a failed payment.
        """
        return cast(
            "PaymentRetryEvaluation",
            self._request(
                "post",
                "/v2/signals/payment_retry_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["PaymentRetryEvaluationCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Creates a new payment retry evaluation for a failed payment.
        """
        return cast(
            "PaymentRetryEvaluation",
            await self._request_async(
                "post",
                "/v2/signals/payment_retry_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PaymentRetryEvaluationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Retrieves a payment retry evaluation by ID.
        """
        return cast(
            "PaymentRetryEvaluation",
            self._request(
                "get",
                "/v2/signals/payment_retry_evaluations/{id}".format(
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
        params: Optional["PaymentRetryEvaluationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Retrieves a payment retry evaluation by ID.
        """
        return cast(
            "PaymentRetryEvaluation",
            await self._request_async(
                "get",
                "/v2/signals/payment_retry_evaluations/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["PaymentRetryEvaluationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Updates an active payment retry evaluation with a replacement payment identifier.
        """
        return cast(
            "PaymentRetryEvaluation",
            self._request(
                "post",
                "/v2/signals/payment_retry_evaluations/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["PaymentRetryEvaluationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Updates an active payment retry evaluation with a replacement payment identifier.
        """
        return cast(
            "PaymentRetryEvaluation",
            await self._request_async(
                "post",
                "/v2/signals/payment_retry_evaluations/{id}".format(
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
        params: Optional["PaymentRetryEvaluationCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Cancels an active payment retry evaluation.
        """
        return cast(
            "PaymentRetryEvaluation",
            self._request(
                "post",
                "/v2/signals/payment_retry_evaluations/{id}/cancel".format(
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
        params: Optional["PaymentRetryEvaluationCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentRetryEvaluation":
        """
        Cancels an active payment retry evaluation.
        """
        return cast(
            "PaymentRetryEvaluation",
            await self._request_async(
                "post",
                "/v2/signals/payment_retry_evaluations/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
