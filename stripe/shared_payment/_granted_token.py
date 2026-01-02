# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, Optional, cast, overload
from typing_extensions import Literal, Type, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.shared_payment._granted_token_create_params import (
        GrantedTokenCreateParams,
    )
    from stripe.params.shared_payment._granted_token_retrieve_params import (
        GrantedTokenRetrieveParams,
    )
    from stripe.params.shared_payment._granted_token_revoke_params import (
        GrantedTokenRevokeParams,
    )


class GrantedToken(APIResource["GrantedToken"]):
    """
    SharedPaymentGrantedToken is the view-only resource of a SharedPaymentIssuedToken, which is a limited-use reference to a PaymentMethod.
    When another Stripe merchant shares a SharedPaymentIssuedToken with you, you can view attributes of the shared token using the SharedPaymentGrantedToken API, and use it with a PaymentIntent.
    """

    OBJECT_NAME: ClassVar[Literal["shared_payment.granted_token"]] = (
        "shared_payment.granted_token"
    )

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
        expires_at: int
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
    Time at which this SharedPaymentGrantedToken expires and can no longer be used to confirm a PaymentIntent.
    """
    deactivated_reason: Optional[Literal["consumed", "expired", "revoked"]]
    """
    The reason why the SharedPaymentGrantedToken has been deactivated.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["shared_payment.granted_token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    shared_metadata: Optional[Dict[str, str]]
    """
    Metadata about the SharedPaymentGrantedToken.
    """
    usage_details: Optional[UsageDetails]
    """
    Some details about how the SharedPaymentGrantedToken has been used already.
    """
    usage_limits: Optional[UsageLimits]
    """
    Limits on how this SharedPaymentGrantedToken can be used.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["GrantedTokenRetrieveParams"]
    ) -> "GrantedToken":
        """
        Retrieves an existing SharedPaymentGrantedToken object
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["GrantedTokenRetrieveParams"]
    ) -> "GrantedToken":
        """
        Retrieves an existing SharedPaymentGrantedToken object
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    class TestHelpers(APIResourceTestHelpers["GrantedToken"]):
        _resource_cls: Type["GrantedToken"]

        @classmethod
        def create(
            cls, **params: Unpack["GrantedTokenCreateParams"]
        ) -> "GrantedToken":
            """
            Creates a new test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to create SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens",
                    params=params,
                ),
            )

        @classmethod
        async def create_async(
            cls, **params: Unpack["GrantedTokenCreateParams"]
        ) -> "GrantedToken":
            """
            Creates a new test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to create SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens",
                    params=params,
                ),
            )

        @classmethod
        def _cls_revoke(
            cls,
            shared_payment_granted_token: str,
            **params: Unpack["GrantedTokenRevokeParams"],
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                        shared_payment_granted_token=sanitize_id(
                            shared_payment_granted_token
                        )
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def revoke(
            shared_payment_granted_token: str,
            **params: Unpack["GrantedTokenRevokeParams"],
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            ...

        @overload
        def revoke(
            self, **params: Unpack["GrantedTokenRevokeParams"]
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            ...

        @class_method_variant("_cls_revoke")
        def revoke(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["GrantedTokenRevokeParams"]
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                        shared_payment_granted_token=sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_revoke_async(
            cls,
            shared_payment_granted_token: str,
            **params: Unpack["GrantedTokenRevokeParams"],
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                        shared_payment_granted_token=sanitize_id(
                            shared_payment_granted_token
                        )
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def revoke_async(
            shared_payment_granted_token: str,
            **params: Unpack["GrantedTokenRevokeParams"],
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            ...

        @overload
        async def revoke_async(
            self, **params: Unpack["GrantedTokenRevokeParams"]
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            ...

        @class_method_variant("_cls_revoke_async")
        async def revoke_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["GrantedTokenRevokeParams"]
        ) -> "GrantedToken":
            """
            Revokes a test SharedPaymentGrantedToken object. This endpoint is only available in test mode and allows sellers to revoke SharedPaymentGrantedTokens for testing their integration
            """
            return cast(
                "GrantedToken",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/shared_payment/granted_tokens/{shared_payment_granted_token}/revoke".format(
                        shared_payment_granted_token=sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "usage_details": UsageDetails,
        "usage_limits": UsageLimits,
    }


GrantedToken.TestHelpers._resource_cls = GrantedToken
