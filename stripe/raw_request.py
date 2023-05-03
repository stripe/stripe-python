from stripe import api_requestor, util


def _raw_request(method_, url_, **params):
    params = None if params is None else params.copy()
    api_key = util.read_special_variable(params, "api_key", None)
    idempotency_key = util.read_special_variable(
        params, "idempotency_key", None
    )
    client = util.read_special_variable(params, "client", None)  # for testing
    stripe_version = util.read_special_variable(params, "stripe_version", None)
    stripe_account = util.read_special_variable(params, "stripe_account", None)
    encoding = util.read_special_variable(params, "encoding", None)
    headers = util.read_special_variable(params, "headers", None)

    requestor = api_requestor.APIRequestor(
        key=api_key,
        client=client,
        api_version=stripe_version,
        account=stripe_account,
    )

    if idempotency_key is not None:
        headers = {} if headers is None else headers.copy()
        headers.update(util.populate_headers(idempotency_key))

    response, _ = requestor.request(method_, url_, params, headers, encoding)
    return response


def _deserialize(
    resp, api_key=None, stripe_version=None, stripe_account=None, params=None
):
    return util.convert_to_stripe_object(
        resp, api_key, stripe_version, stripe_account, params
    )
