# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal


class FundingInstructions(StripeObject):
    """
    Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) that is
    automatically applied to future invoices and payments using the `customer_balance` payment method.
    Customers can fund this balance by initiating a bank transfer to any account in the
    `financial_addresses` field.
    Related guide: [Customer balance funding instructions](https://stripe.com/docs/payments/customer-balance/funding-instructions)
    """

    OBJECT_NAME = "funding_instructions"

    class BankTransfer(StripeObject):
        class FinancialAddress(StripeObject):
            class Iban(StripeObject):
                account_holder_name: str
                bic: str
                country: str
                iban: str

            class SortCode(StripeObject):
                account_holder_name: str
                account_number: str
                sort_code: str

            class Spei(StripeObject):
                bank_code: str
                bank_name: str
                clabe: str

            class Zengin(StripeObject):
                account_holder_name: Optional[str]
                account_number: Optional[str]
                account_type: Optional[str]
                bank_code: Optional[str]
                bank_name: Optional[str]
                branch_code: Optional[str]
                branch_name: Optional[str]

            iban: Optional[Iban]
            sort_code: Optional[SortCode]
            spei: Optional[Spei]
            supported_networks: Optional[
                List[Literal["bacs", "fps", "sepa", "spei", "zengin"]]
            ]
            type: Literal["iban", "sort_code", "spei", "zengin"]
            zengin: Optional[Zengin]
            _inner_class_types = {
                "iban": Iban,
                "sort_code": SortCode,
                "spei": Spei,
                "zengin": Zengin,
            }

        country: str
        financial_addresses: List[FinancialAddress]
        type: Literal["eu_bank_transfer", "jp_bank_transfer"]
        _inner_class_types = {"financial_addresses": FinancialAddress}

    bank_transfer: BankTransfer
    currency: str
    funding_type: Literal["bank_transfer"]
    livemode: bool
    object: Literal["funding_instructions"]

    _inner_class_types = {"bank_transfer": BankTransfer}
