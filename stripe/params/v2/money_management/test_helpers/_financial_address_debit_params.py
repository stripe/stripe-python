# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressDebitParams(TypedDict):
    amount: AmountParam
    """
    Object containing the amount value and currency to debit.
    """
    network: Union[Literal["ach", "bacs"], str]
    """
    The network to use in simulating the funds flow. This will be reflected in the resulting ReceivedDebit.
    """
    network_details: NotRequired["FinancialAddressDebitParamsNetworkDetails"]
    """
    Network-specific details for the simulated debit. Only used for ACH debits; supplied details must be valid.
    """
    statement_descriptor: NotRequired[str]
    """
    String explaining funds flow. Use this field to populate the statement descriptor of the ReceivedDebit created as an eventual result of this simulation.
    """


class FinancialAddressDebitParamsNetworkDetails(TypedDict):
    ach: NotRequired["FinancialAddressDebitParamsNetworkDetailsAch"]
    """
    ACH-specific details for the simulated debit.
    """


class FinancialAddressDebitParamsNetworkDetailsAch(TypedDict):
    originator_company_id: str
    """
    The ACH company ID of the originator of the simulated debit. Must contain exactly 10 alphanumeric characters. Sent to the network in uppercase.
    """
