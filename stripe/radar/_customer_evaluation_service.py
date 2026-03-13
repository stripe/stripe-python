# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.radar._customer_evaluation_create_params import (
        CustomerEvaluationCreateParams,
    )
    from stripe.radar._customer_evaluation import CustomerEvaluation


class CustomerEvaluationService(StripeService):
    def create(
        self,
        params: "CustomerEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerEvaluation":
        """
        Creates a new CustomerEvaluation object.
        """
        return cast(
            "CustomerEvaluation",
            self._request(
                "post",
                "/v1/radar/customer_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CustomerEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerEvaluation":
        """
        Creates a new CustomerEvaluation object.
        """
        return cast(
            "CustomerEvaluation",
            await self._request_async(
                "post",
                "/v1/radar/customer_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
