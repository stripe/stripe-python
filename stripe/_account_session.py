# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, cast
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
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class PaymentDetails(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                """
                Whether to allow capturing and cancelling payment intents. This is `true` by default.
                """
                dispute_management: bool
                """
                Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether to allow sending refunds. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Payments(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                """
                Whether to allow capturing and cancelling payment intents. This is `true` by default.
                """
                dispute_management: bool
                """
                Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether to allow sending refunds. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Payouts(StripeObject):
            class Features(StripeObject):
                edit_payout_schedule: bool
                """
                Whether to allow payout schedule to be changed. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
                """
                instant_payouts: bool
                """
                Whether to allow creation of instant payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
                """
                standard_payouts: bool
                """
                Whether to allow creation of standard payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        account_onboarding: AccountOnboarding
        payment_details: PaymentDetails
        payments: Payments
        payouts: Payouts
        _inner_class_types = {
            "account_onboarding": AccountOnboarding,
            "payment_details": PaymentDetails,
            "payments": Payments,
            "payouts": Payouts,
        }

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
        payment_details: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentDetails"
        ]
        """
        Configuration for the payment details embedded component.
        """
        payments: NotRequired["AccountSession.CreateParamsComponentsPayments"]
        """
        Configuration for the payments embedded component.
        """
        payouts: NotRequired["AccountSession.CreateParamsComponentsPayouts"]
        """
        Configuration for the payouts embedded component.
        """

    class CreateParamsComponentsAccountOnboarding(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsAccountOnboardingFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsAccountOnboardingFeatures(TypedDict):
        pass

    class CreateParamsComponentsPaymentDetails(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentDetailsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentDetailsFeatures(TypedDict):
        capture_payments: NotRequired["bool"]
        """
        Whether to allow capturing and cancelling payment intents. This is `true` by default.
        """
        dispute_management: NotRequired["bool"]
        """
        Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired["bool"]
        """
        Whether to allow sending refunds. This is `true` by default.
        """

    class CreateParamsComponentsPayments(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentsFeatures(TypedDict):
        capture_payments: NotRequired["bool"]
        """
        Whether to allow capturing and cancelling payment intents. This is `true` by default.
        """
        dispute_management: NotRequired["bool"]
        """
        Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired["bool"]
        """
        Whether to allow sending refunds. This is `true` by default.
        """

    class CreateParamsComponentsPayouts(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPayoutsFeatures(TypedDict):
        edit_payout_schedule: NotRequired["bool"]
        """
        Whether to allow payout schedule to be changed. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
        """
        instant_payouts: NotRequired["bool"]
        """
        Whether to allow creation of instant payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
        """
        standard_payouts: NotRequired["bool"]
        """
        Whether to allow creation of standard payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
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
        cls, **params: Unpack["AccountSession.CreateParams"]
    ) -> "AccountSession":
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
        return cast(
            "AccountSession",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"components": Components}
