# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2SignalsAccountSignalFraudulentMerchantReadyEventNotification(
    EventNotification,
):
    LOOKUP_TYPE = "v2.signals.account_signal.fraudulent_merchant_ready"
    type: Literal["v2.signals.account_signal.fraudulent_merchant_ready"]

    @override
    def fetch_event(
        self,
    ) -> "V2SignalsAccountSignalFraudulentMerchantReadyEvent":
        return cast(
            "V2SignalsAccountSignalFraudulentMerchantReadyEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2SignalsAccountSignalFraudulentMerchantReadyEvent":
        return cast(
            "V2SignalsAccountSignalFraudulentMerchantReadyEvent",
            await super().fetch_event_async(),
        )


class V2SignalsAccountSignalFraudulentMerchantReadyEvent(Event):
    LOOKUP_TYPE = "v2.signals.account_signal.fraudulent_merchant_ready"
    type: Literal["v2.signals.account_signal.fraudulent_merchant_ready"]

    class V2SignalsAccountSignalFraudulentMerchantReadyEventData(StripeObject):
        class FraudulentMerchant(StripeObject):
            class Indicator(StripeObject):
                description: str
                """
                A brief explanation of how this indicator contributed to the fraudulent merchant probability.
                """
                impact: Literal[
                    "decrease", "neutral", "slight_increase", "strong_increase"
                ]
                """
                The effect this indicator had on the overall risk level.
                """
                indicator: Literal[
                    "bank_account",
                    "business_information_and_account_activity",
                    "disputes",
                    "failures",
                    "geolocation",
                    "other",
                    "other_related_accounts",
                    "other_transaction_activity",
                    "owner_email",
                    "web_presence",
                ]
                """
                The name of the specific indicator used in the risk assessment.
                """

            indicators: List[Indicator]
            """
            Array of objects representing individual factors that contributed to the calculated probability. Maximum of 3.
            """
            probability: Optional[Decimal]
            """
            The probability of the merchant being fraudulent. Can be between 0.00 and 100.00. May be empty if the risk_level is UNKNOWN or NOT_ASSESSED.
            """
            risk_level: Literal[
                "elevated",
                "highest",
                "low",
                "normal",
                "not_assessed",
                "unknown",
            ]
            """
            Categorical assessment of the fraudulent merchant risk based on probability.
            """
            _inner_class_types = {"indicators": Indicator}
            _field_encodings = {"probability": "decimal_string"}

        account: str
        """
        Account ID that this signal is associated with.
        """
        evaluated_at: str
        """
        Timestamp when the signal was evaluated.
        """
        fraudulent_merchant: Optional[FraudulentMerchant]
        """
        Fraudulent merchant signal data. Present when type is fraudulent_merchant.
        """
        id: str
        """
        Unique identifier for this account signal.
        """
        type: Literal["fraudulent_merchant"]
        """
        The type of account signal. Currently only fraudulent_merchant is supported.
        """
        _inner_class_types = {"fraudulent_merchant": FraudulentMerchant}

    data: V2SignalsAccountSignalFraudulentMerchantReadyEventData
    """
    Data for the v2.signals.account_signal.fraudulent_merchant_ready event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2SignalsAccountSignalFraudulentMerchantReadyEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2SignalsAccountSignalFraudulentMerchantReadyEvent.V2SignalsAccountSignalFraudulentMerchantReadyEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
