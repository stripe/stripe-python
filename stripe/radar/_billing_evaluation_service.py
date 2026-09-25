# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.radar._billing_evaluation_create_params import (
        BillingEvaluationCreateParams,
    )
    from stripe.radar._billing_evaluation import BillingEvaluation


class BillingEvaluationService(StripeService):
    def create(
        self,
        params: "BillingEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BillingEvaluation":
        """
        Request Stripe Radar's assessment of the non-payment abuse risk of an upcoming charge, before the payment is attempted.
        """
        return cast(
            "BillingEvaluation",
            self._request(
                "post",
                "/v1/radar/billing_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "BillingEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BillingEvaluation":
        """
        Request Stripe Radar's assessment of the non-payment abuse risk of an upcoming charge, before the payment is attempted.
        """
        return cast(
            "BillingEvaluation",
            await self._request_async(
                "post",
                "/v1/radar/billing_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
