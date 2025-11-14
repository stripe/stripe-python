# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._singleton_api_resource import SingletonAPIResource
from typing import ClassVar
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.billing.analytics._meter_usage_row import MeterUsageRow
    from stripe.params.billing.analytics._meter_usage_retrieve_params import (
        MeterUsageRetrieveParams,
    )


class MeterUsage(SingletonAPIResource["MeterUsage"]):
    """
    A billing meter usage event represents an aggregated view of a customer's billing meter events within a specified timeframe.
    """

    OBJECT_NAME: ClassVar[Literal["billing.analytics.meter_usage"]] = (
        "billing.analytics.meter_usage"
    )
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.analytics.meter_usage"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    refreshed_at: int
    """
    The timestamp to indicate data freshness, measured in seconds since the Unix epoch.
    """
    rows: ListObject["MeterUsageRow"]

    @classmethod
    def retrieve(
        cls, **params: Unpack["MeterUsageRetrieveParams"]
    ) -> "MeterUsage":
        """
        Returns aggregated meter usage data for a customer within a specified time interval. The data can be grouped by various dimensions and can include multiple meters if specified.
        """
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, **params: Unpack["MeterUsageRetrieveParams"]
    ) -> "MeterUsage":
        """
        Returns aggregated meter usage data for a customer within a specified time interval. The data can be grouped by various dimensions and can include multiple meters if specified.
        """
        instance = cls(None, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/billing/analytics/meter_usage"
