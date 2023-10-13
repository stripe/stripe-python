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
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Location(
    CreateableAPIResource["Location"],
    DeletableAPIResource["Location"],
    ListableAPIResource["Location"],
    UpdateableAPIResource["Location"],
):
    """
    A Location represents a grouping of readers.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    OBJECT_NAME = "terminal.location"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            address: "Location.CreateParamsAddress"
            configuration_overrides: NotRequired["str|None"]
            display_name: str
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class CreateParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: str
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            address: NotRequired["Location.ModifyParamsAddress|None"]
            configuration_overrides: NotRequired["Literal['']|str|None"]
            display_name: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ModifyParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    address: StripeObject
    configuration_overrides: Optional[str]
    display_name: str
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["terminal.location"]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Location.CreateParams"]
    ) -> "Location":
        return cast(
            "Location",
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
        cls, sid: str, **params: Unpack["Location.DeleteParams"]
    ) -> "Location":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Location",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Location.DeleteParams"]) -> "Location":
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
        **params: Unpack["Location.ListParams"]
    ) -> ListObject["Location"]:
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
        cls, id, **params: Unpack["Location.ModifyParams"]
    ) -> "Location":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Location",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Location.RetrieveParams"]
    ) -> "Location":
        instance = cls(id, **params)
        instance.refresh()
        return instance
