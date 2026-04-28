# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.data.analytics._metric_query_create_params import (
        MetricQueryCreateParams,
    )
    from stripe.v2.data.analytics._metric_query_result import MetricQueryResult


class MetricQueryService(StripeService):
    def create(
        self,
        params: "MetricQueryCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MetricQueryResult":
        """
        Run a synchronous metric query against one or more metrics within the same metric namespace.
        """
        return cast(
            "MetricQueryResult",
            self._request(
                "post",
                "/v2/data/analytics/metric_query",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "MetricQueryCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MetricQueryResult":
        """
        Run a synchronous metric query against one or more metrics within the same metric namespace.
        """
        return cast(
            "MetricQueryResult",
            await self._request_async(
                "post",
                "/v2/data/analytics/metric_query",
                base_address="api",
                params=params,
                options=options,
            ),
        )
