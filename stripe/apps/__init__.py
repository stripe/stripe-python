# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.apps._secret import Secret as Secret
    from stripe.apps._secret_service import SecretService as SecretService

_submodules = {
    "Secret": "stripe.apps._secret",
    "SecretService": "stripe.apps._secret_service",
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
