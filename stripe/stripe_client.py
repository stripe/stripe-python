from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util

# from stripe.stripe_object import StripeObject


class StripeClient(object):
    def v1_customers_retrieve(self, id, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/customers/{customer}".format(customer=util.sanitize_id(id)),
            idempotency_key=idempotency_key,
            params=params,
        )

    def v1_llama_create(self, params=None, idempotency_key=None):
        return self._request(
            "post",
            "/v1/llamas",
            idempotency_key=idempotency_key,
            params=params,
            is_json=True
        )

    def _request(
        self,
        method_,
        url_,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        headers=None,
        params=None,
        is_json=False
    ):
        params = None if params is None else params.copy()
        api_key = util.read_special_variable(params, "api_key", api_key)
        idempotency_key = util.read_special_variable(
            params, "idempotency_key", idempotency_key
        )
        stripe_version = util.read_special_variable(
            params, "stripe_version", stripe_version
        )
        stripe_account = util.read_special_variable(
            params, "stripe_account", stripe_account
        )
        headers = util.read_special_variable(params, "headers", headers)

        stripe_account = stripe_account
        stripe_version = stripe_version
        api_key = api_key
        params = params

        requestor = api_requestor.APIRequestor(
            key=api_key,
            api_version=stripe_version,
            account=stripe_account,
        )

        if idempotency_key is not None:
            headers = {} if headers is None else headers.copy()
            headers.update(util.populate_headers(idempotency_key))

        response, api_key = requestor.request(method_, url_, params, headers, is_json=is_json)

        return util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account, params
        )
