# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from typing import ClassVar, List, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class MeterEventAdjustment(CreateableAPIResource["MeterEventAdjustment"]):
    """
    A billing meter event adjustment represents the status of a meter event adjustment.
    """

    OBJECT_NAME: ClassVar[
        Literal["billing.meter_event_adjustment"]
    ] = "billing.meter_event_adjustment"

    class CreateParams(RequestOptions):
        cancel: "MeterEventAdjustment.CreateParamsCancel"
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

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.meter_event_adjustment"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["complete", "pending"]
    """
    The meter event adjustment's status.
    """

    @classmethod
    def create(
        cls, **params: Unpack["MeterEventAdjustment.CreateParams"]
    ) -> "MeterEventAdjustment":
        """
        Creates a billing meter event adjustment
        """
        return cast(
            "MeterEventAdjustment",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["MeterEventAdjustment.CreateParams"]
    ) -> "MeterEventAdjustment":
        """
        Creates a billing meter event adjustment
        """
        return cast(
            "MeterEventAdjustment",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )
