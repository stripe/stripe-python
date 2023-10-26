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
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_account: str
            """
            The FinancialAccount to send funds to.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            origin_payment_method: str
            """
            The origin payment method to be debited for the InboundTransfer.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            The complete description that appears on your customers' statements. Maximum 10 characters.
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
                "Literal['canceled', 'failed', 'processing', 'succeeded']|None"
            ]
            """
            Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.
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
            failure_details: NotRequired[
                "InboundTransfer.FailParamsFailureDetails|None"
            ]
            """
            Details about a failed InboundTransfer.
            """

        class FailParamsFailureDetails(TypedDict):
            code: NotRequired[
                "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'debit_not_authorized', 'incorrect_account_holder_address', 'incorrect_account_holder_name', 'incorrect_account_holder_tax_id', 'insufficient_funds', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']|None"
            ]
            """
            Reason for the failure.
            """

        class ReturnInboundTransferParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class SucceedParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
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
    failure_details: Optional[StripeObject]
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
    linked_flows: StripeObject
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
    origin_payment_method_details: Optional[StripeObject]
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
    status_transitions: StripeObject
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
        **params: Unpack["InboundTransfer.CancelParams"]
    ) -> "InboundTransfer":
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
    @classmethod
    def cancel(
        cls,
        inbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["InboundTransfer.CancelParams"]
    ) -> "InboundTransfer":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["InboundTransfer.CancelParams"]
    ) -> "InboundTransfer":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["InboundTransfer.CancelParams"]
    ) -> "InboundTransfer":
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
        **params: Unpack["InboundTransfer.CreateParams"]
    ) -> "InboundTransfer":
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
        **params: Unpack["InboundTransfer.ListParams"]
    ) -> ListObject["InboundTransfer"]:
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
            **params: Unpack["InboundTransfer.FailParams"]
        ) -> "InboundTransfer":
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
        @classmethod
        def fail(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["InboundTransfer.FailParams"]
        ) -> "InboundTransfer":
            ...

        @overload
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.FailParams"]
        ) -> "InboundTransfer":
            ...

        @class_method_variant("_cls_fail")
        def fail(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.FailParams"]
        ) -> "InboundTransfer":
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
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ) -> "InboundTransfer":
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
        @classmethod
        def return_inbound_transfer(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ) -> "InboundTransfer":
            ...

        @overload
        def return_inbound_transfer(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ) -> "InboundTransfer":
            ...

        @class_method_variant("_cls_return_inbound_transfer")
        def return_inbound_transfer(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ) -> "InboundTransfer":
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
            **params: Unpack["InboundTransfer.SucceedParams"]
        ) -> "InboundTransfer":
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
        @classmethod
        def succeed(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["InboundTransfer.SucceedParams"]
        ) -> "InboundTransfer":
            ...

        @overload
        def succeed(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.SucceedParams"]
        ) -> "InboundTransfer":
            ...

        @class_method_variant("_cls_succeed")
        def succeed(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.SucceedParams"]
        ) -> "InboundTransfer":
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


InboundTransfer.TestHelpers._resource_cls = InboundTransfer
