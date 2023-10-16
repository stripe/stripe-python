# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.issuing.card import Card


class Token(ListableAPIResource["Token"], UpdateableAPIResource["Token"]):
    """
    An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://stripe.com/docs/issuing), you can [view and manage these tokens](https://stripe.com/docs/issuing/controls/token-management) through Stripe.
    """

    OBJECT_NAME = "issuing.token"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            card: str
            created: NotRequired["Token.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['active', 'deleted', 'requested', 'suspended']|None"
            ]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            status: Literal["active", "deleted", "suspended"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    card: ExpandableField["Card"]
    created: int
    device_fingerprint: Optional[str]
    id: str
    last4: Optional[str]
    livemode: bool
    network: Literal["mastercard", "visa"]
    network_data: Optional[StripeObject]
    network_updated_at: int
    object: Literal["issuing.token"]
    status: Literal["active", "deleted", "requested", "suspended"]
    wallet_provider: Optional[
        Literal["apple_pay", "google_pay", "samsung_pay"]
    ]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Token.ListParams"]
    ) -> ListObject["Token"]:
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
    def modify(cls, id, **params: Unpack["Token.ModifyParams"]) -> "Token":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Token",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Token.RetrieveParams"]
    ) -> "Token":
        instance = cls(id, **params)
        instance.refresh()
        return instance
