# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class IssuedToken(StripeObject):
    """
    A SharedPaymentIssuedToken is a limited-use reference to a PaymentMethod that can be created with a secret key. When shared with another Stripe account (Seller), it enables that account to either process a payment on Stripe against a PaymentMethod that your Stripe account owns, or to forward a usable credential created against the originalPaymentMethod to then process the payment off-Stripe.
    """

    OBJECT_NAME: ClassVar[Literal["shared_payment.issued_token"]] = (
        "shared_payment.issued_token"
    )

    class NextAction(StripeObject):
        class UseStripeSdk(StripeObject):
            value: str
            """
            A base64-encoded string used by Stripe.js and the iOS and Android client SDKs to handle the next action. Its content is subject to change.
            """

        type: Literal["use_stripe_sdk"]
        """
        Specifies the type of next action required. Determines which child attribute contains action details.
        """
        use_stripe_sdk: Optional[UseStripeSdk]
        """
        Contains details for handling the next action using Stripe.js, iOS, or Android SDKs. Present when `next_action.type` is `use_stripe_sdk`.
        """
        _inner_class_types = {"use_stripe_sdk": UseStripeSdk}

    class RiskDetails(StripeObject):
        class Insights(StripeObject):
            class Bot(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: float
                """
                Risk score for this insight (float).
                """

            class CardIssuerDecline(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: float
                """
                Risk score for this insight (float).
                """

            class CardTesting(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: float
                """
                Risk score for this insight (float).
                """

            class FraudulentDispute(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: int
                """
                Risk score for this insight (integer).
                """

            class StolenCard(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: int
                """
                Risk score for this insight (integer).
                """

            bot: Optional[Bot]
            """
            Bot risk insight (score: Float, recommended_action).
            """
            card_issuer_decline: Optional[CardIssuerDecline]
            """
            Card issuer decline risk insight (score: Float, recommended_action).
            """
            card_testing: Optional[CardTesting]
            """
            Card testing risk insight (score: Float, recommended_action).
            """
            fraudulent_dispute: Optional[FraudulentDispute]
            """
            Fraudulent dispute risk insight (score: Integer, recommended_action).
            """
            stolen_card: Optional[StolenCard]
            """
            Stolen card risk insight (score: Integer, recommended_action).
            """
            _inner_class_types = {
                "bot": Bot,
                "card_issuer_decline": CardIssuerDecline,
                "card_testing": CardTesting,
                "fraudulent_dispute": FraudulentDispute,
                "stolen_card": StolenCard,
            }

        insights: Insights
        """
        Risk insights for this token, including scores and recommended actions for each risk type.
        """
        _inner_class_types = {"insights": Insights}

    class SellerDetails(StripeObject):
        external_id: str
        """
        A unique id within a network that identifies a logical seller. This should usually be the merchant id on the seller platform.
        """
        network_business_profile: str
        """
        The unique and logical string that identifies the seller platform that this SharedToken is being created for.
        """

    class UsageDetails(StripeObject):
        class AmountCaptured(StripeObject):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: int
            """
            Integer value of the amount in the smallest currency unit.
            """

        amount_captured: Optional[AmountCaptured]
        """
        The total amount captured using this SharedPaymentToken.
        """
        _inner_class_types = {"amount_captured": AmountCaptured}

    class UsageLimits(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        expires_at: Optional[int]
        """
        Time at which this SharedPaymentToken expires and can no longer be used to confirm a PaymentIntent.
        """
        max_amount: int
        """
        Max amount that can be captured using this SharedPaymentToken.
        """
        recurring_interval: Optional[Literal["month", "week", "year"]]
        """
        The recurring interval at which the shared payment token's amount usage restrictions reset.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[str]
    """
    ID of an existing Customer.
    """
    deactivated_at: Optional[int]
    """
    Time at which this SharedPaymentIssuedToken was deactivated.
    """
    deactivated_reason: Optional[
        Literal["consumed", "expired", "resolved", "revoked"]
    ]
    """
    The reason why the SharedPaymentIssuedToken has been deactivated.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    next_action: Optional[NextAction]
    """
    If present, describes the action required to make this `SharedPaymentIssuedToken` usable for payments. Present when the token is in `requires_action` state.
    """
    object: Literal["shared_payment.issued_token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method: Optional[str]
    """
    ID of an existing PaymentMethod.
    """
    return_url: Optional[str]
    """
    If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.
    """
    risk_details: Optional[RiskDetails]
    """
    Risk details of the SharedPaymentIssuedToken.
    """
    seller_details: Optional[SellerDetails]
    """
    Seller details of the SharedPaymentIssuedToken, including network_id and external_id.
    """
    setup_future_usage: Optional[Literal["on_session"]]
    """
    Indicates that you intend to save the PaymentMethod of this SharedPaymentToken to a customer later.
    """
    shared_metadata: Optional[UntypedStripeObject[str]]
    """
    Metadata about the SharedPaymentIssuedToken.
    """
    status: Optional[Literal["active", "deactivated", "requires_action"]]
    """
    Status of this SharedPaymentIssuedToken, one of `active`, `requires_action`, or `deactivated`.
    """
    usage_details: Optional[UsageDetails]
    """
    Usage details of the SharedPaymentIssuedToken
    """
    usage_limits: Optional[UsageLimits]
    """
    Usage limits of the SharedPaymentIssuedToken.
    """
    _inner_class_types = {
        "next_action": NextAction,
        "risk_details": RiskDetails,
        "seller_details": SellerDetails,
        "usage_details": UsageDetails,
        "usage_limits": UsageLimits,
    }
