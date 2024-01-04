from typing import Optional, Dict
from typing_extensions import NotRequired, TypedDict


class RequestOptions(TypedDict):
    api_key: NotRequired[Optional[str]]
    stripe_version: NotRequired[Optional[str]]
    stripe_account: NotRequired[Optional[str]]
    idempotency_key: NotRequired[Optional[str]]
    headers: NotRequired[Optional[Dict[str, str]]]
