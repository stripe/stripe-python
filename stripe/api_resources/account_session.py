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

    class Components(StripeObject):
        class AccountOnboarding(StripeObject):
            enabled: bool

        class PaymentDetails(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                dispute_management: bool
                refund_management: bool

            enabled: bool
            features: Optional[Features]
            _inner_class_types = {"features": Features}

        class Payments(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                dispute_management: bool
                refund_management: bool

            enabled: bool
            features: Optional[Features]
            _inner_class_types = {"features": Features}

        class Payouts(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            features: Optional[Features]
            _inner_class_types = {"features": Features}

        account_onboarding: AccountOnboarding
        payment_details: Optional[PaymentDetails]
        payments: Optional[Payments]
        payouts: Optional[Payouts]
        _inner_class_types = {
            "account_onboarding": AccountOnboarding,
            "payment_details": PaymentDetails,
            "payments": Payments,
            "payouts": Payouts,
        }

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account: str
            components: "AccountSession.CreateParamsComponents"
            expand: NotRequired["List[str]|None"]

        class CreateParamsComponents(TypedDict):
            account_onboarding: NotRequired[
                "AccountSession.CreateParamsComponentsAccountOnboarding|None"
            ]
            payment_details: NotRequired[
                "AccountSession.CreateParamsComponentsPaymentDetails|None"
            ]
            payments: NotRequired[
                "AccountSession.CreateParamsComponentsPayments|None"
            ]
            payouts: NotRequired[
                "AccountSession.CreateParamsComponentsPayouts|None"
            ]

        class CreateParamsComponentsPayouts(TypedDict):
            enabled: bool
            features: NotRequired[
                "AccountSession.CreateParamsComponentsPayoutsFeatures|None"
            ]

        class CreateParamsComponentsPayoutsFeatures(TypedDict):
            pass

        class CreateParamsComponentsPayments(TypedDict):
            enabled: bool
            features: NotRequired[
                "AccountSession.CreateParamsComponentsPaymentsFeatures|None"
            ]

        class CreateParamsComponentsPaymentsFeatures(TypedDict):
            capture_payments: NotRequired["bool|None"]
            dispute_management: NotRequired["bool|None"]
            refund_management: NotRequired["bool|None"]

        class CreateParamsComponentsPaymentDetails(TypedDict):
            enabled: bool
            features: NotRequired[
                "AccountSession.CreateParamsComponentsPaymentDetailsFeatures|None"
            ]

        class CreateParamsComponentsPaymentDetailsFeatures(TypedDict):
            capture_payments: NotRequired["bool|None"]
            dispute_management: NotRequired["bool|None"]
            refund_management: NotRequired["bool|None"]

        class CreateParamsComponentsAccountOnboarding(TypedDict):
            enabled: bool
            features: NotRequired[
                "AccountSession.CreateParamsComponentsAccountOnboardingFeatures|None"
            ]

        class CreateParamsComponentsAccountOnboardingFeatures(TypedDict):
            pass

    account: str
    client_secret: str
    components: Components
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

    _inner_class_types = {"components": Components}
