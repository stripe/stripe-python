# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("attach", http_verb="post")
@custom_method("detach", http_verb="post")
class PaymentMethod(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_method"

    def attach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def detach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
