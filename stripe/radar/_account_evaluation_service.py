# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.radar._account_evaluation_create_params import (
        AccountEvaluationCreateParams,
    )
    from stripe.params.radar._account_evaluation_retrieve_params import (
        AccountEvaluationRetrieveParams,
    )
    from stripe.params.radar._account_evaluation_update_params import (
        AccountEvaluationUpdateParams,
    )
    from stripe.radar._account_evaluation import AccountEvaluation


class AccountEvaluationService(StripeService):
    def retrieve(
        self,
        account_evaluation: str,
        params: Optional["AccountEvaluationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Retrieves an AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            self._request(
                "get",
                "/v1/radar/account_evaluations/{account_evaluation}".format(
                    account_evaluation=sanitize_id(account_evaluation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_evaluation: str,
        params: Optional["AccountEvaluationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Retrieves an AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            await self._request_async(
                "get",
                "/v1/radar/account_evaluations/{account_evaluation}".format(
                    account_evaluation=sanitize_id(account_evaluation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "AccountEvaluationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Creates a new AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            self._request(
                "post",
                "/v1/radar/account_evaluations",
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
        Creates a new AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            await self._request_async(
                "post",
                "/v1/radar/account_evaluations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        account_evaluation: str,
        params: "AccountEvaluationUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Reports an event on an AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            self._request(
                "post",
                "/v1/radar/account_evaluations/{account_evaluation}/report_event".format(
                    account_evaluation=sanitize_id(account_evaluation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        account_evaluation: str,
        params: "AccountEvaluationUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountEvaluation":
        """
        Reports an event on an AccountEvaluation object.
        """
        return cast(
            "AccountEvaluation",
            await self._request_async(
                "post",
                "/v1/radar/account_evaluations/{account_evaluation}/report_event".format(
                    account_evaluation=sanitize_id(account_evaluation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
