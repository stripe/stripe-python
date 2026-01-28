# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.reserve._plan_retrieve_params import PlanRetrieveParams
    from stripe.reserve._plan import Plan


class PlanService(StripeService):
    def retrieve(
        self,
        id: str,
        params: Optional["PlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Plan":
        """
        Retrieve a ReservePlan.
        """
        return cast(
            "Plan",
            self._request(
                "get",
                "/v1/reserve/plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["PlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Plan":
        """
        Retrieve a ReservePlan.
        """
        return cast(
            "Plan",
            await self._request_async(
                "get",
                "/v1/reserve/plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
