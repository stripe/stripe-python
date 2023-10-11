# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal, Type

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class ReceivedDebit(ListableAPIResource["ReceivedDebit"]):
    """
    ReceivedDebits represent funds pulled from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts). These are not initiated from the FinancialAccount.
    """

    OBJECT_NAME = "treasury.received_debit"

    class InitiatingPaymentMethodDetails(StripeObject):
        class BillingDetails(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            address: Address
            email: Optional[str]
            name: Optional[str]
            _inner_class_types = {"address": Address}

        class FinancialAccount(StripeObject):
            id: str
            network: Literal["stripe"]

        class UsBankAccount(StripeObject):
            bank_name: Optional[str]
            last4: Optional[str]
            routing_number: Optional[str]

        balance: Optional[Literal["payments"]]
        billing_details: BillingDetails
        financial_account: Optional[FinancialAccount]
        issuing_card: Optional[str]
        type: Literal[
            "balance",
            "financial_account",
            "issuing_card",
            "stripe",
            "us_bank_account",
        ]
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "financial_account": FinancialAccount,
            "us_bank_account": UsBankAccount,
        }

    class LinkedFlows(StripeObject):
        debit_reversal: Optional[str]
        inbound_transfer: Optional[str]
        issuing_authorization: Optional[str]
        issuing_transaction: Optional[str]
        received_credit_capital_withholding: Optional[str]

    class NetworkDetails(StripeObject):
        class Ach(StripeObject):
            addenda: Optional[str]

        ach: Optional[Ach]
        type: Literal["ach"]
        _inner_class_types = {"ach": Ach}

    class ReversalDetails(StripeObject):
        deadline: Optional[int]
        restricted_reason: Optional[
            Literal[
                "already_reversed",
                "deadline_passed",
                "network_restricted",
                "other",
                "source_flow_restricted",
            ]
        ]

    amount: int
    created: int
    currency: str
    description: str
    failure_code: Optional[
        Literal[
            "account_closed", "account_frozen", "insufficient_funds", "other"
        ]
    ]
    financial_account: Optional[str]
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    initiating_payment_method_details: Optional[InitiatingPaymentMethodDetails]
    linked_flows: LinkedFlows
    livemode: bool
    network: Literal["ach", "card", "stripe"]
    network_details: Optional[NetworkDetails]
    object: Literal["treasury.received_debit"]
    reversal_details: Optional[ReversalDetails]
    status: Literal["failed", "succeeded"]
    transaction: Optional[ExpandableField["Transaction"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["ReceivedDebit"]:
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ReceivedDebit":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["ReceivedDebit"]):
        _resource_cls: Type["ReceivedDebit"]

        @classmethod
        def create(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/received_debits",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "initiating_payment_method_details": InitiatingPaymentMethodDetails,
        "linked_flows": LinkedFlows,
        "network_details": NetworkDetails,
        "reversal_details": ReversalDetails,
    }


ReceivedDebit.TestHelpers._resource_cls = ReceivedDebit
