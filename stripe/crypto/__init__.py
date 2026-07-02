# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.crypto._customer import Customer as Customer
    from stripe.crypto._customer_consumer_wallet import (
        CustomerConsumerWallet as CustomerConsumerWallet,
    )
    from stripe.crypto._customer_consumer_wallet_service import (
        CustomerConsumerWalletService as CustomerConsumerWalletService,
    )
    from stripe.crypto._customer_payment_token import (
        CustomerPaymentToken as CustomerPaymentToken,
    )
    from stripe.crypto._customer_payment_token_service import (
        CustomerPaymentTokenService as CustomerPaymentTokenService,
    )
    from stripe.crypto._customer_service import (
        CustomerService as CustomerService,
    )
    from stripe.crypto._onramp_session import OnrampSession as OnrampSession
    from stripe.crypto._onramp_session_service import (
        OnrampSessionService as OnrampSessionService,
    )
    from stripe.crypto._onramp_transaction_limits import (
        OnrampTransactionLimits as OnrampTransactionLimits,
    )
    from stripe.crypto._onramp_transaction_limits_service import (
        OnrampTransactionLimitsService as OnrampTransactionLimitsService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Customer": ("stripe.crypto._customer", False),
    "CustomerConsumerWallet": (
        "stripe.crypto._customer_consumer_wallet",
        False,
    ),
    "CustomerConsumerWalletService": (
        "stripe.crypto._customer_consumer_wallet_service",
        False,
    ),
    "CustomerPaymentToken": ("stripe.crypto._customer_payment_token", False),
    "CustomerPaymentTokenService": (
        "stripe.crypto._customer_payment_token_service",
        False,
    ),
    "CustomerService": ("stripe.crypto._customer_service", False),
    "OnrampSession": ("stripe.crypto._onramp_session", False),
    "OnrampSessionService": ("stripe.crypto._onramp_session_service", False),
    "OnrampTransactionLimits": (
        "stripe.crypto._onramp_transaction_limits",
        False,
    ),
    "OnrampTransactionLimitsService": (
        "stripe.crypto._onramp_transaction_limits_service",
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
