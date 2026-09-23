# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountCreateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Metadata associated with the FinancialAccount.
    """
    savings: NotRequired["FinancialAccountCreateParamsSavings"]
    """
    Parameters specific to creating `savings` type FinancialAccounts.
    """
    storage: NotRequired["FinancialAccountCreateParamsStorage"]
    """
    Parameters specific to creating `storage` type FinancialAccounts.
    """
    type: Literal["credit", "savings", "storage"]
    """
    The type of FinancialAccount to create.
    """


class FinancialAccountCreateParamsSavings(TypedDict):
    holds_currencies: List[str]
    """
    The currencies that this savings FinancialAccount can hold. Three-letter ISO currency code, in lowercase.
    """


class FinancialAccountCreateParamsStorage(TypedDict):
    crypto: NotRequired["FinancialAccountCreateParamsStorageCrypto"]
    """
    Crypto-specific storage configuration. Only populated when `storage.crypto` is passed in the `include` parameter and the FinancialAccount stores crypto assets. Fiat currencies remain configured only through `holds_currencies`.
    """
    funds_usage_type: NotRequired["Literal['business', 'consumer']|str"]
    """
    The usage type for funds in this FinancialAccount. Can be used to specify that the funds are for Consumer activity.
    """
    holds_currencies: List[str]
    """
    The currencies that this FinancialAccount can hold.
    """


class FinancialAccountCreateParamsStorageCrypto(TypedDict):
    currency_networks: "Dict[str, Union[Literal['tempo'], str]]|UntypedStripeObject[Union[Literal['tempo'], str]]"
    """
    The blockchain network configured for each crypto currency. Keys are lowercase currency codes and must identify crypto currencies also present in `holds_currencies`.
    """
    custody_model: Literal["self", "stripe"]
    """
    Describes who controls the private keys for the crypto storage.
    """
