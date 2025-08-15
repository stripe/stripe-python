# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._account import Account
from stripe.v2._event import Event
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal


class AccountConfigurationRecipientDataFeatureStatusUpdatedEvent(Event):
    LOOKUP_TYPE = "account.configuration_recipient_data.feature_status_updated"
    type: Literal[
        "account.configuration_recipient_data.feature_status_updated"
    ]

    class AccountConfigurationRecipientDataFeatureStatusUpdatedEventData(
        StripeObject,
    ):
        feature_name: Literal[
            "bank_accounts.local", "bank_accounts.wire", "cards"
        ]
        """
        Closed Enum. The recipient_data feature which had its status updated.
        """

    data: AccountConfigurationRecipientDataFeatureStatusUpdatedEventData
    """
    Data for the account.configuration_recipient_data.feature_status_updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "AccountConfigurationRecipientDataFeatureStatusUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = AccountConfigurationRecipientDataFeatureStatusUpdatedEvent.AccountConfigurationRecipientDataFeatureStatusUpdatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt

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

    def fetch_related_object(self) -> Account:
        """
        Retrieves the related object from the API. Makes an API request on every call.
        """
        return cast(
            Account,
            self._requestor.request(
                "get",
                self.related_object.url,
                base_address="api",
                options={"stripe_account": self.context},
            ),
        )
