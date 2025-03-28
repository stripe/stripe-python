# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._event import Event
from stripe.v2._list_object import ListObject
from typing import cast
from typing_extensions import NotRequired, TypedDict


class EventService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page size.
        """
        object_id: str
        """
        Primary object ID used to retrieve related events.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self, params: "EventService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Event]:
        """
        List events, going back up to 30 days.
        """
        return cast(
            ListObject[Event],
            self._request(
                "get",
                "/v2/core/events",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self, params: "EventService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Event]:
        """
        List events, going back up to 30 days.
        """
        return cast(
            ListObject[Event],
            await self._request_async(
                "get",
                "/v2/core/events",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "EventService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Event:
        """
        Retrieves the details of an event.
        """
        return cast(
            Event,
            self._request(
                "get",
                "/v2/core/events/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "EventService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Event:
        """
        Retrieves the details of an event.
        """
        return cast(
            Event,
            await self._request_async(
                "get",
                "/v2/core/events/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
