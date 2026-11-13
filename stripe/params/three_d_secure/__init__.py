# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.three_d_secure._authentication_cancel_params import (
        AuthenticationCancelParams as AuthenticationCancelParams,
    )
    from stripe.params.three_d_secure._authentication_create_params import (
        AuthenticationCreateParams as AuthenticationCreateParams,
        AuthenticationCreateParamsAcquirerDetails as AuthenticationCreateParamsAcquirerDetails,
        AuthenticationCreateParamsChannel as AuthenticationCreateParamsChannel,
        AuthenticationCreateParamsChannelBrowser as AuthenticationCreateParamsChannelBrowser,
        AuthenticationCreateParamsChannelThreeRI as AuthenticationCreateParamsChannelThreeRI,
        AuthenticationCreateParamsFlowPreference as AuthenticationCreateParamsFlowPreference,
        AuthenticationCreateParamsFlowPreferenceChallenge as AuthenticationCreateParamsFlowPreferenceChallenge,
        AuthenticationCreateParamsFlowPreferenceDataShare as AuthenticationCreateParamsFlowPreferenceDataShare,
        AuthenticationCreateParamsFlowPreferenceFrictionless as AuthenticationCreateParamsFlowPreferenceFrictionless,
        AuthenticationCreateParamsFutureUsage as AuthenticationCreateParamsFutureUsage,
        AuthenticationCreateParamsFutureUsageInstallment as AuthenticationCreateParamsFutureUsageInstallment,
        AuthenticationCreateParamsFutureUsageInstallmentExpiry as AuthenticationCreateParamsFutureUsageInstallmentExpiry,
        AuthenticationCreateParamsFutureUsageRecurring as AuthenticationCreateParamsFutureUsageRecurring,
        AuthenticationCreateParamsFutureUsageRecurringExpiry as AuthenticationCreateParamsFutureUsageRecurringExpiry,
        AuthenticationCreateParamsPaymentMethodData as AuthenticationCreateParamsPaymentMethodData,
        AuthenticationCreateParamsPaymentMethodDataBillingDetails as AuthenticationCreateParamsPaymentMethodDataBillingDetails,
        AuthenticationCreateParamsPaymentMethodDataBillingDetailsAddress as AuthenticationCreateParamsPaymentMethodDataBillingDetailsAddress,
        AuthenticationCreateParamsPaymentMethodDataCard as AuthenticationCreateParamsPaymentMethodDataCard,
        AuthenticationCreateParamsShippingAddress as AuthenticationCreateParamsShippingAddress,
    )
    from stripe.params.three_d_secure._authentication_list_params import (
        AuthenticationListParams as AuthenticationListParams,
        AuthenticationListParamsCreated as AuthenticationListParamsCreated,
    )
    from stripe.params.three_d_secure._authentication_retrieve_params import (
        AuthenticationRetrieveParams as AuthenticationRetrieveParams,
    )
    from stripe.params.three_d_secure._authentication_submit_params import (
        AuthenticationSubmitParams as AuthenticationSubmitParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AuthenticationCancelParams": (
        "stripe.params.three_d_secure._authentication_cancel_params",
        False,
    ),
    "AuthenticationCreateParams": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsAcquirerDetails": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsChannel": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsChannelBrowser": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsChannelThreeRI": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFlowPreference": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFlowPreferenceChallenge": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFlowPreferenceDataShare": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFlowPreferenceFrictionless": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFutureUsage": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFutureUsageInstallment": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFutureUsageInstallmentExpiry": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFutureUsageRecurring": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsFutureUsageRecurringExpiry": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsPaymentMethodData": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsPaymentMethodDataBillingDetails": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsPaymentMethodDataBillingDetailsAddress": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsPaymentMethodDataCard": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationCreateParamsShippingAddress": (
        "stripe.params.three_d_secure._authentication_create_params",
        False,
    ),
    "AuthenticationListParams": (
        "stripe.params.three_d_secure._authentication_list_params",
        False,
    ),
    "AuthenticationListParamsCreated": (
        "stripe.params.three_d_secure._authentication_list_params",
        False,
    ),
    "AuthenticationRetrieveParams": (
        "stripe.params.three_d_secure._authentication_retrieve_params",
        False,
    ),
    "AuthenticationSubmitParams": (
        "stripe.params.three_d_secure._authentication_submit_params",
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
