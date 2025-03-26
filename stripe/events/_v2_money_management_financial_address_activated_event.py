# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._event import Event
from stripe.v2.money_management._financial_address import FinancialAddress
from typing import cast
from typing_extensions import Literal


class V2MoneyManagementFinancialAddressActivatedEvent(Event):
    LOOKUP_TYPE = "v2.money_management.financial_address.activated"
    type: Literal["v2.money_management.financial_address.activated"]

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object relevant to the event.
        """
        type: str
        """
        Type of the object relevant to the event.
        """
        url: str
        """
        URL to retrieve the resource.
        """

    related_object: RelatedObject
    """
    Object containing the reference to API resource relevant to the event
    """

    def fetch_related_object(self) -> FinancialAddress:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            FinancialAddress,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
