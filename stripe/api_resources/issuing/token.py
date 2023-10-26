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
from typing import ClassVar, List, Optional, cast
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

    OBJECT_NAME: ClassVar[Literal["issuing.token"]] = "issuing.token"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            card: str
            """
            The Issuing card identifier to list tokens for.
            """
            created: NotRequired["Token.ListParamsCreated|int|None"]
            """
            Select Issuing tokens that were created during the given date interval.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['active', 'deleted', 'requested', 'suspended']|None"
            ]
            """
            Select Issuing tokens with the given status.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            status: Literal["active", "deleted", "suspended"]
            """
            Specifies which status the token should be updated to.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    card: ExpandableField["Card"]
    """
    Card associated with this token.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    device_fingerprint: Optional[str]
    """
    The hashed ID derived from the device ID from the card network associated with the token
    """
    id: str
    """
    Unique identifier for the object.
    """
    last4: Optional[str]
    """
    The last four digits of the token.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: Literal["mastercard", "visa"]
    """
    The token service provider / card network associated with the token.
    """
    network_data: Optional[StripeObject]
    network_updated_at: int
    """
    Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch.
    """
    object: Literal["issuing.token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "deleted", "requested", "suspended"]
    """
    The usage state of the token.
    """
    wallet_provider: Optional[
        Literal["apple_pay", "google_pay", "samsung_pay"]
    ]
    """
    The digital wallet for this token, if one was used.
    """

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
    def modify(
        cls, id: str, **params: Unpack["Token.ModifyParams"]
    ) -> "Token":
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
