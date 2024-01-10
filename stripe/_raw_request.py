from stripe._api_requestor import APIRequestor
from stripe._util import (
    read_special_variable,
    convert_to_stripe_object,
    populate_headers,
)
from stripe._api_version import _ApiVersion


def _raw_request_args(method_, url_, **params):
    params = None if params is None else params.copy()  # type: ignore
    api_key = read_special_variable(params, "api_key", None)
    idempotency_key = read_special_variable(params, "idempotency_key", None)
    stripe_version = read_special_variable(params, "stripe_version", None)
    stripe_account = read_special_variable(params, "stripe_account", None)
    api_mode = read_special_variable(params, "api_mode", None)
    stripe_context = read_special_variable(params, "stripe_context", None)
    headers = read_special_variable(params, "headers", None)

    if api_mode == "preview":
        stripe_version = stripe_version or _ApiVersion.PREVIEW

    requestor = APIRequestor(
        key=api_key,
        api_version=stripe_version,
        account=stripe_account,
    )

    if idempotency_key is not None:
        headers = {} if headers is None else headers.copy()
        headers.update(populate_headers(idempotency_key))

    # stripe-context goes *here* and not in api_requestor. Properties
    # go on api_requestor when you want them to persist onto requests
    # made when you call instance methods on APIResources that come from
    # the first request. No need for that here, as we aren't deserializing APIResources
    if stripe_context is not None:
        headers = {} if headers is None else headers.copy()
        headers.update({"Stripe-Context": stripe_context})

    usage = ["raw_request"]

    return requestor, method_, url_, params, headers, api_mode, usage


def raw_request(method_, url_, **params):
    (
        requestor,
        method_,
        url_,
        params,
        headers,
        api_mode,
        usage,
    ) = _raw_request_args(method_, url_, **params)
    response, _ = requestor.request(
        method_, url_, params, headers, api_mode, _usage=usage
    )
    return response


async def raw_request_async(method_, url_, **params):
    (
        requestor,
        method_,
        url_,
        params,
        headers,
        api_mode,
        usage,
    ) = _raw_request_args(method_, url_, **params)
    response, _ = await requestor.request_async(
        method_, url_, params, headers, api_mode, _usage=usage
    )
    return response


def deserialize(
    resp, api_key=None, stripe_version=None, stripe_account=None, params=None
):
    return convert_to_stripe_object(
        resp, api_key, stripe_version, stripe_account, params
    )
