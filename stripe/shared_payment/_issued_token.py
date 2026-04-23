# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.shared_payment._issued_token_create_params import (
        IssuedTokenCreateParams,
    )
    from stripe.params.shared_payment._issued_token_retrieve_params import (
        IssuedTokenRetrieveParams,
    )
    from stripe.params.shared_payment._issued_token_revoke_params import (
        IssuedTokenRevokeParams,
    )


class IssuedToken(CreateableAPIResource["IssuedToken"]):
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
                Risk score for this insight.
                """

            class CardIssuerDecline(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: float
                """
                Risk score for this insight.
                """

            class CardTesting(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: float
                """
                Risk score for this insight.
                """

            class FraudulentDispute(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: int
                """
                Risk score for this insight.
                """

            class StolenCard(StripeObject):
                recommended_action: str
                """
                Recommended action for this insight.
                """
                score: int
                """
                Risk score for this insight.
                """

            bot: Optional[Bot]
            """
            Bot risk insight.
            """
            card_issuer_decline: Optional[CardIssuerDecline]
            """
            Card issuer decline risk insight.
            """
            card_testing: Optional[CardTesting]
            """
            Card testing risk insight.
            """
            fraudulent_dispute: Optional[FraudulentDispute]
            """
            Fraudulent dispute risk insight.
            """
            stolen_card: Optional[StolenCard]
            """
            Stolen card risk insight.
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

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
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
    payment_method: str
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

    @classmethod
    def create(
        cls, **params: Unpack["IssuedTokenCreateParams"]
    ) -> "IssuedToken":
        """
        Creates a new SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["IssuedTokenCreateParams"]
    ) -> "IssuedToken":
        """
        Creates a new SharedPaymentIssuedToken object
        """
        return cast(
            "IssuedToken",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["IssuedTokenRetrieveParams"]
    ) -> "IssuedToken":
        """
        Retrieves an existing SharedPaymentIssuedToken object
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["IssuedTokenRetrieveParams"]
    ) -> "IssuedToken":
        """
        Retrieves an existing SharedPaymentIssuedToken object
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_revoke(
        cls,
        shared_payment_issued_token: str,
        **params: Unpack["IssuedTokenRevokeParams"],
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            cls._static_request(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def revoke(
        shared_payment_issued_token: str,
        **params: Unpack["IssuedTokenRevokeParams"],
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        ...

    @overload
    def revoke(
        self, **params: Unpack["IssuedTokenRevokeParams"]
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        ...

    @class_method_variant("_cls_revoke")
    def revoke(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["IssuedTokenRevokeParams"]
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            self._request(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        self._data.get("id")
                    )
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_revoke_async(
        cls,
        shared_payment_issued_token: str,
        **params: Unpack["IssuedTokenRevokeParams"],
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            await cls._static_request_async(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        shared_payment_issued_token
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def revoke_async(
        shared_payment_issued_token: str,
        **params: Unpack["IssuedTokenRevokeParams"],
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        ...

    @overload
    async def revoke_async(
        self, **params: Unpack["IssuedTokenRevokeParams"]
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        ...

    @class_method_variant("_cls_revoke_async")
    async def revoke_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["IssuedTokenRevokeParams"]
    ) -> "IssuedToken":
        """
        Revokes a SharedPaymentIssuedToken
        """
        return cast(
            "IssuedToken",
            await self._request_async(
                "post",
                "/v1/shared_payment/issued_tokens/{shared_payment_issued_token}/revoke".format(
                    shared_payment_issued_token=sanitize_id(
                        self._data.get("id")
                    )
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "next_action": NextAction,
        "risk_details": RiskDetails,
        "seller_details": SellerDetails,
        "usage_details": UsageDetails,
        "usage_limits": UsageLimits,
    }
