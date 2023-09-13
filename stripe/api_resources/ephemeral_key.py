# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import DeletableAPIResource
from typing_extensions import Literal


class EphemeralKey(DeletableAPIResource["EphemeralKey"]):
    OBJECT_NAME = "ephemeral_key"
    created: str
    expires: str
    id: str
    livemode: bool
    object: Literal["ephemeral_key"]
    secret: str

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        if stripe_version is None:
            raise ValueError(
                "stripe_version must be specified to create an ephemeral "
                "key"
            )

        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )

        url = cls.class_url()
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)
        return util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
