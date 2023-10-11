# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack


class AccountLink(CreateableAPIResource["AccountLink"]):
    """
    Account Links are the means by which a Connect platform grants a connected account permission to access
    Stripe-hosted applications, such as Connect Onboarding.

    Related guide: [Connect Onboarding](https://stripe.com/docs/connect/custom/hosted-onboarding)
    """

    OBJECT_NAME = "account_link"

    class CreateParams(RequestOptions):
        account: str
        collect: NotRequired[
            Optional[Literal["currently_due", "eventually_due"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        refresh_url: NotRequired[Optional[str]]
        return_url: NotRequired[Optional[str]]
        type: Literal["account_onboarding", "account_update"]

    created: int
    expires_at: int
    object: Literal["account_link"]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["AccountLink.CreateParams"]
    ) -> "AccountLink":
        return cast(
            "AccountLink",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )
