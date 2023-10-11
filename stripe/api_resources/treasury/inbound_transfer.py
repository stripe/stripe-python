# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing_extensions import Literal, NotRequired, Type, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

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

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        amount: int
        currency: str
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        financial_account: str
        metadata: NotRequired[Optional[Dict[str, str]]]
        origin_payment_method: str
        statement_descriptor: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        financial_account: str
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[Literal["canceled", "failed", "processing", "succeeded"]]
        ]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class FailParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        failure_details: NotRequired[
            Optional["InboundTransfer.FailFailureDetailsParams"]
        ]

    class FailFailureDetailsParams(TypedDict):
        code: NotRequired[
            Optional[
                Literal[
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
            ]
        ]

    class ReturnInboundTransferParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SucceedParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
