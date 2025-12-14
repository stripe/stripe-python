# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing import (
        bill_settings as bill_settings,
        collection_settings as collection_settings,
        intents as intents,
        license_fees as license_fees,
        pricing_plan_subscriptions as pricing_plan_subscriptions,
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
    from stripe.params.v2.billing._cadence_cancel_params import (
        CadenceCancelParams as CadenceCancelParams,
    )
    from stripe.params.v2.billing._cadence_create_params import (
        CadenceCreateParams as CadenceCreateParams,
        CadenceCreateParamsBillingCycle as CadenceCreateParamsBillingCycle,
        CadenceCreateParamsBillingCycleDay as CadenceCreateParamsBillingCycleDay,
        CadenceCreateParamsBillingCycleDayTime as CadenceCreateParamsBillingCycleDayTime,
        CadenceCreateParamsBillingCycleMonth as CadenceCreateParamsBillingCycleMonth,
        CadenceCreateParamsBillingCycleMonthTime as CadenceCreateParamsBillingCycleMonthTime,
        CadenceCreateParamsBillingCycleWeek as CadenceCreateParamsBillingCycleWeek,
        CadenceCreateParamsBillingCycleWeekTime as CadenceCreateParamsBillingCycleWeekTime,
        CadenceCreateParamsBillingCycleYear as CadenceCreateParamsBillingCycleYear,
        CadenceCreateParamsBillingCycleYearTime as CadenceCreateParamsBillingCycleYearTime,
        CadenceCreateParamsPayer as CadenceCreateParamsPayer,
        CadenceCreateParamsSettings as CadenceCreateParamsSettings,
        CadenceCreateParamsSettingsBill as CadenceCreateParamsSettingsBill,
        CadenceCreateParamsSettingsCollection as CadenceCreateParamsSettingsCollection,
    )
    from stripe.params.v2.billing._cadence_list_params import (
        CadenceListParams as CadenceListParams,
        CadenceListParamsPayer as CadenceListParamsPayer,
    )
    from stripe.params.v2.billing._cadence_retrieve_params import (
        CadenceRetrieveParams as CadenceRetrieveParams,
    )
    from stripe.params.v2.billing._cadence_update_params import (
        CadenceUpdateParams as CadenceUpdateParams,
        CadenceUpdateParamsPayer as CadenceUpdateParamsPayer,
        CadenceUpdateParamsSettings as CadenceUpdateParamsSettings,
        CadenceUpdateParamsSettingsBill as CadenceUpdateParamsSettingsBill,
        CadenceUpdateParamsSettingsCollection as CadenceUpdateParamsSettingsCollection,
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
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount,
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections,
        CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters as CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
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
        IntentCreateParamsActionApplyInvoiceDiscountRule as IntentCreateParamsActionApplyInvoiceDiscountRule,
        IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff as IntentCreateParamsActionApplyInvoiceDiscountRulePercentOff,
        IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications as IntentCreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications,
        IntentCreateParamsActionDeactivate as IntentCreateParamsActionDeactivate,
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
        IntentCreateParamsActionRemove as IntentCreateParamsActionRemove,
        IntentCreateParamsActionSubscribe as IntentCreateParamsActionSubscribe,
        IntentCreateParamsActionSubscribeEffectiveAt as IntentCreateParamsActionSubscribeEffectiveAt,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetails,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverrides,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehavior,
        IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee as IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailsOverridesPartialPeriodBehaviorLicenseFee,
        IntentCreateParamsActionSubscribeV1SubscriptionDetails as IntentCreateParamsActionSubscribeV1SubscriptionDetails,
        IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem as IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem,
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
    from stripe.params.v2.billing._license_fee_subscription_retrieve_params import (
        LicenseFeeSubscriptionRetrieveParams as LicenseFeeSubscriptionRetrieveParams,
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
        ServiceActionCreateParamsCreditGrantAmountMonetary as ServiceActionCreateParamsCreditGrantAmountMonetary,
        ServiceActionCreateParamsCreditGrantApplicabilityConfig as ServiceActionCreateParamsCreditGrantApplicabilityConfig,
        ServiceActionCreateParamsCreditGrantApplicabilityConfigScope as ServiceActionCreateParamsCreditGrantApplicabilityConfigScope,
        ServiceActionCreateParamsCreditGrantExpiryConfig as ServiceActionCreateParamsCreditGrantExpiryConfig,
        ServiceActionCreateParamsCreditGrantPerTenant as ServiceActionCreateParamsCreditGrantPerTenant,
        ServiceActionCreateParamsCreditGrantPerTenantAmount as ServiceActionCreateParamsCreditGrantPerTenantAmount,
        ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit as ServiceActionCreateParamsCreditGrantPerTenantAmountCustomPricingUnit,
        ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary as ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary,
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
    "intents": ("stripe.params.v2.billing.intents", True),
    "license_fees": ("stripe.params.v2.billing.license_fees", True),
    "pricing_plan_subscriptions": (
        "stripe.params.v2.billing.pricing_plan_subscriptions",
        True,
    ),
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
    "CadenceCancelParams": (
        "stripe.params.v2.billing._cadence_cancel_params",
        False,
    ),
    "CadenceCreateParams": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycle": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleDay": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleDayTime": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleMonth": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleMonthTime": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleWeek": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleWeekTime": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleYear": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsBillingCycleYearTime": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsPayer": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsSettings": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsSettingsBill": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceCreateParamsSettingsCollection": (
        "stripe.params.v2.billing._cadence_create_params",
        False,
    ),
    "CadenceListParams": (
        "stripe.params.v2.billing._cadence_list_params",
        False,
    ),
    "CadenceListParamsPayer": (
        "stripe.params.v2.billing._cadence_list_params",
        False,
    ),
    "CadenceRetrieveParams": (
        "stripe.params.v2.billing._cadence_retrieve_params",
        False,
    ),
    "CadenceUpdateParams": (
        "stripe.params.v2.billing._cadence_update_params",
        False,
    ),
    "CadenceUpdateParamsPayer": (
        "stripe.params.v2.billing._cadence_update_params",
        False,
    ),
    "CadenceUpdateParamsSettings": (
        "stripe.params.v2.billing._cadence_update_params",
        False,
    ),
    "CadenceUpdateParamsSettingsBill": (
        "stripe.params.v2.billing._cadence_update_params",
        False,
    ),
    "CadenceUpdateParamsSettingsCollection": (
        "stripe.params.v2.billing._cadence_update_params",
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
    "IntentCreateParamsActionDeactivate": (
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
    "IntentCreateParamsActionRemove": (
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
    "IntentCreateParamsActionSubscribeV1SubscriptionDetails": (
        "stripe.params.v2.billing._intent_create_params",
        False,
    ),
    "IntentCreateParamsActionSubscribeV1SubscriptionDetailsItem": (
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
    "LicenseFeeSubscriptionRetrieveParams": (
        "stripe.params.v2.billing._license_fee_subscription_retrieve_params",
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
    "ServiceActionCreateParamsCreditGrantAmountMonetary": (
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
    "ServiceActionCreateParamsCreditGrantPerTenantAmountMonetary": (
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
