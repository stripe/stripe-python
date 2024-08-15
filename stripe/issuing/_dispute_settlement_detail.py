# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._request_options import RequestOptions
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class DisputeSettlementDetail(APIResource["DisputeSettlementDetail"]):
    """
    Represents a record from the card network of a money movement or change in state for an Issuing dispute. These records are included in the settlement reports that we receive from networks and expose to users as Settlement objects.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.dispute_settlement_detail"]] = (
        "issuing.dispute_settlement_detail"
    )

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount: int
    """
    Disputed amount in the card's currency and in the smallest currency unit. Usually the amount of the transaction, but can differ (usually because of currency fluctuation).
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    The currency the original transaction was made in. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    dispute: str
    """
    The ID of the linked dispute.
    """
    event_type: Literal["filing", "loss", "representment", "win"]
    """
    The type of event corresponding to this dispute settlement detail, representing the stage in the dispute network lifecycle.
    """
    id: str
    """
    Unique identifier for the object.
    """
    issued_card: str
    """
    The card used to make the original transaction.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: Literal["maestro", "mastercard", "visa"]
    """
    The card network for this dispute settlement detail. One of ["visa", "mastercard", "maestro"]
    """
    object: Literal["issuing.dispute_settlement_detail"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    settlement: Optional[str]
    """
    The ID of the linked card network settlement.
    """

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["DisputeSettlementDetail.RetrieveParams"],
    ) -> "DisputeSettlementDetail":
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["DisputeSettlementDetail.RetrieveParams"],
    ) -> "DisputeSettlementDetail":
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
