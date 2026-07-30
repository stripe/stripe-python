# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.risk._inquiry import Inquiry as Inquiry
    from stripe.v2.risk._inquiry_service import (
        InquiryService as InquiryService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "Inquiry": ("stripe.v2.risk._inquiry", False),
    "InquiryService": ("stripe.v2.risk._inquiry_service", False),
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
