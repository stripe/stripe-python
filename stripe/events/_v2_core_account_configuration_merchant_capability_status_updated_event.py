# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from typing import Any, Dict, Optional
from typing_extensions import Literal


class V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEvent(Event):
    LOOKUP_TYPE = (
        "v2.core.account[configuration.merchant].capability_status_updated"
    )
    type: Literal[
        "v2.core.account[configuration.merchant].capability_status_updated"
    ]

    class V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEventData(
        StripeObject,
    ):
        updated_capability: Literal[
            "ach_debit_payments",
            "acss_debit_payments",
            "affirm_payments",
            "afterpay_clearpay_payments",
            "alma_payments",
            "amazon_pay_payments",
            "au_becs_debit_payments",
            "bacs_debit_payments",
            "bancontact_payments",
            "blik_payments",
            "boleto_payments",
            "card_payments",
            "cartes_bancaires_payments",
            "cashapp_payments",
            "eps_payments",
            "fpx_payments",
            "gb_bank_transfer_payments",
            "grabpay_payments",
            "ideal_payments",
            "jcb_payments",
            "jp_bank_transfer_payments",
            "kakao_pay_payments",
            "klarna_payments",
            "konbini_payments",
            "kr_card_payments",
            "link_payments",
            "mobilepay_payments",
            "multibanco_payments",
            "mx_bank_transfer_payments",
            "naver_pay_payments",
            "oxxo_payments",
            "p24_payments",
            "payco_payments",
            "paynow_payments",
            "pay_by_bank_payments",
            "promptpay_payments",
            "revolut_pay_payments",
            "samsung_pay_payments",
            "sepa_bank_transfer_payments",
            "sepa_debit_payments",
            "swish_payments",
            "twint_payments",
            "us_bank_transfer_payments",
            "zip_payments",
        ]
        """
        Open Enum. The capability which had its status updated.
        """

    data: V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEventData
    """
    Data for the v2.core.account[configuration.merchant].capability_status_updated event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEvent.V2CoreAccountConfigurationMerchantCapabilityStatusUpdatedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
