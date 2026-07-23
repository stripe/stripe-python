# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.crypto._customer_consumer_wallet_list_params import (
        CustomerConsumerWalletListParams as CustomerConsumerWalletListParams,
    )
    from stripe.params.crypto._customer_list_crypto_consumer_wallets_params import (
        CustomerListCryptoConsumerWalletsParams as CustomerListCryptoConsumerWalletsParams,
    )
    from stripe.params.crypto._customer_list_payment_tokens_params import (
        CustomerListPaymentTokensParams as CustomerListPaymentTokensParams,
    )
    from stripe.params.crypto._customer_payment_token_list_params import (
        CustomerPaymentTokenListParams as CustomerPaymentTokenListParams,
    )
    from stripe.params.crypto._customer_retrieve_params import (
        CustomerRetrieveParams as CustomerRetrieveParams,
    )
    from stripe.params.crypto._deposit_address_create_params import (
        DepositAddressCreateParams as DepositAddressCreateParams,
    )
    from stripe.params.crypto._deposit_address_list_params import (
        DepositAddressListParams as DepositAddressListParams,
    )
    from stripe.params.crypto._deposit_address_retrieve_params import (
        DepositAddressRetrieveParams as DepositAddressRetrieveParams,
    )
    from stripe.params.crypto._onramp_session_checkout_params import (
        OnrampSessionCheckoutParams as OnrampSessionCheckoutParams,
        OnrampSessionCheckoutParamsMandateData as OnrampSessionCheckoutParamsMandateData,
        OnrampSessionCheckoutParamsMandateDataCustomerAcceptance as OnrampSessionCheckoutParamsMandateDataCustomerAcceptance,
        OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOffline as OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOffline,
        OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOnline as OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOnline,
    )
    from stripe.params.crypto._onramp_session_create_params import (
        OnrampSessionCreateParams as OnrampSessionCreateParams,
        OnrampSessionCreateParamsKycDetails as OnrampSessionCreateParamsKycDetails,
        OnrampSessionCreateParamsWalletAddresses as OnrampSessionCreateParamsWalletAddresses,
        OnrampSessionCreateParamsWalletAddressesDestinationTags as OnrampSessionCreateParamsWalletAddressesDestinationTags,
    )
    from stripe.params.crypto._onramp_session_list_params import (
        OnrampSessionListParams as OnrampSessionListParams,
        OnrampSessionListParamsCreated as OnrampSessionListParamsCreated,
    )
    from stripe.params.crypto._onramp_session_quote_params import (
        OnrampSessionQuoteParams as OnrampSessionQuoteParams,
    )
    from stripe.params.crypto._onramp_session_retrieve_params import (
        OnrampSessionRetrieveParams as OnrampSessionRetrieveParams,
    )
    from stripe.params.crypto._onramp_transaction_limits_retrieve_params import (
        OnrampTransactionLimitsRetrieveParams as OnrampTransactionLimitsRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "CustomerConsumerWalletListParams": (
        "stripe.params.crypto._customer_consumer_wallet_list_params",
        False,
    ),
    "CustomerListCryptoConsumerWalletsParams": (
        "stripe.params.crypto._customer_list_crypto_consumer_wallets_params",
        False,
    ),
    "CustomerListPaymentTokensParams": (
        "stripe.params.crypto._customer_list_payment_tokens_params",
        False,
    ),
    "CustomerPaymentTokenListParams": (
        "stripe.params.crypto._customer_payment_token_list_params",
        False,
    ),
    "CustomerRetrieveParams": (
        "stripe.params.crypto._customer_retrieve_params",
        False,
    ),
    "DepositAddressCreateParams": (
        "stripe.params.crypto._deposit_address_create_params",
        False,
    ),
    "DepositAddressListParams": (
        "stripe.params.crypto._deposit_address_list_params",
        False,
    ),
    "DepositAddressRetrieveParams": (
        "stripe.params.crypto._deposit_address_retrieve_params",
        False,
    ),
    "OnrampSessionCheckoutParams": (
        "stripe.params.crypto._onramp_session_checkout_params",
        False,
    ),
    "OnrampSessionCheckoutParamsMandateData": (
        "stripe.params.crypto._onramp_session_checkout_params",
        False,
    ),
    "OnrampSessionCheckoutParamsMandateDataCustomerAcceptance": (
        "stripe.params.crypto._onramp_session_checkout_params",
        False,
    ),
    "OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOffline": (
        "stripe.params.crypto._onramp_session_checkout_params",
        False,
    ),
    "OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOnline": (
        "stripe.params.crypto._onramp_session_checkout_params",
        False,
    ),
    "OnrampSessionCreateParams": (
        "stripe.params.crypto._onramp_session_create_params",
        False,
    ),
    "OnrampSessionCreateParamsKycDetails": (
        "stripe.params.crypto._onramp_session_create_params",
        False,
    ),
    "OnrampSessionCreateParamsWalletAddresses": (
        "stripe.params.crypto._onramp_session_create_params",
        False,
    ),
    "OnrampSessionCreateParamsWalletAddressesDestinationTags": (
        "stripe.params.crypto._onramp_session_create_params",
        False,
    ),
    "OnrampSessionListParams": (
        "stripe.params.crypto._onramp_session_list_params",
        False,
    ),
    "OnrampSessionListParamsCreated": (
        "stripe.params.crypto._onramp_session_list_params",
        False,
    ),
    "OnrampSessionQuoteParams": (
        "stripe.params.crypto._onramp_session_quote_params",
        False,
    ),
    "OnrampSessionRetrieveParams": (
        "stripe.params.crypto._onramp_session_retrieve_params",
        False,
    ),
    "OnrampTransactionLimitsRetrieveParams": (
        "stripe.params.crypto._onramp_transaction_limits_retrieve_params",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
