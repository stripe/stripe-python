from stripe import api_requestor, util
from stripe.api_version import _ApiVersion


def _raw_request(method_, url_, **params):
    params = None if params is None else params.copy()
    api_key = util.read_special_variable(params, "api_key", None)
    idempotency_key = util.read_special_variable(
        params, "idempotency_key", None
    )
    stripe_version = util.read_special_variable(params, "stripe_version", None)
    stripe_account = util.read_special_variable(params, "stripe_account", None)
    api_mode = util.read_special_variable(params, "api_mode", None)
    stripe_context = util.read_special_variable(params, "stripe_context", None)
    headers = util.read_special_variable(params, "headers", None)

    if api_mode == "preview":
        stripe_version = stripe_version or _ApiVersion.PREVIEW

    requestor = api_requestor.APIRequestor(
        key=api_key,
        api_version=stripe_version,
        account=stripe_account,
    )

    if idempotency_key is not None:
        headers = {} if headers is None else headers.copy()
        headers.update(util.populate_headers(idempotency_key))

    # stripe-context goes *here* and not in api_requestor. Properties
    # go on api_requestor when you want them to persist onto requests
    # made when you call instance methods on APIResources that come from
    # the first request. No need for that here, as we aren't deserializing APIResources
    if stripe_context is not None:
        headers = {} if headers is None else headers.copy()
        headers.update({"Stripe-Context": stripe_context})

    response, _ = requestor.request(method_, url_, params, headers, api_mode)
    return response


def _deserialize(
    resp, api_key=None, stripe_version=None, stripe_account=None, params=None
):
    return util.convert_to_stripe_object(
        resp, api_key, stripe_version, stripe_account, params
    )
