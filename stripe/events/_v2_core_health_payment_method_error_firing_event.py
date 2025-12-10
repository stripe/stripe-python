# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2CoreHealthPaymentMethodErrorFiringEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.core.health.payment_method_error.firing"
    type: Literal["v2.core.health.payment_method_error.firing"]

    @override
    def fetch_event(self) -> "V2CoreHealthPaymentMethodErrorFiringEvent":
        return cast(
            "V2CoreHealthPaymentMethodErrorFiringEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(
        self,
    ) -> "V2CoreHealthPaymentMethodErrorFiringEvent":
        return cast(
            "V2CoreHealthPaymentMethodErrorFiringEvent",
            await super().fetch_event_async(),
        )


class V2CoreHealthPaymentMethodErrorFiringEvent(Event):
    LOOKUP_TYPE = "v2.core.health.payment_method_error.firing"
    type: Literal["v2.core.health.payment_method_error.firing"]

    class V2CoreHealthPaymentMethodErrorFiringEventData(StripeObject):
        class Impact(StripeObject):
            class TopImpactedAccount(StripeObject):
                account: str
                """
                The account ID of the impacted connected account.
                """
                impacted_requests: int
                """
                The number of impacted requests.
                """
                impacted_requests_percentage: Optional[str]
                """
                The percentage of impacted requests.
                """

            error_code: Optional[str]
            """
            The returned error code.
            """
            impacted_requests: int
            """
            The number of impacted requests.
            """
            impacted_requests_percentage: Optional[str]
            """
            The percentage of impacted requests.
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
                "billie",
                "blik",
                "boleto",
                "card",
                "card_present",
                "cartes_bancaires",
                "cashapp",
                "crypto",
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
                "kriya",
                "kr_card",
                "link",
                "mb_way",
                "mobilepay",
                "mondu",
                "multibanco",
                "naver_pay",
                "ng_bank",
                "ng_bank_transfer",
                "ng_card",
                "ng_market",
                "ng_ussd",
                "ng_wallet",
                "oxxo",
                "p24",
                "paper_check",
                "payco",
                "paynow",
                "paypal",
                "paypay",
                "payto",
                "pay_by_bank",
                "pix",
                "promptpay",
                "rechnung",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "scalapay",
                "sepa_debit",
                "sequra",
                "sofort",
                "sunbit",
                "swish",
                "twint",
                "upi",
                "us_bank_account",
                "vipps",
                "wechat_pay",
                "zip",
            ]
            """
            The type of the payment method.
            """
            top_impacted_accounts: Optional[List[TopImpactedAccount]]
            """
            The top impacted connected accounts (only for platforms).
            """
            _inner_class_types = {"top_impacted_accounts": TopImpactedAccount}

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

    data: V2CoreHealthPaymentMethodErrorFiringEventData
    """
    Data for the v2.core.health.payment_method_error.firing event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreHealthPaymentMethodErrorFiringEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreHealthPaymentMethodErrorFiringEvent.V2CoreHealthPaymentMethodErrorFiringEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
