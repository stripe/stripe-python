from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.stripe_object import StripeObject


class StripeClient(object):
    def v1_customers_retrieve(self, id, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/customers/{customer}".format(customer=util.sanitize_id(id)),
            idempotency_key=idempotency_key,
            params=params,
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
    ):
        obj = StripeObject()
        return obj._request(
            method_,
            url_,
            api_key,
            idempotency_key,
            stripe_version,
            stripe_account,
            headers,
            params,
        )
