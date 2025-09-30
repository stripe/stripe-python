# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressListParams(TypedDict):
    financial_account: NotRequired[str]
    """
    The ID of the FinancialAccount for which FinancialAddresses are to be returned.
    """
    include: NotRequired[
        List[
            Literal[
                "credentials.gb_bank_account.account_number",
                "credentials.sepa_bank_account.iban",
                "credentials.us_bank_account.account_number",
            ]
        ]
    ]
    """
    Open Enum. A list of fields to reveal in the FinancialAddresses returned.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
