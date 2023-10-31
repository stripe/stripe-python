# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
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
    from stripe.api_resources.treasury.transaction import Transaction


class OutboundTransfer(
    CreateableAPIResource["OutboundTransfer"],
    ListableAPIResource["OutboundTransfer"],
):
    """
    Use OutboundTransfers to transfer funds from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](https://stripe.com/docs/api#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user's own external bank account.

    Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.outbound_transfer"]
    ] = "treasury.outbound_transfer"

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
        type: Literal["us_bank_account"]
        """
        The type of the payment method used in the OutboundTransfer.
        """
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "us_bank_account": UsBankAccount,
        }

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
        Timestamp describing when an OutboundTransfer changed status to `canceled`
        """
        failed_at: Optional[int]
        """
        Timestamp describing when an OutboundTransfer changed status to `failed`
        """
        posted_at: Optional[int]
        """
        Timestamp describing when an OutboundTransfer changed status to `posted`
        """
        returned_at: Optional[int]
        """
        Timestamp describing when an OutboundTransfer changed status to `returned`
        """

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
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
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            destination_payment_method: NotRequired["str|None"]
            """
            The PaymentMethod to use as the payment instrument for the OutboundTransfer.
            """
            destination_payment_method_options: NotRequired[
                "OutboundTransfer.CreateParamsDestinationPaymentMethodOptions|None"
            ]
            """
            Hash describing payment method configuration details.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_account: str
            """
            The FinancialAccount to pull funds from.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `wire` transfers. The default value is `transfer`.
            """

        class CreateParamsDestinationPaymentMethodOptions(TypedDict):
            us_bank_account: NotRequired[
                "Literal['']|OutboundTransfer.CreateParamsDestinationPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            Optional fields for `us_bank_account`.
            """

        class CreateParamsDestinationPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            network: NotRequired["Literal['ach', 'us_domestic_wire']|None"]
            """
            Designate the OutboundTransfer as using a US bank account network configuration.
            """

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_account: str
            """
            Returns objects associated with this FinancialAccount.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['canceled', 'failed', 'posted', 'processing', 'returned']|None"
            ]
            """
            Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class FailParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class PostParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ReturnOutboundTransferParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            returned_details: NotRequired[
                "OutboundTransfer.ReturnOutboundTransferParamsReturnedDetails|None"
            ]
            """
            Details about a returned OutboundTransfer.
            """

        class ReturnOutboundTransferParamsReturnedDetails(TypedDict):
            code: NotRequired[
                "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'declined', 'incorrect_account_holder_name', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']|None"
            ]
            """
            Reason for the return.
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
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    destination_payment_method: Optional[str]
    """
    The PaymentMethod used as the payment instrument for an OutboundTransfer.
    """
    destination_payment_method_details: DestinationPaymentMethodDetails
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
    object: Literal["treasury.outbound_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    returned_details: Optional[ReturnedDetails]
    """
    Details about a returned OutboundTransfer. Only set when the status is `returned`.
    """
    statement_descriptor: str
    """
    Information about the OutboundTransfer to be sent to the recipient account.
    """
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    """
    Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`.
    """
    status_transitions: StatusTransitions
    transaction: ExpandableField["Transaction"]
    """
    The Transaction associated with this object.
    """

    @classmethod
    def _cls_cancel(
        cls,
        outbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["OutboundTransfer.CancelParams"]
    ) -> "OutboundTransfer":
        """
        An OutboundTransfer can be canceled if the funds have not yet been paid out.
        """
        return cast(
            "OutboundTransfer",
            cls._static_request(
                "post",
                "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
                    outbound_transfer=util.sanitize_id(outbound_transfer)
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
        outbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["OutboundTransfer.CancelParams"]
    ) -> "OutboundTransfer":
        """
        An OutboundTransfer can be canceled if the funds have not yet been paid out.
        """
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["OutboundTransfer.CancelParams"]
    ) -> "OutboundTransfer":
        """
        An OutboundTransfer can be canceled if the funds have not yet been paid out.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["OutboundTransfer.CancelParams"]
    ) -> "OutboundTransfer":
        """
        An OutboundTransfer can be canceled if the funds have not yet been paid out.
        """
        return cast(
            "OutboundTransfer",
            self._request(
                "post",
                "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
                    outbound_transfer=util.sanitize_id(self.get("id"))
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
        **params: Unpack["OutboundTransfer.CreateParams"]
    ) -> "OutboundTransfer":
        """
        Creates an OutboundTransfer.
        """
        return cast(
            "OutboundTransfer",
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
        **params: Unpack["OutboundTransfer.ListParams"]
    ) -> ListObject["OutboundTransfer"]:
        """
        Returns a list of OutboundTransfers sent from the specified FinancialAccount.
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
        cls, id: str, **params: Unpack["OutboundTransfer.RetrieveParams"]
    ) -> "OutboundTransfer":
        """
        Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["OutboundTransfer"]):
        _resource_cls: Type["OutboundTransfer"]

        @classmethod
        def _cls_fail(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.FailParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                        outbound_transfer=util.sanitize_id(outbound_transfer)
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
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.FailParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @overload
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.FailParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_fail")
        def fail(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.FailParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                        outbound_transfer=util.sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_post(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.PostParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                        outbound_transfer=util.sanitize_id(outbound_transfer)
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
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.PostParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @overload
        def post(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.PostParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_post")
        def post(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.PostParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                        outbound_transfer=util.sanitize_id(
                            self.resource.get("id")
                        )
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_return_outbound_transfer(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.ReturnOutboundTransferParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                        outbound_transfer=util.sanitize_id(outbound_transfer)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def return_outbound_transfer(
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundTransfer.ReturnOutboundTransferParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @overload
        def return_outbound_transfer(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.ReturnOutboundTransferParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_return_outbound_transfer")
        def return_outbound_transfer(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundTransfer.ReturnOutboundTransferParams"]
        ) -> "OutboundTransfer":
            """
            Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.
            """
            return cast(
                "OutboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                        outbound_transfer=util.sanitize_id(
                            self.resource.get("id")
                        )
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
        "returned_details": ReturnedDetails,
        "status_transitions": StatusTransitions,
    }


OutboundTransfer.TestHelpers._resource_cls = OutboundTransfer
