# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._deleted_object import DeletedObject
from stripe.v2._event import Event
from stripe.v2._event_destination import EventDestination
from stripe.v2._list_object import ListObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class EventDestinationService(StripeService):
    class CreateParams(TypedDict):
        description: NotRequired[str]
        """
        An optional description of what the event destination is used for.
        """
        enabled_events: List[str]
        """
        The list of events to enable for this endpoint.
        """
        event_payload: Literal["snapshot", "thin"]
        """
        Payload type of events being subscribed to.
        """
        events_from: NotRequired[List[Literal["other_accounts", "self"]]]
        """
        Where events should be routed from.
        """
        include: NotRequired[
            List[
                Literal[
                    "webhook_endpoint.signing_secret", "webhook_endpoint.url"
                ]
            ]
        ]
        """
        Additional fields to include in the response.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Metadata.
        """
        name: str
        """
        Event destination name.
        """
        snapshot_api_version: NotRequired[str]
        """
        If using the snapshot event payload, the API version events are rendered as.
        """
        type: Literal["amazon_eventbridge", "webhook_endpoint"]
        """
        Event destination type.
        """
        amazon_eventbridge: NotRequired[
            "EventDestinationService.CreateParamsAmazonEventbridge"
        ]
        """
        Amazon EventBridge configuration.
        """
        webhook_endpoint: NotRequired[
            "EventDestinationService.CreateParamsWebhookEndpoint"
        ]
        """
        Webhook endpoint configuration.
        """

    class CreateParamsAmazonEventbridge(TypedDict):
        aws_account_id: str
        """
        The AWS account ID.
        """
        aws_region: str
        """
        The region of the AWS event source.
        """

    class CreateParamsWebhookEndpoint(TypedDict):
        url: str
        """
        The URL of the webhook endpoint.
        """

    class DeleteParams(TypedDict):
        pass

    class DisableParams(TypedDict):
        pass

    class EnableParams(TypedDict):
        pass

    class ListParams(TypedDict):
        include: NotRequired[List[Literal["webhook_endpoint.url"]]]
        """
        Additional fields to include in the response. Currently supports `webhook_endpoint.url`.
        """
        limit: NotRequired[int]
        """
        The page size.
        """

    class PingParams(TypedDict):
        pass

    class RetrieveParams(TypedDict):
        include: NotRequired[List[Literal["webhook_endpoint.url"]]]
        """
        Additional fields to include in the response.
        """

    class UpdateParams(TypedDict):
        description: NotRequired[str]
        """
        An optional description of what the event destination is used for.
        """
        enabled_events: NotRequired[List[str]]
        """
        The list of events to enable for this endpoint.
        """
        include: NotRequired[List[Literal["webhook_endpoint.url"]]]
        """
        Additional fields to include in the response. Currently supports `webhook_endpoint.url`.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Metadata.
        """
        name: NotRequired[str]
        """
        Event destination name.
        """
        webhook_endpoint: NotRequired[
            "EventDestinationService.UpdateParamsWebhookEndpoint"
        ]
        """
        Webhook endpoint configuration.
        """

    class UpdateParamsWebhookEndpoint(TypedDict):
        url: str
        """
        The URL of the webhook endpoint.
        """

    def list(
        self,
        params: Optional["EventDestinationService.ListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[EventDestination]:
        """
        Lists all event destinations.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            ListObject[EventDestination],
            self._request(
                "get",
                "/v2/core/event_destinations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["EventDestinationService.ListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[EventDestination]:
        """
        Lists all event destinations.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            ListObject[EventDestination],
            await self._request_async(
                "get",
                "/v2/core/event_destinations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "EventDestinationService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Create a new event destination.
        """
        if options is None:
            options = {}
        return cast(
            EventDestination,
            self._request(
                "post",
                "/v2/core/event_destinations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "EventDestinationService.CreateParams",
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Create a new event destination.
        """
        if options is None:
            options = {}
        return cast(
            EventDestination,
            await self._request_async(
                "post",
                "/v2/core/event_destinations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def delete(
        self,
        id: str,
        params: Optional["EventDestinationService.DeleteParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> DeletedObject:
        """
        Delete an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            DeletedObject,
            self._request(
                "delete",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: Optional["EventDestinationService.DeleteParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> DeletedObject:
        """
        Delete an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            DeletedObject,
            await self._request_async(
                "delete",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["EventDestinationService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Retrieves the details of an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            self._request(
                "get",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["EventDestinationService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Retrieves the details of an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            await self._request_async(
                "get",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["EventDestinationService.UpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Update the details of an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            self._request(
                "post",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["EventDestinationService.UpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Update the details of an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            await self._request_async(
                "post",
                "/v2/core/event_destinations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def disable(
        self,
        id: str,
        params: Optional["EventDestinationService.DisableParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Disable an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            self._request(
                "post",
                "/v2/core/event_destinations/{id}/disable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def disable_async(
        self,
        id: str,
        params: Optional["EventDestinationService.DisableParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Disable an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            await self._request_async(
                "post",
                "/v2/core/event_destinations/{id}/disable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def enable(
        self,
        id: str,
        params: Optional["EventDestinationService.EnableParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Enable an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            self._request(
                "post",
                "/v2/core/event_destinations/{id}/enable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def enable_async(
        self,
        id: str,
        params: Optional["EventDestinationService.EnableParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> EventDestination:
        """
        Enable an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            EventDestination,
            await self._request_async(
                "post",
                "/v2/core/event_destinations/{id}/enable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def ping(
        self,
        id: str,
        params: Optional["EventDestinationService.PingParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> Event:
        """
        Send a `ping` event to an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Event,
            self._request(
                "post",
                "/v2/core/event_destinations/{id}/ping".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def ping_async(
        self,
        id: str,
        params: Optional["EventDestinationService.PingParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> Event:
        """
        Send a `ping` event to an event destination.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Event,
            await self._request_async(
                "post",
                "/v2/core/event_destinations/{id}/ping".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
