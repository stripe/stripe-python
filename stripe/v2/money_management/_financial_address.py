# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class FinancialAddress(StripeObject):
    """
    A FinancialAddress contains information needed to transfer money to a Financial Account. A Financial Account can have more than one Financial Address.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_address"]] = (
        "v2.money_management.financial_address"
    )

    class Credentials(StripeObject):
        class GbBankAccount(StripeObject):
            account_holder_name: str
            """
            The account holder name to be used during bank transference.
            """
            account_number: Optional[str]
            """
            The account number of the UK Bank Account.
            """
            last4: str
            """
            The last four digits of the UK Bank Account number. This will always be returned.
            To view the full account number when retrieving or listing FinancialAddresses, use the `include` request parameter.
            """
            sort_code: str
            """
            The sort code of the UK Bank Account.
            """

        class SepaBankAccount(StripeObject):
            account_holder_name: str
            """
            The account holder name to be used during bank transfers.
            """
            bank_name: str
            """
            The name of the Bank.
            """
            bic: str
            """
            The BIC of the SEPA Bank Account.
            """
            country: str
            """
            The originating country of the SEPA Bank account.
            """
            iban: str
            """
            The IBAN of the SEPA Bank Account.
            """
            last4: str
            """
            The last four digits of the SEPA Bank Account number. This will always be returned.
            To view the full account number when retrieving or listing FinancialAddresses, use the `include` request parameter.
            """

        class UsBankAccount(StripeObject):
            account_number: Optional[str]
            """
            The account number of the US Bank Account.
            """
            bank_name: Optional[str]
            """
            The name of the Bank.
            """
            last4: str
            """
            The last four digits of the US Bank Account number. This will always be returned.
            To view the full account number when retrieving or listing FinancialAddresses, use the `include` request parameter.
            """
            routing_number: str
            """
            The routing number of the US Bank Account.
            """
            swift_code: Optional[str]
            """
            The swift code of the bank or financial institution.
            """

        gb_bank_account: Optional[GbBankAccount]
        """
        The credentials of the UK Bank Account for the FinancialAddress. This contains unique banking details such as the sort code, account number, etc. of a UK bank account.
        """
        sepa_bank_account: Optional[SepaBankAccount]
        """
        The credentials of the SEPA Bank Account for the FinancialAddress. This contains unique banking details such as the IBAN, BIC, etc. of a SEPA bank account.
        """
        type: Literal[
            "gb_bank_account", "sepa_bank_account", "us_bank_account"
        ]
        """
        Open Enum. The type of Credentials that are provisioned for the FinancialAddress.
        """
        us_bank_account: Optional[UsBankAccount]
        """
        The credentials of the US Bank Account for the FinancialAddress. This contains unique banking details such as the routing number, account number, etc. of a US bank account.
        """
        _inner_class_types = {
            "gb_bank_account": GbBankAccount,
            "sepa_bank_account": SepaBankAccount,
            "us_bank_account": UsBankAccount,
        }

    created: str
    """
    The creation timestamp of the FinancialAddress.
    """
    credentials: Optional[Credentials]
    """
    Object indicates the type of credentials that have been allocated and attached to the FinancialAddress.
    It contains all necessary banking details with which to perform money movements with the FinancialAddress.
    This field is only available for FinancialAddresses with an active status.
    """
    currency: str
    """
    Open Enum. The currency the FinancialAddress supports.
    """
    financial_account: str
    """
    A ID of the FinancialAccount this FinancialAddress corresponds to.
    """
    id: str
    """
    The ID of a FinancialAddress.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.financial_address"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    settlement_currency: Optional[str]
    """
    Open Enum. The currency the FinancialAddress settles into the FinancialAccount.
    """
    status: Literal["active", "archived", "failed", "pending"]
    """
    Closed Enum. An enum representing the status of the FinancialAddress. This indicates whether or not the FinancialAddress can be used for any money movement flows.
    """
    _inner_class_types = {"credentials": Credentials}
