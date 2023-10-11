# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.issuing.card import Card


class Token(ListableAPIResource["Token"], UpdateableAPIResource["Token"]):
    """
    An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://stripe.com/docs/issuing), you can view and manage these tokens through Stripe.
    """

    OBJECT_NAME = "issuing.token"

    class NetworkData(StripeObject):
        class Device(StripeObject):
            device_fingerprint: Optional[str]
            ip_address: Optional[str]
            location: Optional[str]
            name: Optional[str]
            phone_number: Optional[str]
            type: Optional[Literal["other", "phone", "watch"]]

        class Mastercard(StripeObject):
            card_reference_id: Optional[str]
            token_reference_id: str
            token_requestor_id: str
            token_requestor_name: Optional[str]

        class Visa(StripeObject):
            card_reference_id: str
            token_reference_id: str
            token_requestor_id: str
            token_risk_score: Optional[str]

        class WalletProvider(StripeObject):
            class CardholderAddress(StripeObject):
                line1: str
                postal_code: str

            account_id: Optional[str]
            account_trust_score: Optional[int]
            card_number_source: Optional[
                Literal["app", "manual", "on_file", "other"]
            ]
            cardholder_address: Optional[CardholderAddress]
            cardholder_name: Optional[str]
            device_trust_score: Optional[int]
            hashed_account_email_address: Optional[str]
            reason_codes: Optional[
                List[
                    Literal[
                        "account_card_too_new",
                        "account_recently_changed",
                        "account_too_new",
                        "account_too_new_since_launch",
                        "additional_device",
                        "data_expired",
                        "defer_id_v_decision",
                        "device_recently_lost",
                        "good_activity_history",
                        "has_suspended_tokens",
                        "high_risk",
                        "inactive_account",
                        "long_account_tenure",
                        "low_account_score",
                        "low_device_score",
                        "low_phone_number_score",
                        "network_service_error",
                        "outside_home_territory",
                        "provisioning_cardholder_mismatch",
                        "provisioning_device_and_cardholder_mismatch",
                        "provisioning_device_mismatch",
                        "same_device_no_prior_authentication",
                        "same_device_successful_prior_authentication",
                        "software_update",
                        "suspicious_activity",
                        "too_many_different_cardholders",
                        "too_many_recent_attempts",
                        "too_many_recent_tokens",
                    ]
                ]
            ]
            suggested_decision: Optional[
                Literal["approve", "decline", "require_auth"]
            ]
            suggested_decision_version: Optional[str]
            _inner_class_types = {"cardholder_address": CardholderAddress}

        device: Optional[Device]
        mastercard: Optional[Mastercard]
        type: Literal["mastercard", "visa"]
        visa: Optional[Visa]
        wallet_provider: Optional[WalletProvider]
        _inner_class_types = {
            "device": Device,
            "mastercard": Mastercard,
            "visa": Visa,
            "wallet_provider": WalletProvider,
        }

    card: ExpandableField["Card"]
    created: int
    device_fingerprint: Optional[str]
    id: str
    last4: Optional[str]
    livemode: bool
    network: Literal["mastercard", "visa"]
    network_data: Optional[NetworkData]
    network_updated_at: int
    object: Literal["issuing.token"]
    status: Literal["active", "deleted", "requested", "suspended"]
    wallet_provider: Optional[
        Literal["apple_pay", "google_pay", "samsung_pay"]
    ]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Token"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Any) -> "Token":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Token",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Token":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"network_data": NetworkData}
