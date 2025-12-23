# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.shared_payment._granted_token_create_params import (
        GrantedTokenCreateParams as GrantedTokenCreateParams,
        GrantedTokenCreateParamsUsageLimits as GrantedTokenCreateParamsUsageLimits,
    )
    from stripe.params.shared_payment._granted_token_retrieve_params import (
        GrantedTokenRetrieveParams as GrantedTokenRetrieveParams,
    )
    from stripe.params.shared_payment._granted_token_revoke_params import (
        GrantedTokenRevokeParams as GrantedTokenRevokeParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "GrantedTokenCreateParams": (
        "stripe.params.shared_payment._granted_token_create_params",
        False,
    ),
    "GrantedTokenCreateParamsUsageLimits": (
        "stripe.params.shared_payment._granted_token_create_params",
        False,
    ),
    "GrantedTokenRetrieveParams": (
        "stripe.params.shared_payment._granted_token_retrieve_params",
        False,
    ),
    "GrantedTokenRevokeParams": (
        "stripe.params.shared_payment._granted_token_revoke_params",
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
