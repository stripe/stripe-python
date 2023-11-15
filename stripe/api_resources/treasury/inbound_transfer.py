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


class InboundTransfer(
    CreateableAPIResource["InboundTransfer"],
    ListableAPIResource["InboundTransfer"],
):
    """
    Use [InboundTransfers](https://stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers) to add funds to your [FinancialAccount](https://stripe.com/docs/api#financial_accounts) via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.inbound_transfer"]
    ] = "treasury.inbound_transfer"

    class FailureDetails(StripeObject):
        code: Literal[
            "account_closed",
            "account_frozen",
            "bank_account_restricted",
            "bank_ownership_changed",
            "debit_not_authorized",
            "incorrect_account_holder_address",
            "incorrect_account_holder_name",
            "incorrect_account_holder_tax_id",
            "insufficient_funds",
            "invalid_account_number",
            "invalid_currency",
            "no_account",
            "other",
        ]
        """
        Reason for the failure.
        """

    class LinkedFlows(StripeObject):
        received_debit: Optional[str]
        """
        If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return.
        """

    class OriginPaymentMethodDetails(StripeObject):
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
            network: Literal["ach"]
            """
            The US bank account network used to debit funds.
            """
            routing_number: Optional[str]
            """
            Routing number of the bank account.
            """

        billing_details: BillingDetails
        type: Literal["us_bank_account"]
        """
        The type of the payment method used in the InboundTransfer.
        """
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "us_bank_account": UsBankAccount,
        }

    class StatusTransitions(StripeObject):
        canceled_at: Optional[int]
        """
        Timestamp describing when an InboundTransfer changed status to `canceled`.
        """
        failed_at: Optional[int]
        """
        Timestamp describing when an InboundTransfer changed status to `failed`.
        """
        succeeded_at: Optional[int]
        """
        Timestamp describing when an InboundTransfer changed status to `succeeded`.
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
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        financial_account: str
        """
        The FinancialAccount to send funds to.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        origin_payment_method: str
        """
        The origin payment method to be debited for the InboundTransfer.
        """
        statement_descriptor: NotRequired["str"]
        """
        The complete description that appears on your customers' statements. Maximum 10 characters.
        """

    class ListParams(RequestOptions):
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
            "Literal['canceled', 'failed', 'processing', 'succeeded']"
        ]
        """
        Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class FailParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        failure_details: NotRequired[
            "InboundTransfer.FailParamsFailureDetails"
        ]
        """
        Details about a failed InboundTransfer.
        """

    class FailParamsFailureDetails(TypedDict):
        code: NotRequired[
            "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'debit_not_authorized', 'incorrect_account_holder_address', 'incorrect_account_holder_name', 'incorrect_account_holder_tax_id', 'insufficient_funds', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']"
        ]
        """
        Reason for the failure.
        """

    class ReturnInboundTransferParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SucceedParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    amount: int
    """
    Amount (in cents) transferred.
    """
    cancelable: bool
    """
    Returns `true` if the InboundTransfer is able to be canceled.
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
    failure_details: Optional[FailureDetails]
    """
    Details about this InboundTransfer's failure. Only set when status is `failed`.
    """
    financial_account: str
    """
    The FinancialAccount that received the funds.
    """
    hosted_regulatory_receipt_url: Optional[str]
    """
    A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    id: str
    """
    Unique identifier for the object.
    """
    linked_flows: LinkedFlows
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["treasury.inbound_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    origin_payment_method: str
    """
    The origin payment method to be debited for an InboundTransfer.
    """
    origin_payment_method_details: Optional[OriginPaymentMethodDetails]
    """
    Details about the PaymentMethod for an InboundTransfer.
    """
    returned: Optional[bool]
    """
    Returns `true` if the funds for an InboundTransfer were returned after the InboundTransfer went to the `succeeded` state.
    """
    statement_descriptor: str
    """
    Statement descriptor shown when funds are debited from the source. Not all payment networks support `statement_descriptor`.
    """
    status: Literal["canceled", "failed", "processing", "succeeded"]
    """
    Status of the InboundTransfer: `processing`, `succeeded`, `failed`, and `canceled`. An InboundTransfer is `processing` if it is created and pending. The status changes to `succeeded` once the funds have been "confirmed" and a `transaction` is created and posted. The status changes to `failed` if the transfer fails.
    """
    status_transitions: StatusTransitions
    transaction: Optional[ExpandableField["Transaction"]]
    """
    The Transaction associated with this object.
    """

    @classmethod
    def _cls_cancel(
        cls,
        inbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "InboundTransfer.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "InboundTransfer":
        """
        Cancels an InboundTransfer.
        """
        return cast(
            "InboundTransfer",
            cls._static_request(
                "post",
                "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel".format(
                    inbound_transfer=util.sanitize_id(inbound_transfer)
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
        inbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "InboundTransfer.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "InboundTransfer":
        """
        Cancels an InboundTransfer.
        """
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "InboundTransfer.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "InboundTransfer":
        """
        Cancels an InboundTransfer.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "InboundTransfer.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "InboundTransfer":
        """
        Cancels an InboundTransfer.
        """
        return cast(
            "InboundTransfer",
            self._request(
                "post",
                "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel".format(
                    inbound_transfer=util.sanitize_id(self.get("id"))
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
            "InboundTransfer.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "InboundTransfer":
        """
        Creates an InboundTransfer.
        """
        return cast(
            "InboundTransfer",
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
            "InboundTransfer.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["InboundTransfer"]:
        """
        Returns a list of InboundTransfers sent from the specified FinancialAccount.
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
        cls, id: str, **params: Unpack["InboundTransfer.RetrieveParams"]
    ) -> "InboundTransfer":
        """
        Retrieves the details of an existing InboundTransfer.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["InboundTransfer"]):
        _resource_cls: Type["InboundTransfer"]

        @classmethod
        def _cls_fail(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.
            """
            return cast(
                "InboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
                        id=util.sanitize_id(id)
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
                "InboundTransfer.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.
            """
            ...

        @overload
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_fail")
        def fail(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.FailParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.
            """
            return cast(
                "InboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
                        id=util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_return_inbound_transfer(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.ReturnInboundTransferParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.
            """
            return cast(
                "InboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
                        id=util.sanitize_id(id)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def return_inbound_transfer(
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.ReturnInboundTransferParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.
            """
            ...

        @overload
        def return_inbound_transfer(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.ReturnInboundTransferParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.
            """
            ...

        @class_method_variant("_cls_return_inbound_transfer")
        def return_inbound_transfer(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.ReturnInboundTransferParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.
            """
            return cast(
                "InboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
                        id=util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

        @classmethod
        def _cls_succeed(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.SucceedParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the succeeded status. The InboundTransfer must already be in the processing state.
            """
            return cast(
                "InboundTransfer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
                        id=util.sanitize_id(id)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def succeed(
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.SucceedParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the succeeded status. The InboundTransfer must already be in the processing state.
            """
            ...

        @overload
        def succeed(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.SucceedParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the succeeded status. The InboundTransfer must already be in the processing state.
            """
            ...

        @class_method_variant("_cls_succeed")
        def succeed(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "InboundTransfer.SucceedParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "InboundTransfer":
            """
            Transitions a test mode created InboundTransfer to the succeeded status. The InboundTransfer must already be in the processing state.
            """
            return cast(
                "InboundTransfer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
                        id=util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "failure_details": FailureDetails,
        "linked_flows": LinkedFlows,
        "origin_payment_method_details": OriginPaymentMethodDetails,
        "status_transitions": StatusTransitions,
    }


InboundTransfer.TestHelpers._resource_cls = InboundTransfer
