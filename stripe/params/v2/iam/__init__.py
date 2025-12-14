# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.iam._api_key_create_params import (
        ApiKeyCreateParams as ApiKeyCreateParams,
        ApiKeyCreateParamsPublicKey as ApiKeyCreateParamsPublicKey,
        ApiKeyCreateParamsPublicKeyPemKey as ApiKeyCreateParamsPublicKeyPemKey,
    )
    from stripe.params.v2.iam._api_key_expire_params import (
        ApiKeyExpireParams as ApiKeyExpireParams,
    )
    from stripe.params.v2.iam._api_key_list_params import (
        ApiKeyListParams as ApiKeyListParams,
    )
    from stripe.params.v2.iam._api_key_retrieve_params import (
        ApiKeyRetrieveParams as ApiKeyRetrieveParams,
    )
    from stripe.params.v2.iam._api_key_rotate_params import (
        ApiKeyRotateParams as ApiKeyRotateParams,
        ApiKeyRotateParamsPublicKey as ApiKeyRotateParamsPublicKey,
        ApiKeyRotateParamsPublicKeyPemKey as ApiKeyRotateParamsPublicKeyPemKey,
    )
    from stripe.params.v2.iam._api_key_update_params import (
        ApiKeyUpdateParams as ApiKeyUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ApiKeyCreateParams": (
        "stripe.params.v2.iam._api_key_create_params",
        False,
    ),
    "ApiKeyCreateParamsPublicKey": (
        "stripe.params.v2.iam._api_key_create_params",
        False,
    ),
    "ApiKeyCreateParamsPublicKeyPemKey": (
        "stripe.params.v2.iam._api_key_create_params",
        False,
    ),
    "ApiKeyExpireParams": (
        "stripe.params.v2.iam._api_key_expire_params",
        False,
    ),
    "ApiKeyListParams": ("stripe.params.v2.iam._api_key_list_params", False),
    "ApiKeyRetrieveParams": (
        "stripe.params.v2.iam._api_key_retrieve_params",
        False,
    ),
    "ApiKeyRotateParams": (
        "stripe.params.v2.iam._api_key_rotate_params",
        False,
    ),
    "ApiKeyRotateParamsPublicKey": (
        "stripe.params.v2.iam._api_key_rotate_params",
        False,
    ),
    "ApiKeyRotateParamsPublicKeyPemKey": (
        "stripe.params.v2.iam._api_key_rotate_params",
        False,
    ),
    "ApiKeyUpdateParams": (
        "stripe.params.v2.iam._api_key_update_params",
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
