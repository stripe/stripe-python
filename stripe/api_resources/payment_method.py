# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class PaymentMethod(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_method"

    @classmethod
    def _cls_attach(
        cls,
        payment_method,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_attach")
    def attach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_detach(
        cls,
        payment_method,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_detach")
    def detach(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
