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
from typing import Dict, List, Optional, cast
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

    OBJECT_NAME = "treasury.inbound_transfer"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            currency: str
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            metadata: NotRequired["Dict[str, str]|None"]
            origin_payment_method: str
            statement_descriptor: NotRequired["str|None"]

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['canceled', 'failed', 'processing', 'succeeded']|None"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class FailParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            failure_details: NotRequired[
                "InboundTransfer.FailParamsFailureDetails|None"
            ]

        class FailParamsFailureDetails(TypedDict):
            code: NotRequired[
                "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'debit_not_authorized', 'incorrect_account_holder_address', 'incorrect_account_holder_name', 'incorrect_account_holder_tax_id', 'insufficient_funds', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']|None"
            ]

        class ReturnInboundTransferParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SucceedParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount: int
    cancelable: bool
    created: int
    currency: str
    description: Optional[str]
    failure_details: Optional[StripeObject]
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    linked_flows: StripeObject
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["treasury.inbound_transfer"]
    origin_payment_method: str
    origin_payment_method_details: Optional[StripeObject]
    returned: Optional[bool]
    statement_descriptor: str
    status: Literal["canceled", "failed", "processing", "succeeded"]
    status_transitions: StripeObject
    transaction: Optional[ExpandableField["Transaction"]]

    @classmethod
    def _cls_cancel(
        cls,
        inbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["InboundTransfer.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel".format(
                inbound_transfer=util.sanitize_id(inbound_transfer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["InboundTransfer.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel".format(
                inbound_transfer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
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
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_fail")
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.FailParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/fail".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_return_inbound_transfer(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_return_inbound_transfer")
        def return_inbound_transfer(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.ReturnInboundTransferParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/return".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_succeed(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["InboundTransfer.SucceedParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_succeed")
        def succeed(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["InboundTransfer.SucceedParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


InboundTransfer.TestHelpers._resource_cls = InboundTransfer
