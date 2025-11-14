# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing import (
        bill_settings as bill_settings,
        collection_settings as collection_settings,
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

# name -> (import_target, is_submodule)
_import_map = {
    "bill_settings": ("stripe.params.v2.billing.bill_settings", True),
    "collection_settings": (
        "stripe.params.v2.billing.collection_settings",
        True,
    ),
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
