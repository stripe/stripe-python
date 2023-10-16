# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class ConnectionToken(CreateableAPIResource["ConnectionToken"]):
    """
    A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    OBJECT_NAME = "terminal.connection_token"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            location: NotRequired["str|None"]

    location: Optional[str]
    object: Literal["terminal.connection_token"]
    secret: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ConnectionToken.CreateParams"]
    ) -> "ConnectionToken":
        return cast(
            "ConnectionToken",
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
