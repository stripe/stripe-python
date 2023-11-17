# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class AccountSession(CreateableAPIResource["AccountSession"]):
    """
    An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

    We recommend that you create an AccountSession each time you need to display an embedded component
    to your user. Do not save AccountSessions to your database as they expire relatively
    quickly, and cannot be used more than once.

    Related guide: [Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components)
    """

    OBJECT_NAME: ClassVar[Literal["account_session"]] = "account_session"

    class Components(StripeObject):
        class AccountOnboarding(StripeObject):
            enabled: bool
            """
            Whether the embedded component is enabled.
            """

        account_onboarding: AccountOnboarding
        _inner_class_types = {"account_onboarding": AccountOnboarding}

    class CreateParams(RequestOptions):
        account: str
        """
        The identifier of the account to create an Account Session for.
        """
        components: "AccountSession.CreateParamsComponents"
        """
        Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParamsComponents(TypedDict):
        account_onboarding: NotRequired[
            "AccountSession.CreateParamsComponentsAccountOnboarding"
        ]
        """
        Configuration for the account onboarding embedded component.
        """

    class CreateParamsComponentsAccountOnboarding(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """

    account: str
    """
    The ID of the account the AccountSession was created for
    """
    client_secret: str
    """
    The client secret of this AccountSession. Used on the client to set up secure access to the given `account`.

    The client secret can be used to provide access to `account` from your frontend. It should not be stored, logged, or exposed to anyone other than the connected account. Make sure that you have TLS enabled on any page that includes the client secret.

    Refer to our docs to [setup Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components) and learn about how `client_secret` should be handled.
    """
    components: Components
    expires_at: int
    """
    The timestamp at which this AccountSession will expire.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["account_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "AccountSession.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "AccountSession":
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
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

    _inner_class_types = {"components": Components}
