# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            alias: str
            expand: NotRequired["List[str]|None"]
            item_type: NotRequired[
                "Literal['card_bin', 'card_fingerprint', 'case_sensitive_string', 'country', 'customer_id', 'email', 'ip_address', 'sepa_debit_fingerprint', 'string', 'us_bank_account_fingerprint']|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            alias: NotRequired["str|None"]
            contains: NotRequired["str|None"]
            created: NotRequired["ValueList.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            alias: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
