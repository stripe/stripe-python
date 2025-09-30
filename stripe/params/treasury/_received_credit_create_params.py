# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ReceivedCreditCreateParams(RequestOptions):
    amount: int
    """
    Amount (in cents) to be transferred.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    financial_account: str
    """
    The FinancialAccount to send funds to.
    """
    initiating_payment_method_details: NotRequired[
        "ReceivedCreditCreateParamsInitiatingPaymentMethodDetails"
    ]
    """
    Initiating payment method details for the object.
    """
    network: Literal["ach", "us_domestic_wire"]
    """
    Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type.
    """
    network_details: NotRequired["ReceivedCreditCreateParamsNetworkDetails"]
    """
    Details about the network used for the ReceivedCredit.
    """


class ReceivedCreditCreateParamsInitiatingPaymentMethodDetails(TypedDict):
    type: Literal["us_bank_account"]
    """
    The source type.
    """
    us_bank_account: NotRequired[
        "ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount"
    ]
    """
    Optional fields for `us_bank_account`.
    """


class ReceivedCreditCreateParamsInitiatingPaymentMethodDetailsUsBankAccount(
    TypedDict,
):
    account_holder_name: NotRequired[str]
    """
    The bank account holder's name.
    """
    account_number: NotRequired[str]
    """
    The bank account number.
    """
    routing_number: NotRequired[str]
    """
    The bank account's routing number.
    """


class ReceivedCreditCreateParamsNetworkDetails(TypedDict):
    ach: NotRequired["ReceivedCreditCreateParamsNetworkDetailsAch"]
    """
    Optional fields for `ach`.
    """
    type: Literal["ach"]
    """
    The type of flow that originated the ReceivedCredit.
    """


class ReceivedCreditCreateParamsNetworkDetailsAch(TypedDict):
    addenda: NotRequired[str]
    """
    ACH Addenda record
    """
