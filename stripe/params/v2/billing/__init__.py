# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing import (
        bill_settings as bill_settings,
        collection_settings as collection_settings,
        contracts as contracts,
        groups as groups,
        intents as intents,
        license_fees as license_fees,
        pricing_plans as pricing_plans,
        rate_cards as rate_cards,
    )
    from stripe.params.v2.billing._bill_setting_create_params import (
        BillSettingCreateParams as BillSettingCreateParams,
        BillSettingCreateParamsCalculation as BillSettingCreateParamsCalculation,
        BillSettingCreateParamsCalculationTax as BillSettingCreateParamsCalculationTax,
        BillSettingCreateParamsInvoice as BillSettingCreateParamsInvoice,
        BillSettingCreateParamsInvoiceTimeUntilDue as BillSettingCreateParamsInvoiceTimeUntilDue,
    )
    from stripe.params.v2.billing._bill_setting_list_params import (
        BillSettingListParams as BillSettingListParams,
    )
    from stripe.params.v2.billing._bill_setting_retrieve_params import (
        BillSettingRetrieveParams as BillSettingRetrieveParams,
    )
    from stripe.params.v2.billing._bill_setting_update_params import (
        BillSettingUpdateParams as BillSettingUpdateParams,
        BillSettingUpdateParamsCalculation as BillSettingUpdateParamsCalculation,
        BillSettingUpdateParamsCalculationTax as BillSettingUpdateParamsCalculationTax,
        BillSettingUpdateParamsInvoice as BillSettingUpdateParamsInvoice,
        BillSettingUpdateParamsInvoiceTimeUntilDue as BillSettingUpdateParamsInvoiceTimeUntilDue,
    )
    from stripe.params.v2.billing._collection_setting_create_params import (
        CollectionSettingCreateParams as CollectionSettingCreateParams,
        CollectionSettingCreateParamsEmailDelivery as CollectionSettingCreateParamsEmailDelivery,
        CollectionSettingCreateParamsEmailDeliveryPaymentDue as CollectionSettingCreateParamsEmailDeliveryPaymentDue,
        CollectionSettingCreateParamsPaymentMethodOptions as CollectionSettingCreateParamsPaymentMethodOptions,
        CollectionSettingCreateParamsPaymentMethodOptionsAcssDebit as CollectionSettingCreateParamsPaymentMethodOptionsAcssDebit,
        CollectionSettingCreateParamsPaymentMethodOptionsAcssDebitMandateOptions as CollectionSettingCreateParamsPaymentMethodOptionsAcssDebitMandateOptions,
        CollectionSettingCreateParamsPaymentMethodOptionsBancontact as CollectionSettingCreateParamsPaymentMethodOptionsBancontact,
        CollectionSettingCreateParamsPaymentMethodOptionsCard as CollectionSettingCreateParamsPaymentMethodOptionsCard,
        CollectionSettingCreateParamsPaymentMethodOptionsCardMandateOptions as CollectionSettingCreateParamsPaymentMethodOptionsCardMandateOptions,
        CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalance as CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalance,
        CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer as CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer,
        CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        CollectionSettingCreateParamsPaymentMethodOptionsKonbini as CollectionSettingCreateParamsPaymentMethodOptionsKonbini,
        CollectionSettingCreateParamsPaymentMethodOptionsSepaDebit as CollectionSettingCreateParamsPaymentMethodOptionsSepaDebit,
        CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccount as CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccount,
        CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections as CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections,
        CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
    )
    from stripe.params.v2.billing._collection_setting_list_params import (
        CollectionSettingListParams as CollectionSettingListParams,
    )
    from stripe.params.v2.billing._collection_setting_retrieve_params import (
        CollectionSettingRetrieveParams as CollectionSettingRetrieveParams,
    )
    from stripe.params.v2.billing._collection_setting_update_params import (
        CollectionSettingUpdateParams as CollectionSettingUpdateParams,
        CollectionSettingUpdateParamsEmailDelivery as CollectionSettingUpdateParamsEmailDelivery,
        CollectionSettingUpdateParamsEmailDeliveryPaymentDue as CollectionSettingUpdateParamsEmailDeliveryPaymentDue,
        CollectionSettingUpdateParamsPaymentMethodOptions as CollectionSettingUpdateParamsPaymentMethodOptions,
        CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebit as CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebit,
        CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebitMandateOptions as CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebitMandateOptions,
        CollectionSettingUpdateParamsPaymentMethodOptionsBancontact as CollectionSettingUpdateParamsPaymentMethodOptionsBancontact,
        CollectionSettingUpdateParamsPaymentMethodOptionsCard as CollectionSettingUpdateParamsPaymentMethodOptionsCard,
        CollectionSettingUpdateParamsPaymentMethodOptionsCardMandateOptions as CollectionSettingUpdateParamsPaymentMethodOptionsCardMandateOptions,
        CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalance as CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalance,
        CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer as CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer,
        CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        CollectionSettingUpdateParamsPaymentMethodOptionsKonbini as CollectionSettingUpdateParamsPaymentMethodOptionsKonbini,
        CollectionSettingUpdateParamsPaymentMethodOptionsSepaDebit as CollectionSettingUpdateParamsPaymentMethodOptionsSepaDebit,
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount,
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections,
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
    )
    from stripe.params.v2.billing._contract_activate_params import (
        ContractActivateParams as ContractActivateParams,
    )
    from stripe.params.v2.billing._contract_cancel_params import (
        ContractCancelParams as ContractCancelParams,
        ContractCancelParamsTerm as ContractCancelParamsTerm,
        ContractCancelParamsTermTerm as ContractCancelParamsTermTerm,
    )
    from stripe.params.v2.billing._contract_create_params import (
        ContractCreateParams as ContractCreateParams,
        ContractCreateParamsBillingCycleAnchor as ContractCreateParamsBillingCycleAnchor,
        ContractCreateParamsBillingCycleAnchorConfig as ContractCreateParamsBillingCycleAnchorConfig,
        ContractCreateParamsBillingSettings as ContractCreateParamsBillingSettings,
        ContractCreateParamsBillingSettingsBillSettingsDetails as ContractCreateParamsBillingSettingsBillSettingsDetails,
        ContractCreateParamsBillingSettingsBillSettingsDetailsCalculation as ContractCreateParamsBillingSettingsBillSettingsDetailsCalculation,
        ContractCreateParamsBillingSettingsBillSettingsDetailsCalculationTax as ContractCreateParamsBillingSettingsBillSettingsDetailsCalculationTax,
        ContractCreateParamsBillingSettingsBillSettingsDetailsInvoice as ContractCreateParamsBillingSettingsBillSettingsDetailsInvoice,
        ContractCreateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue as ContractCreateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue,
        ContractCreateParamsBillingSettingsBillingProfileDetails as ContractCreateParamsBillingSettingsBillingProfileDetails,
        ContractCreateParamsBillingSettingsCollectionSettingsDetails as ContractCreateParamsBillingSettingsCollectionSettingsDetails,
        ContractCreateParamsTerm as ContractCreateParamsTerm,
        ContractCreateParamsTermPricingOverride as ContractCreateParamsTermPricingOverride,
        ContractCreateParamsTermPricingOverrideCriterion as ContractCreateParamsTermPricingOverrideCriterion,
        ContractCreateParamsTermPricingOverrideCriterionTerm as ContractCreateParamsTermPricingOverrideCriterionTerm,
        ContractCreateParamsTermPricingOverrideEndsAt as ContractCreateParamsTermPricingOverrideEndsAt,
        ContractCreateParamsTermPricingOverrideMultiply as ContractCreateParamsTermPricingOverrideMultiply,
        ContractCreateParamsTermPricingOverrideOverwrite as ContractCreateParamsTermPricingOverrideOverwrite,
        ContractCreateParamsTermPricingOverrideStartsAt as ContractCreateParamsTermPricingOverrideStartsAt,
        ContractCreateParamsTermRecurringPrice as ContractCreateParamsTermRecurringPrice,
        ContractCreateParamsTermRecurringPriceEndsAt as ContractCreateParamsTermRecurringPriceEndsAt,
        ContractCreateParamsTermRecurringPriceStartsAt as ContractCreateParamsTermRecurringPriceStartsAt,
        ContractCreateParamsTermScheduledFee as ContractCreateParamsTermScheduledFee,
        ContractCreateParamsTermScheduledFeeBillSchedule as ContractCreateParamsTermScheduledFeeBillSchedule,
        ContractCreateParamsTermScheduledFeeBillScheduleCustom as ContractCreateParamsTermScheduledFeeBillScheduleCustom,
        ContractCreateParamsTermScheduledFeeBillScheduleCustomBillAt as ContractCreateParamsTermScheduledFeeBillScheduleCustomBillAt,
        ContractCreateParamsTermScheduledFeeServicePeriod as ContractCreateParamsTermScheduledFeeServicePeriod,
        ContractCreateParamsTermScheduledFeeServicePeriodEndsAt as ContractCreateParamsTermScheduledFeeServicePeriodEndsAt,
        ContractCreateParamsTermScheduledFeeServicePeriodStartsAt as ContractCreateParamsTermScheduledFeeServicePeriodStartsAt,
    )
    from stripe.params.v2.billing._contract_delete_params import (
        ContractDeleteParams as ContractDeleteParams,
    )
    from stripe.params.v2.billing._contract_list_params import (
        ContractListParams as ContractListParams,
    )
    from stripe.params.v2.billing._contract_retrieve_params import (
        ContractRetrieveParams as ContractRetrieveParams,
    )
    from stripe.params.v2.billing._contract_update_params import (
        ContractUpdateParams as ContractUpdateParams,
        ContractUpdateParamsAction as ContractUpdateParamsAction,
        ContractUpdateParamsActionAddTerm as ContractUpdateParamsActionAddTerm,
        ContractUpdateParamsActionAddTermPricingOverride as ContractUpdateParamsActionAddTermPricingOverride,
        ContractUpdateParamsActionAddTermPricingOverrideCriterion as ContractUpdateParamsActionAddTermPricingOverrideCriterion,
        ContractUpdateParamsActionAddTermPricingOverrideCriterionTerm as ContractUpdateParamsActionAddTermPricingOverrideCriterionTerm,
        ContractUpdateParamsActionAddTermPricingOverrideEndsAt as ContractUpdateParamsActionAddTermPricingOverrideEndsAt,
        ContractUpdateParamsActionAddTermPricingOverrideMultiply as ContractUpdateParamsActionAddTermPricingOverrideMultiply,
        ContractUpdateParamsActionAddTermPricingOverrideOverwrite as ContractUpdateParamsActionAddTermPricingOverrideOverwrite,
        ContractUpdateParamsActionAddTermPricingOverrideStartsAt as ContractUpdateParamsActionAddTermPricingOverrideStartsAt,
        ContractUpdateParamsActionAddTermRecurringPrice as ContractUpdateParamsActionAddTermRecurringPrice,
        ContractUpdateParamsActionAddTermRecurringPriceEndsAt as ContractUpdateParamsActionAddTermRecurringPriceEndsAt,
        ContractUpdateParamsActionAddTermRecurringPriceStartsAt as ContractUpdateParamsActionAddTermRecurringPriceStartsAt,
        ContractUpdateParamsActionAddTermScheduledFee as ContractUpdateParamsActionAddTermScheduledFee,
        ContractUpdateParamsActionAddTermScheduledFeeBillSchedule as ContractUpdateParamsActionAddTermScheduledFeeBillSchedule,
        ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustom as ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustom,
        ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustomBillAt as ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustomBillAt,
        ContractUpdateParamsActionAddTermScheduledFeeServicePeriod as ContractUpdateParamsActionAddTermScheduledFeeServicePeriod,
        ContractUpdateParamsActionAddTermScheduledFeeServicePeriodEndsAt as ContractUpdateParamsActionAddTermScheduledFeeServicePeriodEndsAt,
        ContractUpdateParamsActionAddTermScheduledFeeServicePeriodStartsAt as ContractUpdateParamsActionAddTermScheduledFeeServicePeriodStartsAt,
        ContractUpdateParamsActionRemoveTerm as ContractUpdateParamsActionRemoveTerm,
        ContractUpdateParamsActionRemoveTermTerm as ContractUpdateParamsActionRemoveTermTerm,
        ContractUpdateParamsActionUpdateTerm as ContractUpdateParamsActionUpdateTerm,
        ContractUpdateParamsActionUpdateTermPricingOverride as ContractUpdateParamsActionUpdateTermPricingOverride,
        ContractUpdateParamsActionUpdateTermPricingOverrideEndsAt as ContractUpdateParamsActionUpdateTermPricingOverrideEndsAt,
        ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt as ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt,
        ContractUpdateParamsActionUpdateTermRecurringPrice as ContractUpdateParamsActionUpdateTermRecurringPrice,
        ContractUpdateParamsActionUpdateTermRecurringPriceEndsAt as ContractUpdateParamsActionUpdateTermRecurringPriceEndsAt,
        ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt as ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt,
        ContractUpdateParamsActionUpdateTermScheduledFee as ContractUpdateParamsActionUpdateTermScheduledFee,
        ContractUpdateParamsActionUpdateTermScheduledFeeBillSchedule as ContractUpdateParamsActionUpdateTermScheduledFeeBillSchedule,
        ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustom as ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustom,
        ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustomBillAt as ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustomBillAt,
        ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriod as ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriod,
        ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodEndsAt as ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodEndsAt,
        ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodStartsAt as ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodStartsAt,
        ContractUpdateParamsActionUpdateTermTerm as ContractUpdateParamsActionUpdateTermTerm,
        ContractUpdateParamsBillingSettings as ContractUpdateParamsBillingSettings,
        ContractUpdateParamsBillingSettingsBillSettingsDetails as ContractUpdateParamsBillingSettingsBillSettingsDetails,
        ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculation as ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculation,
        ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculationTax as ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculationTax,
        ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoice as ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoice,
        ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue as ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue,
        ContractUpdateParamsBillingSettingsBillingProfileDetails as ContractUpdateParamsBillingSettingsBillingProfileDetails,
        ContractUpdateParamsBillingSettingsCollectionSettingsDetails as ContractUpdateParamsBillingSettingsCollectionSettingsDetails,
    )
    from stripe.params.v2.billing._custom_pricing_unit_create_params import (
        CustomPricingUnitCreateParams as CustomPricingUnitCreateParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_list_params import (
        CustomPricingUnitListParams as CustomPricingUnitListParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_retrieve_params import (
        CustomPricingUnitRetrieveParams as CustomPricingUnitRetrieveParams,
    )
    from stripe.params.v2.billing._custom_pricing_unit_update_params import (
        CustomPricingUnitUpdateParams as CustomPricingUnitUpdateParams,
    )
    from stripe.params.v2.billing._group_cancel_params import (
        GroupCancelParams as GroupCancelParams,
    )
    from stripe.params.v2.billing._group_create_params import (
        GroupCreateParams as GroupCreateParams,
        GroupCreateParamsBillingSettings as GroupCreateParamsBillingSettings,
        GroupCreateParamsBillingSettingsEmailDelivery as GroupCreateParamsBillingSettingsEmailDelivery,
        GroupCreateParamsBillingSettingsEmailDeliveryPaymentDue as GroupCreateParamsBillingSettingsEmailDeliveryPaymentDue,
        GroupCreateParamsBillingSettingsInvoicePresentation as GroupCreateParamsBillingSettingsInvoicePresentation,
        GroupCreateParamsBillingSettingsInvoiceTimeUntilDue as GroupCreateParamsBillingSettingsInvoiceTimeUntilDue,
        GroupCreateParamsBillingSettingsPaymentMethodOptions as GroupCreateParamsBillingSettingsPaymentMethodOptions,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebit as GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebit,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions as GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsBancontact as GroupCreateParamsBillingSettingsPaymentMethodOptionsBancontact,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsCard as GroupCreateParamsBillingSettingsPaymentMethodOptionsCard,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions as GroupCreateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalance as GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalance,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer as GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsKonbini as GroupCreateParamsBillingSettingsPaymentMethodOptionsKonbini,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsSepaDebit as GroupCreateParamsBillingSettingsPaymentMethodOptionsSepaDebit,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccount as GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccount,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections as GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections,
        GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
        GroupCreateParamsBillingSettingsTax as GroupCreateParamsBillingSettingsTax,
        GroupCreateParamsGroupingBehavior as GroupCreateParamsGroupingBehavior,
        GroupCreateParamsGroupingBehaviorByCadence as GroupCreateParamsGroupingBehaviorByCadence,
        GroupCreateParamsGroupingBehaviorByCadenceDay as GroupCreateParamsGroupingBehaviorByCadenceDay,
        GroupCreateParamsGroupingBehaviorByCadenceDayTime as GroupCreateParamsGroupingBehaviorByCadenceDayTime,
        GroupCreateParamsGroupingBehaviorByCadenceMonth as GroupCreateParamsGroupingBehaviorByCadenceMonth,
        GroupCreateParamsGroupingBehaviorByCadenceMonthTime as GroupCreateParamsGroupingBehaviorByCadenceMonthTime,
        GroupCreateParamsGroupingBehaviorByCadenceWeek as GroupCreateParamsGroupingBehaviorByCadenceWeek,
        GroupCreateParamsGroupingBehaviorByCadenceWeekTime as GroupCreateParamsGroupingBehaviorByCadenceWeekTime,
        GroupCreateParamsGroupingBehaviorByCadenceYear as GroupCreateParamsGroupingBehaviorByCadenceYear,
        GroupCreateParamsGroupingBehaviorByCadenceYearTime as GroupCreateParamsGroupingBehaviorByCadenceYearTime,
    )
    from stripe.params.v2.billing._group_list_params import (
        GroupListParams as GroupListParams,
    )
    from stripe.params.v2.billing._group_retrieve_params import (
        GroupRetrieveParams as GroupRetrieveParams,
    )
    from stripe.params.v2.billing._group_update_params import (
        GroupUpdateParams as GroupUpdateParams,
        GroupUpdateParamsBillingSettings as GroupUpdateParamsBillingSettings,
        GroupUpdateParamsBillingSettingsEmailDelivery as GroupUpdateParamsBillingSettingsEmailDelivery,
        GroupUpdateParamsBillingSettingsEmailDeliveryPaymentDue as GroupUpdateParamsBillingSettingsEmailDeliveryPaymentDue,
        GroupUpdateParamsBillingSettingsInvoicePresentation as GroupUpdateParamsBillingSettingsInvoicePresentation,
        GroupUpdateParamsBillingSettingsInvoiceTimeUntilDue as GroupUpdateParamsBillingSettingsInvoiceTimeUntilDue,
        GroupUpdateParamsBillingSettingsPaymentMethodOptions as GroupUpdateParamsBillingSettingsPaymentMethodOptions,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebit as GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebit,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions as GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsBancontact as GroupUpdateParamsBillingSettingsPaymentMethodOptionsBancontact,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsCard as GroupUpdateParamsBillingSettingsPaymentMethodOptionsCard,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions as GroupUpdateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalance as GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalance,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer as GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsKonbini as GroupUpdateParamsBillingSettingsPaymentMethodOptionsKonbini,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsSepaDebit as GroupUpdateParamsBillingSettingsPaymentMethodOptionsSepaDebit,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccount as GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccount,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections as GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections,
        GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
        GroupUpdateParamsBillingSettingsTax as GroupUpdateParamsBillingSettingsTax,
    )
    from stripe.params.v2.billing._intent_cancel_params import (
        IntentCancelParams as IntentCancelParams,
    )
    from stripe.params.v2.billing._intent_commit_params import (
        IntentCommitParams as IntentCommitParams,
    )
    from stripe.params.v2.billing._intent_create_params import (
        IntentCreateParams as IntentCreateParams,
        IntentCreateParamsAction as IntentCreateParamsAction,
        IntentCreateParamsActionApply as IntentCreateParamsActionApply,
        IntentCreateParamsActionApplyDiscount as IntentCreateParamsActionApplyDiscount,
        IntentCreateParamsActionApplyEffectiveAt as IntentCreateParamsActionApplyEffectiveAt,
        IntentCreateParamsActionApplyInvoiceDiscountRule as IntentCreateParamsActionApplyInvoiceDiscountRule,
        IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff as IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff,
        IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications as IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications,
        IntentCreateParamsActionApplySpendModifierRule as IntentCreateParamsActionApplySpendModifierRule,
        IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend as IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend,
        IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount as IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount,
        IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit as IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit,
        IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendCustomPricingUnitOverageRate as IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendCustomPricingUnitOverageRate,
        IntentCreateParamsActionDeactivate as IntentCreateParamsActionDeactivate,
        IntentCreateParamsActionDeactivateCancellationDetails as IntentCreateParamsActionDeactivateCancellationDetails,
        IntentCreateParamsActionDeactivateEffectiveAt as IntentCreateParamsActionDeactivateEffectiveAt,
        IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails as IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails,
        IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides as IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides,
        IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior as IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior,
        IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee as IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee,
        IntentCreateParamsActionModify as IntentCreateParamsActionModify,
        IntentCreateParamsActionModifyEffectiveAt as IntentCreateParamsActionModifyEffectiveAt,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetails as IntentCreateParamsActionModifyPricingPlanSubscriptionDetails,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration as IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides as IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior as IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee as IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee,
        IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant as IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant,
        IntentCreateParamsActionRemove as IntentCreateParamsActionRemove,
        IntentCreateParamsActionRemoveEffectiveAt as IntentCreateParamsActionRemoveEffectiveAt,
        IntentCreateParamsActionSubscribe as IntentCreateParamsActionSubscribe,
        IntentCreateParamsActionSubscribeEffectiveAt as IntentCreateParamsActionSubscribeEffectiveAt,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant,
        IntentCreateParamsActionSubscribeV1SubscriptionDetails as IntentCreateParamsActionSubscribeV1SubscriptionDetails,
        IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem as IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem,
        IntentCreateParamsBillingGroupData as IntentCreateParamsBillingGroupData,
        IntentCreateParamsBillingGroupDataBillingSettings as IntentCreateParamsBillingGroupDataBillingSettings,
        IntentCreateParamsBillingGroupDataBillingSettingsEmailDelivery as IntentCreateParamsBillingGroupDataBillingSettingsEmailDelivery,
        IntentCreateParamsBillingGroupDataBillingSettingsEmailDeliveryPaymentDue as IntentCreateParamsBillingGroupDataBillingSettingsEmailDeliveryPaymentDue,
        IntentCreateParamsBillingGroupDataBillingSettingsInvoicePresentation as IntentCreateParamsBillingGroupDataBillingSettingsInvoicePresentation,
        IntentCreateParamsBillingGroupDataBillingSettingsInvoiceTimeUntilDue as IntentCreateParamsBillingGroupDataBillingSettingsInvoiceTimeUntilDue,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptions as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptions,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebit as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebit,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsBancontact as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsBancontact,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCard as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCard,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCardMandateOptions as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCardMandateOptions,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalance as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalance,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsKonbini as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsKonbini,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsSepaDebit as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsSepaDebit,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccount as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccount,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections,
        IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
        IntentCreateParamsBillingGroupDataBillingSettingsTax as IntentCreateParamsBillingGroupDataBillingSettingsTax,
        IntentCreateParamsBillingGroupDataGroupingBehavior as IntentCreateParamsBillingGroupDataGroupingBehavior,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadence as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadence,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDay as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDay,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDayTime as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDayTime,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonth as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonth,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonthTime as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonthTime,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeek as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeek,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeekTime as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeekTime,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYear as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYear,
        IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYearTime as IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYearTime,
    )
    from stripe.params.v2.billing._intent_list_params import (
        IntentListParams as IntentListParams,
    )
    from stripe.params.v2.billing._intent_release_reservation_params import (
        IntentReleaseReservationParams as IntentReleaseReservationParams,
    )
    from stripe.params.v2.billing._intent_reserve_params import (
        IntentReserveParams as IntentReserveParams,
    )
    from stripe.params.v2.billing._intent_retrieve_params import (
        IntentRetrieveParams as IntentRetrieveParams,
    )
    from stripe.params.v2.billing._license_fee_create_params import (
        LicenseFeeCreateParams as LicenseFeeCreateParams,
        LicenseFeeCreateParamsTier as LicenseFeeCreateParamsTier,
        LicenseFeeCreateParamsTransformQuantity as LicenseFeeCreateParamsTransformQuantity,
    )
    from stripe.params.v2.billing._license_fee_list_params import (
        LicenseFeeListParams as LicenseFeeListParams,
    )
    from stripe.params.v2.billing._license_fee_retrieve_params import (
        LicenseFeeRetrieveParams as LicenseFeeRetrieveParams,
    )
    from stripe.params.v2.billing._license_fee_update_params import (
        LicenseFeeUpdateParams as LicenseFeeUpdateParams,
        LicenseFeeUpdateParamsTier as LicenseFeeUpdateParamsTier,
        LicenseFeeUpdateParamsTransformQuantity as LicenseFeeUpdateParamsTransformQuantity,
    )
    from stripe.params.v2.billing._licensed_item_create_params import (
        LicensedItemCreateParams as LicensedItemCreateParams,
        LicensedItemCreateParamsTaxDetails as LicensedItemCreateParamsTaxDetails,
    )
    from stripe.params.v2.billing._licensed_item_list_params import (
        LicensedItemListParams as LicensedItemListParams,
    )
    from stripe.params.v2.billing._licensed_item_retrieve_params import (
        LicensedItemRetrieveParams as LicensedItemRetrieveParams,
    )
    from stripe.params.v2.billing._licensed_item_update_params import (
        LicensedItemUpdateParams as LicensedItemUpdateParams,
        LicensedItemUpdateParamsTaxDetails as LicensedItemUpdateParamsTaxDetails,
    )
    from stripe.params.v2.billing._meter_event_adjustment_create_params import (
        MeterEventAdjustmentCreateParams as MeterEventAdjustmentCreateParams,
        MeterEventAdjustmentCreateParamsCancel as MeterEventAdjustmentCreateParamsCancel,
    )
    from stripe.params.v2.billing._meter_event_create_params import (
        MeterEventCreateParams as MeterEventCreateParams,
    )
    from stripe.params.v2.billing._meter_event_session_create_params import (
        MeterEventSessionCreateParams as MeterEventSessionCreateParams,
    )
    from stripe.params.v2.billing._meter_event_stream_create_params import (
        MeterEventStreamCreateParams as MeterEventStreamCreateParams,
        MeterEventStreamCreateParamsEvent as MeterEventStreamCreateParamsEvent,
    )
    from stripe.params.v2.billing._metered_item_create_params import (
        MeteredItemCreateParams as MeteredItemCreateParams,
        MeteredItemCreateParamsMeterSegmentCondition as MeteredItemCreateParamsMeterSegmentCondition,
        MeteredItemCreateParamsTaxDetails as MeteredItemCreateParamsTaxDetails,
    )
    from stripe.params.v2.billing._metered_item_list_params import (
        MeteredItemListParams as MeteredItemListParams,
    )
    from stripe.params.v2.billing._metered_item_retrieve_params import (
        MeteredItemRetrieveParams as MeteredItemRetrieveParams,
    )
    from stripe.params.v2.billing._metered_item_update_params import (
        MeteredItemUpdateParams as MeteredItemUpdateParams,
        MeteredItemUpdateParamsTaxDetails as MeteredItemUpdateParamsTaxDetails,
    )
    from stripe.params.v2.billing._one_time_item_create_params import (
        OneTimeItemCreateParams as OneTimeItemCreateParams,
        OneTimeItemCreateParamsTaxDetails as OneTimeItemCreateParamsTaxDetails,
    )
    from stripe.params.v2.billing._one_time_item_list_params import (
        OneTimeItemListParams as OneTimeItemListParams,
    )
    from stripe.params.v2.billing._one_time_item_retrieve_params import (
        OneTimeItemRetrieveParams as OneTimeItemRetrieveParams,
    )
    from stripe.params.v2.billing._one_time_item_update_params import (
        OneTimeItemUpdateParams as OneTimeItemUpdateParams,
        OneTimeItemUpdateParamsTaxDetails as OneTimeItemUpdateParamsTaxDetails,
    )
    from stripe.params.v2.billing._pricing_plan_create_params import (
        PricingPlanCreateParams as PricingPlanCreateParams,
    )
    from stripe.params.v2.billing._pricing_plan_list_params import (
        PricingPlanListParams as PricingPlanListParams,
    )
    from stripe.params.v2.billing._pricing_plan_retrieve_params import (
        PricingPlanRetrieveParams as PricingPlanRetrieveParams,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_list_params import (
        PricingPlanSubscriptionListParams as PricingPlanSubscriptionListParams,
        PricingPlanSubscriptionListParamsPayer as PricingPlanSubscriptionListParamsPayer,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_remove_discounts_params import (
        PricingPlanSubscriptionRemoveDiscountsParams as PricingPlanSubscriptionRemoveDiscountsParams,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_retrieve_params import (
        PricingPlanSubscriptionRetrieveParams as PricingPlanSubscriptionRetrieveParams,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_update_params import (
        PricingPlanSubscriptionUpdateParams as PricingPlanSubscriptionUpdateParams,
    )
    from stripe.params.v2.billing._pricing_plan_update_params import (
        PricingPlanUpdateParams as PricingPlanUpdateParams,
    )
    from stripe.params.v2.billing._profile_create_params import (
        ProfileCreateParams as ProfileCreateParams,
    )
    from stripe.params.v2.billing._profile_list_params import (
        ProfileListParams as ProfileListParams,
    )
    from stripe.params.v2.billing._profile_retrieve_params import (
        ProfileRetrieveParams as ProfileRetrieveParams,
    )
    from stripe.params.v2.billing._profile_update_params import (
        ProfileUpdateParams as ProfileUpdateParams,
    )
    from stripe.params.v2.billing._rate_card_create_params import (
        RateCardCreateParams as RateCardCreateParams,
    )
    from stripe.params.v2.billing._rate_card_list_params import (
        RateCardListParams as RateCardListParams,
    )
    from stripe.params.v2.billing._rate_card_modify_rates_params import (
        RateCardModifyRatesParams as RateCardModifyRatesParams,
        RateCardModifyRatesParamsRatesToCreate as RateCardModifyRatesParamsRatesToCreate,
        RateCardModifyRatesParamsRatesToCreateMeteredItemData as RateCardModifyRatesParamsRatesToCreateMeteredItemData,
        RateCardModifyRatesParamsRatesToCreateMeteredItemDataMeterSegmentCondition as RateCardModifyRatesParamsRatesToCreateMeteredItemDataMeterSegmentCondition,
        RateCardModifyRatesParamsRatesToCreateTier as RateCardModifyRatesParamsRatesToCreateTier,
        RateCardModifyRatesParamsRatesToCreateTransformQuantity as RateCardModifyRatesParamsRatesToCreateTransformQuantity,
        RateCardModifyRatesParamsRatesToDelete as RateCardModifyRatesParamsRatesToDelete,
    )
    from stripe.params.v2.billing._rate_card_retrieve_params import (
        RateCardRetrieveParams as RateCardRetrieveParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_cancel_params import (
        RateCardSubscriptionCancelParams as RateCardSubscriptionCancelParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_create_params import (
        RateCardSubscriptionCreateParams as RateCardSubscriptionCreateParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_list_params import (
        RateCardSubscriptionListParams as RateCardSubscriptionListParams,
        RateCardSubscriptionListParamsPayer as RateCardSubscriptionListParamsPayer,
    )
    from stripe.params.v2.billing._rate_card_subscription_retrieve_params import (
        RateCardSubscriptionRetrieveParams as RateCardSubscriptionRetrieveParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_update_params import (
        RateCardSubscriptionUpdateParams as RateCardSubscriptionUpdateParams,
    )
    from stripe.params.v2.billing._rate_card_update_params import (
        RateCardUpdateParams as RateCardUpdateParams,
    )
    from stripe.params.v2.billing._service_action_create_params import (
        ServiceActionCreateParams as ServiceActionCreateParams,
        ServiceActionCreateParamsCreditGrant as ServiceActionCreateParamsCreditGrant,
        ServiceActionCreateParamsCreditGrantAmount as ServiceActionCreateParamsCreditGrantAmount,
        ServiceActionCreateParamsCreditGrantAmountCustomPricingUnit as ServiceActionCreateParamsCreditGrantAmountCustomPricingUnit,
        ServiceActionCreateParamsCreditGrantApplicabilityConfig as ServiceActionCreateParamsCreditGrantApplicabilityConfig,
        ServiceActionCreateParamsCreditGrantApplicabilityConfigScope as ServiceActionCreateParamsCreditGrantApplicabilityConfigScope,
        ServiceActionCreateParamsCreditGrantExpiryConfig as ServiceActionCreateParamsCreditGrantExpiryConfig,
        ServiceActionCreateParamsCreditGrantPerTenant as ServiceActionCreateParamsCreditGrantPerTenant,
        ServiceActionCreateParamsCreditGrantPerTenantAmount as ServiceActionCreateParamsCreditGrantPerTenantAmount,
        ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit as ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit,
        ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfig as ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfig,
        ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfigScope as ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfigScope,
        ServiceActionCreateParamsCreditGrantPerTenantExpiryConfig as ServiceActionCreateParamsCreditGrantPerTenantExpiryConfig,
        ServiceActionCreateParamsCreditGrantPerTenantGrantCondition as ServiceActionCreateParamsCreditGrantPerTenantGrantCondition,
        ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod as ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod,
        ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition as ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition,
        ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension as ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension,
    )
    from stripe.params.v2.billing._service_action_retrieve_params import (
        ServiceActionRetrieveParams as ServiceActionRetrieveParams,
    )
    from stripe.params.v2.billing._service_action_update_params import (
        ServiceActionUpdateParams as ServiceActionUpdateParams,
        ServiceActionUpdateParamsCreditGrant as ServiceActionUpdateParamsCreditGrant,
        ServiceActionUpdateParamsCreditGrantPerTenant as ServiceActionUpdateParamsCreditGrantPerTenant,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "bill_settings": ("stripe.params.v2.billing.bill_settings", True),
    "collection_settings": (
        "stripe.params.v2.billing.collection_settings",
        True,
    ),
    "contracts": ("stripe.params.v2.billing.contracts", True),
    "groups": ("stripe.params.v2.billing.groups", True),
    "intents": ("stripe.params.v2.billing.intents", True),
    "license_fees": ("stripe.params.v2.billing.license_fees", True),
    "pricing_plans": ("stripe.params.v2.billing.pricing_plans", True),
    "rate_cards": ("stripe.params.v2.billing.rate_cards", True),
    "BillSettingCreateParams": (
        "stripe.params.v2.billing._bill_setting_create_params",
        False,
    ),
    "BillSettingCreateParamsCalculation": (
        "stripe.params.v2.billing._bill_setting_create_params",
        False,
    ),
    "BillSettingCreateParamsCalculationTax": (
        "stripe.params.v2.billing._bill_setting_create_params",
        False,
    ),
    "BillSettingCreateParamsInvoice": (
        "stripe.params.v2.billing._bill_setting_create_params",
        False,
    ),
    "BillSettingCreateParamsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._bill_setting_create_params",
        False,
    ),
    "BillSettingListParams": (
        "stripe.params.v2.billing._bill_setting_list_params",
        False,
    ),
    "BillSettingRetrieveParams": (
        "stripe.params.v2.billing._bill_setting_retrieve_params",
        False,
    ),
    "BillSettingUpdateParams": (
        "stripe.params.v2.billing._bill_setting_update_params",
        False,
    ),
    "BillSettingUpdateParamsCalculation": (
        "stripe.params.v2.billing._bill_setting_update_params",
        False,
    ),
    "BillSettingUpdateParamsCalculationTax": (
        "stripe.params.v2.billing._bill_setting_update_params",
        False,
    ),
    "BillSettingUpdateParamsInvoice": (
        "stripe.params.v2.billing._bill_setting_update_params",
        False,
    ),
    "BillSettingUpdateParamsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._bill_setting_update_params",
        False,
    ),
    "CollectionSettingCreateParams": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsEmailDelivery": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsEmailDeliveryPaymentDue": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptions": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsAcssDebit": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsBancontact": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsCard": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsCardMandateOptions": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsKonbini": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsSepaDebit": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters": (
        "stripe.params.v2.billing._collection_setting_create_params",
        False,
    ),
    "CollectionSettingListParams": (
        "stripe.params.v2.billing._collection_setting_list_params",
        False,
    ),
    "CollectionSettingRetrieveParams": (
        "stripe.params.v2.billing._collection_setting_retrieve_params",
        False,
    ),
    "CollectionSettingUpdateParams": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsEmailDelivery": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsEmailDeliveryPaymentDue": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptions": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebit": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsBancontact": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsCard": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsCardMandateOptions": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsKonbini": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsSepaDebit": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters": (
        "stripe.params.v2.billing._collection_setting_update_params",
        False,
    ),
    "ContractActivateParams": (
        "stripe.params.v2.billing._contract_activate_params",
        False,
    ),
    "ContractCancelParams": (
        "stripe.params.v2.billing._contract_cancel_params",
        False,
    ),
    "ContractCancelParamsTerm": (
        "stripe.params.v2.billing._contract_cancel_params",
        False,
    ),
    "ContractCancelParamsTermTerm": (
        "stripe.params.v2.billing._contract_cancel_params",
        False,
    ),
    "ContractCreateParams": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingCycleAnchor": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingCycleAnchorConfig": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettings": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillSettingsDetails": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillSettingsDetailsCalculation": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillSettingsDetailsCalculationTax": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillSettingsDetailsInvoice": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsBillingProfileDetails": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsBillingSettingsCollectionSettingsDetails": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTerm": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverride": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideCriterion": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideCriterionTerm": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideEndsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideMultiply": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideOverwrite": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermPricingOverrideStartsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermRecurringPrice": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermRecurringPriceEndsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermRecurringPriceStartsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFee": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeBillSchedule": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeBillScheduleCustom": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeBillScheduleCustomBillAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeServicePeriod": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeServicePeriodEndsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractCreateParamsTermScheduledFeeServicePeriodStartsAt": (
        "stripe.params.v2.billing._contract_create_params",
        False,
    ),
    "ContractDeleteParams": (
        "stripe.params.v2.billing._contract_delete_params",
        False,
    ),
    "ContractListParams": (
        "stripe.params.v2.billing._contract_list_params",
        False,
    ),
    "ContractRetrieveParams": (
        "stripe.params.v2.billing._contract_retrieve_params",
        False,
    ),
    "ContractUpdateParams": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsAction": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverride": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideCriterion": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideCriterionTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideMultiply": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideOverwrite": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermPricingOverrideStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermRecurringPrice": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermRecurringPriceEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermRecurringPriceStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFee": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeBillSchedule": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustom": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeBillScheduleCustomBillAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeServicePeriod": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeServicePeriodEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionAddTermScheduledFeeServicePeriodStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionRemoveTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionRemoveTermTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermPricingOverride": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermPricingOverrideEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermPricingOverrideStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermRecurringPrice": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermRecurringPriceEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermRecurringPriceStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFee": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeBillSchedule": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustom": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeBillScheduleCustomBillAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriod": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodEndsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermScheduledFeeServicePeriodStartsAt": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsActionUpdateTermTerm": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettings": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillSettingsDetails": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculation": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillSettingsDetailsCalculationTax": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoice": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillSettingsDetailsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsBillingProfileDetails": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "ContractUpdateParamsBillingSettingsCollectionSettingsDetails": (
        "stripe.params.v2.billing._contract_update_params",
        False,
    ),
    "CustomPricingUnitCreateParams": (
        "stripe.params.v2.billing._custom_pricing_unit_create_params",
        False,
    ),
    "CustomPricingUnitListParams": (
        "stripe.params.v2.billing._custom_pricing_unit_list_params",
        False,
    ),
    "CustomPricingUnitRetrieveParams": (
        "stripe.params.v2.billing._custom_pricing_unit_retrieve_params",
        False,
    ),
    "CustomPricingUnitUpdateParams": (
        "stripe.params.v2.billing._custom_pricing_unit_update_params",
        False,
    ),
    "GroupCancelParams": (
        "stripe.params.v2.billing._group_cancel_params",
        False,
    ),
    "GroupCreateParams": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettings": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsEmailDelivery": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsEmailDeliveryPaymentDue": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsInvoicePresentation": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptions": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebit": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsBancontact": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsCard": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsKonbini": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsSepaDebit": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsBillingSettingsTax": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehavior": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadence": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceDay": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceDayTime": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceMonth": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceMonthTime": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceWeek": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceWeekTime": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceYear": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupCreateParamsGroupingBehaviorByCadenceYearTime": (
        "stripe.params.v2.billing._group_create_params",
        False,
    ),
    "GroupListParams": ("stripe.params.v2.billing._group_list_params", False),
    "GroupRetrieveParams": (
        "stripe.params.v2.billing._group_retrieve_params",
        False,
    ),
    "GroupUpdateParams": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettings": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsEmailDelivery": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsEmailDeliveryPaymentDue": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsInvoicePresentation": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptions": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebit": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsBancontact": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCard": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsKonbini": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsSepaDebit": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "GroupUpdateParamsBillingSettingsTax": (
        "stripe.params.v2.billing._group_update_params",
        False,
    ),
    "IntentCancelParams": (
        "stripe.params.v2.billing._intent_cancel_params",
        False,
    ),
    "IntentCommitParams": (
        "stripe.params.v2.billing._intent_commit_params",
        False,
    ),
    "IntentCreateParams": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsAction": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApply": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplyDiscount": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplyEffectiveAt": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplyInvoiceDiscountRule": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplySpendModifierRule": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpend": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmount": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendCustomPricingUnitOverageRate": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivate": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivateCancellationDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivateEffectiveAt": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverrides": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModify": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyEffectiveAt": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverrides": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionModifyPricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionRemove": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionRemoveEffectiveAt": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribe": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribeEffectiveAt": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorRecurringCreditGrant": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribeV1SubscriptionDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupData": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettings": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsEmailDelivery": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsEmailDeliveryPaymentDue": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsInvoicePresentation": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsInvoiceTimeUntilDue": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptions": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebit": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsBancontact": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCard": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCardMandateOptions": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsKonbini": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsSepaDebit": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataBillingSettingsTax": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehavior": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadence": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDay": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceDayTime": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonth": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceMonthTime": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeek": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceWeekTime": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYear": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsBillingGroupDataGroupingBehaviorByCadenceYearTime": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentListParams": (
        "stripe.params.v2.billing._intent_list_params",
        False,
    ),
    "IntentReleaseReservationParams": (
        "stripe.params.v2.billing._intent_release_reservation_params",
        False,
    ),
    "IntentReserveParams": (
        "stripe.params.v2.billing._intent_reserve_params",
        False,
    ),
    "IntentRetrieveParams": (
        "stripe.params.v2.billing._intent_retrieve_params",
        False,
    ),
    "LicenseFeeCreateParams": (
        "stripe.params.v2.billing._license_fee_create_params",
        False,
    ),
    "LicenseFeeCreateParamsTier": (
        "stripe.params.v2.billing._license_fee_create_params",
        False,
    ),
    "LicenseFeeCreateParamsTransformQuantity": (
        "stripe.params.v2.billing._license_fee_create_params",
        False,
    ),
    "LicenseFeeListParams": (
        "stripe.params.v2.billing._license_fee_list_params",
        False,
    ),
    "LicenseFeeRetrieveParams": (
        "stripe.params.v2.billing._license_fee_retrieve_params",
        False,
    ),
    "LicenseFeeUpdateParams": (
        "stripe.params.v2.billing._license_fee_update_params",
        False,
    ),
    "LicenseFeeUpdateParamsTier": (
        "stripe.params.v2.billing._license_fee_update_params",
        False,
    ),
    "LicenseFeeUpdateParamsTransformQuantity": (
        "stripe.params.v2.billing._license_fee_update_params",
        False,
    ),
    "LicensedItemCreateParams": (
        "stripe.params.v2.billing._licensed_item_create_params",
        False,
    ),
    "LicensedItemCreateParamsTaxDetails": (
        "stripe.params.v2.billing._licensed_item_create_params",
        False,
    ),
    "LicensedItemListParams": (
        "stripe.params.v2.billing._licensed_item_list_params",
        False,
    ),
    "LicensedItemRetrieveParams": (
        "stripe.params.v2.billing._licensed_item_retrieve_params",
        False,
    ),
    "LicensedItemUpdateParams": (
        "stripe.params.v2.billing._licensed_item_update_params",
        False,
    ),
    "LicensedItemUpdateParamsTaxDetails": (
        "stripe.params.v2.billing._licensed_item_update_params",
        False,
    ),
    "MeterEventAdjustmentCreateParams": (
        "stripe.params.v2.billing._meter_event_adjustment_create_params",
        False,
    ),
    "MeterEventAdjustmentCreateParamsCancel": (
        "stripe.params.v2.billing._meter_event_adjustment_create_params",
        False,
    ),
    "MeterEventCreateParams": (
        "stripe.params.v2.billing._meter_event_create_params",
        False,
    ),
    "MeterEventSessionCreateParams": (
        "stripe.params.v2.billing._meter_event_session_create_params",
        False,
    ),
    "MeterEventStreamCreateParams": (
        "stripe.params.v2.billing._meter_event_stream_create_params",
        False,
    ),
    "MeterEventStreamCreateParamsEvent": (
        "stripe.params.v2.billing._meter_event_stream_create_params",
        False,
    ),
    "MeteredItemCreateParams": (
        "stripe.params.v2.billing._metered_item_create_params",
        False,
    ),
    "MeteredItemCreateParamsMeterSegmentCondition": (
        "stripe.params.v2.billing._metered_item_create_params",
        False,
    ),
    "MeteredItemCreateParamsTaxDetails": (
        "stripe.params.v2.billing._metered_item_create_params",
        False,
    ),
    "MeteredItemListParams": (
        "stripe.params.v2.billing._metered_item_list_params",
        False,
    ),
    "MeteredItemRetrieveParams": (
        "stripe.params.v2.billing._metered_item_retrieve_params",
        False,
    ),
    "MeteredItemUpdateParams": (
        "stripe.params.v2.billing._metered_item_update_params",
        False,
    ),
    "MeteredItemUpdateParamsTaxDetails": (
        "stripe.params.v2.billing._metered_item_update_params",
        False,
    ),
    "OneTimeItemCreateParams": (
        "stripe.params.v2.billing._one_time_item_create_params",
        False,
    ),
    "OneTimeItemCreateParamsTaxDetails": (
        "stripe.params.v2.billing._one_time_item_create_params",
        False,
    ),
    "OneTimeItemListParams": (
        "stripe.params.v2.billing._one_time_item_list_params",
        False,
    ),
    "OneTimeItemRetrieveParams": (
        "stripe.params.v2.billing._one_time_item_retrieve_params",
        False,
    ),
    "OneTimeItemUpdateParams": (
        "stripe.params.v2.billing._one_time_item_update_params",
        False,
    ),
    "OneTimeItemUpdateParamsTaxDetails": (
        "stripe.params.v2.billing._one_time_item_update_params",
        False,
    ),
    "PricingPlanCreateParams": (
        "stripe.params.v2.billing._pricing_plan_create_params",
        False,
    ),
    "PricingPlanListParams": (
        "stripe.params.v2.billing._pricing_plan_list_params",
        False,
    ),
    "PricingPlanRetrieveParams": (
        "stripe.params.v2.billing._pricing_plan_retrieve_params",
        False,
    ),
    "PricingPlanSubscriptionListParams": (
        "stripe.params.v2.billing._pricing_plan_subscription_list_params",
        False,
    ),
    "PricingPlanSubscriptionListParamsPayer": (
        "stripe.params.v2.billing._pricing_plan_subscription_list_params",
        False,
    ),
    "PricingPlanSubscriptionRemoveDiscountsParams": (
        "stripe.params.v2.billing._pricing_plan_subscription_remove_discounts_params",
        False,
    ),
    "PricingPlanSubscriptionRetrieveParams": (
        "stripe.params.v2.billing._pricing_plan_subscription_retrieve_params",
        False,
    ),
    "PricingPlanSubscriptionUpdateParams": (
        "stripe.params.v2.billing._pricing_plan_subscription_update_params",
        False,
    ),
    "PricingPlanUpdateParams": (
        "stripe.params.v2.billing._pricing_plan_update_params",
        False,
    ),
    "ProfileCreateParams": (
        "stripe.params.v2.billing._profile_create_params",
        False,
    ),
    "ProfileListParams": (
        "stripe.params.v2.billing._profile_list_params",
        False,
    ),
    "ProfileRetrieveParams": (
        "stripe.params.v2.billing._profile_retrieve_params",
        False,
    ),
    "ProfileUpdateParams": (
        "stripe.params.v2.billing._profile_update_params",
        False,
    ),
    "RateCardCreateParams": (
        "stripe.params.v2.billing._rate_card_create_params",
        False,
    ),
    "RateCardListParams": (
        "stripe.params.v2.billing._rate_card_list_params",
        False,
    ),
    "RateCardModifyRatesParams": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToCreate": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToCreateMeteredItemData": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToCreateMeteredItemDataMeterSegmentCondition": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToCreateTier": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToCreateTransformQuantity": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardModifyRatesParamsRatesToDelete": (
        "stripe.params.v2.billing._rate_card_modify_rates_params",
        False,
    ),
    "RateCardRetrieveParams": (
        "stripe.params.v2.billing._rate_card_retrieve_params",
        False,
    ),
    "RateCardSubscriptionCancelParams": (
        "stripe.params.v2.billing._rate_card_subscription_cancel_params",
        False,
    ),
    "RateCardSubscriptionCreateParams": (
        "stripe.params.v2.billing._rate_card_subscription_create_params",
        False,
    ),
    "RateCardSubscriptionListParams": (
        "stripe.params.v2.billing._rate_card_subscription_list_params",
        False,
    ),
    "RateCardSubscriptionListParamsPayer": (
        "stripe.params.v2.billing._rate_card_subscription_list_params",
        False,
    ),
    "RateCardSubscriptionRetrieveParams": (
        "stripe.params.v2.billing._rate_card_subscription_retrieve_params",
        False,
    ),
    "RateCardSubscriptionUpdateParams": (
        "stripe.params.v2.billing._rate_card_subscription_update_params",
        False,
    ),
    "RateCardUpdateParams": (
        "stripe.params.v2.billing._rate_card_update_params",
        False,
    ),
    "ServiceActionCreateParams": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrant": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantAmount": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantAmountCustomPricingUnit": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantApplicabilityConfig": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantApplicabilityConfigScope": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantExpiryConfig": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenant": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantAmount": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfig": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantApplicabilityConfigScope": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantExpiryConfig": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantGrantCondition": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionCreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension": (
        "stripe.params.v2.billing._service_action_create_params",
        False,
    ),
    "ServiceActionRetrieveParams": (
        "stripe.params.v2.billing._service_action_retrieve_params",
        False,
    ),
    "ServiceActionUpdateParams": (
        "stripe.params.v2.billing._service_action_update_params",
        False,
    ),
    "ServiceActionUpdateParamsCreditGrant": (
        "stripe.params.v2.billing._service_action_update_params",
        False,
    ),
    "ServiceActionUpdateParamsCreditGrantPerTenant": (
        "stripe.params.v2.billing._service_action_update_params",
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
