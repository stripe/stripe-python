# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.terminal._reader_collected_data_retrieve_params import (
        ReaderCollectedDataRetrieveParams,
    )


class ReaderCollectedData(APIResource["ReaderCollectedData"]):
    """
    Returns data collected by Terminal readers. This data is only stored for 24 hours.
    """

    OBJECT_NAME: ClassVar[Literal["terminal.reader_collected_data"]] = (
        "terminal.reader_collected_data"
    )

    class Magstripe(StripeObject):
        data: Optional[str]
        """
        The raw magstripe data collected by the reader.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    magstripe: Optional[Magstripe]
    """
    The magstripe data collected by the reader.
    """
    object: Literal["terminal.reader_collected_data"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    type: Literal["magstripe"]
    """
    The type of data collected by the reader.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ReaderCollectedDataRetrieveParams"]
    ) -> "ReaderCollectedData":
        """
        Retrieve data collected using Reader hardware.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["ReaderCollectedDataRetrieveParams"]
    ) -> "ReaderCollectedData":
        """
        Retrieve data collected using Reader hardware.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/terminal/reader_collected_data"

    _inner_class_types = {"magstripe": Magstripe}
