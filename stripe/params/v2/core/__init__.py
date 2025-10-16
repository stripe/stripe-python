# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core._event_destination_create_params import (
        EventDestinationCreateParams as EventDestinationCreateParams,
        EventDestinationCreateParamsAmazonEventbridge as EventDestinationCreateParamsAmazonEventbridge,
        EventDestinationCreateParamsWebhookEndpoint as EventDestinationCreateParamsWebhookEndpoint,
    )
    from stripe.params.v2.core._event_destination_delete_params import (
        EventDestinationDeleteParams as EventDestinationDeleteParams,
    )
    from stripe.params.v2.core._event_destination_disable_params import (
        EventDestinationDisableParams as EventDestinationDisableParams,
    )
    from stripe.params.v2.core._event_destination_enable_params import (
        EventDestinationEnableParams as EventDestinationEnableParams,
    )
    from stripe.params.v2.core._event_destination_list_params import (
        EventDestinationListParams as EventDestinationListParams,
    )
    from stripe.params.v2.core._event_destination_ping_params import (
        EventDestinationPingParams as EventDestinationPingParams,
    )
    from stripe.params.v2.core._event_destination_retrieve_params import (
        EventDestinationRetrieveParams as EventDestinationRetrieveParams,
    )
    from stripe.params.v2.core._event_destination_update_params import (
        EventDestinationUpdateParams as EventDestinationUpdateParams,
        EventDestinationUpdateParamsWebhookEndpoint as EventDestinationUpdateParamsWebhookEndpoint,
    )
    from stripe.params.v2.core._event_list_params import (
        EventListParams as EventListParams,
    )
    from stripe.params.v2.core._event_retrieve_params import (
        EventRetrieveParams as EventRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "EventDestinationCreateParams": (
        "stripe.params.v2.core._event_destination_create_params",
        False,
    ),
    "EventDestinationCreateParamsAmazonEventbridge": (
        "stripe.params.v2.core._event_destination_create_params",
        False,
    ),
    "EventDestinationCreateParamsWebhookEndpoint": (
        "stripe.params.v2.core._event_destination_create_params",
        False,
    ),
    "EventDestinationDeleteParams": (
        "stripe.params.v2.core._event_destination_delete_params",
        False,
    ),
    "EventDestinationDisableParams": (
        "stripe.params.v2.core._event_destination_disable_params",
        False,
    ),
    "EventDestinationEnableParams": (
        "stripe.params.v2.core._event_destination_enable_params",
        False,
    ),
    "EventDestinationListParams": (
        "stripe.params.v2.core._event_destination_list_params",
        False,
    ),
    "EventDestinationPingParams": (
        "stripe.params.v2.core._event_destination_ping_params",
        False,
    ),
    "EventDestinationRetrieveParams": (
        "stripe.params.v2.core._event_destination_retrieve_params",
        False,
    ),
    "EventDestinationUpdateParams": (
        "stripe.params.v2.core._event_destination_update_params",
        False,
    ),
    "EventDestinationUpdateParamsWebhookEndpoint": (
        "stripe.params.v2.core._event_destination_update_params",
        False,
    ),
    "EventListParams": ("stripe.params.v2.core._event_list_params", False),
    "EventRetrieveParams": (
        "stripe.params.v2.core._event_retrieve_params",
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
