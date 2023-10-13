# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
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
    from stripe.api_resources.file import File


class FileLink(
    CreateableAPIResource["FileLink"],
    ListableAPIResource["FileLink"],
    UpdateableAPIResource["FileLink"],
):
    """
    To share the contents of a `File` object with non-Stripe users, you can
    create a `FileLink`. `FileLink`s contain a URL that you can use to
    retrieve the contents of the file without authentication.
    """

    OBJECT_NAME = "file_link"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]
            file: str
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ListParams(RequestOptions):
            created: NotRequired["FileLink.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            expired: NotRequired["bool|None"]
            file: NotRequired["str|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["Literal['']|Literal['now']|int|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    created: int
    expired: bool
    expires_at: Optional[int]
    file: ExpandableField["File"]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["file_link"]
    url: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FileLink.CreateParams"]
    ) -> "FileLink":
        return cast(
            "FileLink",
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
        **params: Unpack["FileLink.ListParams"]
    ) -> ListObject["FileLink"]:
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
        cls, id, **params: Unpack["FileLink.ModifyParams"]
    ) -> "FileLink":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "FileLink",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FileLink.RetrieveParams"]
    ) -> "FileLink":
        instance = cls(id, **params)
        instance.refresh()
        return instance
