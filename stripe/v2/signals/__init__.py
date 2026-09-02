# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.signals._account_activity import (
        AccountActivity as AccountActivity,
    )
    from stripe.v2.signals._account_activity_service import (
        AccountActivityService as AccountActivityService,
    )
    from stripe.v2.signals._account_evaluation import (
        AccountEvaluation as AccountEvaluation,
    )
    from stripe.v2.signals._account_evaluation_service import (
        AccountEvaluationService as AccountEvaluationService,
    )
    from stripe.v2.signals._account_signal import (
        AccountSignal as AccountSignal,
    )
    from stripe.v2.signals._account_signal_service import (
        AccountSignalService as AccountSignalService,
    )
    from stripe.v2.signals._payment_retry_evaluation import (
        PaymentRetryEvaluation as PaymentRetryEvaluation,
    )
    from stripe.v2.signals._payment_retry_evaluation_service import (
        PaymentRetryEvaluationService as PaymentRetryEvaluationService,
    )
    from stripe.v2.signals._payment_retry_signal import (
        PaymentRetrySignal as PaymentRetrySignal,
    )
    from stripe.v2.signals._payment_retry_signal_service import (
        PaymentRetrySignalService as PaymentRetrySignalService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AccountActivity": ("stripe.v2.signals._account_activity", False),
    "AccountActivityService": (
        "stripe.v2.signals._account_activity_service",
        False,
    ),
    "AccountEvaluation": ("stripe.v2.signals._account_evaluation", False),
    "AccountEvaluationService": (
        "stripe.v2.signals._account_evaluation_service",
        False,
    ),
    "AccountSignal": ("stripe.v2.signals._account_signal", False),
    "AccountSignalService": (
        "stripe.v2.signals._account_signal_service",
        False,
    ),
    "PaymentRetryEvaluation": (
        "stripe.v2.signals._payment_retry_evaluation",
        False,
    ),
    "PaymentRetryEvaluationService": (
        "stripe.v2.signals._payment_retry_evaluation_service",
        False,
    ),
    "PaymentRetrySignal": ("stripe.v2.signals._payment_retry_signal", False),
    "PaymentRetrySignalService": (
        "stripe.v2.signals._payment_retry_signal_service",
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
