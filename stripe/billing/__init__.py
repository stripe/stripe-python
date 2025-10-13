# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.billing._alert import Alert as Alert
    from stripe.billing._alert_service import AlertService as AlertService
    from stripe.billing._alert_triggered import (
        AlertTriggered as AlertTriggered,
    )
    from stripe.billing._credit_balance_summary import (
        CreditBalanceSummary as CreditBalanceSummary,
    )
    from stripe.billing._credit_balance_summary_service import (
        CreditBalanceSummaryService as CreditBalanceSummaryService,
    )
    from stripe.billing._credit_balance_transaction import (
        CreditBalanceTransaction as CreditBalanceTransaction,
    )
    from stripe.billing._credit_balance_transaction_service import (
        CreditBalanceTransactionService as CreditBalanceTransactionService,
    )
    from stripe.billing._credit_grant import CreditGrant as CreditGrant
    from stripe.billing._credit_grant_service import (
        CreditGrantService as CreditGrantService,
    )
    from stripe.billing._meter import Meter as Meter
    from stripe.billing._meter_event import MeterEvent as MeterEvent
    from stripe.billing._meter_event_adjustment import (
        MeterEventAdjustment as MeterEventAdjustment,
    )
    from stripe.billing._meter_event_adjustment_service import (
        MeterEventAdjustmentService as MeterEventAdjustmentService,
    )
    from stripe.billing._meter_event_service import (
        MeterEventService as MeterEventService,
    )
    from stripe.billing._meter_event_summary import (
        MeterEventSummary as MeterEventSummary,
    )
    from stripe.billing._meter_event_summary_service import (
        MeterEventSummaryService as MeterEventSummaryService,
    )
    from stripe.billing._meter_service import MeterService as MeterService

_submodules = {
    "Alert": "stripe.billing._alert",
    "AlertService": "stripe.billing._alert_service",
    "AlertTriggered": "stripe.billing._alert_triggered",
    "CreditBalanceSummary": "stripe.billing._credit_balance_summary",
    "CreditBalanceSummaryService": "stripe.billing._credit_balance_summary_service",
    "CreditBalanceTransaction": "stripe.billing._credit_balance_transaction",
    "CreditBalanceTransactionService": "stripe.billing._credit_balance_transaction_service",
    "CreditGrant": "stripe.billing._credit_grant",
    "CreditGrantService": "stripe.billing._credit_grant_service",
    "Meter": "stripe.billing._meter",
    "MeterEvent": "stripe.billing._meter_event",
    "MeterEventAdjustment": "stripe.billing._meter_event_adjustment",
    "MeterEventAdjustmentService": "stripe.billing._meter_event_adjustment_service",
    "MeterEventService": "stripe.billing._meter_event_service",
    "MeterEventSummary": "stripe.billing._meter_event_summary",
    "MeterEventSummaryService": "stripe.billing._meter_event_summary_service",
    "MeterService": "stripe.billing._meter_service",
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
