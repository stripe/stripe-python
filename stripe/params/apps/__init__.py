# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.apps._install_create_params import (
        InstallCreateParams as InstallCreateParams,
    )
    from stripe.params.apps._install_list_params import (
        InstallListParams as InstallListParams,
        InstallListParamsCreated as InstallListParamsCreated,
    )
    from stripe.params.apps._install_modify_params import (
        InstallModifyParams as InstallModifyParams,
    )
    from stripe.params.apps._install_retrieve_params import (
        InstallRetrieveParams as InstallRetrieveParams,
    )
    from stripe.params.apps._install_uninstall_params import (
        InstallUninstallParams as InstallUninstallParams,
    )
    from stripe.params.apps._install_update_params import (
        InstallUpdateParams as InstallUpdateParams,
    )
    from stripe.params.apps._secret_create_params import (
        SecretCreateParams as SecretCreateParams,
        SecretCreateParamsScope as SecretCreateParamsScope,
    )
    from stripe.params.apps._secret_delete_where_params import (
        SecretDeleteWhereParams as SecretDeleteWhereParams,
        SecretDeleteWhereParamsScope as SecretDeleteWhereParamsScope,
    )
    from stripe.params.apps._secret_find_params import (
        SecretFindParams as SecretFindParams,
        SecretFindParamsScope as SecretFindParamsScope,
    )
    from stripe.params.apps._secret_list_params import (
        SecretListParams as SecretListParams,
        SecretListParamsScope as SecretListParamsScope,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "InstallCreateParams": (
        "stripe.params.apps._install_create_params",
        False,
    ),
    "InstallListParams": ("stripe.params.apps._install_list_params", False),
    "InstallListParamsCreated": (
        "stripe.params.apps._install_list_params",
        False,
    ),
    "InstallModifyParams": (
        "stripe.params.apps._install_modify_params",
        False,
    ),
    "InstallRetrieveParams": (
        "stripe.params.apps._install_retrieve_params",
        False,
    ),
    "InstallUninstallParams": (
        "stripe.params.apps._install_uninstall_params",
        False,
    ),
    "InstallUpdateParams": (
        "stripe.params.apps._install_update_params",
        False,
    ),
    "SecretCreateParams": ("stripe.params.apps._secret_create_params", False),
    "SecretCreateParamsScope": (
        "stripe.params.apps._secret_create_params",
        False,
    ),
    "SecretDeleteWhereParams": (
        "stripe.params.apps._secret_delete_where_params",
        False,
    ),
    "SecretDeleteWhereParamsScope": (
        "stripe.params.apps._secret_delete_where_params",
        False,
    ),
    "SecretFindParams": ("stripe.params.apps._secret_find_params", False),
    "SecretFindParamsScope": ("stripe.params.apps._secret_find_params", False),
    "SecretListParams": ("stripe.params.apps._secret_list_params", False),
    "SecretListParamsScope": ("stripe.params.apps._secret_list_params", False),
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
