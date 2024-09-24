from stripe._api_requestor import _APIRequestor
from stripe._util import _convert_to_stripe_object, get_api_mode

from typing import Any, Dict, Optional, Union

from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._request_options import extract_options_from_dict
from stripe._api_mode import ApiMode


def raw_request(method_, url_, **params):
    params = params.copy()
    options, params = extract_options_from_dict(params)
    api_mode = get_api_mode(url_)
    base_address = params.pop("base", "api")

    requestor = _APIRequestor._global_instance()

    rbody, rcode, rheaders = requestor.request_raw(
        method_,
        url_,
        params=params,
        options=options,
        base_address=base_address,
        api_mode=api_mode,
    )

    return requestor._interpret_response(rbody, rcode, rheaders, api_mode)


def deserialize(
    resp: Union[StripeResponse, Dict[str, Any]],
    api_key: Optional[str] = None,
    stripe_version: Optional[str] = None,
    stripe_account: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    *,
    api_mode: ApiMode,
) -> StripeObject:
    return _convert_to_stripe_object(
        resp=resp,
        params=params,
        requestor=_APIRequestor._global_with_options(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        ),
        api_mode=api_mode,
    )
