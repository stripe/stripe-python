# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.radar._issuing_authorization_evaluation_create_params import (
        IssuingAuthorizationEvaluationCreateParams,
    )
    from stripe.radar._issuing_authorization_evaluation import (
        IssuingAuthorizationEvaluation,
    )


class IssuingAuthorizationEvaluationService(StripeService):
    def create(
        self,
        params: "IssuingAuthorizationEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "IssuingAuthorizationEvaluation":
        """
        Request a fraud risk assessment from Stripe for an Issuing card authorization.
        """
        return cast(
            "IssuingAuthorizationEvaluation",
            self._request(
                "post",
                "/v1/radar/issuing_authorization_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "IssuingAuthorizationEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "IssuingAuthorizationEvaluation":
        """
        Request a fraud risk assessment from Stripe for an Issuing card authorization.
        """
        return cast(
            "IssuingAuthorizationEvaluation",
            await self._request_async(
                "post",
                "/v1/radar/issuing_authorization_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
