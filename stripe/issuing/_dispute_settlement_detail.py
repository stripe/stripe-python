# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class DisputeSettlementDetail(ListableAPIResource["DisputeSettlementDetail"]):
    """
    Represents a record from the card network of a money movement or change in state for an Issuing dispute. These records are included in the settlement reports that we receive from networks and expose to users as Settlement objects.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.dispute_settlement_detail"]] = (
        "issuing.dispute_settlement_detail"
    )

    class NetworkData(StripeObject):
        processing_date: Optional[str]
        """
        The date the transaction was processed by the card network. This can be different from the date the seller recorded the transaction depending on when the acquirer submits the transaction to the network.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        settlement: NotRequired[str]
        """
        Select the Issuing dispute settlement details for the given settlement.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount: int
    """
    Disputed amount in the card's currency and in the smallest currency unit. Usually the amount of the transaction, but can differ (usually because of currency fluctuation).
    """
    card: str
    """
    The card used to make the original transaction.
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
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: Literal["maestro", "mastercard", "visa"]
    """
    The card network for this dispute settlement detail. One of ["visa", "mastercard", "maestro"]
    """
    network_data: Optional[NetworkData]
    """
    Details about the transaction, such as processing dates, set by the card network.
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
    def list(
        cls, **params: Unpack["DisputeSettlementDetail.ListParams"]
    ) -> ListObject["DisputeSettlementDetail"]:
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["DisputeSettlementDetail.ListParams"]
    ) -> ListObject["DisputeSettlementDetail"]:
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

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

    _inner_class_types = {"network_data": NetworkData}
