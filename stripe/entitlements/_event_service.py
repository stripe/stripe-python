# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.entitlements._event import Event
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class EventService(StripeService):
    class CreateParams(TypedDict):
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
        grant: NotRequired["EventService.CreateParamsGrant"]
        """
        Contains information about type=grant entitlement event.
        """
        quantity: NotRequired["EventService.CreateParamsQuantity"]
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

    def create(
        self, params: "EventService.CreateParams", options: RequestOptions = {}
    ) -> Event:
        """
        Create an entitlement event manually, outside of the entitlement events automatically created by Stripe lifecycle events.
        """
        return cast(
            Event,
            self._request(
                "post",
                "/v1/entitlements/events",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self, params: "EventService.CreateParams", options: RequestOptions = {}
    ) -> Event:
        """
        Create an entitlement event manually, outside of the entitlement events automatically created by Stripe lifecycle events.
        """
        return cast(
            Event,
            await self._request_async(
                "post",
                "/v1/entitlements/events",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
