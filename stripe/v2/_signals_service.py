# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.signals._account_activity_service import (
        AccountActivityService,
    )
    from stripe.v2.signals._account_evaluation_service import (
        AccountEvaluationService,
    )
    from stripe.v2.signals._account_signal_service import AccountSignalService
    from stripe.v2.signals._payment_retry_evaluation_service import (
        PaymentRetryEvaluationService,
    )
    from stripe.v2.signals._payment_retry_signal_service import (
        PaymentRetrySignalService,
    )

_subservices = {
    "account_activity": [
        "stripe.v2.signals._account_activity_service",
        "AccountActivityService",
    ],
    "account_evaluations": [
        "stripe.v2.signals._account_evaluation_service",
        "AccountEvaluationService",
    ],
    "account_signals": [
        "stripe.v2.signals._account_signal_service",
        "AccountSignalService",
    ],
    "payment_retry_evaluations": [
        "stripe.v2.signals._payment_retry_evaluation_service",
        "PaymentRetryEvaluationService",
    ],
    "payment_retry_signals": [
        "stripe.v2.signals._payment_retry_signal_service",
        "PaymentRetrySignalService",
    ],
}


class SignalsService(StripeService):
    account_activity: "AccountActivityService"
    account_evaluations: "AccountEvaluationService"
    account_signals: "AccountSignalService"
    payment_retry_evaluations: "PaymentRetryEvaluationService"
    payment_retry_signals: "PaymentRetrySignalService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
