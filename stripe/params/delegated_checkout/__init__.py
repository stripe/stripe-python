# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.delegated_checkout._requested_session_confirm_params import (
        RequestedSessionConfirmParams as RequestedSessionConfirmParams,
    )
    from stripe.params.delegated_checkout._requested_session_create_params import (
        RequestedSessionCreateParams as RequestedSessionCreateParams,
    )
    from stripe.params.delegated_checkout._requested_session_expire_params import (
        RequestedSessionExpireParams as RequestedSessionExpireParams,
    )
    from stripe.params.delegated_checkout._requested_session_modify_params import (
        RequestedSessionModifyParams as RequestedSessionModifyParams,
    )
    from stripe.params.delegated_checkout._requested_session_retrieve_params import (
        RequestedSessionRetrieveParams as RequestedSessionRetrieveParams,
    )
    from stripe.params.delegated_checkout._requested_session_update_params import (
        RequestedSessionUpdateParams as RequestedSessionUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RequestedSessionConfirmParams": (
        "stripe.params.delegated_checkout._requested_session_confirm_params",
        False,
    ),
    "RequestedSessionCreateParams": (
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
    "RequestedSessionRetrieveParams": (
        "stripe.params.delegated_checkout._requested_session_retrieve_params",
        False,
    ),
    "RequestedSessionUpdateParams": (
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
