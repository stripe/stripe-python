# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.risk._form import Form as Form
    from stripe.risk._form_service import FormService as FormService

# name -> (import_target, is_submodule)
_import_map = {
    "Form": ("stripe.risk._form", False),
    "FormService": ("stripe.risk._form_service", False),
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
