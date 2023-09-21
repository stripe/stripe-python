# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract import DeletableAPIResource
from typing import Any, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class EphemeralKey(DeletableAPIResource["EphemeralKey"]):
    OBJECT_NAME = "ephemeral_key"
    created: int
    expires: int
    id: str
    livemode: bool
    object: Literal["ephemeral_key"]
    secret: Optional[str]

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> "EphemeralKey":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "EphemeralKey",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "EphemeralKey":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

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
