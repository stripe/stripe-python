# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountUpdateParams(TypedDict):
    display_name: NotRequired[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    forwarding_settings: NotRequired[
        "FinancialAccountUpdateParamsForwardingSettings"
    ]
    """
    Forwarding settings for a closed FinancialAccount. Post-close forwarding updates are not yet implemented.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Metadata associated with the FinancialAccount.
    """
    storage: NotRequired["FinancialAccountUpdateParamsStorage"]
    """
    Parameters for updating storage-specific fields on the FinancialAccount.
    """


class FinancialAccountUpdateParamsForwardingSettings(TypedDict):
    payment_method: NotRequired[str]
    """
    The address to send forwarded payments to.
    """
    payout_method: NotRequired[str]
    """
    The address to send forwarded payouts to.
    """
    skip_exportable_balances: NotRequired[bool]
    """
    Whether to skip forwarding exportable self-custodied wallet balances. Defaults to false. This does not skip non-exportable or fiat balances, inbound-pending checks, or negative-balance requirements.
    """


class FinancialAccountUpdateParamsStorage(TypedDict):
    crypto: NotRequired["FinancialAccountUpdateParamsStorageCrypto"]
    """
    Crypto-specific storage configuration used when adding crypto to a fiat-only FinancialAccount.
    `custody_model` is required for the initial crypto update and cannot be changed afterward.
    """
    holds_currencies: NotRequired[List[str]]
    """
    The currencies that this storage FinancialAccount can hold a balance in. Three-letter ISO currency code, in lowercase.
    Adding currencies requires the corresponding holds_currencies storer capabilities to be enabled.
    Removing currencies is not supported as of March 2026.
    """


class FinancialAccountUpdateParamsStorageCrypto(TypedDict):
    currency_networks: "Dict[str, Union[Literal['tempo'], str]]|UntypedStripeObject[Union[Literal['tempo'], str]]"
    """
    The blockchain network configured for each crypto currency. Keys are lowercase currency codes and must identify crypto currencies also present in `holds_currencies`.
    """
    custody_model: Literal["self", "stripe"]
    """
    Describes who controls the private keys for the crypto storage.
    """
