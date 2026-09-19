# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class FinancialAddress(StripeObject):
    """
    A FinancialAddress contains information needed to transfer money to a Financial Account. A Financial Account can have more than one Financial Address.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_address"]] = (
        "v2.money_management.financial_address"
    )

    class BankAccount(StripeObject):
        class Aba(StripeObject):
            class AccountHolderAddress(StripeObject):
                city: str
                """
                City.
                """
                country: str
                """
                Country.
                """
                line1: str
                """
                Address line 1.
                """
                line2: str
                """
                Address line 2.
                """
                postal_code: str
                """
                Postal code.
                """
                state: str
                """
                State or province.
                """
                town: str
                """
                Town or suburb.
                """

            account_holder_address: Optional[AccountHolderAddress]
            """
            The address of the account holder.
            """
            account_holder_name: Optional[str]
            """
            The name of the account holder.
            """
            account_number: Optional[str]
            """
            The full account number.
            """
            bank_name: Optional[str]
            """
            The name of the bank.
            """
            last4: str
            """
            The last four digits of the account number.
            """
            routing_number: str
            """
            The ABA routing number.
            """
            _inner_class_types = {
                "account_holder_address": AccountHolderAddress,
            }

        class Clabe(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            clabe: str
            """
            The CLABE interbank code.
            """

        class Cpa(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            account_number: Optional[str]
            """
            The full account number.
            """
            bank_name: str
            """
            The name of the bank.
            """
            institution_number: str
            """
            The institution number.
            """
            last4: str
            """
            The last four digits of the account number.
            """
            transit_number: str
            """
            The transit number.
            """

        class Iban(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            bank_name: str
            """
            The name of the bank.
            """
            country: str
            """
            The country of the bank account.
            """
            iban: Optional[str]
            """
            The full IBAN.
            """
            last4: str
            """
            The last four digits of the IBAN.
            """

        class SortCode(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            account_number: Optional[str]
            """
            The full account number.
            """
            last4: str
            """
            The last four digits of the account number.
            """
            sort_code: str
            """
            The sort code.
            """

        aba: Optional[Aba]
        """
        ABA bank account details (US).
        """
        clabe: Optional[Clabe]
        """
        CLABE bank account details (Mexico).
        """
        country: Optional[str]
        """
        The country of the bank account.
        """
        cpa: Optional[Cpa]
        """
        CPA bank account details (Canada).
        """
        currency: str
        """
        Open Enum. The currency of the bank account.
        """
        iban: Optional[Iban]
        """
        IBAN bank account details.
        """
        sort_code: Optional[SortCode]
        """
        Sort code bank account details (UK).
        """
        type: Union[Literal["aba", "clabe", "cpa", "iban", "sort_code"], str]
        """
        Open Enum. The type of bank account details.
        """
        _inner_class_types = {
            "aba": Aba,
            "clabe": Clabe,
            "cpa": Cpa,
            "iban": Iban,
            "sort_code": SortCode,
        }

    class CryptoWallet(StripeObject):
        address: str
        """
        The blockchain wallet address.
        """
        memo: Optional[str]
        """
        An optional memo or tag required by some networks to identify the recipient.
        """
        network: Union[
            Literal[
                "arbitrum",
                "avalanche_c_chain",
                "base",
                "ethereum",
                "optimism",
                "polygon",
                "solana",
                "stellar",
                "tempo",
            ],
            str,
        ]
        """
        Open Enum. The blockchain network of the crypto wallet.
        """

    bank_account: Optional[BankAccount]
    """
    Bank account details for this FinancialAddress.
    """
    created: str
    """
    The creation timestamp of the FinancialAddress.
    """
    crypto_wallet: Optional[CryptoWallet]
    """
    Crypto wallet details for this FinancialAddress.
    """
    financial_account: str
    """
    The ID of the FinancialAccount this FinancialAddress corresponds to.
    """
    id: str
    """
    The ID of the FinancialAddress.
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
    Closed Enum. The status of the FinancialAddress.
    """
    type: Union[Literal["bank_account", "crypto_wallet"], str]
    """
    Open Enum. The type of FinancialAddress.
    """
    _inner_class_types = {
        "bank_account": BankAccount,
        "crypto_wallet": CryptoWallet,
    }
