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


class ReceivedCredit(ListableAPIResource["ReceivedCredit"]):
    """
    ReceivedCredits represent funds sent to a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.
    """

    OBJECT_NAME = "treasury.received_credit"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            limit: NotRequired["int|None"]
            linked_flows: NotRequired[
                "ReceivedCredit.ListParamsLinkedFlows|None"
            ]
            starting_after: NotRequired["str|None"]
            status: NotRequired["Literal['failed', 'succeeded']|None"]

        class ListParamsLinkedFlows(TypedDict):
            source_flow_type: Literal[
                "credit_reversal", "other", "outbound_payment", "payout"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            currency: str
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            initiating_payment_method_details: NotRequired[
                "ReceivedCredit.CreateParamsInitiatingPaymentMethodDetails|None"
            ]
            network: Literal["ach", "us_domestic_wire"]

        class CreateParamsInitiatingPaymentMethodDetails(TypedDict):
            type: Literal["us_bank_account"]
            us_bank_account: NotRequired[
                "ReceivedCredit.CreateParamsInitiatingPaymentMethodDetailsUsBankAccount|None"
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
        Literal["account_closed", "account_frozen", "other"]
    ]
    financial_account: Optional[str]
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    initiating_payment_method_details: StripeObject
    linked_flows: StripeObject
    livemode: bool
    network: Literal["ach", "card", "stripe", "us_domestic_wire"]
    object: Literal["treasury.received_credit"]
    reversal_details: Optional[StripeObject]
    status: Literal["failed", "succeeded"]
    transaction: Optional[ExpandableField["Transaction"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ReceivedCredit.ListParams"]
    ) -> ListObject["ReceivedCredit"]:
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
        cls, id: str, **params: Unpack["ReceivedCredit.RetrieveParams"]
    ) -> "ReceivedCredit":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["ReceivedCredit"]):
        _resource_cls: Type["ReceivedCredit"]

        @classmethod
        def create(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["ReceivedCredit.CreateParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/received_credits",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


ReceivedCredit.TestHelpers._resource_cls = ReceivedCredit
