# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Dispute(ListableAPIResource, UpdateableAPIResource):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you're given the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate. You can find more
    information about the dispute process in our [Disputes and
    Fraud](https://stripe.com/docs/disputes) documentation.

    Related guide: [Disputes and Fraud](https://stripe.com/docs/disputes).
    """

    OBJECT_NAME = "dispute"

    @classmethod
    def _cls_close(
        cls,
        dispute,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/disputes/{dispute}/close".format(
                dispute=util.sanitize_id(dispute)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_close")
    def close(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/disputes/{dispute}/close".format(
                dispute=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
