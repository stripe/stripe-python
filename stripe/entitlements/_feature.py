# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class Feature(
    CreateableAPIResource["Feature"], ListableAPIResource["Feature"]
):
    """
    A feature represents a monetizable ability or functionality in your system.
    Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.
    """

    OBJECT_NAME: ClassVar[
        Literal["entitlements.feature"]
    ] = "entitlements.feature"

    class Quantity(StripeObject):
        units_available: int
        """
        The quantity of units made available by this feature. This quantity will be multiplied by the line_item quantity for line_items that contain this feature.
        """

    class CreateParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        lookup_key: str
        """
        A unique key you provide as your own system identifier. This may be up to 80 characters.
        """
        name: str
        """
        The feature's name, for your own purpose, not meant to be displayable to the customer.
        """
        quantity: NotRequired["Feature.CreateParamsQuantity"]
        """
        Contains information about type=quantity features. This is required when type=quantity.
        """
        type: Literal["quantity", "switch"]
        """
        The type of feature.
        """

    class CreateParamsQuantity(TypedDict):
        units_available: int
        """
        The quantity of units made available by this feature. This quantity will be multiplied by the line_item quantity for line_items that contain this feature.
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
    name: str
    """
    The feature's name, for your own purpose, not meant to be displayable to the customer.
    """
    object: Literal["entitlements.feature"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    quantity: Optional[Quantity]
    """
    Contains information about type=quantity features. This is required when type=quantity.
    """
    type: Literal["quantity", "switch"]
    """
    The type of feature.
    """

    @classmethod
    def create(cls, **params: Unpack["Feature.CreateParams"]) -> "Feature":
        """
        Creates a feature
        """
        return cast(
            "Feature",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Feature.CreateParams"]
    ) -> "Feature":
        """
        Creates a feature
        """
        return cast(
            "Feature",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["Feature.ListParams"]
    ) -> ListObject["Feature"]:
        """
        Retrieve a list of features
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
        cls, **params: Unpack["Feature.ListParams"]
    ) -> ListObject["Feature"]:
        """
        Retrieve a list of features
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
