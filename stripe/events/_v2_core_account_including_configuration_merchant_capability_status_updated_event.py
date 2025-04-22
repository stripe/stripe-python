# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._api_requestor import _APIRequestor
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2._event import Event
from stripe.v2.core._account import Account
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal


class V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent(
    Event,
):
    LOOKUP_TYPE = (
        "v2.core.account[configuration.merchant].capability_status_updated"
    )
    type: Literal[
        "v2.core.account[configuration.merchant].capability_status_updated"
    ]

    class V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventData(
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
            "stripe_balance.payouts",
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

    data: V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventData
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
    ) -> "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventData._construct_from(
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
