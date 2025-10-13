# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.forwarding._request_create_params import (
        RequestCreateParams as RequestCreateParams,
        RequestCreateParamsRequest as RequestCreateParamsRequest,
        RequestCreateParamsRequestHeader as RequestCreateParamsRequestHeader,
    )
    from stripe.params.forwarding._request_list_params import (
        RequestListParams as RequestListParams,
        RequestListParamsCreated as RequestListParamsCreated,
    )
    from stripe.params.forwarding._request_retrieve_params import (
        RequestRetrieveParams as RequestRetrieveParams,
    )

_submodules = {
    "RequestCreateParams": "stripe.params.forwarding._request_create_params",
    "RequestCreateParamsRequest": "stripe.params.forwarding._request_create_params",
    "RequestCreateParamsRequestHeader": "stripe.params.forwarding._request_create_params",
    "RequestListParams": "stripe.params.forwarding._request_list_params",
    "RequestListParamsCreated": "stripe.params.forwarding._request_list_params",
    "RequestRetrieveParams": "stripe.params.forwarding._request_retrieve_params",
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
