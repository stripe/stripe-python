# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


class AccountSession(CreateableAPIResource["AccountSession"]):
    """
    An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

    We recommend that you create an AccountSession each time you need to display an embedded component
    to your user. Do not save AccountSessions to your database as they expire relatively
    quickly, and cannot be used more than once.

    Related guide: [Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components)
    """

    OBJECT_NAME = "account_session"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account: str
            components: "AccountSession.CreateParamsComponents"
            expand: NotRequired["List[str]|None"]

        class CreateParamsComponents(TypedDict):
            account_onboarding: NotRequired[
                "AccountSession.CreateParamsComponentsAccountOnboarding|None"
            ]

        class CreateParamsComponentsAccountOnboarding(TypedDict):
            enabled: bool

    account: str
    client_secret: str
    components: StripeObject
    expires_at: int
    livemode: bool
    object: Literal["account_session"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["AccountSession.CreateParams"]
    ) -> "AccountSession":
        return cast(
            "AccountSession",
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
