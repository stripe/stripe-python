# -*- coding: utf-8 -*-
# NOT codegenned
from typing import Any, Dict, Generic, Optional, TypeVar, cast

from typing_extensions import TYPE_CHECKING

from stripe._util import get_api_mode

if TYPE_CHECKING:
    from stripe._stripe_client import StripeClient

T = TypeVar("T")


class Ref(Generic[T]):
    """
    Represents a typed object reference with wire shape
    ``{"type": str, "id": str, "url": str}``.

    Call :meth:`fetch` (or :meth:`fetch_async`) to retrieve the full
    API resource that this reference points to.
    """

    type: str
    """The object type string of the referenced resource (e.g. ``"billing.meter"``)."""

    id: str
    """The ID of the referenced resource."""

    url: str
    """The URL path that can be used to fetch the referenced resource."""

    _client: Optional["StripeClient"]

    def __init__(
        self, parsed_body: Dict[str, Any], client: Optional["StripeClient"]
    ) -> None:
        self.type = parsed_body["type"]
        self.id = parsed_body["id"]
        self.url = parsed_body["url"]
        self._client = client

    def fetch(self) -> T:
        """
        Fetches the full API resource that this reference points to.

        Raises ``RuntimeError`` if no client is associated with this ``Ref``.
        """
        if self._client is None:
            raise RuntimeError(
                "Cannot call fetch() on a Ref that has no associated StripeClient."
            )
        response = self._client.raw_request(
            "get",
            self.url,
            usage=["ref_fetch"],
        )
        return cast(T, self._client.deserialize(response, api_mode=get_api_mode(self.url)))

    async def fetch_async(self) -> T:
        """
        Fetches the full API resource that this reference points to,
        using an async HTTP request.

        Raises ``RuntimeError`` if no client is associated with this ``Ref``.
        """
        if self._client is None:
            raise RuntimeError(
                "Cannot call fetch_async() on a Ref that has no associated StripeClient."
            )
        response = await self._client.raw_request_async(
            "get",
            self.url,
            usage=["ref_fetch", "ref_fetch_async"],
        )
        return cast(T, self._client.deserialize(response, api_mode=get_api_mode(self.url)))

    def __repr__(self) -> str:
        return f"<Ref type={self.type} id={self.id} url={self.url}>"
