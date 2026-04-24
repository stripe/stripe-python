# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
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
    Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    network_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsNetworkDetails"
    ]
    """
    Details about the authorization, such as identifiers, set by the card network.
    """
    token_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsTokenDetails"
    ]
    """
    Details about the token, if a tokenized payment method was used for the authorization.
    """
    verification_details: NotRequired[
        "IssuingAuthorizationEvaluationCreateParamsVerificationDetails"
    ]
    """
    Details about verification data for the authorization.
    """


class IssuingAuthorizationEvaluationCreateParamsAuthorizationDetails(
    TypedDict
):
    amount: int
    """
    The total amount of the authorization in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    authorization_method: NotRequired[
        Literal["chip", "contactless", "keyed_in", "online", "swipe"]
    ]
    """
    How the card details were provided.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
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
    Defines how the card's information was entered for the authorization.
    """
    entry_mode_raw_code: NotRequired[str]
    """
    Raw code indicating the entry mode from the network message.
    """
    initiated_at: int
    """
    The time the authorization was initiated, as a Unix timestamp in seconds. Must not be in the future.
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
    Defines how the card was read at the point of sale.
    """
    point_of_sale_condition_raw_code: NotRequired[str]
    """
    Raw code indicating the point of sale condition from the network message.
    """
    reference: str
    """
    User's specified unique ID for this authorization attempt (e.g., RRN or internal reference).
    """


class IssuingAuthorizationEvaluationCreateParamsCardDetails(TypedDict):
    bin: str
    """
    The Bank Identification Number (BIN) of the card.
    """
    bin_country: str
    """
    The two-letter country code of the BIN issuer.
    """
    card_type: Literal["physical", "virtual"]
    """
    The type of the card.
    """
    created_at: int
    """
    The timestamp when the card was created, as a Unix timestamp in seconds.
    """
    last4: NotRequired[str]
    """
    The last 4 digits of the card number.
    """
    reference: str
    """
    User's specified unique ID of the card for this authorization attempt (e.g., RRN or internal reference).
    """


class IssuingAuthorizationEvaluationCreateParamsCardholderDetails(TypedDict):
    created_at: NotRequired[int]
    """
    The timestamp when the cardholder was created.
    """
    reference: NotRequired[str]
    """
    User's specified unique ID of the cardholder for this authorization attempt (e.g., RRN or internal reference).
    """


class IssuingAuthorizationEvaluationCreateParamsMerchantDetails(TypedDict):
    category_code: str
    """
    The merchant category code for the seller's business.
    """
    country: NotRequired[str]
    """
    Country where the seller is located.
    """
    name: str
    """
    Name of the seller.
    """
    network_id: str
    """
    Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.
    """
    terminal_id: NotRequired[str]
    """
    An ID assigned by the seller to the location of the sale.
    """


class IssuingAuthorizationEvaluationCreateParamsNetworkDetails(TypedDict):
    acquiring_institution_id: NotRequired[str]
    """
    Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be null.
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
    The card network over which Stripe received the authorization.
    """


class IssuingAuthorizationEvaluationCreateParamsTokenDetails(TypedDict):
    created_at: NotRequired[int]
    """
    The timestamp when the network token was created.
    """
    reference: NotRequired[str]
    """
    User's specified unique ID of the card token for this authorization attempt (e.g., RRN or internal reference).
    """
    wallet: NotRequired[Literal["apple_pay", "google_pay", "samsung_pay"]]
    """
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.
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
    The outcome of the 3D Secure authentication request.
    """
