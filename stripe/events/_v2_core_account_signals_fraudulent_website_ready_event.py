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


class V2CoreAccountSignalsFraudulentWebsiteReadyEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.core.account_signals.fraudulent_website_ready"
    type: Literal["v2.core.account_signals.fraudulent_website_ready"]

    @override
    def fetch_event(self) -> "V2CoreAccountSignalsFraudulentWebsiteReadyEvent":
        return cast(
            "V2CoreAccountSignalsFraudulentWebsiteReadyEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreAccountSignalsFraudulentWebsiteReadyEvent":
        return cast(
            "V2CoreAccountSignalsFraudulentWebsiteReadyEvent",
            await super().fetch_event_async(),
        )


class V2CoreAccountSignalsFraudulentWebsiteReadyEvent(Event):
    LOOKUP_TYPE = "v2.core.account_signals.fraudulent_website_ready"
    type: Literal["v2.core.account_signals.fraudulent_website_ready"]

    class V2CoreAccountSignalsFraudulentWebsiteReadyEventData(StripeObject):
        account: Optional[str]
        """
        The account for which the signals belong to. Empty if this was an entityless request.
        """
        details: str
        """
        Human readable description of concerns found in the website, produced by LLM. If risk_level is unknown, this explains why evaluation could not run.
        """
        evaluated_at: str
        """
        Time at which the signal was evaluated.
        """
        evaluation_id: str
        """
        Unique identifier for the fraudulent website evaluation request.
        """
        risk_level: Literal[
            "elevated", "highest", "low", "normal", "not_assessed", "unknown"
        ]
        """
        Risk level for the fraudulent website signal. If evaluation could not run (like invalid website), we return unknown.
        """
        signal_id: str
        """
        Unique identifier for the fraudulent website signal.
        """

    data: V2CoreAccountSignalsFraudulentWebsiteReadyEventData
    """
    Data for the v2.core.account_signals.fraudulent_website_ready event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreAccountSignalsFraudulentWebsiteReadyEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountSignalsFraudulentWebsiteReadyEvent.V2CoreAccountSignalsFraudulentWebsiteReadyEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
