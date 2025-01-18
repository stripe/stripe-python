# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class PaymentAttemptRecord(ListableAPIResource["PaymentAttemptRecord"]):
    """
    A Payment Attempt Record represents an individual attempt at making a payment, on or off Stripe.
    Each payment attempt tries to collect a fixed amount of money from a fixed customer and payment
    method. Payment Attempt Records are attached to Payment Records. Only one attempt per Payment Record
    can have guaranteed funds.
    """

    OBJECT_NAME: ClassVar[Literal["payment_attempt_record"]] = (
        "payment_attempt_record"
    )

    class AmountCanceled(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountFailed(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountGuaranteed(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class AmountRequested(StripeObject):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class CustomerDetails(StripeObject):
        customer: Optional[str]
        """
        ID of the Stripe Customer associated with this payment.
        """
        email: Optional[str]
        """
        The customer's email address.
        """
        name: Optional[str]
        """
        The customer's name.
        """
        phone: Optional[str]
        """
        The customer's phone number.
        """

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
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """

            address: Address
            """
            A representation of a physical address.
            """
            email: Optional[str]
            """
            The billing email associated with the method of payment.
            """
            name: Optional[str]
            """
            The billing name associated with the method of payment.
            """
            phone: Optional[str]
            """
            The billing phone number associated with the method of payment.
            """
            _inner_class_types = {"address": Address}

        class Custom(StripeObject):
            display_name: str
            """
            Display name for the custom (user-defined) payment method type used to make this payment.
            """
            type: Optional[str]
            """
            The custom payment method type associated with this payment.
            """

        billing_details: Optional[BillingDetails]
        """
        The billing details associated with the method of payment.
        """
        custom: Optional[Custom]
        """
        Information about the custom (user-defined) payment method used to make this payment.
        """
        payment_method: Optional[str]
        """
        ID of the Stripe PaymentMethod used to make this payment.
        """
        type: Literal["custom"]
        """
        The type of Payment Method used for this payment attempt.
        """
        _inner_class_types = {
            "billing_details": BillingDetails,
            "custom": Custom,
        }

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
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Address
        """
        A representation of a physical address.
        """
        name: Optional[str]
        """
        The shipping recipient's name.
        """
        phone: Optional[str]
        """
        The shipping recipient's phone number.
        """
        _inner_class_types = {"address": Address}

    class ListParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_record: str
        """
        The ID of the Payment Record.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount_canceled: AmountCanceled
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_failed: AmountFailed
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_guaranteed: AmountGuaranteed
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    amount_requested: AmountRequested
    """
    A representation of an amount of money, consisting of an amount and a currency.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer_details: Optional[CustomerDetails]
    """
    Customer information for this payment.
    """
    customer_presence: Optional[Literal["off_session", "on_session"]]
    """
    Indicates whether the customer was present in your checkout flow during this payment.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_attempt_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method_details: Optional[PaymentMethodDetails]
    """
    Information about the Payment Method debited for this payment.
    """
    payment_record: str
    """
    ID of the Payment Record this Payment Attempt Record belongs to.
    """
    payment_reference: Optional[str]
    """
    An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
    """
    shipping_details: Optional[ShippingDetails]
    """
    Shipping information for this payment.
    """

    @classmethod
    def list(
        cls, **params: Unpack["PaymentAttemptRecord.ListParams"]
    ) -> ListObject["PaymentAttemptRecord"]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
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
        cls, **params: Unpack["PaymentAttemptRecord.ListParams"]
    ) -> ListObject["PaymentAttemptRecord"]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
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
    def retrieve(
        cls, id: str, **params: Unpack["PaymentAttemptRecord.RetrieveParams"]
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentAttemptRecord.RetrieveParams"]
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "amount_canceled": AmountCanceled,
        "amount_failed": AmountFailed,
        "amount_guaranteed": AmountGuaranteed,
        "amount_requested": AmountRequested,
        "customer_details": CustomerDetails,
        "payment_method_details": PaymentMethodDetails,
        "shipping_details": ShippingDetails,
    }
