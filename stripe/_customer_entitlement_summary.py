# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from typing import ClassVar, List
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer_entitlement import CustomerEntitlement


class CustomerEntitlementSummary(APIResource["CustomerEntitlementSummary"]):
    """
    A summary of a customer's entitlements.
    """

    OBJECT_NAME: ClassVar[
        Literal["customer_entitlement_summary"]
    ] = "customer_entitlement_summary"

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    customer: str
    """
    The customer that is entitled to this feature.
    """
    entitlements: ListObject["CustomerEntitlement"]
    """
    The list of entitlements this customer has.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["customer_entitlement_summary"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["CustomerEntitlementSummary.RetrieveParams"]
    ) -> "CustomerEntitlementSummary":
        """
        Retrieve the entitlement summary for a customer
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["CustomerEntitlementSummary.RetrieveParams"]
    ) -> "CustomerEntitlementSummary":
        """
        Retrieve the entitlement summary for a customer
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
