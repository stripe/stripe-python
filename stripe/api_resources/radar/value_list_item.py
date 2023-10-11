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
from stripe.request_options import RequestOptions
from typing import List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus


class ValueListItem(
    CreateableAPIResource["ValueListItem"],
    DeletableAPIResource["ValueListItem"],
    ListableAPIResource["ValueListItem"],
):
    """
    Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

    Related guide: [Managing list items](https://stripe.com/docs/radar/lists#managing-list-items)
    """

    OBJECT_NAME = "radar.value_list_item"

    class CreateParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        value: str
        value_list: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["ValueListItem.ListParamsCreated", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        value: NotRequired[Optional[str]]
        value_list: str

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    created: int
    created_by: str
    id: str
    livemode: bool
    object: Literal["radar.value_list_item"]
    value: str
    value_list: str
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ValueListItem.CreateParams"]
    ) -> "ValueListItem":
        return cast(
            "ValueListItem",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["ValueListItem.DeleteParams"]
    ) -> "ValueListItem":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "ValueListItem",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["ValueListItem.DeleteParams"]
    ) -> "ValueListItem":
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
        **params: Unpack["ValueListItem.ListParams"]
    ) -> ListObject["ValueListItem"]:
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
    def retrieve(
        cls, id: str, **params: Unpack["ValueListItem.RetrieveParams"]
    ) -> "ValueListItem":
        instance = cls(id, **params)
        instance.refresh()
        return instance
