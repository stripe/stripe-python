# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core.health._alert_list_params import AlertListParams
    from stripe.params.v2.core.health._alert_retrieve_params import (
        AlertRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core.health._alert import Alert
    from stripe.v2.core.health.alerts._history_service import HistoryService

_subservices = {
    "history": [
        "stripe.v2.core.health.alerts._history_service",
        "HistoryService",
    ],
}


class AlertService(StripeService):
    history: "HistoryService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["AlertListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Alert]":
        """
        Retrieves a list of health alerts.
        """
        return cast(
            "ListObject[Alert]",
            self._request(
                "get",
                "/v2/core/health/alerts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["AlertListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Alert]":
        """
        Retrieves a list of health alerts.
        """
        return cast(
            "ListObject[Alert]",
            await self._request_async(
                "get",
                "/v2/core/health/alerts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AlertRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Alert":
        """
        Retrieves a health alert by ID.
        """
        return cast(
            "Alert",
            self._request(
                "get",
                "/v2/core/health/alerts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AlertRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Alert":
        """
        Retrieves a health alert by ID.
        """
        return cast(
            "Alert",
            await self._request_async(
                "get",
                "/v2/core/health/alerts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
