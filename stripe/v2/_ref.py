# -*- coding: utf-8 -*-
# NOT codegenned
from typing import Any, Dict, Optional

from stripe._api_mode import ApiMode
from stripe._stripe_object import StripeObject


class Ref(StripeObject):
    """
    A reference to a Stripe object. Holds the object's id and type.
    """

    type: str
    """The object type string of the referenced resource (e.g. ``"v2.core.account"``)."""

    id: str
    """The ID of the referenced resource."""

    def __init__(self, parsed_body: Dict[str, Any]) -> None:
        self.type = parsed_body["type"]
        self.id = parsed_body["id"]

    @classmethod
    def _construct_from(
        cls,
        *,
        values: Dict[str, Any],
        last_response: Optional[Any] = None,
        api_mode: ApiMode = "V2",
    ) -> "Ref":
        return cls(values)

    def __repr__(self) -> str:
        return f"<Ref type={self.type} id={self.id}>"
