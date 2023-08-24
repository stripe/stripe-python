# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal


class SubscriptionSchedule(
    CreateableAPIResource["SubscriptionSchedule"],
    ListableAPIResource["SubscriptionSchedule"],
    UpdateableAPIResource["SubscriptionSchedule"],
):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)
    """

    OBJECT_NAME = "subscription_schedule"
    application: Optional[Any]
    canceled_at: Optional[str]
    completed_at: Optional[str]
    created: str
    current_phase: Optional[Any]
    customer: Any
    default_settings: Any
    end_behavior: str
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["subscription_schedule"]
    phases: List[Any]
    released_at: Optional[str]
    released_subscription: Optional[str]
    status: str
    subscription: Optional[Any]
    test_clock: Optional[Any]

    @classmethod
    def _cls_cancel(
        cls,
        schedule,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_release(
        cls,
        schedule,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_release")
    def release(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
