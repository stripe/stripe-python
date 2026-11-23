# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.risk._evaluation_outcome_list_params import (
        EvaluationOutcomeListParams,
    )
    from stripe.params.v2.risk._evaluation_outcome_retrieve_params import (
        EvaluationOutcomeRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.risk._evaluation_outcome import EvaluationOutcome


class EvaluationOutcomeService(StripeService):
    def list(
        self,
        params: "EvaluationOutcomeListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[EvaluationOutcome]":
        """
        Lists all matching historical evaluation outcomes, newest first.
        """
        return cast(
            "ListObject[EvaluationOutcome]",
            self._request(
                "get",
                "/v2/risk/evaluation_outcomes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "EvaluationOutcomeListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[EvaluationOutcome]":
        """
        Lists all matching historical evaluation outcomes, newest first.
        """
        return cast(
            "ListObject[EvaluationOutcome]",
            await self._request_async(
                "get",
                "/v2/risk/evaluation_outcomes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["EvaluationOutcomeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "EvaluationOutcome":
        """
        Retrieves an evaluation outcome by its ID.
        """
        return cast(
            "EvaluationOutcome",
            self._request(
                "get",
                "/v2/risk/evaluation_outcomes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["EvaluationOutcomeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "EvaluationOutcome":
        """
        Retrieves an evaluation outcome by its ID.
        """
        return cast(
            "EvaluationOutcome",
            await self._request_async(
                "get",
                "/v2/risk/evaluation_outcomes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
