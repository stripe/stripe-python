# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.test_helpers.terminal._reader_present_payment_method_params import (
        ReaderPresentPaymentMethodParams as ReaderPresentPaymentMethodParams,
        ReaderPresentPaymentMethodParamsCard as ReaderPresentPaymentMethodParamsCard,
        ReaderPresentPaymentMethodParamsCardPresent as ReaderPresentPaymentMethodParamsCardPresent,
        ReaderPresentPaymentMethodParamsInteracPresent as ReaderPresentPaymentMethodParamsInteracPresent,
    )
    from stripe.params.test_helpers.terminal._reader_succeed_input_collection_params import (
        ReaderSucceedInputCollectionParams as ReaderSucceedInputCollectionParams,
    )
    from stripe.params.test_helpers.terminal._reader_timeout_input_collection_params import (
        ReaderTimeoutInputCollectionParams as ReaderTimeoutInputCollectionParams,
    )

_submodules = {
    "ReaderPresentPaymentMethodParams": "stripe.params.test_helpers.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsCard": "stripe.params.test_helpers.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsCardPresent": "stripe.params.test_helpers.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsInteracPresent": "stripe.params.test_helpers.terminal._reader_present_payment_method_params",
    "ReaderSucceedInputCollectionParams": "stripe.params.test_helpers.terminal._reader_succeed_input_collection_params",
    "ReaderTimeoutInputCollectionParams": "stripe.params.test_helpers.terminal._reader_timeout_input_collection_params",
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
