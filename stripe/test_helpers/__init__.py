# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.test_helpers._confirmation_token_service import (
        ConfirmationTokenService as ConfirmationTokenService,
    )
    from stripe.test_helpers._customer_service import (
        CustomerService as CustomerService,
    )
    from stripe.test_helpers._issuing_service import (
        IssuingService as IssuingService,
    )
    from stripe.test_helpers._refund_service import (
        RefundService as RefundService,
    )
    from stripe.test_helpers._terminal_service import (
        TerminalService as TerminalService,
    )
    from stripe.test_helpers._test_clock import TestClock as TestClock
    from stripe.test_helpers._test_clock_service import (
        TestClockService as TestClockService,
    )
    from stripe.test_helpers._treasury_service import (
        TreasuryService as TreasuryService,
    )

_submodules = {
    "ConfirmationTokenService": "stripe.test_helpers._confirmation_token_service",
    "CustomerService": "stripe.test_helpers._customer_service",
    "IssuingService": "stripe.test_helpers._issuing_service",
    "RefundService": "stripe.test_helpers._refund_service",
    "TerminalService": "stripe.test_helpers._terminal_service",
    "TestClock": "stripe.test_helpers._test_clock",
    "TestClockService": "stripe.test_helpers._test_clock_service",
    "TreasuryService": "stripe.test_helpers._treasury_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
