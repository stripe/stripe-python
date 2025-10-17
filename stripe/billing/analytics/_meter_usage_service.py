# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.billing.analytics._meter_usage import MeterUsage
    from stripe.params.billing.analytics._meter_usage_retrieve_params import (
        MeterUsageRetrieveParams,
    )


class MeterUsageService(StripeService):
    def retrieve(
        self,
        params: "MeterUsageRetrieveParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MeterUsage":
        """
        Returns aggregated meter usage data for a customer within a specified time interval. The data can be grouped by various dimensions and can include multiple meters if specified.
        """
        return cast(
            "MeterUsage",
            self._request(
                "get",
                "/v1/billing/analytics/meter_usage",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: "MeterUsageRetrieveParams",
        options: Optional["RequestOptions"] = None,
    ) -> "MeterUsage":
        """
        Returns aggregated meter usage data for a customer within a specified time interval. The data can be grouped by various dimensions and can include multiple meters if specified.
        """
        return cast(
            "MeterUsage",
            await self._request_async(
                "get",
                "/v1/billing/analytics/meter_usage",
                base_address="api",
                params=params,
                options=options,
            ),
        )
