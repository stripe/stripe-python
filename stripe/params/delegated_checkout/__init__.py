# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.delegated_checkout._requested_session_confirm_params import (
        RequestedSessionConfirmParams as RequestedSessionConfirmParams,
        RequestedSessionConfirmParamsPaymentMethodData as RequestedSessionConfirmParamsPaymentMethodData,
        RequestedSessionConfirmParamsPaymentMethodDataBillingDetails as RequestedSessionConfirmParamsPaymentMethodDataBillingDetails,
        RequestedSessionConfirmParamsPaymentMethodDataBillingDetailsAddress as RequestedSessionConfirmParamsPaymentMethodDataBillingDetailsAddress,
        RequestedSessionConfirmParamsPaymentMethodDataCard as RequestedSessionConfirmParamsPaymentMethodDataCard,
        RequestedSessionConfirmParamsRiskDetails as RequestedSessionConfirmParamsRiskDetails,
        RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails as RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails,
    )
    from stripe.params.delegated_checkout._requested_session_create_params import (
        RequestedSessionCreateParams as RequestedSessionCreateParams,
        RequestedSessionCreateParamsFulfillmentDetails as RequestedSessionCreateParamsFulfillmentDetails,
        RequestedSessionCreateParamsFulfillmentDetailsAddress as RequestedSessionCreateParamsFulfillmentDetailsAddress,
        RequestedSessionCreateParamsLineItemDetail as RequestedSessionCreateParamsLineItemDetail,
        RequestedSessionCreateParamsPaymentMethodData as RequestedSessionCreateParamsPaymentMethodData,
        RequestedSessionCreateParamsPaymentMethodDataBillingDetails as RequestedSessionCreateParamsPaymentMethodDataBillingDetails,
        RequestedSessionCreateParamsPaymentMethodDataBillingDetailsAddress as RequestedSessionCreateParamsPaymentMethodDataBillingDetailsAddress,
        RequestedSessionCreateParamsPaymentMethodDataCard as RequestedSessionCreateParamsPaymentMethodDataCard,
        RequestedSessionCreateParamsSellerDetails as RequestedSessionCreateParamsSellerDetails,
    )
    from stripe.params.delegated_checkout._requested_session_expire_params import (
        RequestedSessionExpireParams as RequestedSessionExpireParams,
    )
    from stripe.params.delegated_checkout._requested_session_modify_params import (
        RequestedSessionModifyParams as RequestedSessionModifyParams,
        RequestedSessionModifyParamsFulfillmentDetails as RequestedSessionModifyParamsFulfillmentDetails,
        RequestedSessionModifyParamsFulfillmentDetailsAddress as RequestedSessionModifyParamsFulfillmentDetailsAddress,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOption as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOption,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping,
        RequestedSessionModifyParamsLineItemDetail as RequestedSessionModifyParamsLineItemDetail,
        RequestedSessionModifyParamsPaymentMethodData as RequestedSessionModifyParamsPaymentMethodData,
        RequestedSessionModifyParamsPaymentMethodDataBillingDetails as RequestedSessionModifyParamsPaymentMethodDataBillingDetails,
        RequestedSessionModifyParamsPaymentMethodDataBillingDetailsAddress as RequestedSessionModifyParamsPaymentMethodDataBillingDetailsAddress,
        RequestedSessionModifyParamsPaymentMethodDataCard as RequestedSessionModifyParamsPaymentMethodDataCard,
    )
    from stripe.params.delegated_checkout._requested_session_retrieve_params import (
        RequestedSessionRetrieveParams as RequestedSessionRetrieveParams,
    )
    from stripe.params.delegated_checkout._requested_session_update_params import (
        RequestedSessionUpdateParams as RequestedSessionUpdateParams,
        RequestedSessionUpdateParamsFulfillmentDetails as RequestedSessionUpdateParamsFulfillmentDetails,
        RequestedSessionUpdateParamsFulfillmentDetailsAddress as RequestedSessionUpdateParamsFulfillmentDetailsAddress,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping,
        RequestedSessionUpdateParamsLineItemDetail as RequestedSessionUpdateParamsLineItemDetail,
        RequestedSessionUpdateParamsPaymentMethodData as RequestedSessionUpdateParamsPaymentMethodData,
        RequestedSessionUpdateParamsPaymentMethodDataBillingDetails as RequestedSessionUpdateParamsPaymentMethodDataBillingDetails,
        RequestedSessionUpdateParamsPaymentMethodDataBillingDetailsAddress as RequestedSessionUpdateParamsPaymentMethodDataBillingDetailsAddress,
        RequestedSessionUpdateParamsPaymentMethodDataCard as RequestedSessionUpdateParamsPaymentMethodDataCard,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RequestedSessionConfirmParams": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsPaymentMethodData": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsPaymentMethodDataBillingDetails": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsPaymentMethodDataCard": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsRiskDetails": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionCreateParams": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsFulfillmentDetails": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsFulfillmentDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsLineItemDetail": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsPaymentMethodData": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsPaymentMethodDataBillingDetails": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsPaymentMethodDataCard": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsSellerDetails": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionExpireParams": (
        "stripe.params.delegated_checkout._requested_session_expire_params",
        False,
    ),
    "RequestedSessionModifyParams": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetails": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOption": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsLineItemDetail": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsPaymentMethodData": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsPaymentMethodDataBillingDetails": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsPaymentMethodDataCard": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionRetrieveParams": (
        "stripe.params.delegated_checkout._requested_session_retrieve_params",
        False,
    ),
    "RequestedSessionUpdateParams": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetails": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsLineItemDetail": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsPaymentMethodData": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsPaymentMethodDataBillingDetails": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsPaymentMethodDataCard": (
        "stripe.params.delegated_checkout._requested_session_update_params",
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
