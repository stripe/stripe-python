# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class Event(CreateableAPIResource["Event"]):
    """
    An entitlement event either grants or revokes an entitlement to a feature for a customer.
    """

    OBJECT_NAME: ClassVar[Literal["entitlements.event"]] = "entitlements.event"

    class Grant(StripeObject):
        class SubscriptionItem(StripeObject):
            item_quantity: int
            """
            The subscription line item quantity.
            """
            price: str
            """
            The price for the product that contains the feature for this entitlement event.
            """
            product: str
            """
            The product that contains the feature for this entitlement event.
            """
            subscription: str
            """
            The subscription that created this entitlement event.
            """
            subscription_item: str
            """
            The subscription item that created this entitlement event.
            """

        expires_at: int
        """
        When manually creating a grant entitlement event, you can make it a temporary grant by setting it to expire.
        """
        granted_by: Literal["subscription_item", "user"]
        """
        Who/what created this grant entitlement event.
        """
        subscription_item: Optional[SubscriptionItem]
        """
        If this entitlement event was created by a subscription_item, this will contains information about the subscription_item.
        """
        _inner_class_types = {"subscription_item": SubscriptionItem}

    class Quantity(StripeObject):
        units: int
        """
        When granting or revoking an entitlement to a type=quantity feature, you must specify the number of units you're granting/revoking. When the entitlement event type=grant, this number increments the total quantity available to the customer, and when type=revoke it decrements the total quantity available to the customer.
        """

    class Revoke(StripeObject):
        class SubscriptionItem(StripeObject):
            item_quantity: int
            """
            The subscription line item quantity.
            """
            price: str
            """
            The price for the product that contains the feature for this entitlement event.
            """
            product: str
            """
            The product that contains the feature for this entitlement event.
            """
            subscription: str
            """
            The subscription that created this entitlement event.
            """
            subscription_item: str
            """
            The subscription item that created this entitlement event.
            """

        expires_at: int
        """
        A revoke entitlement event will always expire at the same time as the grant it is revoking.
        """
        revoked_by: Literal["subscription_item", "user"]
        """
        Who/what created this revoke entitlement event.
        """
        subscription_item: Optional[SubscriptionItem]
        """
        If this entitlement event was created by a subscription_item, this will contains information about the subscription_item.
        """
        _inner_class_types = {"subscription_item": SubscriptionItem}

    class CreateParams(RequestOptions):
        customer: str
        """
        The customer that is being granted or revoked entitlement to/from a feature.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        feature: str
        """
        The feature that the customer is being granted/revoked entitlement to/from.
        """
        grant: NotRequired["Event.CreateParamsGrant"]
        """
        Contains information about type=grant entitlement event.
        """
        quantity: NotRequired["Event.CreateParamsQuantity"]
        """
        Contains information about entitlement events relating to features with type=quantity. Required when the feature has type=quantity.
        """
        type: Literal["grant", "revoke"]
        """
        Whether the event is a grant or revocation of the feature.
        """

    class CreateParamsGrant(TypedDict):
        expires_at: int
        """
        When manually creating a grant entitlement event, you can make it a temporary grant by setting it to expire.
        """

    class CreateParamsQuantity(TypedDict):
        units: int
        """
        When granting or revoking an entitlement to a type=quantity feature, you must specify the number of units you're granting/revoking. When the entitlement event type=grant, this number increments the total quantity available to the customer, and when type=revoke it decrements the total quantity available to the customer.
        """

    customer: str
    """
    The customer that is being granted or revoked entitlement to/from a feature.
    """
    feature: str
    """
    The feature that the customer is being granted/revoked entitlement to/from.
    """
    grant: Optional[Grant]
    """
    Contains information about type=grant entitlement event.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["entitlements.event"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    quantity: Optional[Quantity]
    """
    Contains information about entitlement events relating to features with type=quantity. Required when the feature has type=quantity.
    """
    revoke: Optional[Revoke]
    """
    Contains information about type=revoke entitlement event.
    """
    type: Literal["grant", "revoke"]
    """
    Whether the event is a grant or revocation of the feature.
    """

    @classmethod
    def create(cls, **params: Unpack["Event.CreateParams"]) -> "Event":
        """
        Create an entitlement event manually, outside of the entitlement events automatically created by Stripe lifecycle events.
        """
        return cast(
            "Event",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Event.CreateParams"]
    ) -> "Event":
        """
        Create an entitlement event manually, outside of the entitlement events automatically created by Stripe lifecycle events.
        """
        return cast(
            "Event",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {
        "grant": Grant,
        "quantity": Quantity,
        "revoke": Revoke,
    }
