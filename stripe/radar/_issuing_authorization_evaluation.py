# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.radar._issuing_authorization_evaluation_create_params import (
        IssuingAuthorizationEvaluationCreateParams,
    )


class IssuingAuthorizationEvaluation(
    CreateableAPIResource["IssuingAuthorizationEvaluation"],
):
    """
    Authorization Evaluations represent fraud risk assessments for Issuing card authorizations. They include fraud risk signals and contextual details about the authorization.
    """

    OBJECT_NAME: ClassVar[
        Literal["radar.issuing_authorization_evaluation"]
    ] = "radar.issuing_authorization_evaluation"

    class AuthorizationDetails(StripeObject):
        amount: int
        """
        The total amount of the authorization in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        authorization_method: Optional[
            Literal["chip", "contactless", "keyed_in", "online", "swipe"]
        ]
        """
        How the card details were provided.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        entry_mode: Optional[
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
        entry_mode_raw_code: Optional[str]
        """
        Raw code indicating the entry mode from the network message.
        """
        initiated_at: int
        """
        The timestamp of the authorization initiated in seconds.
        """
        point_of_sale_condition: Optional[
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
        point_of_sale_condition_raw_code: Optional[str]
        """
        Raw code indicating the point of sale condition from the network message.
        """
        reference: str
        """
        User's specified unique ID for this authorization attempt (e.g., RRN or internal reference).
        """

    class CardDetails(StripeObject):
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
        The timestamp when the card was created.
        """
        last4: str
        """
        The last 4 digits of the card number.
        """
        reference: str
        """
        User's specified unique ID of the card for this authorization attempt (e.g., RRN or internal reference).
        """

    class CardholderDetails(StripeObject):
        created_at: Optional[int]
        """
        The timestamp when the cardholder was created.
        """
        reference: Optional[str]
        """
        User's specified unique ID of the cardholder for this authorization attempt (e.g., RRN or internal reference).
        """

    class MerchantDetails(StripeObject):
        category_code: str
        """
        The merchant category code for the seller's business.
        """
        country: Optional[str]
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
        terminal_id: Optional[str]
        """
        An ID assigned by the seller to the location of the sale.
        """

    class NetworkDetails(StripeObject):
        acquiring_institution_id: Optional[str]
        """
        Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be null.
        """
        routed_network: Optional[
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

    class Signals(StripeObject):
        class FraudRisk(StripeObject):
            class Data(StripeObject):
                evaluated_at: int
                """
                The time when this signal was evaluated.
                """
                level: Literal[
                    "elevated",
                    "highest",
                    "low",
                    "normal",
                    "not_assessed",
                    "unknown",
                ]
                """
                Risk level, based on the score.
                """
                score: float
                """
                Fraud risk score for this evaluation. Score in the range [0,100], formatted as a 2 decimal float, with higher scores indicating a higher likelihood of fraud.
                """

            data: Optional[Data]
            """
            Signal evaluation data, including score and level.
            """
            error: Optional[Dict[str, str]]
            """
            Details of an error that prevented reporting this signal.
            """
            status: Literal["error", "success"]
            """
            The status of this signal.
            """
            _inner_class_types = {"data": Data}

        fraud_risk: FraudRisk
        """
        A fraud risk signal with status, error, and data fields.
        """
        _inner_class_types = {"fraud_risk": FraudRisk}

    class TokenDetails(StripeObject):
        created_at: Optional[int]
        """
        The timestamp when the network token was created.
        """
        reference: Optional[str]
        """
        User's specified unique ID of the card token for this authorization attempt (e.g., RRN or internal reference).
        """
        wallet: Optional[Literal["apple_pay", "google_pay", "samsung_pay"]]
        """
        The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.
        """

    class VerificationDetails(StripeObject):
        three_d_secure_result: Optional[
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

    authorization_details: Optional[AuthorizationDetails]
    """
    Details about the authorization.
    """
    card_details: Optional[CardDetails]
    """
    Details about the card used in the authorization.
    """
    cardholder_details: Optional[CardholderDetails]
    """
    Details about the cardholder.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    merchant_details: Optional[MerchantDetails]
    """
    Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network_details: Optional[NetworkDetails]
    """
    Details about the authorization, such as identifiers, set by the card network.
    """
    object: Literal["radar.issuing_authorization_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    signals: Signals
    """
    Collection of fraud risk signals for this authorization evaluation.
    """
    token_details: Optional[TokenDetails]
    """
    Details about the token, if a tokenized payment method was used for the authorization.
    """
    verification_details: Optional[VerificationDetails]
    """
    Details about verification data for the authorization.
    """

    @classmethod
    def create(
        cls, **params: Unpack["IssuingAuthorizationEvaluationCreateParams"]
    ) -> "IssuingAuthorizationEvaluation":
        """
        Request a fraud risk assessment from Stripe for an Issuing card authorization.
        """
        return cast(
            "IssuingAuthorizationEvaluation",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["IssuingAuthorizationEvaluationCreateParams"]
    ) -> "IssuingAuthorizationEvaluation":
        """
        Request a fraud risk assessment from Stripe for an Issuing card authorization.
        """
        return cast(
            "IssuingAuthorizationEvaluation",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {
        "authorization_details": AuthorizationDetails,
        "card_details": CardDetails,
        "cardholder_details": CardholderDetails,
        "merchant_details": MerchantDetails,
        "network_details": NetworkDetails,
        "signals": Signals,
        "token_details": TokenDetails,
        "verification_details": VerificationDetails,
    }
