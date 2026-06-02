# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.issuing._card import Card
    from stripe.params.issuing._token_list_params import TokenListParams
    from stripe.params.issuing._token_modify_params import TokenModifyParams
    from stripe.params.issuing._token_retrieve_params import (
        TokenRetrieveParams,
    )


class Token(ListableAPIResource["Token"], UpdateableAPIResource["Token"]):
    """
    An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://docs.stripe.com/issuing), you can [view and manage these tokens](https://docs.stripe.com/issuing/controls/token-management) through Stripe.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.token"]] = "issuing.token"

    class NetworkData(StripeObject):
        class Device(StripeObject):
            device_fingerprint: Optional[str]
            """
            An obfuscated ID derived from the device ID.
            """
            ip_address: Optional[str]
            """
            The IP address of the device at provisioning time.
            """
            language: Optional[
                Literal[
                    "aa",
                    "ab",
                    "ae",
                    "af",
                    "ak",
                    "am",
                    "an",
                    "ar",
                    "as",
                    "av",
                    "ay",
                    "az",
                    "ba",
                    "be",
                    "bg",
                    "bi",
                    "bm",
                    "bn",
                    "bo",
                    "br",
                    "bs",
                    "ca",
                    "ce",
                    "ch",
                    "co",
                    "cr",
                    "cs",
                    "cu",
                    "cv",
                    "cy",
                    "da",
                    "de",
                    "dv",
                    "dz",
                    "ee",
                    "el",
                    "en",
                    "eo",
                    "es",
                    "et",
                    "eu",
                    "fa",
                    "ff",
                    "fi",
                    "fj",
                    "fo",
                    "fr",
                    "fy",
                    "ga",
                    "gd",
                    "gl",
                    "gn",
                    "gu",
                    "gv",
                    "ha",
                    "he",
                    "hi",
                    "ho",
                    "hr",
                    "ht",
                    "hu",
                    "hy",
                    "hz",
                    "ia",
                    "id",
                    "ie",
                    "ig",
                    "ii",
                    "ik",
                    "io",
                    "is",
                    "it",
                    "iu",
                    "ja",
                    "jv",
                    "ka",
                    "kg",
                    "ki",
                    "kj",
                    "kk",
                    "kl",
                    "km",
                    "kn",
                    "ko",
                    "kr",
                    "ks",
                    "ku",
                    "kv",
                    "kw",
                    "ky",
                    "la",
                    "lb",
                    "lg",
                    "li",
                    "ln",
                    "lo",
                    "lt",
                    "lu",
                    "lv",
                    "mg",
                    "mh",
                    "mi",
                    "mk",
                    "ml",
                    "mn",
                    "mr",
                    "ms",
                    "mt",
                    "my",
                    "na",
                    "nb",
                    "nd",
                    "ne",
                    "ng",
                    "nl",
                    "nn",
                    "no",
                    "nr",
                    "nv",
                    "ny",
                    "oc",
                    "oj",
                    "om",
                    "or",
                    "os",
                    "pa",
                    "pi",
                    "pl",
                    "ps",
                    "pt",
                    "qu",
                    "rm",
                    "rn",
                    "ro",
                    "ru",
                    "rw",
                    "sa",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "si",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sq",
                    "sr",
                    "ss",
                    "st",
                    "su",
                    "sv",
                    "sw",
                    "ta",
                    "te",
                    "tg",
                    "th",
                    "ti",
                    "tk",
                    "tl",
                    "tn",
                    "to",
                    "tr",
                    "ts",
                    "tt",
                    "tw",
                    "ty",
                    "ug",
                    "uk",
                    "ur",
                    "uz",
                    "ve",
                    "vi",
                    "vo",
                    "wa",
                    "wo",
                    "xh",
                    "yi",
                    "yo",
                    "za",
                    "zh",
                    "zu",
                ]
            ]
            """
            The ISO 639-1 language code of the device associated with the tokenization request.
            """
            location: Optional[str]
            """
            The geographic latitude/longitude coordinates of the device at provisioning time. The format is [+-]decimal/[+-]decimal.
            """
            name: Optional[str]
            """
            The name of the device used for tokenization.
            """
            phone_number: Optional[str]
            """
            The phone number of the device used for tokenization.
            """
            type: Optional[Literal["other", "phone", "watch"]]
            """
            The type of device used for tokenization.
            """

        class Mastercard(StripeObject):
            card_reference_id: Optional[str]
            """
            A unique reference ID from MasterCard to represent the card account number.
            """
            token_reference_id: str
            """
            The network-unique identifier for the token.
            """
            token_requestor_id: str
            """
            The ID of the entity requesting tokenization, specific to MasterCard.
            """
            token_requestor_name: Optional[str]
            """
            The name of the entity requesting tokenization, if known. This is directly provided from MasterCard.
            """

        class Visa(StripeObject):
            card_reference_id: Optional[str]
            """
            A unique reference ID from Visa to represent the card account number.
            """
            token_decision_recommendation: Optional[
                Literal["approve", "decline", "recommend_id_and_v"]
            ]
            """
            Stripe's recommendation to the network for this token activation request, derived from the same risk signals used for the activation decision.
            """
            token_reference_id: str
            """
            The network-unique identifier for the token.
            """
            token_requestor_id: str
            """
            The ID of the entity requesting tokenization, specific to Visa.
            """
            token_risk_score: Optional[str]
            """
            Degree of risk associated with the token between `01` and `99`, with higher number indicating higher risk. A `00` value indicates the token was not scored by Visa.
            """

        class WalletProvider(StripeObject):
            class CardholderAddress(StripeObject):
                line1: str
                """
                The street address of the cardholder tokenizing the card.
                """
                postal_code: str
                """
                The postal code of the cardholder tokenizing the card.
                """

            account_id: Optional[str]
            """
            The wallet provider-given account ID of the digital wallet the token belongs to.
            """
            account_trust_score: Optional[int]
            """
            An evaluation on the trustworthiness of the wallet account between 1 and 5. A higher score indicates more trustworthy.
            """
            card_number_source: Optional[
                Literal["app", "manual", "on_file", "other"]
            ]
            """
            The method used for tokenizing a card.
            """
            cardholder_address: Optional[CardholderAddress]
            cardholder_name: Optional[str]
            """
            The name of the cardholder tokenizing the card.
            """
            device_trust_score: Optional[int]
            """
            An evaluation on the trustworthiness of the device. A higher score indicates more trustworthy.
            """
            hashed_account_email_address: Optional[str]
            """
            The hashed email address of the cardholder's account with the wallet provider.
            """
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
            """
            The reasons for suggested tokenization given by the card network.
            """
            suggested_decision: Optional[
                Literal["approve", "decline", "require_auth"]
            ]
            """
            The recommendation on responding to the tokenization request.
            """
            suggested_decision_version: Optional[str]
            """
            The version of the standard for mapping reason codes followed by the wallet provider.
            """
            _inner_class_types = {"cardholder_address": CardholderAddress}

        device: Optional[Device]
        mastercard: Optional[Mastercard]
        type: Literal["mastercard", "visa"]
        """
        The network that the token is associated with. An additional hash is included with a name matching this value, containing tokenization data specific to the card network.
        """
        visa: Optional[Visa]
        wallet_provider: Optional[WalletProvider]
        _inner_class_types = {
            "device": Device,
            "mastercard": Mastercard,
            "visa": Visa,
            "wallet_provider": WalletProvider,
        }

    card: ExpandableField["Card"]
    """
    Card associated with this token.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    device_fingerprint: Optional[str]
    """
    The hashed ID derived from the device ID from the card network associated with the token.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last4: Optional[str]
    """
    The last four digits of the token.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    network: Literal["mastercard", "visa"]
    """
    The token service provider / card network associated with the token.
    """
    network_data: Optional[NetworkData]
    network_updated_at: int
    """
    Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch.
    """
    object: Literal["issuing.token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    provisioning_decision: Optional[
        Literal["approve", "approve_pending_id_and_v", "decline"]
    ]
    """
    The decision made during token provisioning.
    """
    status: Literal["active", "deleted", "requested", "suspended"]
    """
    The usage state of the token.
    """
    token_type: Optional[
        Literal[
            "card_on_file",
            "cloud_based",
            "commerce_platform",
            "commercial_virtual_account",
            "secure_element",
            "static_credential",
        ]
    ]
    """
    The type of the token, indicating how it is used.
    """
    wallet_provider: Optional[
        Literal["apple_pay", "google_pay", "samsung_pay"]
    ]
    """
    The digital wallet for this token, if one was used.
    """

    @classmethod
    def list(cls, **params: Unpack["TokenListParams"]) -> ListObject["Token"]:
        """
        Lists all Issuing Token objects for a given card.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["TokenListParams"]
    ) -> ListObject["Token"]:
        """
        Lists all Issuing Token objects for a given card.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id: str, **params: Unpack["TokenModifyParams"]) -> "Token":
        """
        Attempts to update the specified Issuing Token object to the status specified.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Token",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["TokenModifyParams"]
    ) -> "Token":
        """
        Attempts to update the specified Issuing Token object to the status specified.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Token",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["TokenRetrieveParams"]
    ) -> "Token":
        """
        Retrieves an Issuing Token object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["TokenRetrieveParams"]
    ) -> "Token":
        """
        Retrieves an Issuing Token object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"network_data": NetworkData}
