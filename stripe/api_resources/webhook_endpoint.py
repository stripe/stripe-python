# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class WebhookEndpoint(
    CreateableAPIResource["WebhookEndpoint"],
    DeletableAPIResource["WebhookEndpoint"],
    ListableAPIResource["WebhookEndpoint"],
    UpdateableAPIResource["WebhookEndpoint"],
):
    """
    You can configure [webhook endpoints](https://stripe.com/docs/webhooks/) via the API to be
    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up webhooks](https://stripe.com/docs/webhooks/configure)
    """

    OBJECT_NAME = "webhook_endpoint"
    api_version: Optional[str]
    application: Optional[str]
    created: int
    description: Optional[str]
    enabled_events: List[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["webhook_endpoint"]
    secret: Optional[str]
    status: str
    url: str
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "WebhookEndpoint":
        return cast(
            "WebhookEndpoint",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> "WebhookEndpoint":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "WebhookEndpoint",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "WebhookEndpoint":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["WebhookEndpoint"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Any) -> "WebhookEndpoint":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "WebhookEndpoint",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "WebhookEndpoint":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
