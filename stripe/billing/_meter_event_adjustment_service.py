# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.billing._meter_event_adjustment import MeterEventAdjustment
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class MeterEventAdjustmentService(StripeService):
    class CreateParams(TypedDict):
        cancel: "MeterEventAdjustmentService.CreateParamsCancel"
        """
        Specifies which event to cancel.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        type: NotRequired[Literal["cancel"]]
        """
        Specifies whether to cancel a single event or a range of events for a time period.
        """

    class CreateParamsCancel(TypedDict):
        identifier: str
        """
        Unique identifier for the event.
        """

    def create(
        self,
        params: "MeterEventAdjustmentService.CreateParams",
        options: RequestOptions = {},
    ) -> MeterEventAdjustment:
        """
        Creates a billing meter event adjustment
        """
        return cast(
            MeterEventAdjustment,
            self._request(
                "post",
                "/v1/billing/meter_event_adjustments",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "MeterEventAdjustmentService.CreateParams",
        options: RequestOptions = {},
    ) -> MeterEventAdjustment:
        """
        Creates a billing meter event adjustment
        """
        return cast(
            MeterEventAdjustment,
            await self._request_async(
                "post",
                "/v1/billing/meter_event_adjustments",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
