# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.billing._alert_activate_params import (
        AlertActivateParams as AlertActivateParams,
    )
    from stripe.params.billing._alert_archive_params import (
        AlertArchiveParams as AlertArchiveParams,
    )
    from stripe.params.billing._alert_create_params import (
        AlertCreateParams as AlertCreateParams,
        AlertCreateParamsUsageThreshold as AlertCreateParamsUsageThreshold,
        AlertCreateParamsUsageThresholdFilter as AlertCreateParamsUsageThresholdFilter,
    )
    from stripe.params.billing._alert_deactivate_params import (
        AlertDeactivateParams as AlertDeactivateParams,
    )
    from stripe.params.billing._alert_list_params import (
        AlertListParams as AlertListParams,
    )
    from stripe.params.billing._alert_retrieve_params import (
        AlertRetrieveParams as AlertRetrieveParams,
    )
    from stripe.params.billing._credit_balance_summary_retrieve_params import (
        CreditBalanceSummaryRetrieveParams as CreditBalanceSummaryRetrieveParams,
        CreditBalanceSummaryRetrieveParamsFilter as CreditBalanceSummaryRetrieveParamsFilter,
        CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope as CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope,
        CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopePrice as CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopePrice,
    )
    from stripe.params.billing._credit_balance_transaction_list_params import (
        CreditBalanceTransactionListParams as CreditBalanceTransactionListParams,
    )
    from stripe.params.billing._credit_balance_transaction_retrieve_params import (
        CreditBalanceTransactionRetrieveParams as CreditBalanceTransactionRetrieveParams,
    )
    from stripe.params.billing._credit_grant_create_params import (
        CreditGrantCreateParams as CreditGrantCreateParams,
        CreditGrantCreateParamsAmount as CreditGrantCreateParamsAmount,
        CreditGrantCreateParamsAmountMonetary as CreditGrantCreateParamsAmountMonetary,
        CreditGrantCreateParamsApplicabilityConfig as CreditGrantCreateParamsApplicabilityConfig,
        CreditGrantCreateParamsApplicabilityConfigScope as CreditGrantCreateParamsApplicabilityConfigScope,
        CreditGrantCreateParamsApplicabilityConfigScopePrice as CreditGrantCreateParamsApplicabilityConfigScopePrice,
    )
    from stripe.params.billing._credit_grant_expire_params import (
        CreditGrantExpireParams as CreditGrantExpireParams,
    )
    from stripe.params.billing._credit_grant_list_params import (
        CreditGrantListParams as CreditGrantListParams,
    )
    from stripe.params.billing._credit_grant_modify_params import (
        CreditGrantModifyParams as CreditGrantModifyParams,
    )
    from stripe.params.billing._credit_grant_retrieve_params import (
        CreditGrantRetrieveParams as CreditGrantRetrieveParams,
    )
    from stripe.params.billing._credit_grant_update_params import (
        CreditGrantUpdateParams as CreditGrantUpdateParams,
    )
    from stripe.params.billing._credit_grant_void_grant_params import (
        CreditGrantVoidGrantParams as CreditGrantVoidGrantParams,
    )
    from stripe.params.billing._meter_create_params import (
        MeterCreateParams as MeterCreateParams,
        MeterCreateParamsCustomerMapping as MeterCreateParamsCustomerMapping,
        MeterCreateParamsDefaultAggregation as MeterCreateParamsDefaultAggregation,
        MeterCreateParamsValueSettings as MeterCreateParamsValueSettings,
    )
    from stripe.params.billing._meter_deactivate_params import (
        MeterDeactivateParams as MeterDeactivateParams,
    )
    from stripe.params.billing._meter_event_adjustment_create_params import (
        MeterEventAdjustmentCreateParams as MeterEventAdjustmentCreateParams,
        MeterEventAdjustmentCreateParamsCancel as MeterEventAdjustmentCreateParamsCancel,
    )
    from stripe.params.billing._meter_event_create_params import (
        MeterEventCreateParams as MeterEventCreateParams,
    )
    from stripe.params.billing._meter_event_summary_list_params import (
        MeterEventSummaryListParams as MeterEventSummaryListParams,
    )
    from stripe.params.billing._meter_list_event_summaries_params import (
        MeterListEventSummariesParams as MeterListEventSummariesParams,
    )
    from stripe.params.billing._meter_list_params import (
        MeterListParams as MeterListParams,
    )
    from stripe.params.billing._meter_modify_params import (
        MeterModifyParams as MeterModifyParams,
    )
    from stripe.params.billing._meter_reactivate_params import (
        MeterReactivateParams as MeterReactivateParams,
    )
    from stripe.params.billing._meter_retrieve_params import (
        MeterRetrieveParams as MeterRetrieveParams,
    )
    from stripe.params.billing._meter_update_params import (
        MeterUpdateParams as MeterUpdateParams,
    )

_submodules = {
    "AlertActivateParams": "stripe.params.billing._alert_activate_params",
    "AlertArchiveParams": "stripe.params.billing._alert_archive_params",
    "AlertCreateParams": "stripe.params.billing._alert_create_params",
    "AlertCreateParamsUsageThreshold": "stripe.params.billing._alert_create_params",
    "AlertCreateParamsUsageThresholdFilter": "stripe.params.billing._alert_create_params",
    "AlertDeactivateParams": "stripe.params.billing._alert_deactivate_params",
    "AlertListParams": "stripe.params.billing._alert_list_params",
    "AlertRetrieveParams": "stripe.params.billing._alert_retrieve_params",
    "CreditBalanceSummaryRetrieveParams": "stripe.params.billing._credit_balance_summary_retrieve_params",
    "CreditBalanceSummaryRetrieveParamsFilter": "stripe.params.billing._credit_balance_summary_retrieve_params",
    "CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope": "stripe.params.billing._credit_balance_summary_retrieve_params",
    "CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopePrice": "stripe.params.billing._credit_balance_summary_retrieve_params",
    "CreditBalanceTransactionListParams": "stripe.params.billing._credit_balance_transaction_list_params",
    "CreditBalanceTransactionRetrieveParams": "stripe.params.billing._credit_balance_transaction_retrieve_params",
    "CreditGrantCreateParams": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantCreateParamsAmount": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantCreateParamsAmountMonetary": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantCreateParamsApplicabilityConfig": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantCreateParamsApplicabilityConfigScope": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantCreateParamsApplicabilityConfigScopePrice": "stripe.params.billing._credit_grant_create_params",
    "CreditGrantExpireParams": "stripe.params.billing._credit_grant_expire_params",
    "CreditGrantListParams": "stripe.params.billing._credit_grant_list_params",
    "CreditGrantModifyParams": "stripe.params.billing._credit_grant_modify_params",
    "CreditGrantRetrieveParams": "stripe.params.billing._credit_grant_retrieve_params",
    "CreditGrantUpdateParams": "stripe.params.billing._credit_grant_update_params",
    "CreditGrantVoidGrantParams": "stripe.params.billing._credit_grant_void_grant_params",
    "MeterCreateParams": "stripe.params.billing._meter_create_params",
    "MeterCreateParamsCustomerMapping": "stripe.params.billing._meter_create_params",
    "MeterCreateParamsDefaultAggregation": "stripe.params.billing._meter_create_params",
    "MeterCreateParamsValueSettings": "stripe.params.billing._meter_create_params",
    "MeterDeactivateParams": "stripe.params.billing._meter_deactivate_params",
    "MeterEventAdjustmentCreateParams": "stripe.params.billing._meter_event_adjustment_create_params",
    "MeterEventAdjustmentCreateParamsCancel": "stripe.params.billing._meter_event_adjustment_create_params",
    "MeterEventCreateParams": "stripe.params.billing._meter_event_create_params",
    "MeterEventSummaryListParams": "stripe.params.billing._meter_event_summary_list_params",
    "MeterListEventSummariesParams": "stripe.params.billing._meter_list_event_summaries_params",
    "MeterListParams": "stripe.params.billing._meter_list_params",
    "MeterModifyParams": "stripe.params.billing._meter_modify_params",
    "MeterReactivateParams": "stripe.params.billing._meter_reactivate_params",
    "MeterRetrieveParams": "stripe.params.billing._meter_retrieve_params",
    "MeterUpdateParams": "stripe.params.billing._meter_update_params",
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
