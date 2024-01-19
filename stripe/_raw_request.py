from stripe._api_requestor import _APIRequestor
from stripe._util import _convert_to_stripe_object

from typing import Any, Dict, Optional, Union

from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._request_options import extract_options_from_dict


def raw_request(method_, url_, **params):
    params = params.copy()
    options, params = extract_options_from_dict(params)
    api_mode = params.pop("api_mode", None)
    base_address = params.pop("base", "api")

    stripe_context = params.pop("stripe_context", None)

    # stripe-context goes *here* and not in api_requestor. Properties
    # go on api_requestor when you want them to persist onto requests
    # made when you call instance methods on APIResources that come from
    # the first request. No need for that here, as we aren't deserializing APIResources
    if stripe_context is not None:
        options["headers"] = options.get("headers", {})
        assert isinstance(options["headers"], dict)
        options["headers"].update({"Stripe-Context": stripe_context})

    requestor = _APIRequestor._global_instance()

    rbody, rcode, rheaders = requestor.request_raw(
        method_,
        url_,
        params=params,
        options=options,
        base_address=base_address,
        api_mode=api_mode,
        _usage=["raw_request"],
    )

    return requestor._interpret_response(rbody, rcode, rheaders)


async def raw_request_async(method_, url_, **params):
    params = params.copy()
    options, params = extract_options_from_dict(params)
    api_mode = params.pop("api_mode", None)
    base_address = params.pop("base", "api")

    requestor = _APIRequestor._global_instance()

    rbody, rcode, rheaders = await requestor.request_raw_async(
        method_,
        url_,
        params=params,
        options=options,
        base_address=base_address,
        api_mode=api_mode,
        _usage=["raw_request"],
    )

    return requestor._interpret_response(rbody, rcode, rheaders)


def deserialize(
    resp: Union[StripeResponse, Dict[str, Any]],
    api_key: Optional[str] = None,
    stripe_version: Optional[str] = None,
    stripe_account: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> StripeObject:
    return _convert_to_stripe_object(
        resp=resp,
        params=params,
        requestor=_APIRequestor._global_with_options(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        ),
        api_mode="V1",
    )
