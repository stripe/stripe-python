# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource


class Form(ListableAPIResource):
    """
    Tax forms are legal documents which are delivered to one or more tax authorities for information reporting purposes.

    Related guide: [US tax reporting for Connect platforms](https://stripe.com/docs/connect/tax-reporting)
    """

    OBJECT_NAME = "tax.form"

    @classmethod
    def _cls_pdf(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/tax/forms/{id}/pdf".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_pdf")
    def pdf(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/tax/forms/{id}/pdf".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
