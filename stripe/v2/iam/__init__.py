# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.iam._api_key import ApiKey as ApiKey
    from stripe.v2.iam._api_key_service import ApiKeyService as ApiKeyService

# name -> (import_target, is_submodule)
_import_map = {
    "ApiKey": ("stripe.v2.iam._api_key", False),
    "ApiKeyService": ("stripe.v2.iam._api_key_service", False),
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
