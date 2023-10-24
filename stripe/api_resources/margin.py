# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus


class Margin(
    CreateableAPIResource["Margin"],
    ListableAPIResource["Margin"],
    UpdateableAPIResource["Margin"],
):
    """
    A (partner) margin represents a specific discount distributed in partner reseller programs to business partners who
    resell products and services and earn a discount (margin) for doing so.
    """

    OBJECT_NAME: ClassVar[Literal["margin"]] = "margin"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: NotRequired["str|None"]
            percent_off: float

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    active: bool
    created: int
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["margin"]
    percent_off: float
    updated: int

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Margin.CreateParams"]
    ) -> "Margin":
        return cast(
            "Margin",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Margin.ListParams"]
    ) -> ListObject["Margin"]:
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
        cls, id: str, **params: Unpack["Margin.ModifyParams"]
    ) -> "Margin":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Margin",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Margin.RetrieveParams"]
    ) -> "Margin":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/billing/margins"
