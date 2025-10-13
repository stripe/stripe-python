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

_submodules = {
    "EventDestinationCreateParams": "stripe.params.v2.core._event_destination_create_params",
    "EventDestinationCreateParamsAmazonEventbridge": "stripe.params.v2.core._event_destination_create_params",
    "EventDestinationCreateParamsWebhookEndpoint": "stripe.params.v2.core._event_destination_create_params",
    "EventDestinationDeleteParams": "stripe.params.v2.core._event_destination_delete_params",
    "EventDestinationDisableParams": "stripe.params.v2.core._event_destination_disable_params",
    "EventDestinationEnableParams": "stripe.params.v2.core._event_destination_enable_params",
    "EventDestinationListParams": "stripe.params.v2.core._event_destination_list_params",
    "EventDestinationPingParams": "stripe.params.v2.core._event_destination_ping_params",
    "EventDestinationRetrieveParams": "stripe.params.v2.core._event_destination_retrieve_params",
    "EventDestinationUpdateParams": "stripe.params.v2.core._event_destination_update_params",
    "EventDestinationUpdateParamsWebhookEndpoint": "stripe.params.v2.core._event_destination_update_params",
    "EventListParams": "stripe.params.v2.core._event_list_params",
    "EventRetrieveParams": "stripe.params.v2.core._event_retrieve_params",
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
