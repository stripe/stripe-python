# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.signals._account_activity_create_params import (
        AccountActivityCreateParams as AccountActivityCreateParams,
        AccountActivityCreateParamsAccountDetails as AccountActivityCreateParamsAccountDetails,
        AccountActivityCreateParamsAccountDetailsData as AccountActivityCreateParamsAccountDetailsData,
        AccountActivityCreateParamsAccountDetailsDataDefaults as AccountActivityCreateParamsAccountDetailsDataDefaults,
        AccountActivityCreateParamsAccountDetailsDataDefaultsProfile as AccountActivityCreateParamsAccountDetailsDataDefaultsProfile,
        AccountActivityCreateParamsAccountDetailsDataIdentity as AccountActivityCreateParamsAccountDetailsDataIdentity,
        AccountActivityCreateParamsAccountDetailsDataIdentityBusinessDetails as AccountActivityCreateParamsAccountDetailsDataIdentityBusinessDetails,
        AccountActivityCreateParamsAccountRestricted as AccountActivityCreateParamsAccountRestricted,
        AccountActivityCreateParamsAccountSuspended as AccountActivityCreateParamsAccountSuspended,
        AccountActivityCreateParamsLoginAttempt as AccountActivityCreateParamsLoginAttempt,
        AccountActivityCreateParamsLoginAttemptClientDetails as AccountActivityCreateParamsLoginAttemptClientDetails,
        AccountActivityCreateParamsLoginAttemptClientDetailsData as AccountActivityCreateParamsLoginAttemptClientDetailsData,
        AccountActivityCreateParamsLoginDecision as AccountActivityCreateParamsLoginDecision,
        AccountActivityCreateParamsRegistrationAttempt as AccountActivityCreateParamsRegistrationAttempt,
        AccountActivityCreateParamsRegistrationAttemptClientDetails as AccountActivityCreateParamsRegistrationAttemptClientDetails,
        AccountActivityCreateParamsRegistrationAttemptClientDetailsData as AccountActivityCreateParamsRegistrationAttemptClientDetailsData,
        AccountActivityCreateParamsRegistrationDecision as AccountActivityCreateParamsRegistrationDecision,
    )
    from stripe.params.v2.signals._account_activity_delete_params import (
        AccountActivityDeleteParams as AccountActivityDeleteParams,
    )
    from stripe.params.v2.signals._account_activity_retrieve_params import (
        AccountActivityRetrieveParams as AccountActivityRetrieveParams,
    )
    from stripe.params.v2.signals._account_evaluation_create_params import (
        AccountEvaluationCreateParams as AccountEvaluationCreateParams,
        AccountEvaluationCreateParamsAccountActivityDetails as AccountEvaluationCreateParamsAccountActivityDetails,
        AccountEvaluationCreateParamsAccountActivityDetailsData as AccountEvaluationCreateParamsAccountActivityDetailsData,
        AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt as AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt,
        AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetails as AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetails,
        AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetailsData as AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetailsData,
        AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttempt as AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttempt,
        AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetails as AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetails,
        AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetailsData as AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetailsData,
        AccountEvaluationCreateParamsAccountDetails as AccountEvaluationCreateParamsAccountDetails,
        AccountEvaluationCreateParamsAccountDetailsData as AccountEvaluationCreateParamsAccountDetailsData,
        AccountEvaluationCreateParamsAccountDetailsDataDefaults as AccountEvaluationCreateParamsAccountDetailsDataDefaults,
        AccountEvaluationCreateParamsAccountDetailsDataDefaultsProfile as AccountEvaluationCreateParamsAccountDetailsDataDefaultsProfile,
        AccountEvaluationCreateParamsAccountDetailsDataIdentity as AccountEvaluationCreateParamsAccountDetailsDataIdentity,
        AccountEvaluationCreateParamsAccountDetailsDataIdentityBusinessDetails as AccountEvaluationCreateParamsAccountDetailsDataIdentityBusinessDetails,
    )
    from stripe.params.v2.signals._account_evaluation_retrieve_params import (
        AccountEvaluationRetrieveParams as AccountEvaluationRetrieveParams,
    )
    from stripe.params.v2.signals._account_signal_list_params import (
        AccountSignalListParams as AccountSignalListParams,
        AccountSignalListParamsAccountDetails as AccountSignalListParamsAccountDetails,
    )
    from stripe.params.v2.signals._account_signal_retrieve_params import (
        AccountSignalRetrieveParams as AccountSignalRetrieveParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_cancel_params import (
        PaymentRetryEvaluationCancelParams as PaymentRetryEvaluationCancelParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_create_params import (
        PaymentRetryEvaluationCreateParams as PaymentRetryEvaluationCreateParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_retrieve_params import (
        PaymentRetryEvaluationRetrieveParams as PaymentRetryEvaluationRetrieveParams,
    )
    from stripe.params.v2.signals._payment_retry_evaluation_update_params import (
        PaymentRetryEvaluationUpdateParams as PaymentRetryEvaluationUpdateParams,
    )
    from stripe.params.v2.signals._payment_retry_signal_retrieve_params import (
        PaymentRetrySignalRetrieveParams as PaymentRetrySignalRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "AccountActivityCreateParams": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetails": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetailsData": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetailsDataDefaults": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetailsDataDefaultsProfile": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetailsDataIdentity": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountDetailsDataIdentityBusinessDetails": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountRestricted": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsAccountSuspended": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsLoginAttempt": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsLoginAttemptClientDetails": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsLoginAttemptClientDetailsData": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsLoginDecision": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsRegistrationAttempt": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsRegistrationAttemptClientDetails": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsRegistrationAttemptClientDetailsData": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityCreateParamsRegistrationDecision": (
        "stripe.params.v2.signals._account_activity_create_params",
        False,
    ),
    "AccountActivityDeleteParams": (
        "stripe.params.v2.signals._account_activity_delete_params",
        False,
    ),
    "AccountActivityRetrieveParams": (
        "stripe.params.v2.signals._account_activity_retrieve_params",
        False,
    ),
    "AccountEvaluationCreateParams": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetails": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsData": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttempt": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetails": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataLoginAttemptClientDetailsData": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttempt": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetails": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountActivityDetailsDataRegistrationAttemptClientDetailsData": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetails": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetailsData": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetailsDataDefaults": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetailsDataDefaultsProfile": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetailsDataIdentity": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationCreateParamsAccountDetailsDataIdentityBusinessDetails": (
        "stripe.params.v2.signals._account_evaluation_create_params",
        False,
    ),
    "AccountEvaluationRetrieveParams": (
        "stripe.params.v2.signals._account_evaluation_retrieve_params",
        False,
    ),
    "AccountSignalListParams": (
        "stripe.params.v2.signals._account_signal_list_params",
        False,
    ),
    "AccountSignalListParamsAccountDetails": (
        "stripe.params.v2.signals._account_signal_list_params",
        False,
    ),
    "AccountSignalRetrieveParams": (
        "stripe.params.v2.signals._account_signal_retrieve_params",
        False,
    ),
    "PaymentRetryEvaluationCancelParams": (
        "stripe.params.v2.signals._payment_retry_evaluation_cancel_params",
        False,
    ),
    "PaymentRetryEvaluationCreateParams": (
        "stripe.params.v2.signals._payment_retry_evaluation_create_params",
        False,
    ),
    "PaymentRetryEvaluationRetrieveParams": (
        "stripe.params.v2.signals._payment_retry_evaluation_retrieve_params",
        False,
    ),
    "PaymentRetryEvaluationUpdateParams": (
        "stripe.params.v2.signals._payment_retry_evaluation_update_params",
        False,
    ),
    "PaymentRetrySignalRetrieveParams": (
        "stripe.params.v2.signals._payment_retry_signal_retrieve_params",
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
