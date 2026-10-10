# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
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
            bic: Optional[str]
            """
            The SWIFT/BIC code.
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

        class BreB(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            bre_b_key: str
            """
            The BRE-B payment key.
            """

        class Clabe(StripeObject):
            account_holder_name: str
            clabe: str

        class Cpa(StripeObject):
            account_holder_name: str
            account_number: Optional[str]
            bank_name: str
            bic: Optional[str]
            institution_number: str
            last4: str
            transit_number: str

        class Iban(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            bank_name: str
            """
            The name of the bank.
            """
            bic: str
            """
            The SWIFT/BIC code.
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

        class Nip(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            bank_code: str
            """
            The NIP bank code.
            """
            bank_name: str
            """
            The name of the bank.
            """
            nuban: str
            """
            The NUBAN account number.
            """

        class Pix(StripeObject):
            account_holder_name: str
            """
            The name of the account holder.
            """
            br_code: str
            """
            The Pix BR code.
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
            bic: Optional[str]
            """
            The SWIFT/BIC code.
            """
            iban: Optional[str]
            """
            The full IBAN.
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
        bre_b: Optional[BreB]
        """
        BRE-B bank account details (Colombia).
        """
        clabe: Optional[Clabe]
        country: Optional[str]
        """
        The country of the bank account.
        """
        cpa: Optional[Cpa]
        currency: str
        """
        Open Enum. The currency of the bank account.
        """
        iban: Optional[Iban]
        """
        IBAN bank account details.
        """
        nip: Optional[Nip]
        """
        NIP bank account details (Nigeria).
        """
        pix: Optional[Pix]
        """
        Pix bank account details (Brazil).
        """
        sort_code: Optional[SortCode]
        """
        Sort code bank account details (UK).
        """
        type: Union[
            Literal[
                "aba",
                "bre_b",
                "clabe",
                "cpa",
                "iban",
                "nip",
                "pix",
                "sort_code",
            ],
            str,
        ]
        """
        Open Enum. The type of bank account details.
        """
        _inner_class_types = {
            "aba": Aba,
            "bre_b": BreB,
            "clabe": Clabe,
            "cpa": Cpa,
            "iban": Iban,
            "nip": Nip,
            "pix": Pix,
            "sort_code": SortCode,
        }

    class CryptoWallet(StripeObject):
        class SupportedNetworkDetails(StripeObject):
            supported_token_currencies: List[
                Union[Literal["btc", "eth", "sol", "usdc", "usdt"], str]
            ]
            """
            The token currencies supported on this network.
            """

        address: str
        memo: Optional[str]
        network: Union[
            Literal[
                "arbitrum",
                "avalanche_c_chain",
                "base",
                "bitcoin",
                "ethereum",
                "optimism",
                "polygon",
                "solana",
                "stellar",
                "tempo",
            ],
            str,
        ]
        supported_network_details: UntypedStripeObject[SupportedNetworkDetails]
        """
        A map of supported network names to their details, including supported token currencies.
        """
        _inner_class_types = {
            "supported_network_details": SupportedNetworkDetails,
        }
        _inner_class_dicts = ["supported_network_details"]

    account: Optional[str]
    """
    The ID of the Account that owns this FinancialAddress.
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
