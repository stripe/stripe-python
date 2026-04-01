# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.delegated_checkout._requested_session_confirm_params import (
        RequestedSessionConfirmParams as RequestedSessionConfirmParams,
        RequestedSessionConfirmParamsAffiliateAttribution as RequestedSessionConfirmParamsAffiliateAttribution,
        RequestedSessionConfirmParamsAffiliateAttributionSource as RequestedSessionConfirmParamsAffiliateAttributionSource,
        RequestedSessionConfirmParamsRiskDetails as RequestedSessionConfirmParamsRiskDetails,
        RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails as RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails,
    )
    from stripe.params.delegated_checkout._requested_session_create_params import (
        RequestedSessionCreateParams as RequestedSessionCreateParams,
        RequestedSessionCreateParamsAffiliateAttribution as RequestedSessionCreateParamsAffiliateAttribution,
        RequestedSessionCreateParamsAffiliateAttributionSource as RequestedSessionCreateParamsAffiliateAttributionSource,
        RequestedSessionCreateParamsFulfillmentDetails as RequestedSessionCreateParamsFulfillmentDetails,
        RequestedSessionCreateParamsFulfillmentDetailsAddress as RequestedSessionCreateParamsFulfillmentDetailsAddress,
        RequestedSessionCreateParamsLineItemDetail as RequestedSessionCreateParamsLineItemDetail,
        RequestedSessionCreateParamsPaymentMethodOptions as RequestedSessionCreateParamsPaymentMethodOptions,
        RequestedSessionCreateParamsPaymentMethodOptionsCard as RequestedSessionCreateParamsPaymentMethodOptionsCard,
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
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionDigital as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionDigital,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverride as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverride,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping,
        RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping as RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionShipping,
        RequestedSessionModifyParamsLineItemDetail as RequestedSessionModifyParamsLineItemDetail,
        RequestedSessionModifyParamsPaymentMethodOptions as RequestedSessionModifyParamsPaymentMethodOptions,
        RequestedSessionModifyParamsPaymentMethodOptionsCard as RequestedSessionModifyParamsPaymentMethodOptionsCard,
    )
    from stripe.params.delegated_checkout._requested_session_retrieve_params import (
        RequestedSessionRetrieveParams as RequestedSessionRetrieveParams,
    )
    from stripe.params.delegated_checkout._requested_session_update_params import (
        RequestedSessionUpdateParams as RequestedSessionUpdateParams,
        RequestedSessionUpdateParamsFulfillmentDetails as RequestedSessionUpdateParamsFulfillmentDetails,
        RequestedSessionUpdateParamsFulfillmentDetailsAddress as RequestedSessionUpdateParamsFulfillmentDetailsAddress,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOption,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionDigital as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionDigital,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverride as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverride,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping,
        RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping as RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionShipping,
        RequestedSessionUpdateParamsLineItemDetail as RequestedSessionUpdateParamsLineItemDetail,
        RequestedSessionUpdateParamsPaymentMethodOptions as RequestedSessionUpdateParamsPaymentMethodOptions,
        RequestedSessionUpdateParamsPaymentMethodOptionsCard as RequestedSessionUpdateParamsPaymentMethodOptionsCard,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RequestedSessionConfirmParams": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsAffiliateAttribution": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionConfirmParamsAffiliateAttributionSource": (
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
    "RequestedSessionCreateParamsAffiliateAttribution": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsAffiliateAttributionSource": (
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
    "RequestedSessionCreateParamsPaymentMethodOptions": (
        "stripe.params.delegated_checkout._requested_session_create_params",
        False,
    ),
    "RequestedSessionCreateParamsPaymentMethodOptionsCard": (
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
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionDigital": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverride": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping": (
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
    "RequestedSessionModifyParamsPaymentMethodOptions": (
        "stripe.params.delegated_checkout._requested_session_modify_params",
        False,
    ),
    "RequestedSessionModifyParamsPaymentMethodOptionsCard": (
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
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionDigital": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverride": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideDigital": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsFulfillmentDetailsSelectedFulfillmentOptionOverrideShipping": (
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
    "RequestedSessionUpdateParamsPaymentMethodOptions": (
        "stripe.params.delegated_checkout._requested_session_update_params",
        False,
    ),
    "RequestedSessionUpdateParamsPaymentMethodOptionsCard": (
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
