# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, Union, cast, overload
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

    class AgentDetails(StripeObject):
        network_business_profile: Optional[str]
        """
        The Stripe Profile ID of the agent that issued this SharedPaymentGrantedToken.
        """

    class PaymentMethodDetails(StripeObject):
        class Affirm(StripeObject):
            pass

        class BillingDetails(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[str]
                """
                Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                """
                line1: Optional[str]
                """
                Address line 1, such as the street, PO Box, or company name.
                """
                line2: Optional[str]
                """
                Address line 2, such as the apartment, suite, unit, or building.
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                """

            address: Optional[Address]
            """
            Billing address.
            """
            email: Optional[str]
            """
            Email address.
            """
            name: Optional[str]
            """
            Full name.
            """
            phone: Optional[str]
            """
            Billing phone number (including extension).
            """
            tax_id: Optional[str]
            """
            Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.
            """
            _inner_class_types = {"address": Address}

        class Card(StripeObject):
            class Checks(StripeObject):
                address_line1_check: Optional[str]
                """
                If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
                """
                address_postal_code_check: Optional[str]
                """
                If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
                """
                cvc_check: Optional[str]
                """
                If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
                """

            class Networks(StripeObject):
                available: List[str]
                """
                All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
                """
                preferred: Optional[str]
                """
                The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.
                """

            class Wallet(StripeObject):
                class AmexExpressCheckout(StripeObject):
                    pass

                class ApplePay(StripeObject):
                    pass

                class GooglePay(StripeObject):
                    pass

                class Link(StripeObject):
                    pass

                class Masterpass(StripeObject):
                    class BillingAddress(StripeObject):
                        city: Optional[str]
                        """
                        City, district, suburb, town, or village.
                        """
                        country: Optional[str]
                        """
                        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                        """
                        line1: Optional[str]
                        """
                        Address line 1, such as the street, PO Box, or company name.
                        """
                        line2: Optional[str]
                        """
                        Address line 2, such as the apartment, suite, unit, or building.
                        """
                        postal_code: Optional[str]
                        """
                        ZIP or postal code.
                        """
                        state: Optional[str]
                        """
                        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                        """

                    class ShippingAddress(StripeObject):
                        city: Optional[str]
                        """
                        City, district, suburb, town, or village.
                        """
                        country: Optional[str]
                        """
                        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                        """
                        line1: Optional[str]
                        """
                        Address line 1, such as the street, PO Box, or company name.
                        """
                        line2: Optional[str]
                        """
                        Address line 2, such as the apartment, suite, unit, or building.
                        """
                        postal_code: Optional[str]
                        """
                        ZIP or postal code.
                        """
                        state: Optional[str]
                        """
                        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                        """

                    billing_address: Optional[BillingAddress]
                    """
                    Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    email: Optional[str]
                    """
                    Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    name: Optional[str]
                    """
                    Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    shipping_address: Optional[ShippingAddress]
                    """
                    Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    _inner_class_types = {
                        "billing_address": BillingAddress,
                        "shipping_address": ShippingAddress,
                    }

                class SamsungPay(StripeObject):
                    pass

                class VisaCheckout(StripeObject):
                    class BillingAddress(StripeObject):
                        city: Optional[str]
                        """
                        City, district, suburb, town, or village.
                        """
                        country: Optional[str]
                        """
                        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                        """
                        line1: Optional[str]
                        """
                        Address line 1, such as the street, PO Box, or company name.
                        """
                        line2: Optional[str]
                        """
                        Address line 2, such as the apartment, suite, unit, or building.
                        """
                        postal_code: Optional[str]
                        """
                        ZIP or postal code.
                        """
                        state: Optional[str]
                        """
                        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                        """

                    class ShippingAddress(StripeObject):
                        city: Optional[str]
                        """
                        City, district, suburb, town, or village.
                        """
                        country: Optional[str]
                        """
                        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                        """
                        line1: Optional[str]
                        """
                        Address line 1, such as the street, PO Box, or company name.
                        """
                        line2: Optional[str]
                        """
                        Address line 2, such as the apartment, suite, unit, or building.
                        """
                        postal_code: Optional[str]
                        """
                        ZIP or postal code.
                        """
                        state: Optional[str]
                        """
                        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                        """

                    billing_address: Optional[BillingAddress]
                    """
                    Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    email: Optional[str]
                    """
                    Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    name: Optional[str]
                    """
                    Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    shipping_address: Optional[ShippingAddress]
                    """
                    Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                    """
                    _inner_class_types = {
                        "billing_address": BillingAddress,
                        "shipping_address": ShippingAddress,
                    }

                amex_express_checkout: Optional[AmexExpressCheckout]
                apple_pay: Optional[ApplePay]
                dynamic_last4: Optional[str]
                """
                (For tokenized numbers only.) The last four digits of the device account number.
                """
                google_pay: Optional[GooglePay]
                link: Optional[Link]
                masterpass: Optional[Masterpass]
                samsung_pay: Optional[SamsungPay]
                type: Literal[
                    "amex_express_checkout",
                    "apple_pay",
                    "google_pay",
                    "link",
                    "masterpass",
                    "samsung_pay",
                    "visa_checkout",
                ]
                """
                The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
                """
                visa_checkout: Optional[VisaCheckout]
                _inner_class_types = {
                    "amex_express_checkout": AmexExpressCheckout,
                    "apple_pay": ApplePay,
                    "google_pay": GooglePay,
                    "link": Link,
                    "masterpass": Masterpass,
                    "samsung_pay": SamsungPay,
                    "visa_checkout": VisaCheckout,
                }

            brand: str
            """
            Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
            """
            checks: Optional[Checks]
            """
            Checks on Card address and CVC if provided.
            """
            country: Optional[str]
            """
            Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
            """
            description: Optional[str]
            """
            A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
            """
            display_brand: Optional[str]
            """
            The brand to use when displaying the card, this accounts for customer's brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.
            """
            exp_month: int
            """
            Two-digit number representing the card's expiration month.
            """
            exp_year: int
            """
            Four-digit number representing the card's expiration year.
            """
            fingerprint: Optional[str]
            """
            Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

            *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
            """
            funding: str
            """
            Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
            """
            iin: Optional[str]
            """
            Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
            """
            issuer: Optional[str]
            """
            The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
            """
            last4: str
            """
            The last four digits of the card.
            """
            networks: Optional[Networks]
            """
            Contains information about card networks that can be used to process the payment.
            """
            wallet: Optional[Wallet]
            """
            If this Card is part of a card wallet, this contains the details of the card wallet.
            """
            _inner_class_types = {
                "checks": Checks,
                "networks": Networks,
                "wallet": Wallet,
            }

        class Klarna(StripeObject):
            class Dob(StripeObject):
                day: Optional[int]
                """
                The day of birth, between 1 and 31.
                """
                month: Optional[int]
                """
                The month of birth, between 1 and 12.
                """
                year: Optional[int]
                """
                The four-digit year of birth.
                """

            dob: Optional[Dob]
            """
            The customer's date of birth, if provided.
            """
            _inner_class_types = {"dob": Dob}

        class Link(StripeObject):
            email: Optional[str]
            """
            Account owner's email address.
            """
            persistent_token: Optional[str]
            """
            [Deprecated] This is a legacy parameter that no longer has any function.
            """

        affirm: Optional[Affirm]
        billing_details: Optional[BillingDetails]
        """
        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
        """
        card: Optional[Card]
        klarna: Optional[Klarna]
        link: Optional[Link]
        type: Union[
            Literal["affirm", "card", "klarna", "link", "shop_pay"], str
        ]
        """
        The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
        """
        _inner_class_types = {
            "affirm": Affirm,
            "billing_details": BillingDetails,
            "card": Card,
            "klarna": Klarna,
            "link": Link,
        }

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
        recurring_interval: Optional[
            Union[Literal["month", "week", "year"], str]
        ]
        """
        The recurring interval at which the shared payment token's amount usage restrictions reset.
        """

    agent_details: Optional[AgentDetails]
    """
    Details about the agent that issued this SharedPaymentGrantedToken.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deactivated_at: Optional[int]
    """
    Time at which this SharedPaymentGrantedToken expires and can no longer be used to confirm a PaymentIntent.
    """
    deactivated_reason: Optional[
        Union[Literal["consumed", "expired", "resolved", "revoked"], str]
    ]
    """
    The reason why the SharedPaymentGrantedToken has been deactivated.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["shared_payment.granted_token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method_details: Optional[PaymentMethodDetails]
    """
    Details of the PaymentMethod that was shared via this token.
    """
    risk_details: Optional[RiskDetails]
    """
    Risk details of the SharedPaymentGrantedToken.
    """
    shared_metadata: Optional[UntypedStripeObject[str]]
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
                            self.resource._data.get("id")
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
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "agent_details": AgentDetails,
        "payment_method_details": PaymentMethodDetails,
        "risk_details": RiskDetails,
        "usage_details": UsageDetails,
        "usage_limits": UsageLimits,
    }


GrantedToken.TestHelpers._resource_cls = GrantedToken
