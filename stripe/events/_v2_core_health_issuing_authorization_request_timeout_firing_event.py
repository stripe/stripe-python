# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.core.health.issuing_authorization_request_timeout.firing"
    type: Literal[
        "v2.core.health.issuing_authorization_request_timeout.firing"
    ]

    @override
    def fetch_event(
        self,
    ) -> "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent":
        return cast(
            "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent":
        return cast(
            "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.issuing_authorization_request_timeout.firing"
    type: Literal[
        "v2.core.health.issuing_authorization_request_timeout.firing"
    ]

    class V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventData(
        StripeObject,
    ):
        class Impact(StripeObject):
            class ApprovedAmount(StripeObject):
                currency: Optional[str]
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: Optional[int]
                """
                A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
                """

            class DeclinedAmount(StripeObject):
                currency: Optional[str]
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: Optional[int]
                """
                A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
                """

            approved_amount: Optional[ApprovedAmount]
            """
            Estimated aggregated amount for the approved requests.
            """
            approved_impacted_requests: Optional[int]
            """
            The number of approved requests which are impacted.
            """
            declined_amount: Optional[DeclinedAmount]
            """
            Estimated aggregated amount for the declined requests.
            """
            declined_impacted_requests: Optional[int]
            """
            The number of declined requests which are impacted.
            """
            _inner_class_types = {
                "approved_amount": ApprovedAmount,
                "declined_amount": DeclinedAmount,
            }

        alert_id: str
        """
        The alert ID.
        """
        grouping_key: str
        """
        The grouping key for the alert.
        """
        impact: Impact
        """
        The user impact.
        """
        started_at: str
        """
        The time when impact on the user experience was first detected.
        """
        summary: str
        """
        A short description of the alert.
        """
        _inner_class_types = {"impact": Impact}

    data: V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventData
    """
    Data for the v2.core.health.issuing_authorization_request_timeout.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
