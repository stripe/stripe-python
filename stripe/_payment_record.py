# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class PaymentRecord(APIResource["PaymentRecord"]):
    """
    A Payment Record is a resource that allows you to represent payments that occur on- or off-Stripe.
    For example, you can create a Payment Record to model a payment made on a different payment processor,
    in order to mark an Invoice as paid and a Subscription as active. Payment Records consist of one or
    more Payment Attempt Records, which represent individual attempts made on a payment network.
    """

    OBJECT_NAME: ClassVar[Literal["payment_record"]] = "payment_record"

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

    class ReportPaymentAttemptCanceledParams(RequestOptions):
        canceled_at: int
        """
        When the reported payment was canceled. Measured in seconds since the Unix epoch.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired[Dict[str, str]]

    class ReportPaymentAttemptFailedParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        failed_at: int
        """
        When the reported payment failed. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired[Dict[str, str]]

    class ReportPaymentAttemptGuaranteedParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        guaranteed_at: int
        """
        When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired[Dict[str, str]]

    class ReportPaymentAttemptParams(RequestOptions):
        description: NotRequired[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        failed: NotRequired["PaymentRecord.ReportPaymentAttemptParamsFailed"]
        """
        Information about the payment attempt failure.
        """
        guaranteed: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsGuaranteed"
        ]
        """
        Information about the payment attempt guarantee.
        """
        initiated_at: int
        """
        When the reported payment was initiated. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        outcome: NotRequired[Literal["failed", "guaranteed"]]
        """
        The outcome of the reported payment.
        """
        payment_method_details: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsPaymentMethodDetails"
        ]
        """
        Information about the Payment Method debited for this payment.
        """
        shipping_details: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsShippingDetails"
        ]
        """
        Shipping information for this payment.
        """

    class ReportPaymentAttemptParamsFailed(TypedDict):
        failed_at: int
        """
        When the reported payment failed. Measured in seconds since the Unix epoch.
        """

    class ReportPaymentAttemptParamsGuaranteed(TypedDict):
        guaranteed_at: int
        """
        When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
        """

    class ReportPaymentAttemptParamsPaymentMethodDetails(TypedDict):
        billing_details: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetails"
        ]
        """
        The billing details associated with the method of payment.
        """
        custom: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsPaymentMethodDetailsCustom"
        ]
        """
        Information about the custom (user-defined) payment method used to make this payment.
        """
        payment_method: NotRequired[str]
        """
        ID of the Stripe Payment Method used to make this payment.
        """
        type: NotRequired[Literal["custom"]]
        """
        The type of the payment method details. An additional hash is included on the payment_method_details with a name matching this value. It contains additional information specific to the type.
        """

    class ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetails(
        TypedDict,
    ):
        address: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetailsAddress"
        ]
        """
        The billing address associated with the method of payment.
        """
        email: NotRequired[str]
        """
        The billing email associated with the method of payment.
        """
        name: NotRequired[str]
        """
        The billing name associated with the method of payment.
        """
        phone: NotRequired[str]
        """
        The billing phone number associated with the method of payment.
        """

    class ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetailsAddress(
        TypedDict,
    ):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ReportPaymentAttemptParamsPaymentMethodDetailsCustom(TypedDict):
        display_name: NotRequired[str]
        """
        Display name for the custom (user-defined) payment method type used to make this payment.
        """
        type: NotRequired[str]
        """
        The custom payment method type associated with this payment.
        """

    class ReportPaymentAttemptParamsShippingDetails(TypedDict):
        address: NotRequired[
            "PaymentRecord.ReportPaymentAttemptParamsShippingDetailsAddress"
        ]
        """
        The physical shipping address.
        """
        name: NotRequired[str]
        """
        The shipping recipient's name.
        """
        phone: NotRequired[str]
        """
        The shipping recipient's phone number.
        """

    class ReportPaymentAttemptParamsShippingDetailsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ReportPaymentParams(RequestOptions):
        amount_requested: "PaymentRecord.ReportPaymentParamsAmountRequested"
        """
        The amount you intend to collect for this payment.
        """
        customer_details: NotRequired[
            "PaymentRecord.ReportPaymentParamsCustomerDetails"
        ]
        """
        Customer information for this payment.
        """
        customer_presence: NotRequired[Literal["off_session", "on_session"]]
        """
        Indicates whether the customer was present in your checkout flow during this payment.
        """
        description: NotRequired[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        failed: NotRequired["PaymentRecord.ReportPaymentParamsFailed"]
        """
        Information about the payment attempt failure.
        """
        guaranteed: NotRequired["PaymentRecord.ReportPaymentParamsGuaranteed"]
        """
        Information about the payment attempt guarantee.
        """
        initiated_at: int
        """
        When the reported payment was initiated. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        outcome: NotRequired[Literal["failed", "guaranteed"]]
        """
        The outcome of the reported payment.
        """
        payment_method_details: (
            "PaymentRecord.ReportPaymentParamsPaymentMethodDetails"
        )
        """
        Information about the Payment Method debited for this payment.
        """
        payment_reference: str
        """
        An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
        """
        shipping_details: NotRequired[
            "PaymentRecord.ReportPaymentParamsShippingDetails"
        ]
        """
        Shipping information for this payment.
        """

    class ReportPaymentParamsAmountRequested(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: int
        """
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) e.g., 100 cents for $1.00 or 100 for ¥100, a zero-decimal currency).
        """

    class ReportPaymentParamsCustomerDetails(TypedDict):
        customer: NotRequired[str]
        """
        The customer who made the payment.
        """
        email: NotRequired[str]
        """
        The customer's phone number.
        """
        name: NotRequired[str]
        """
        The customer's name.
        """
        phone: NotRequired[str]
        """
        The customer's phone number.
        """

    class ReportPaymentParamsFailed(TypedDict):
        failed_at: int
        """
        When the reported payment failed. Measured in seconds since the Unix epoch.
        """

    class ReportPaymentParamsGuaranteed(TypedDict):
        guaranteed_at: int
        """
        When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
        """

    class ReportPaymentParamsPaymentMethodDetails(TypedDict):
        billing_details: NotRequired[
            "PaymentRecord.ReportPaymentParamsPaymentMethodDetailsBillingDetails"
        ]
        """
        The billing details associated with the method of payment.
        """
        custom: NotRequired[
            "PaymentRecord.ReportPaymentParamsPaymentMethodDetailsCustom"
        ]
        """
        Information about the custom (user-defined) payment method used to make this payment.
        """
        payment_method: NotRequired[str]
        """
        ID of the Stripe Payment Method used to make this payment.
        """
        type: NotRequired[Literal["custom"]]
        """
        The type of the payment method details. An additional hash is included on the payment_method_details with a name matching this value. It contains additional information specific to the type.
        """

    class ReportPaymentParamsPaymentMethodDetailsBillingDetails(TypedDict):
        address: NotRequired[
            "PaymentRecord.ReportPaymentParamsPaymentMethodDetailsBillingDetailsAddress"
        ]
        """
        The billing address associated with the method of payment.
        """
        email: NotRequired[str]
        """
        The billing email associated with the method of payment.
        """
        name: NotRequired[str]
        """
        The billing name associated with the method of payment.
        """
        phone: NotRequired[str]
        """
        The billing phone number associated with the method of payment.
        """

    class ReportPaymentParamsPaymentMethodDetailsBillingDetailsAddress(
        TypedDict,
    ):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ReportPaymentParamsPaymentMethodDetailsCustom(TypedDict):
        display_name: NotRequired[str]
        """
        Display name for the custom (user-defined) payment method type used to make this payment.
        """
        type: NotRequired[str]
        """
        The custom payment method type associated with this payment.
        """

    class ReportPaymentParamsShippingDetails(TypedDict):
        address: NotRequired[
            "PaymentRecord.ReportPaymentParamsShippingDetailsAddress"
        ]
        """
        The physical shipping address.
        """
        name: NotRequired[str]
        """
        The shipping recipient's name.
        """
        phone: NotRequired[str]
        """
        The shipping recipient's phone number.
        """

    class ReportPaymentParamsShippingDetailsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
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
    latest_payment_attempt_record: str
    """
    ID of the latest Payment Attempt Record attached to this Payment Record.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_method_details: Optional[PaymentMethodDetails]
    """
    Information about the Payment Method debited for this payment.
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
    def report_payment(
        cls, **params: Unpack["PaymentRecord.ReportPaymentParams"]
    ) -> "PaymentRecord":
        """
        Report a new Payment Record. You may report a Payment Record as it is
         initialized and later report updates through the other report_* methods, or report Payment
         Records in a terminal state directly, through this method.
        """
        return cast(
            "PaymentRecord",
            cls._static_request(
                "post",
                "/v1/payment_records/report_payment",
                params=params,
            ),
        )

    @classmethod
    async def report_payment_async(
        cls, **params: Unpack["PaymentRecord.ReportPaymentParams"]
    ) -> "PaymentRecord":
        """
        Report a new Payment Record. You may report a Payment Record as it is
         initialized and later report updates through the other report_* methods, or report Payment
         Records in a terminal state directly, through this method.
        """
        return cast(
            "PaymentRecord",
            await cls._static_request_async(
                "post",
                "/v1/payment_records/report_payment",
                params=params,
            ),
        )

    @classmethod
    def _cls_report_payment_attempt(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"],
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            "PaymentRecord",
            cls._static_request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def report_payment_attempt(
        id: str, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        ...

    @overload
    def report_payment_attempt(
        self, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt")
    def report_payment_attempt(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            "PaymentRecord",
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_report_payment_attempt_async(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"],
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            "PaymentRecord",
            await cls._static_request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def report_payment_attempt_async(
        id: str, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        ...

    @overload
    async def report_payment_attempt_async(
        self, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_async")
    async def report_payment_attempt_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentRecord.ReportPaymentAttemptParams"]
    ) -> "PaymentRecord":
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            "PaymentRecord",
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_report_payment_attempt_canceled(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            "PaymentRecord",
            cls._static_request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def report_payment_attempt_canceled(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        ...

    @overload
    def report_payment_attempt_canceled(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_canceled")
    def report_payment_attempt_canceled(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            "PaymentRecord",
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_report_payment_attempt_canceled_async(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            "PaymentRecord",
            await cls._static_request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def report_payment_attempt_canceled_async(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        ...

    @overload
    async def report_payment_attempt_canceled_async(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_canceled_async")
    async def report_payment_attempt_canceled_async(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptCanceledParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            "PaymentRecord",
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_report_payment_attempt_failed(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            "PaymentRecord",
            cls._static_request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def report_payment_attempt_failed(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        ...

    @overload
    def report_payment_attempt_failed(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_failed")
    def report_payment_attempt_failed(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            "PaymentRecord",
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_report_payment_attempt_failed_async(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            "PaymentRecord",
            await cls._static_request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def report_payment_attempt_failed_async(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        ...

    @overload
    async def report_payment_attempt_failed_async(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_failed_async")
    async def report_payment_attempt_failed_async(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptFailedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            "PaymentRecord",
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_report_payment_attempt_guaranteed(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            "PaymentRecord",
            cls._static_request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def report_payment_attempt_guaranteed(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        ...

    @overload
    def report_payment_attempt_guaranteed(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_guaranteed")
    def report_payment_attempt_guaranteed(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            "PaymentRecord",
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_report_payment_attempt_guaranteed_async(
        cls,
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            "PaymentRecord",
            await cls._static_request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def report_payment_attempt_guaranteed_async(
        id: str,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        ...

    @overload
    async def report_payment_attempt_guaranteed_async(
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        ...

    @class_method_variant("_cls_report_payment_attempt_guaranteed_async")
    async def report_payment_attempt_guaranteed_async(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        **params: Unpack["PaymentRecord.ReportPaymentAttemptGuaranteedParams"],
    ) -> "PaymentRecord":
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            "PaymentRecord",
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentRecord.RetrieveParams"]
    ) -> "PaymentRecord":
        """
        Retrieves a Payment Record with the given ID
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentRecord.RetrieveParams"]
    ) -> "PaymentRecord":
        """
        Retrieves a Payment Record with the given ID
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
