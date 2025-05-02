# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._payment_record import PaymentRecord
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentRecordService(StripeService):
    class ReportPaymentAttemptCanceledParams(TypedDict):
        canceled_at: int
        """
        When the reported payment was canceled. Measured in seconds since the Unix epoch.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]

    class ReportPaymentAttemptFailedParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        failed_at: int
        """
        When the reported payment failed. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]

    class ReportPaymentAttemptGuaranteedParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        guaranteed_at: int
        """
        When the reported payment was guaranteed. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]

    class ReportPaymentAttemptParams(TypedDict):
        description: NotRequired[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        failed: NotRequired[
            "PaymentRecordService.ReportPaymentAttemptParamsFailed"
        ]
        """
        Information about the payment attempt failure.
        """
        guaranteed: NotRequired[
            "PaymentRecordService.ReportPaymentAttemptParamsGuaranteed"
        ]
        """
        Information about the payment attempt guarantee.
        """
        initiated_at: int
        """
        When the reported payment was initiated. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        outcome: NotRequired[Literal["failed", "guaranteed"]]
        """
        The outcome of the reported payment.
        """
        payment_method_details: NotRequired[
            "PaymentRecordService.ReportPaymentAttemptParamsPaymentMethodDetails"
        ]
        """
        Information about the Payment Method debited for this payment.
        """
        shipping_details: NotRequired[
            "PaymentRecordService.ReportPaymentAttemptParamsShippingDetails"
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
            "PaymentRecordService.ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetails"
        ]
        """
        The billing details associated with the method of payment.
        """
        custom: NotRequired[
            "PaymentRecordService.ReportPaymentAttemptParamsPaymentMethodDetailsCustom"
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
            "PaymentRecordService.ReportPaymentAttemptParamsPaymentMethodDetailsBillingDetailsAddress"
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
            "PaymentRecordService.ReportPaymentAttemptParamsShippingDetailsAddress"
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

    class ReportPaymentParams(TypedDict):
        amount_requested: (
            "PaymentRecordService.ReportPaymentParamsAmountRequested"
        )
        """
        The amount you initially requested for this payment.
        """
        customer_details: NotRequired[
            "PaymentRecordService.ReportPaymentParamsCustomerDetails"
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
        failed: NotRequired["PaymentRecordService.ReportPaymentParamsFailed"]
        """
        Information about the payment attempt failure.
        """
        guaranteed: NotRequired[
            "PaymentRecordService.ReportPaymentParamsGuaranteed"
        ]
        """
        Information about the payment attempt guarantee.
        """
        initiated_at: int
        """
        When the reported payment was initiated. Measured in seconds since the Unix epoch.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        outcome: NotRequired[Literal["failed", "guaranteed"]]
        """
        The outcome of the reported payment.
        """
        payment_method_details: (
            "PaymentRecordService.ReportPaymentParamsPaymentMethodDetails"
        )
        """
        Information about the Payment Method debited for this payment.
        """
        payment_reference: NotRequired[str]
        """
        An opaque string for manual reconciliation of this payment, for example a check number or a payment processor ID.
        """
        shipping_details: NotRequired[
            "PaymentRecordService.ReportPaymentParamsShippingDetails"
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
        A positive integer representing the amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) for example, 100 cents for 1 USD or 100 for 100 JPY, a zero-decimal currency.
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
            "PaymentRecordService.ReportPaymentParamsPaymentMethodDetailsBillingDetails"
        ]
        """
        The billing details associated with the method of payment.
        """
        custom: NotRequired[
            "PaymentRecordService.ReportPaymentParamsPaymentMethodDetailsCustom"
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
            "PaymentRecordService.ReportPaymentParamsPaymentMethodDetailsBillingDetailsAddress"
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
            "PaymentRecordService.ReportPaymentParamsShippingDetailsAddress"
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

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        id: str,
        params: "PaymentRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Retrieves a Payment Record with the given ID
        """
        return cast(
            PaymentRecord,
            self._request(
                "get",
                "/v1/payment_records/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "PaymentRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Retrieves a Payment Record with the given ID
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "get",
                "/v1/payment_records/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_payment_attempt(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            PaymentRecord,
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_payment_attempt_async(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report a new payment attempt on the specified Payment Record. A new payment
         attempt can only be specified if all other payment attempts are canceled or failed.
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_payment_attempt_canceled(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptCanceledParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            PaymentRecord,
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_payment_attempt_canceled_async(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptCanceledParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         was canceled.
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_canceled".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_payment_attempt_failed(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptFailedParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            PaymentRecord,
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_payment_attempt_failed_async(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptFailedParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         failed or errored.
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_failed".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_payment_attempt_guaranteed(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptGuaranteedParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            PaymentRecord,
            self._request(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_payment_attempt_guaranteed_async(
        self,
        id: str,
        params: "PaymentRecordService.ReportPaymentAttemptGuaranteedParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report that the most recent payment attempt on the specified Payment Record
         was guaranteed.
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "post",
                "/v1/payment_records/{id}/report_payment_attempt_guaranteed".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_payment(
        self,
        params: "PaymentRecordService.ReportPaymentParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report a new Payment Record. You may report a Payment Record as it is
         initialized and later report updates through the other report_* methods, or report Payment
         Records in a terminal state directly, through this method.
        """
        return cast(
            PaymentRecord,
            self._request(
                "post",
                "/v1/payment_records/report_payment",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_payment_async(
        self,
        params: "PaymentRecordService.ReportPaymentParams",
        options: RequestOptions = {},
    ) -> PaymentRecord:
        """
        Report a new Payment Record. You may report a Payment Record as it is
         initialized and later report updates through the other report_* methods, or report Payment
         Records in a terminal state directly, through this method.
        """
        return cast(
            PaymentRecord,
            await self._request_async(
                "post",
                "/v1/payment_records/report_payment",
                base_address="api",
                params=params,
                options=options,
            ),
        )
