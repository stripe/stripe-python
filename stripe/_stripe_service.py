from stripe._api_requestor import _APIRequestor, StripeStreamResponse
from stripe._stripe_object import StripeObject
from stripe._request_options import RequestOptions
from stripe._base_address import BaseAddress
from stripe._api_mode import ApiMode

from typing import Any, Mapping, Optional


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
        api_mode: ApiMode,
    ) -> StripeObject:
        return self._requestor.request(
            method,
            url,
            params,
            options,
            base_address=base_address,
            api_mode=api_mode,
            _usage=["stripe_client"],
        )

    def _request_stream(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
        *,
        base_address: BaseAddress,
        api_mode: ApiMode,
    ) -> StripeStreamResponse:
        return self._requestor.request_stream(
            method,
            url,
            params,
            options,
            base_address=base_address,
            api_mode=api_mode,
            _usage=["stripe_client"],
        )
