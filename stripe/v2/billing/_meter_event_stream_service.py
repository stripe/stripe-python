# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import Dict, List
from typing_extensions import NotRequired, TypedDict


class MeterEventStreamService(StripeService):
    class CreateParams(TypedDict):
        events: List["MeterEventStreamService.CreateParamsEvent"]
        """
        List of meter events to include in the request.
        """

    class CreateParamsEvent(TypedDict):
        event_name: str
        """
        The name of the meter event. Corresponds with the `event_name` field on a meter.
        """
        identifier: NotRequired[str]
        """
        A unique identifier for the event. If not provided, one will be generated.
        We recommend using a globally unique identifier for this. We'll enforce
        uniqueness within a rolling 24 hour period.
        """
        payload: Dict[str, str]
        """
        The payload of the event. This must contain the fields corresponding to a meter's
        `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and
        `value_settings.event_payload_key` (default is `value`). Read more about
        the
        [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
        """
        timestamp: NotRequired[str]
        """
        The time of the event. Must be within the past 35 calendar days or up to
        5 minutes in the future. Defaults to current timestamp if not specified.
        """

    def create(
        self,
        params: "MeterEventStreamService.CreateParams",
        options: RequestOptions = {},
    ) -> None:
        """
        Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.
        """
        self._request(
            "post",
            "/v2/billing/meter_event_stream",
            base_address="meter_events",
            params=params,
            options=options,
        )

    async def create_async(
        self,
        params: "MeterEventStreamService.CreateParams",
        options: RequestOptions = {},
    ) -> None:
        """
        Creates meter events. Events are processed asynchronously, including validation. Requires a meter event session for authentication. Supports up to 10,000 requests per second in livemode. For even higher rate-limits, contact sales.
        """
        await self._request_async(
            "post",
            "/v2/billing/meter_event_stream",
            base_address="meter_events",
            params=params,
            options=options,
        )
