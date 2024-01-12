# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.treasury._transaction import Transaction


class OutboundPayment(
    CreateableAPIResource["OutboundPayment"],
    ListableAPIResource["OutboundPayment"],
):
    """
    Use OutboundPayments to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).

    Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.outbound_payment"]
    ] = "treasury.outbound_payment"

    class DestinationPaymentMethodDetails(StripeObject):
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
            email: Optional[str]
            """
            Email address.
            """
            name: Optional[str]
            """
            Full name.
            """
            _inner_class_types = {"address": Address}

        class FinancialAccount(StripeObject):
            id: str
            """
            Token of the FinancialAccount.
            """
            network: Literal["stripe"]
            """
            The rails used to send funds.
            """

        class UsBankAccount(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
            """
            Account holder type: individual or company.
            """
            account_type: Optional[Literal["checking", "savings"]]
            """
            Account type: checkings or savings. Defaults to checking if omitted.
            """
            bank_name: Optional[str]
            """
            Name of the bank associated with the bank account.
            """
            fingerprint: Optional[str]
            """
            Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
            """
            last4: Optional[str]
            """
            Last four digits of the bank account number.
            """
            network: Literal["ach", "us_domestic_wire"]
            """
            The US bank account network used to send funds.
            """
            routing_number: Optional[str]
            """
            Routing number of the bank account.
            """

        billing_details: BillingDetails
        financial_account: Optional[FinancialAccount]
        type: Literal["financial_account", "us_bank_account"]
        """
        The type of the payment method used in the OutboundPayment.
        """
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "financial_account": FinancialAccount,
            "us_bank_account": UsBankAccount,
        }

    class EndUserDetails(StripeObject):
        ip_address: Optional[str]
        """
        IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.
        """
        present: bool
        """
        `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.
        """

    class ReturnedDetails(StripeObject):
        code: Literal[
            "account_closed",
            "account_frozen",
            "bank_account_restricted",
            "bank_ownership_changed",
            "declined",
            "incorrect_account_holder_name",
            "invalid_account_number",
            "invalid_currency",
            "no_account",
            "other",
        ]
        """
        Reason for the return.
        """
        transaction: ExpandableField["Transaction"]
        """
        The Transaction associated with this object.
        """

    class StatusTransitions(StripeObject):
        canceled_at: Optional[int]
        """
        Timestamp describing when an OutboundPayment changed status to `canceled`.
        """
        failed_at: Optional[int]
        """
        Timestamp describing when an OutboundPayment changed status to `failed`.
        """
        posted_at: Optional[int]
        """
        Timestamp describing when an OutboundPayment changed status to `posted`.
        """
        returned_at: Optional[int]
        """
        Timestamp describing when an OutboundPayment changed status to `returned`.
        """

    class CancelParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        amount: int
        """
        Amount (in cents) to be transferred.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: NotRequired["str"]
        """
        ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        destination_payment_method: NotRequired["str"]
        """
        The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.
        """
        destination_payment_method_data: NotRequired[
            "OutboundPayment.CreateParamsDestinationPaymentMethodData"
        ]
        """
        Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
        """
        destination_payment_method_options: NotRequired[
            "OutboundPayment.CreateParamsDestinationPaymentMethodOptions"
        ]
        """
        Payment method-specific configuration for this OutboundPayment.
        """
        end_user_details: NotRequired[
            "OutboundPayment.CreateParamsEndUserDetails"
        ]
        """
        End user details.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        financial_account: str
        """
        The FinancialAccount to pull funds from.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        statement_descriptor: NotRequired["str"]
        """
        The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment".
        """

    class CreateParamsDestinationPaymentMethodData(TypedDict):
        billing_details: NotRequired[
            "OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetails"
        ]
        """
        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
        """
        financial_account: NotRequired["str"]
        """
        Required if type is set to `financial_account`. The FinancialAccount ID to send funds to.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        type: Literal["financial_account", "us_bank_account"]
        """
        The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
        """
        us_bank_account: NotRequired[
            "OutboundPayment.CreateParamsDestinationPaymentMethodDataUsBankAccount"
        ]
        """
        Required hash if type is set to `us_bank_account`.
        """

    class CreateParamsDestinationPaymentMethodDataBillingDetails(TypedDict):
        address: NotRequired[
            "Literal['']|OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetailsAddress"
        ]
        """
        Billing address.
        """
        email: NotRequired["Literal['']|str"]
        """
        Email address.
        """
        name: NotRequired["Literal['']|str"]
        """
        Full name.
        """
        phone: NotRequired["Literal['']|str"]
        """
        Billing phone number (including extension).
        """

    class CreateParamsDestinationPaymentMethodDataBillingDetailsAddress(
        TypedDict,
    ):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State, county, province, or region.
        """

    class CreateParamsDestinationPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired["Literal['company', 'individual']"]
        """
        Account holder type: individual or company.
        """
        account_number: NotRequired["str"]
        """
        Account number of the bank account.
        """
        account_type: NotRequired["Literal['checking', 'savings']"]
        """
        Account type: checkings or savings. Defaults to checking if omitted.
        """
        financial_connections_account: NotRequired["str"]
        """
        The ID of a Financial Connections Account to use as a payment method.
        """
        routing_number: NotRequired["str"]
        """
        Routing number of the bank account.
        """

    class CreateParamsDestinationPaymentMethodOptions(TypedDict):
        us_bank_account: NotRequired[
            "Literal['']|OutboundPayment.CreateParamsDestinationPaymentMethodOptionsUsBankAccount"
        ]
        """
        Optional fields for `us_bank_account`.
        """

    class CreateParamsDestinationPaymentMethodOptionsUsBankAccount(TypedDict):
        network: NotRequired["Literal['ach', 'us_domestic_wire']"]
        """
        The US bank account network that must be used for this OutboundPayment. If not set, we will default to the PaymentMethod's preferred network.
        """

    class CreateParamsEndUserDetails(TypedDict):
        ip_address: NotRequired["str"]
        """
        IP address of the user initiating the OutboundPayment. Must be supplied if `present` is set to `true`.
        """
        present: bool
        """
        `True` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.
        """

    class FailParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(RequestOptions):
        customer: NotRequired["str"]
        """
        Only return OutboundPayments sent to this customer.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        financial_account: str
        """
        Returns objects associated with this FinancialAccount.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            "Literal['canceled', 'failed', 'posted', 'processing', 'returned']"
        ]
        """
        Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`.
        """

    class PostParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReturnOutboundPaymentParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        returned_details: NotRequired[
            "OutboundPayment.ReturnOutboundPaymentParamsReturnedDetails"
        ]
        """
        Optional hash to set the the return code.
        """

    class ReturnOutboundPaymentParamsReturnedDetails(TypedDict):
        code: NotRequired[
            "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'declined', 'incorrect_account_holder_name', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']"
        ]
        """
        The return code to be set on the OutboundPayment object.
        """

    amount: int
    """
    Amount (in cents) transferred.
    """
    cancelable: bool
    """
    Returns `true` if the object can be canceled, and `false` otherwise.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[str]
    """
    ID of the [customer](https://stripe.com/docs/api/customers) to whom an OutboundPayment is sent.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    destination_payment_method: Optional[str]
    """
    The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.
    """
    destination_payment_method_details: Optional[
        DestinationPaymentMethodDetails
    ]
    """
    Details about the PaymentMethod for an OutboundPayment.
    """
    end_user_details: Optional[EndUserDetails]
    """
    Details about the end user.
    """
    expected_arrival_date: int
    """
    The date when funds are expected to arrive in the destination account.
    """
    financial_account: str
    """
    The FinancialAccount that funds were pulled from.
    """
    hosted_regulatory_receipt_url: Optional[str]
    """
    A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["treasury.outbound_payment"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    returned_details: Optional[ReturnedDetails]
    """
    Details about a returned OutboundPayment. Only set when the status is `returned`.
    """
    statement_descriptor: str
    """
    The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).
    """
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    """
    Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.
    """
    status_transitions: StatusTransitions
    transaction: ExpandableField["Transaction"]
    """
    The Transaction associated with this object.
    """

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "OutboundPayment":
        """
        Cancel an OutboundPayment.
        """
        return cast(
            "OutboundPayment",
            cls._static_request(
                "post",
                "/v1/treasury/outbound_payments/{id}/cancel".format(
                    id=_util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "OutboundPayment":
        """
        Cancel an OutboundPayment.
        """
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "OutboundPayment":
        """
        Cancel an OutboundPayment.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "OutboundPayment":
        """
        Cancel an OutboundPayment.
        """
        return cast(
            "OutboundPayment",
            self._request(
                "post",
                "/v1/treasury/outbound_payments/{id}/cancel".format(
                    id=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "OutboundPayment":
        """
        Creates an OutboundPayment.
        """
        return cast(
            "OutboundPayment",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "OutboundPayment.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["OutboundPayment"]:
        """
        Returns a list of OutboundPayments sent from the specified FinancialAccount.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
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
        cls, id: str, **params: Unpack["OutboundPayment.RetrieveParams"]
    ) -> "OutboundPayment":
        """
        Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["OutboundPayment"]):
        _resource_cls: Type["OutboundPayment"]

        @classmethod
        def _cls_fail(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                        id=_util.sanitize_id(id)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def fail(
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.
            """
            ...

        @overload
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_fail")
        def fail(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                        id=_util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_post(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.PostParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                        id=_util.sanitize_id(id)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def post(
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.PostParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.
            """
            ...

        @overload
        def post(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.PostParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_post")
        def post(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.PostParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                        id=_util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_return_outbound_payment(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.ReturnOutboundPaymentParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                        id=_util.sanitize_id(id)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def return_outbound_payment(
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.ReturnOutboundPaymentParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.
            """
            ...

        @overload
        def return_outbound_payment(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.ReturnOutboundPaymentParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_return_outbound_payment")
        def return_outbound_payment(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "OutboundPayment.ReturnOutboundPaymentParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "OutboundPayment":
            """
            Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.
            """
            return cast(
                "OutboundPayment",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                        id=_util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "destination_payment_method_details": DestinationPaymentMethodDetails,
        "end_user_details": EndUserDetails,
        "returned_details": ReturnedDetails,
        "status_transitions": StatusTransitions,
    }


OutboundPayment.TestHelpers._resource_cls = OutboundPayment
