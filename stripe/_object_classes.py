# -*- coding: utf-8 -*-
from importlib import import_module
from typing import Dict, Tuple
from typing_extensions import TYPE_CHECKING, Type

from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe._api_mode import ApiMode

OBJECT_CLASSES: Dict[str, Tuple[str, str]] = {
    # data structures
    "list": ("stripe._list_object", "ListObject"),
    "search_result": ("stripe._search_result_object", "SearchResultObject"),
    "file": ("stripe._file", "File"),
    # there's also an alt name for compatibility
    "file_upload": ("stripe._file", "File"),
    # Object classes: The beginning of the section generated from our OpenAPI spec
    # Object classes: The end of the section generated from our OpenAPI spec
}

V2_OBJECT_CLASSES: Dict[str, Tuple[str, str]] = {
    # V2 Object classes: The beginning of the section generated from our OpenAPI spec
    # V2 Object classes: The end of the section generated from our OpenAPI spec
}


def get_object_class(
    api_mode: "ApiMode", object_name: str
) -> Type[StripeObject]:
    mapping = OBJECT_CLASSES if api_mode == "V1" else V2_OBJECT_CLASSES

    if object_name not in mapping:
        return StripeObject

    import_path, class_name = mapping[object_name]
    return getattr(
        import_module(import_path),
        class_name,
    )
