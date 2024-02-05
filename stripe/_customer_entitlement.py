# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class CustomerEntitlement(ListableAPIResource["CustomerEntitlement"]):
    """
    A entitlement for a customer describes access to a feature.
    """

    OBJECT_NAME: ClassVar[
        Literal["customer_entitlement"]
    ] = "customer_entitlement"

    class Quantity(StripeObject):
        total_available: int
        """
        The total quantity available to the customer.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    feature: str
    """
    The feature that the customer is entitled to.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: str
    """
    A unique key you provide as your own system identifier. This may be up to 80 characters.
    """
    object: Literal["customer_entitlement"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    quantity: Optional[Quantity]
    """
    Contains information about entitlements relating to features with type=quantity. Required when the feature has type=quantity.
    """
    type: Literal["quantity", "switch"]
    """
    The type of feature.
    """

    @classmethod
    def list(
        cls, **params: Unpack["CustomerEntitlement.ListParams"]
    ) -> ListObject["CustomerEntitlement"]:
        """
        Retrieve a list of entitlements for a customer
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
        cls, **params: Unpack["CustomerEntitlement.ListParams"]
    ) -> ListObject["CustomerEntitlement"]:
        """
        Retrieve a list of entitlements for a customer
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

    _inner_class_types = {"quantity": Quantity}
