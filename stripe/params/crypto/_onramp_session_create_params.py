# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class OnrampSessionCreateParams(RequestOptions):
    customer_ip_address: NotRequired[str]
    """
    The IP address of the customer the platform intends to onramp.

    If the user's IP is in a region we can't support, we return an `HTTP 400` with an appropriate error code.

    We support IPv4 and IPv6 addresses. Geographic supportability is checked again later in the onramp flow, which provides a way to hide the onramp option from ineligible users for a better user experience.
    """
    destination_amount: NotRequired[str]
    """
    The default amount of crypto to exchange into.

    * When left null, a default value is computed if `source_amount`, `destination_currency`, and `destination_network` are set.
    * When set, both `destination_currency` and `destination_network` must also be set. All cryptocurrencies are supported to their full precisions (for example, 18 decimal places for `eth`). We validate and generate an error if the amount exceeds the supported precision based on the exchange currency. Setting `source_amount` is mutually exclusive with setting `destination_amount` (only one or the other is supported). Users can update the amount in the onramp UI.
    """
    destination_currencies: NotRequired[
        List[
            Literal["avax", "btc", "eth", "matic", "sol", "usdc", "wld", "xlm"]
        ]
    ]
    """
    The list of destination cryptocurrencies a user can choose from.

    * When left null, all supported cryptocurrencies are shown in the onramp UI subject to `destination_networks` if set.
    * When set, it must be a non-empty array where all values in the array are valid cryptocurrencies. You can use it to lock users to a specific cryptocurrency by passing a single value array. Users **cannot** override this parameter.
    """
    destination_currency: NotRequired[
        Literal["avax", "btc", "eth", "matic", "sol", "usdc", "wld", "xlm"]
    ]
    """
    The default destination cryptocurrency.

    * When left null, the first value of `destination_currencies` is selected.
    * When set, if `destination_currencies` is also set, the value of `destination_currency` must be present in that array. To lock a `destination_currency`, specify that value as the single value for `destination_currencies`. Users can select a different cryptocurrency in the onramp UI subject to `destination_currencies` if set.
    """
    destination_network: NotRequired[
        Literal[
            "avalanche",
            "base",
            "bitcoin",
            "ethereum",
            "optimism",
            "polygon",
            "solana",
            "stellar",
            "worldchain",
        ]
    ]
    """
    The default destination crypto network.

    * When left null, the first value of `destination_networks` is selected.
    * When set, if `destination_networks` is also set, the value of `destination_network` must be present in that array. To lock a `destination_network`, specify that value as the single value for `destination_networks`. Users can select a different network in the onramp UI subject to `destination_networks` if set.
    """
    destination_networks: NotRequired[
        List[
            Literal[
                "avalanche",
                "base",
                "bitcoin",
                "ethereum",
                "optimism",
                "polygon",
                "solana",
                "stellar",
                "worldchain",
            ]
        ]
    ]
    """
    The list of destination crypto networks user can choose from.

    * When left null, all supported crypto networks are shown in the onramp UI.
    * When set, it must be a non-empty array where values in the array are each a valid crypto network. It can be used to lock users to a specific network by passing a single value array. Users **cannot** override this parameter.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    kyc_details: NotRequired["OnrampSessionCreateParamsKycDetails"]
    """
    Pre-populate some of the required KYC information for the user if you've already collected it within your application.

    Related guide: [Using the API](https://docs.stripe.com/crypto/using-the-api#how-to-pre-populate-customer-information)
    """
    lock_wallet_address: NotRequired[bool]
    """
    Whether or not to lock the suggested wallet address. If destination tags are provided, this will also lock the destination tags.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    settlement_speed: NotRequired[Literal["instant", "standard"]]
    """
    Speed at which the cryptocurrency is delivered to the wallet
    One of:
     `instant` (default): crypto is delivered when payment is confirmed
     `standard`: crypto is delivered when payment settles
    """
    source_amount: NotRequired[str]
    """
    The default amount of fiat (in decimal) to exchange into crypto.

    * When left null, a default value is computed if `destination_amount` is set.
    * When set, setting `source_amount` is mutually exclusive with setting `destination_amount` (only one or the other is supported). We don't support fractional pennies. If fractional minor units of a currency are passed in, it generates an error. Users can update the value in the onramp UI.
    """
    source_currency: NotRequired[Literal["eur", "gbp", "usd"]]
    """
    The default source fiat currency for the onramp session.

    * When left null, a default currency is selected based on user locale.
    * When set, it must be one of the fiat currencies supported by onramp. Users can still select a different currency in the onramp UI.
    """
    wallet_addresses: NotRequired["OnrampSessionCreateParamsWalletAddresses"]
    """
    The end customer's crypto wallet address (for each network) to use for this transaction.

    * When left null, the user enters their wallet in the onramp UI.
    * When set, the platform must set either `destination_networks` or `destination_network` and we perform address validation. Users can still select a different wallet in the onramp UI.
    """


class OnrampSessionCreateParamsKycDetails(TypedDict):
    pass


class OnrampSessionCreateParamsWalletAddresses(TypedDict):
    destination_tags: NotRequired[
        "OnrampSessionCreateParamsWalletAddressesDestinationTags"
    ]
    """
    The end customer's crypto wallet destination tag (for each network) to use for this transaction. This only applies for tag-based assets such as XLM.

    * When left null, the user enters their wallet in the onramp UI.
    """


class OnrampSessionCreateParamsWalletAddressesDestinationTags(TypedDict):
    stellar: NotRequired[str]
