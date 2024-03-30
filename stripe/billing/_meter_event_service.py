# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.billing._meter_event import MeterEvent
from typing import Dict, List, cast
from typing_extensions import NotRequired, TypedDict


class MeterEventService(StripeService):
    class CreateParams(TypedDict):
        event_name: str
        """
        The name of the meter event. Corresponds with the `event_name` field on a meter.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        identifier: NotRequired[str]
        """
        A unique identifier for the event. If not provided, one will be generated.
        """
        payload: Dict[str, str]
        """
        The payload of the event. This must contain a field with the event's numerical value and a field to map the event to a customer.
        """
        timestamp: int
        """
        The time of the event. Measured in seconds since the Unix epoch.
        """

    def create(
        self,
        params: "MeterEventService.CreateParams",
        options: RequestOptions = {},
    ) -> MeterEvent:
        """
        Creates a billing meter event
        """
        return cast(
            MeterEvent,
            self._request(
                "post",
                "/v1/billing/meter_events",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
