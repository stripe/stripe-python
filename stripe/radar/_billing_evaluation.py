# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.radar._billing_evaluation_create_params import (
        BillingEvaluationCreateParams,
    )


class BillingEvaluation(CreateableAPIResource["BillingEvaluation"]):
    """
    Billing Evaluations represent Stripe Radar's assessment of the non-payment abuse risk of an upcoming charge. Unlike a [Payment Evaluation](https://docs.stripe.com/api/radar/payment-evaluation), a billing evaluation is created before the payment is attempted and returns the `non_payment_abuse` signal only.
    """

    OBJECT_NAME: ClassVar[Literal["radar.billing_evaluation"]] = (
        "radar.billing_evaluation"
    )

    class ClientDeviceMetadataDetails(StripeObject):
        radar_session: Optional[str]
        """
        ID for the Radar Session associated with the billing evaluation. A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
        """

    class CustomerDetails(StripeObject):
        class Data(StripeObject):
            email: Optional[str]
            """
            The customer's email address.
            """
            name: Optional[str]
            """
            The customer's full name or business name.
            """
            phone: Optional[str]
            """
            The customer's phone number.
            """

        customer: Optional[str]
        """
        The ID of the customer whose upcoming payment was evaluated.
        """
        customer_account: Optional[str]
        """
        The ID of the Account representing the customer whose upcoming payment was evaluated.
        """
        data: Optional[Data]
        """
        Attributes of the customer being evaluated. These are populated from the `customer` or `customer_account` object when one was supplied, and from the request otherwise.
        """
        _inner_class_types = {"data": Data}

    class PaymentDetails(StripeObject):
        class MoneyMovementDetails(StripeObject):
            class Card(StripeObject):
                customer_presence: Optional[
                    Union[Literal["off_session", "on_session"], str]
                ]
                """
                Describes the presence of the customer during the payment.
                """
                payment_type: Optional[
                    Union[
                        Literal[
                            "one_off",
                            "recurring",
                            "setup_one_off",
                            "setup_recurring",
                        ],
                        str,
                    ]
                ]
                """
                Describes the type of payment.
                """

            card: Optional[Card]
            """
            Describes card money movement details.
            """
            money_movement_type: Literal["card"]
            """
            Describes the type of money movement. Currently only `card` is supported.
            """
            _inner_class_types = {"card": Card}

        class PaymentMethodDetails(StripeObject):
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

                address: Address
                """
                Address data.
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
                _inner_class_types = {"address": Address}

            billing_details: Optional[BillingDetails]
            """
            Billing information associated with the billing evaluation.
            """
            payment_method: Optional[str]
            """
            The payment method that will be charged.
            """
            _inner_class_types = {"billing_details": BillingDetails}

        class ShippingDetails(StripeObject):
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

            address: Address
            """
            Address data.
            """
            name: Optional[str]
            """
            Shipping name.
            """
            phone: Optional[str]
            """
            Shipping phone number.
            """
            _inner_class_types = {"address": Address}

        amount: int
        """
        Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        description: Optional[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        money_movement_details: Optional[MoneyMovementDetails]
        """
        Details about the payment's customer presence and type.
        """
        payment_method_details: Optional[PaymentMethodDetails]
        """
        Details about the payment method that will be charged.
        """
        shipping_details: Optional[ShippingDetails]
        """
        Shipping details for the billing evaluation.
        """
        statement_descriptor: Optional[str]
        """
        Payment statement descriptor.
        """
        _inner_class_types = {
            "money_movement_details": MoneyMovementDetails,
            "payment_method_details": PaymentMethodDetails,
            "shipping_details": ShippingDetails,
        }

    class Signals(StripeObject):
        class NonPaymentAbuse(StripeObject):
            evaluated_at: int
            """
            The time when this signal was evaluated.
            """
            risk_level: Union[
                Literal[
                    "elevated",
                    "highest",
                    "low",
                    "normal",
                    "not_assessed",
                    "unknown",
                ],
                str,
            ]
            """
            Risk level.
            """

        non_payment_abuse: Optional[NonPaymentAbuse]
        """
        Stripe Radar's assessment of the likelihood that the upcoming charge results in non-payment abuse.
        """
        _inner_class_types = {"non_payment_abuse": NonPaymentAbuse}

    client_device_metadata_details: Optional[ClientDeviceMetadataDetails]
    """
    Client device metadata attached to this billing evaluation.
    """
    created_at: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer_details: Optional[CustomerDetails]
    """
    Details of the customer this billing evaluation assesses.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["radar.billing_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_details: Optional[PaymentDetails]
    """
    Payment details for the upcoming charge this billing evaluation assesses.
    """
    signals: Signals
    """
    Stripe Radar's signals for the upcoming charge this billing evaluation assesses.
    """

    @classmethod
    def create(
        cls, **params: Unpack["BillingEvaluationCreateParams"]
    ) -> "BillingEvaluation":
        """
        Request Stripe Radar's assessment of the non-payment abuse risk of an upcoming charge, before the payment is attempted.
        """
        return cast(
            "BillingEvaluation",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["BillingEvaluationCreateParams"]
    ) -> "BillingEvaluation":
        """
        Request Stripe Radar's assessment of the non-payment abuse risk of an upcoming charge, before the payment is attempted.
        """
        return cast(
            "BillingEvaluation",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {
        "client_device_metadata_details": ClientDeviceMetadataDetails,
        "customer_details": CustomerDetails,
        "payment_details": PaymentDetails,
        "signals": Signals,
    }
