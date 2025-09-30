# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressRetrieveParams(TypedDict):
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
