# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class ConnectionToken(CreateableAPIResource["ConnectionToken"]):
    """
    A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    OBJECT_NAME: ClassVar[
        Literal["terminal.connection_token"]
    ] = "terminal.connection_token"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            location: NotRequired["str|None"]
            """
            The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://stripe.com/docs/terminal/fleet/locations#connection-tokens).
            """

    location: Optional[str]
    """
    The id of the location that this connection token is scoped to. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://stripe.com/docs/terminal/fleet/locations#connection-tokens).
    """
    object: Literal["terminal.connection_token"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    secret: str
    """
    Your application should pass this token to the Stripe Terminal SDK.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ConnectionToken.CreateParams"]
    ) -> "ConnectionToken":
        """
        To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.
        """
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
