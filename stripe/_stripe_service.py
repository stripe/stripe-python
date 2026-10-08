from stripe._api_requestor import (
    _APIRequestor,
)
from stripe._stripe_response import (
    StripeStreamResponse,
    StripeStreamResponseAsync,
)
from stripe._stripe_object import StripeObject
from stripe._request_options import RequestOptions
from stripe._base_address import BaseAddress

from typing import Any, Dict, Mapping, Optional, Tuple
from urllib.parse import quote

from stripe._encode import _coerce_v2_params, _SchemaNode


def _split_v2_search_params(
    url: str, params: Optional[Mapping[str, Any]]
) -> Tuple[str, Optional[Mapping[str, Any]]]:
    if params is None or "limit" not in params:
        return url, params
    body_params = dict(params)
    limit = body_params.pop("limit")
    if "limit=" not in url:
        separator = "&" if "?" in url else "?"
        url = "%s%slimit=%s" % (url, separator, quote(str(limit), safe=""))
    return url, body_params


class StripeService(object):
    _requestor: _APIRequestor

    def __init__(self, requestor):
        self._requestor = requestor

    def _request(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
        *,
        base_address: BaseAddress,
        _param_encodings: Optional[Dict[str, _SchemaNode]] = None,
    ) -> StripeObject:
        if _param_encodings:
            params = _coerce_v2_params(params, _param_encodings)
        if (
            method == "post"
            and url.split("?", 1)[0].startswith("/v2/")
            and url.split("?", 1)[0].endswith("/search")
        ):
            url, params = _split_v2_search_params(url, params)
        return self._requestor.request(
            method,
            url,
            params,
            options,
            base_address=base_address,
            usage=["stripe_client"],
        )

    async def _request_async(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
        *,
        base_address: BaseAddress,
        _param_encodings: Optional[Dict[str, _SchemaNode]] = None,
    ) -> StripeObject:
        if _param_encodings:
            params = _coerce_v2_params(params, _param_encodings)
        if (
            method == "post"
            and url.split("?", 1)[0].startswith("/v2/")
            and url.split("?", 1)[0].endswith("/search")
        ):
            url, params = _split_v2_search_params(url, params)
        return await self._requestor.request_async(
            method,
            url,
            params,
            options,
            base_address=base_address,
            usage=["stripe_client"],
        )

    def _request_stream(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
        *,
        base_address: BaseAddress,
    ) -> StripeStreamResponse:
        return self._requestor.request_stream(
            method,
            url,
            params,
            options,
            base_address=base_address,
            usage=["stripe_client"],
        )

    async def _request_stream_async(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
        *,
        base_address: BaseAddress,
    ) -> StripeStreamResponseAsync:
        return await self._requestor.request_stream_async(
            method,
            url,
            params,
            options,
            base_address=base_address,
            usage=["stripe_client"],
        )
