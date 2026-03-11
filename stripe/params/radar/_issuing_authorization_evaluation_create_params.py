# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class IssuingAuthorizationEvaluationCreateParams(RequestOptions):
    authorization_details: (
        "IssuingAuthorizationEvaluationCreateParamsAuthorizationDetails"
    )
    """
    Details about the authorization.
    """
    card_details: "IssuingAuthorizationEvaluationCreateParamsCardDetails"
    """
    Details about the card used in the authorization.
    """
    cardholder_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsCardholderDetails"
    ]
    """
    Details about the cardholder.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    merchant_details: (
        "IssuingAuthorizationEvaluationCreateParamsMerchantDetails"
    )
    """
    Details about the merchant where the authorization occurred.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    network_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsNetworkDetails"
    ]
    """
    Details about the card network processing.
    """
    token_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsTokenDetails"
    ]
    """
    Details about the token, if a tokenized payment method was used.
    """
    verification_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsVerificationDetails"
    ]
    """
    Details about verification checks performed.
    """


class IssuingAuthorizationEvaluationCreateParamsAuthorizationDetails(
    TypedDict
):
    amount: int
    """
    The authorization amount in the smallest currency unit.
    """
    authorization_method: NotRequired[
        Literal["chip", "contactless", "keyed_in", "online", "swipe"]
    ]
    """
    The method used for authorization.
    """
    currency: str
    """
    Three-letter ISO currency code in lowercase.
    """
    entry_mode: NotRequired[
        Literal[
            "contactless",
            "contactless_magstripe",
            "credential_on_file",
            "integrated_circuit_card",
            "magstripe",
            "magstripe_no_cvv",
            "manual",
            "other",
            "unknown",
        ]
    ]
    """
    The card entry mode.
    """
    entry_mode_raw_code: NotRequired[str]
    """
    The raw code for the card entry mode.
    """
    initiated_at: int
    """
    The time when the authorization was initiated (Unix timestamp).
    """
    point_of_sale_condition: NotRequired[
        Literal[
            "account_verification",
            "card_not_present",
            "card_present",
            "e_commerce",
            "key_entered_pos",
            "missing",
            "moto",
            "other",
            "pin_entered",
            "recurring",
        ]
    ]
    """
    The point of sale condition.
    """
    point_of_sale_condition_raw_code: NotRequired[str]
    """
    The raw code for the point of sale condition.
    """
    reference: str
    """
    External reference for the authorization.
    """


class IssuingAuthorizationEvaluationCreateParamsCardDetails(TypedDict):
    bin: str
    """
    Bank Identification Number (BIN) of the card.
    """
    bin_country: NotRequired[str]
    """
    Two-letter ISO country code of the card's issuing bank.
    """
    card_type: Literal["physical", "virtual"]
    """
    The type of card (physical or virtual).
    """
    created_at: int
    """
    The time when the card was created (Unix timestamp).
    """
    last4: NotRequired[str]
    """
    Last 4 digits of the card number.
    """
    reference: str
    """
    External reference for the card.
    """


class IssuingAuthorizationEvaluationCreateParamsCardholderDetails(TypedDict):
    created_at: NotRequired[int]
    """
    The time when the cardholder was created (Unix timestamp).
    """
    reference: NotRequired[str]
    """
    External reference for the cardholder.
    """


class IssuingAuthorizationEvaluationCreateParamsMerchantDetails(TypedDict):
    category_code: str
    """
    Merchant Category Code (MCC).
    """
    country: NotRequired[str]
    """
    Two-letter ISO country code of the merchant.
    """
    name: str
    """
    Name of the merchant.
    """
    network_id: str
    """
    Network merchant identifier.
    """
    terminal_id: NotRequired[str]
    """
    Terminal identifier.
    """


class IssuingAuthorizationEvaluationCreateParamsNetworkDetails(TypedDict):
    acquiring_institution_id: NotRequired[str]
    """
    The acquiring institution identifier.
    """
    routed_network: NotRequired[
        Literal[
            "cirrus",
            "interlink",
            "maestro",
            "mastercard",
            "other",
            "plus",
            "visa",
        ]
    ]
    """
    The card network that routed the authorization.
    """


class IssuingAuthorizationEvaluationCreateParamsTokenDetails(TypedDict):
    created_at: NotRequired[int]
    """
    The time when the token was created (Unix timestamp).
    """
    reference: NotRequired[str]
    """
    External reference for the token.
    """
    wallet: NotRequired[Literal["apple_pay", "google_pay", "samsung_pay"]]
    """
    The wallet provider for the tokenized payment method.
    """


class IssuingAuthorizationEvaluationCreateParamsVerificationDetails(TypedDict):
    three_d_secure_result: NotRequired[
        Literal[
            "attempt_acknowledged",
            "authenticated",
            "exempted",
            "failed",
            "required",
        ]
    ]
    """
    The result of 3D Secure verification.
    """
