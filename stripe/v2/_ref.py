# -*- coding: utf-8 -*-
# NOT codegenned
from typing import Any, Dict, Generic, Optional, TypeVar, cast

from typing_extensions import TYPE_CHECKING

from stripe._api_mode import ApiMode

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor
    from stripe._stripe_response import StripeResponse

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

    _requestor: Optional["_APIRequestor"]

    def __init__(
        self,
        parsed_body: Dict[str, Any],
        requestor: Optional["_APIRequestor"],
    ) -> None:
        self.type = parsed_body["type"]
        self.id = parsed_body["id"]
        self.url = parsed_body["url"]
        self._requestor = requestor

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional["StripeResponse"] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> "Ref[Any]":
        return cls(values, requestor=requestor)

    def fetch(self) -> T:
        """
        Fetches the full API resource that this reference points to.

        Raises ``RuntimeError`` if no requestor is associated with this ``Ref``.
        """
        if self._requestor is None:
            raise RuntimeError(
                "Cannot call fetch() on a Ref that has no associated requestor."
            )
        return cast(
            T,
            self._requestor.request(
                "get",
                self.url,
                base_address="api",
                usage=["ref_fetch"],
            ),
        )

    async def fetch_async(self) -> T:
        """
        Fetches the full API resource that this reference points to,
        using an async HTTP request.

        Raises ``RuntimeError`` if no requestor is associated with this ``Ref``.
        """
        if self._requestor is None:
            raise RuntimeError(
                "Cannot call fetch_async() on a Ref that has no associated requestor."
            )
        return cast(
            T,
            await self._requestor.request_async(
                "get",
                self.url,
                base_address="api",
                usage=["ref_fetch", "ref_fetch_async"],
            ),
        )

    def __repr__(self) -> str:
        return f"<Ref type={self.type} id={self.id} url={self.url}>"
