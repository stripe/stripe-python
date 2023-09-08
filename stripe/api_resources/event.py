# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class Event(ListableAPIResource["Event"]):
    """
    Events are our way of letting you know when something interesting happens in
    your account. When an interesting event occurs, we create a new `Event`
    object. For example, when a charge succeeds, we create a `charge.succeeded`
    event; and when an invoice payment attempt fails, we create an
    `invoice.payment_failed` event. Note that many API requests may cause multiple
    events to be created. For example, if you create a new subscription for a
    customer, you will receive both a `customer.subscription.created` event and a
    `charge.succeeded` event.

    Events occur when the state of another API resource changes. The state of that
    resource at the time of the change is embedded in the event's data field. For
    example, a `charge.succeeded` event will contain a charge, and an
    `invoice.payment_failed` event will contain an invoice.

    As with other API resources, you can use endpoints to retrieve an
    [individual event](https://stripe.com/docs/api#retrieve_event) or a [list of events](https://stripe.com/docs/api#list_events)
    from the API. We also have a separate
    [webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the
    `Event` objects directly to an endpoint on your server. Webhooks are managed
    in your
    [account settings](https://dashboard.stripe.com/account/webhooks),
    and our [Using Webhooks](https://stripe.com/docs/webhooks) guide will help you get set up.

    When using [Connect](https://stripe.com/docs/connect), you can also receive notifications of
    events that occur in connected accounts. For these events, there will be an
    additional `account` attribute in the received `Event` object.

    **NOTE:** Right now, access to events through the [Retrieve Event API](https://stripe.com/docs/api#retrieve_event) is
    guaranteed only for 30 days.
    """

    OBJECT_NAME = "event"
    account: str
    api_version: Optional[str]
    created: str
    data: StripeObject
    id: str
    livemode: bool
    object: Literal["event"]
    pending_webhooks: int
    request: Optional[StripeObject]
    type: str

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["Event"]:
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
    def retrieve(cls, id, api_key=None, **params) -> "Event":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
