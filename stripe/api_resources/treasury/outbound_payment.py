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
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, Type, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class OutboundPayment(
    CreateableAPIResource["OutboundPayment"],
    ListableAPIResource["OutboundPayment"],
):
    """
    Use OutboundPayments to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).

    Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.
    """

    OBJECT_NAME = "treasury.outbound_payment"

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        amount: int
        currency: str
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        destination_payment_method: NotRequired[Optional[str]]
        destination_payment_method_data: NotRequired[
            Optional[
                "OutboundPayment.CreateParamsDestinationPaymentMethodData"
            ]
        ]
        destination_payment_method_options: NotRequired[
            Optional[
                "OutboundPayment.CreateParamsDestinationPaymentMethodOptions"
            ]
        ]
        end_user_details: NotRequired[
            Optional["OutboundPayment.CreateParamsEndUserDetails"]
        ]
        expand: NotRequired[Optional[List[str]]]
        financial_account: str
        metadata: NotRequired[Optional[Dict[str, str]]]
        statement_descriptor: NotRequired[Optional[str]]

    class CreateParamsEndUserDetails(TypedDict):
        ip_address: NotRequired[Optional[str]]
        present: bool

    class CreateParamsDestinationPaymentMethodOptions(TypedDict):
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "OutboundPayment.CreateParamsDestinationPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]

    class CreateParamsDestinationPaymentMethodOptionsUsBankAccount(TypedDict):
        network: NotRequired[Optional[Literal["ach", "us_domestic_wire"]]]

    class CreateParamsDestinationPaymentMethodData(TypedDict):
        billing_details: NotRequired[
            Optional[
                "OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetails"
            ]
        ]
        financial_account: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        type: Literal["financial_account", "us_bank_account"]
        us_bank_account: NotRequired[
            Optional[
                "OutboundPayment.CreateParamsDestinationPaymentMethodDataUsBankAccount"
            ]
        ]

    class CreateParamsDestinationPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreateParamsDestinationPaymentMethodDataBillingDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsDestinationPaymentMethodDataBillingDetailsAddress(
        TypedDict,
    ):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        financial_account: str
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[
                Literal[
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ]
        ]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class FailParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class PostParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ReturnOutboundPaymentParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        returned_details: NotRequired[
            Optional[
                "OutboundPayment.ReturnOutboundPaymentParamsReturnedDetails"
            ]
        ]

    class ReturnOutboundPaymentParamsReturnedDetails(TypedDict):
        code: NotRequired[
            Optional[
                Literal[
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
            ]
        ]

    amount: int
    cancelable: bool
    created: int
    currency: str
    customer: Optional[str]
    description: Optional[str]
    destination_payment_method: Optional[str]
    destination_payment_method_details: Optional[StripeObject]
    end_user_details: Optional[StripeObject]
    expected_arrival_date: int
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["treasury.outbound_payment"]
    returned_details: Optional[StripeObject]
    statement_descriptor: str
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    status_transitions: StripeObject
    transaction: ExpandableField["Transaction"]

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["OutboundPayment.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/outbound_payments/{id}/cancel".format(
                id=util.sanitize_id(id)
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
        **params: Unpack["OutboundPayment.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/treasury/outbound_payments/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
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
        **params: Unpack["OutboundPayment.CreateParams"]
    ) -> "OutboundPayment":
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
        **params: Unpack["OutboundPayment.ListParams"]
    ) -> ListObject["OutboundPayment"]:
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
            **params: Unpack["OutboundPayment.FailParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
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
            **params: Unpack["OutboundPayment.FailParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_post(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundPayment.PostParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_post")
        def post(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundPayment.PostParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_return_outbound_payment(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundPayment.ReturnOutboundPaymentParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_return_outbound_payment")
        def return_outbound_payment(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundPayment.ReturnOutboundPaymentParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


OutboundPayment.TestHelpers._resource_cls = OutboundPayment
