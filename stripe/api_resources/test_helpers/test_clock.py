# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from typing import Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class TestClock(
    CreateableAPIResource["TestClock"],
    DeletableAPIResource["TestClock"],
    ListableAPIResource["TestClock"],
):
    """
    A test clock enables deterministic control over objects in testmode. With a test clock, you can create
    objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances,
    you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.
    """

    OBJECT_NAME = "test_helpers.test_clock"
    created: int
    deletes_after: int
    frozen_time: int
    id: str
    livemode: bool
    name: Optional[str]
    object: Literal["test_helpers.test_clock"]
    status: Literal["advancing", "internal_failure", "ready"]

    @classmethod
    def _cls_advance(
        cls,
        test_clock,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/test_helpers/test_clocks/{test_clock}/advance".format(
                test_clock=util.sanitize_id(test_clock)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_advance")
    def advance(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/test_helpers/test_clocks/{test_clock}/advance".format(
                test_clock=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> "TestClock":
        return cast(
            "TestClock",
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
    def _cls_delete(cls, sid, **params) -> "TestClock":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "TestClock",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params) -> "TestClock":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["TestClock"]:
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
    def retrieve(cls, id, api_key=None, **params) -> "TestClock":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
