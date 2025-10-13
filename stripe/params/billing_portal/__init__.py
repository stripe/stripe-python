# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.billing_portal._configuration_create_params import (
        ConfigurationCreateParams as ConfigurationCreateParams,
        ConfigurationCreateParamsBusinessProfile as ConfigurationCreateParamsBusinessProfile,
        ConfigurationCreateParamsFeatures as ConfigurationCreateParamsFeatures,
        ConfigurationCreateParamsFeaturesCustomerUpdate as ConfigurationCreateParamsFeaturesCustomerUpdate,
        ConfigurationCreateParamsFeaturesInvoiceHistory as ConfigurationCreateParamsFeaturesInvoiceHistory,
        ConfigurationCreateParamsFeaturesPaymentMethodUpdate as ConfigurationCreateParamsFeaturesPaymentMethodUpdate,
        ConfigurationCreateParamsFeaturesSubscriptionCancel as ConfigurationCreateParamsFeaturesSubscriptionCancel,
        ConfigurationCreateParamsFeaturesSubscriptionCancelCancellationReason as ConfigurationCreateParamsFeaturesSubscriptionCancelCancellationReason,
        ConfigurationCreateParamsFeaturesSubscriptionUpdate as ConfigurationCreateParamsFeaturesSubscriptionUpdate,
        ConfigurationCreateParamsFeaturesSubscriptionUpdateProduct as ConfigurationCreateParamsFeaturesSubscriptionUpdateProduct,
        ConfigurationCreateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity as ConfigurationCreateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity,
        ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd as ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
        ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition as ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition,
        ConfigurationCreateParamsLoginPage as ConfigurationCreateParamsLoginPage,
    )
    from stripe.params.billing_portal._configuration_list_params import (
        ConfigurationListParams as ConfigurationListParams,
    )
    from stripe.params.billing_portal._configuration_modify_params import (
        ConfigurationModifyParams as ConfigurationModifyParams,
        ConfigurationModifyParamsBusinessProfile as ConfigurationModifyParamsBusinessProfile,
        ConfigurationModifyParamsFeatures as ConfigurationModifyParamsFeatures,
        ConfigurationModifyParamsFeaturesCustomerUpdate as ConfigurationModifyParamsFeaturesCustomerUpdate,
        ConfigurationModifyParamsFeaturesInvoiceHistory as ConfigurationModifyParamsFeaturesInvoiceHistory,
        ConfigurationModifyParamsFeaturesPaymentMethodUpdate as ConfigurationModifyParamsFeaturesPaymentMethodUpdate,
        ConfigurationModifyParamsFeaturesSubscriptionCancel as ConfigurationModifyParamsFeaturesSubscriptionCancel,
        ConfigurationModifyParamsFeaturesSubscriptionCancelCancellationReason as ConfigurationModifyParamsFeaturesSubscriptionCancelCancellationReason,
        ConfigurationModifyParamsFeaturesSubscriptionUpdate as ConfigurationModifyParamsFeaturesSubscriptionUpdate,
        ConfigurationModifyParamsFeaturesSubscriptionUpdateProduct as ConfigurationModifyParamsFeaturesSubscriptionUpdateProduct,
        ConfigurationModifyParamsFeaturesSubscriptionUpdateProductAdjustableQuantity as ConfigurationModifyParamsFeaturesSubscriptionUpdateProductAdjustableQuantity,
        ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd as ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
        ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition as ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition,
        ConfigurationModifyParamsLoginPage as ConfigurationModifyParamsLoginPage,
    )
    from stripe.params.billing_portal._configuration_retrieve_params import (
        ConfigurationRetrieveParams as ConfigurationRetrieveParams,
    )
    from stripe.params.billing_portal._configuration_update_params import (
        ConfigurationUpdateParams as ConfigurationUpdateParams,
        ConfigurationUpdateParamsBusinessProfile as ConfigurationUpdateParamsBusinessProfile,
        ConfigurationUpdateParamsFeatures as ConfigurationUpdateParamsFeatures,
        ConfigurationUpdateParamsFeaturesCustomerUpdate as ConfigurationUpdateParamsFeaturesCustomerUpdate,
        ConfigurationUpdateParamsFeaturesInvoiceHistory as ConfigurationUpdateParamsFeaturesInvoiceHistory,
        ConfigurationUpdateParamsFeaturesPaymentMethodUpdate as ConfigurationUpdateParamsFeaturesPaymentMethodUpdate,
        ConfigurationUpdateParamsFeaturesSubscriptionCancel as ConfigurationUpdateParamsFeaturesSubscriptionCancel,
        ConfigurationUpdateParamsFeaturesSubscriptionCancelCancellationReason as ConfigurationUpdateParamsFeaturesSubscriptionCancelCancellationReason,
        ConfigurationUpdateParamsFeaturesSubscriptionUpdate as ConfigurationUpdateParamsFeaturesSubscriptionUpdate,
        ConfigurationUpdateParamsFeaturesSubscriptionUpdateProduct as ConfigurationUpdateParamsFeaturesSubscriptionUpdateProduct,
        ConfigurationUpdateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity as ConfigurationUpdateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity,
        ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd as ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
        ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition as ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition,
        ConfigurationUpdateParamsLoginPage as ConfigurationUpdateParamsLoginPage,
    )
    from stripe.params.billing_portal._session_create_params import (
        SessionCreateParams as SessionCreateParams,
        SessionCreateParamsFlowData as SessionCreateParamsFlowData,
        SessionCreateParamsFlowDataAfterCompletion as SessionCreateParamsFlowDataAfterCompletion,
        SessionCreateParamsFlowDataAfterCompletionHostedConfirmation as SessionCreateParamsFlowDataAfterCompletionHostedConfirmation,
        SessionCreateParamsFlowDataAfterCompletionRedirect as SessionCreateParamsFlowDataAfterCompletionRedirect,
        SessionCreateParamsFlowDataSubscriptionCancel as SessionCreateParamsFlowDataSubscriptionCancel,
        SessionCreateParamsFlowDataSubscriptionCancelRetention as SessionCreateParamsFlowDataSubscriptionCancelRetention,
        SessionCreateParamsFlowDataSubscriptionCancelRetentionCouponOffer as SessionCreateParamsFlowDataSubscriptionCancelRetentionCouponOffer,
        SessionCreateParamsFlowDataSubscriptionUpdate as SessionCreateParamsFlowDataSubscriptionUpdate,
        SessionCreateParamsFlowDataSubscriptionUpdateConfirm as SessionCreateParamsFlowDataSubscriptionUpdateConfirm,
        SessionCreateParamsFlowDataSubscriptionUpdateConfirmDiscount as SessionCreateParamsFlowDataSubscriptionUpdateConfirmDiscount,
        SessionCreateParamsFlowDataSubscriptionUpdateConfirmItem as SessionCreateParamsFlowDataSubscriptionUpdateConfirmItem,
    )

_submodules = {
    "ConfigurationCreateParams": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsBusinessProfile": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeatures": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesCustomerUpdate": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesInvoiceHistory": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesPaymentMethodUpdate": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionCancel": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionCancelCancellationReason": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionUpdate": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionUpdateProduct": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationCreateParamsLoginPage": "stripe.params.billing_portal._configuration_create_params",
    "ConfigurationListParams": "stripe.params.billing_portal._configuration_list_params",
    "ConfigurationModifyParams": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsBusinessProfile": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeatures": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesCustomerUpdate": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesInvoiceHistory": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesPaymentMethodUpdate": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionCancel": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionCancelCancellationReason": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionUpdate": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionUpdateProduct": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionUpdateProductAdjustableQuantity": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationModifyParamsLoginPage": "stripe.params.billing_portal._configuration_modify_params",
    "ConfigurationRetrieveParams": "stripe.params.billing_portal._configuration_retrieve_params",
    "ConfigurationUpdateParams": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsBusinessProfile": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeatures": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesCustomerUpdate": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesInvoiceHistory": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesPaymentMethodUpdate": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionCancel": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionCancelCancellationReason": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionUpdate": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionUpdateProduct": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionUpdateProductAdjustableQuantity": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEnd": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsFeaturesSubscriptionUpdateScheduleAtPeriodEndCondition": "stripe.params.billing_portal._configuration_update_params",
    "ConfigurationUpdateParamsLoginPage": "stripe.params.billing_portal._configuration_update_params",
    "SessionCreateParams": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowData": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataAfterCompletion": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataAfterCompletionHostedConfirmation": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataAfterCompletionRedirect": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionCancel": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionCancelRetention": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionCancelRetentionCouponOffer": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionUpdate": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionUpdateConfirm": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionUpdateConfirmDiscount": "stripe.params.billing_portal._session_create_params",
    "SessionCreateParamsFlowDataSubscriptionUpdateConfirmItem": "stripe.params.billing_portal._session_create_params",
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
