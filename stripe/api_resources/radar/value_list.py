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
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.radar.value_list_item import ValueListItem


class ValueList(
    CreateableAPIResource["ValueList"],
    DeletableAPIResource["ValueList"],
    ListableAPIResource["ValueList"],
    UpdateableAPIResource["ValueList"],
):
    """
    Value lists allow you to group values together which can then be referenced in rules.

    Related guide: [Default Stripe lists](https://stripe.com/docs/radar/lists#managing-list-items)
    """

    OBJECT_NAME = "radar.value_list"

    class CreateParams(RequestOptions):
        alias: str
        expand: NotRequired[Optional[List[str]]]
        item_type: NotRequired[
            Optional[
                Literal[
                    "card_bin",
                    "card_fingerprint",
                    "case_sensitive_string",
                    "country",
                    "customer_id",
                    "email",
                    "ip_address",
                    "sepa_debit_fingerprint",
                    "string",
                    "us_bank_account_fingerprint",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        name: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        alias: NotRequired[Optional[str]]
        contains: NotRequired[Optional[str]]
        created: NotRequired[
            Optional[Union["ValueList.ListCreatedParams", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        alias: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        name: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    alias: str
    created: int
    created_by: str
    id: str
    item_type: Literal[
        "card_bin",
        "card_fingerprint",
        "case_sensitive_string",
        "country",
        "customer_id",
        "email",
        "ip_address",
        "sepa_debit_fingerprint",
        "string",
        "us_bank_account_fingerprint",
    ]
    list_items: ListObject["ValueListItem"]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["radar.value_list"]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ValueList.CreateParams"]
    ) -> "ValueList":
        return cast(
            "ValueList",
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
        cls, sid: str, **params: Unpack["ValueList.DeleteParams"]
    ) -> "ValueList":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "ValueList",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["ValueList.DeleteParams"]
    ) -> "ValueList":
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
        **params: Unpack["ValueList.ListParams"]
    ) -> ListObject["ValueList"]:
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
    def modify(
        cls, id, **params: Unpack["ValueList.ModifyParams"]
    ) -> "ValueList":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "ValueList",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ValueList.RetrieveParams"]
    ) -> "ValueList":
        instance = cls(id, **params)
        instance.refresh()
        return instance
