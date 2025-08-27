# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, List, Optional
from typing_extensions import Literal


class V2CoreHealthAuthorizationRateDropResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.authorization_rate_drop.resolved"
    type: Literal["v2.core.health.authorization_rate_drop.resolved"]

    class V2CoreHealthAuthorizationRateDropResolvedEventData(StripeObject):
        class Impact(StripeObject):
            class Dimension(StripeObject):
                issuer: Optional[str]
                """
                The issuer dimension.
                """
                type: Literal["issuer"]
                """
                The type of the dimension.
                """

            charge_type: Literal["money_moving", "validation"]
            """
            The type of the charge.
            """
            current_percentage: str
            """
            The current authorization rate percentage.
            """
            dimensions: Optional[List[Dimension]]
            """
            Dimensions that describe what subset of payments are impacted.
            """
            payment_method_type: Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "apple_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "blik",
                "boleto",
                "card",
                "card_present",
                "cartes_bancaires",
                "cashapp",
                "dummy_passthrough_card",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "interac_present",
                "kakao_pay",
                "klarna",
                "konbini",
                "link",
                "mobilepay",
                "multibanco",
                "naver_pay",
                "oxxo",
                "p24",
                "paper_check",
                "paynow",
                "paypal",
                "payto",
                "pay_by_bank",
                "pix",
                "promptpay",
                "revolut_pay",
                "sepa_debit",
                "sofort",
                "swish",
                "twint",
                "upi",
                "wechat_pay",
                "zip",
            ]
            """
            The type of the payment method.
            """
            previous_percentage: str
            """
            The previous authorization rate percentage.
            """
            _inner_class_types = {"dimensions": Dimension}

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
        started_at: str
        """
        The time when impact on the user experience was first detected.
        """
        summary: str
        """
        A short description of the alert.
        """
        _inner_class_types = {"impact": Impact}

    data: V2CoreHealthAuthorizationRateDropResolvedEventData
    """
    Data for the v2.core.health.authorization_rate_drop.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthAuthorizationRateDropResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthAuthorizationRateDropResolvedEvent.V2CoreHealthAuthorizationRateDropResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
