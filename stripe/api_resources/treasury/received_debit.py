# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
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


class ReceivedDebit(ListableAPIResource["ReceivedDebit"]):
    """
    ReceivedDebits represent funds pulled from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts). These are not initiated from the FinancialAccount.
    """

    OBJECT_NAME = "treasury.received_debit"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired["Literal['failed', 'succeeded']|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            currency: str
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            initiating_payment_method_details: NotRequired[
                "ReceivedDebit.CreateParamsInitiatingPaymentMethodDetails|None"
            ]
            network: Literal["ach"]

        class CreateParamsInitiatingPaymentMethodDetails(TypedDict):
            type: Literal["us_bank_account"]
            us_bank_account: NotRequired[
                "ReceivedDebit.CreateParamsInitiatingPaymentMethodDetailsUsBankAccount|None"
            ]

        class CreateParamsInitiatingPaymentMethodDetailsUsBankAccount(
            TypedDict,
        ):
            account_holder_name: NotRequired["str|None"]
            account_number: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

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
    initiating_payment_method_details: Optional[StripeObject]
    linked_flows: StripeObject
    livemode: bool
    network: Literal["ach", "card", "stripe"]
    object: Literal["treasury.received_debit"]
    reversal_details: Optional[StripeObject]
    status: Literal["failed", "succeeded"]
    transaction: Optional[ExpandableField["Transaction"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ReceivedDebit.ListParams"]
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
        cls, id: str, **params: Unpack["ReceivedDebit.RetrieveParams"]
    ) -> "ReceivedDebit":
        instance = cls(id, **params)
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
            **params: Unpack["ReceivedDebit.CreateParams"]
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


ReceivedDebit.TestHelpers._resource_cls = ReceivedDebit
