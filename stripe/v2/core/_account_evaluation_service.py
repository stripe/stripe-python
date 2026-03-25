# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._account_evaluation_create_params import (
        AccountEvaluationCreateParams,
    )
    from stripe.v2.core._account_evaluation import AccountEvaluation


class AccountEvaluationService(StripeService):
    def create(
        self,
        params: "AccountEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Creates a new account evaluation to trigger signal evaluations on an account or account data.
        """
        return cast(
            "AccountEvaluation",
            self._request(
                "post",
                "/v2/core/account_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Creates a new account evaluation to trigger signal evaluations on an account or account data.
        """
        return cast(
            "AccountEvaluation",
            await self._request_async(
                "post",
                "/v2/core/account_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
