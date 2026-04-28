# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe.v2.core._event import Event, EventNotification
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, TYPE_CHECKING, override

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor


class V2ExtendExtensionRunFailedEventNotification(EventNotification):
    LOOKUP_TYPE = "v2.extend.extension_run.failed"
    type: Literal["v2.extend.extension_run.failed"]

    @override
    def fetch_event(self) -> "V2ExtendExtensionRunFailedEvent":
        return cast(
            "V2ExtendExtensionRunFailedEvent",
            super().fetch_event(),
        )

    @override
    async def fetch_event_async(self) -> "V2ExtendExtensionRunFailedEvent":
        return cast(
            "V2ExtendExtensionRunFailedEvent",
            await super().fetch_event_async(),
        )


class V2ExtendExtensionRunFailedEvent(Event):
    LOOKUP_TYPE = "v2.extend.extension_run.failed"
    type: Literal["v2.extend.extension_run.failed"]

    class V2ExtendExtensionRunFailedEventData(StripeObject):
        class Error(StripeObject):
            debug_url: str
            """
            URL to the extension run in Workbench for deeper debugging.
            """
            message: str
            """
            Detailed error message.
            """

        class Extension(StripeObject):
            id: str
            """
            The extension's unique identifier.
            """
            method: str
            """
            The extension method called where the failure occurred.
            """
            name: str
            """
            Human-readable name of the extension.
            """
            version: str
            """
            Version of the extension that failed.
            """

        error: Error
        """
        Details about the error that occurred.
        """
        extension: Extension
        """
        Details about the extension that failed.
        """
        extension_run_id: str
        """
        The ID of the extension run that failed.
        """
        _inner_class_types = {"error": Error, "extension": Extension}

    data: V2ExtendExtensionRunFailedEventData
    """
    Data for the v2.extend.extension_run.failed event
    """

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "V2ExtendExtensionRunFailedEvent":
        evt = super()._construct_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        if hasattr(evt, "data"):
            evt.data = V2ExtendExtensionRunFailedEvent.V2ExtendExtensionRunFailedEventData._construct_from(
                values=evt.data,
                last_response=last_response,
                requestor=requestor,
                api_mode=api_mode,
            )
        return evt
