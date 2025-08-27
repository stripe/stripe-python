# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, Optional
from typing_extensions import Literal


class V2CoreHealthPaymentMethodErrorResolvedEvent(Event):
    LOOKUP_TYPE = "v2.core.health.payment_method_error.resolved"
    type: Literal["v2.core.health.payment_method_error.resolved"]

    class V2CoreHealthPaymentMethodErrorResolvedEventData(StripeObject):
        class Impact(StripeObject):
            error_code: Optional[str]
            """
            The returned error code.
            """
            impacted_requests: int
            """
            The number of impacted requests.
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

    data: V2CoreHealthPaymentMethodErrorResolvedEventData
    """
    Data for the v2.core.health.payment_method_error.resolved event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthPaymentMethodErrorResolvedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthPaymentMethodErrorResolvedEvent.V2CoreHealthPaymentMethodErrorResolvedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
