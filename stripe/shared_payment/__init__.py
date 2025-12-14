# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.shared_payment._granted_token import (
        GrantedToken as GrantedToken,
    )
    from stripe.shared_payment._granted_token_service import (
        GrantedTokenService as GrantedTokenService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "GrantedToken": ("stripe.shared_payment._granted_token", False),
    "GrantedTokenService": (
        "stripe.shared_payment._granted_token_service",
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
