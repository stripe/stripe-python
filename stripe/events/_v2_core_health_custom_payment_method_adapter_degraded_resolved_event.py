# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, Union, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = (
        "v2.core.health.custom_payment_method_adapter_degraded.resolved"
    )
    type: Literal[
        "v2.core.health.custom_payment_method_adapter_degraded.resolved"
    ]

    @override
    def fetch_event(
        self,
    ) -> "V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent":
        return cast(
            "V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent":
        return cast(
            "V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent(Event):
    LOOKUP_TYPE = (
        "v2.core.health.custom_payment_method_adapter_degraded.resolved"
    )
    type: Literal[
        "v2.core.health.custom_payment_method_adapter_degraded.resolved"
    ]

    class V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEventData(
        StripeObject,
    ):
        class Impact(StripeObject):
            class CustomPaymentMethodTypeDetails(StripeObject):
                auto_disabled_at: Optional[str]
                """
                The time when the custom payment method was automatically disabled. Null when it is enabled.
                """
                display_name: str
                """
                The display name of the custom payment method type.
                """
                reverse_api_url: str
                """
                The URL of the user's self-hosted adapter endpoint.
                """
                type: str
                """
                The identifier of the custom payment method type (e.g., "cpmt_...").
                """

            custom_payment_method_disabled_from_checkout: bool
            """
            Whether the custom payment method was disabled in Checkout as a result of the degradation. True while the alert is open and false when it is resolved.
            """
            custom_payment_method_type_details: CustomPaymentMethodTypeDetails
            """
            The custom payment method type whose adapter is unhealthy.
            """
            degraded_health_reason: str
            """
            The reason the adapter's health is degraded.
            """
            _inner_class_types = {
                "custom_payment_method_type_details": CustomPaymentMethodTypeDetails,
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
        resolved_at: str
        """
        The time when the user experience has returned to expected levels.
        """
        severity: Union[Literal["critical", "non_critical"], str]
        """
        The severity of the alert.
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

    data: V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEventData
    """
    Data for the v2.core.health.custom_payment_method_adapter_degraded.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEvent.V2CoreHealthCustomPaymentMethodAdapterDegradedResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
