# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
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

if TYPE_CHECKING:
    from stripe.api_resources.billing_portal.configuration import Configuration


class Session(CreateableAPIResource["Session"]):
    """
    The Billing customer portal is a Stripe-hosted UI for subscription and
    billing management.

    A portal configuration describes the functionality and features that you
    want to provide to your customers through the portal.

    A portal session describes the instantiation of the customer portal for
    a particular customer. By visiting the session's URL, the customer
    can manage their subscriptions and billing details. For security reasons,
    sessions are short-lived and will expire if the customer does not visit the URL.
    Create sessions on-demand when customers intend to manage their subscriptions
    and billing details.

    Learn more in the [integration guide](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal).
    """

    OBJECT_NAME = "billing_portal.session"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            configuration: NotRequired["str|None"]
            customer: str
            expand: NotRequired["List[str]|None"]
            flow_data: NotRequired["Session.CreateParamsFlowData|None"]
            locale: NotRequired[
                "Literal['auto', 'bg', 'cs', 'da', 'de', 'el', 'en', 'en-AU', 'en-CA', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-SG', 'es', 'es-419', 'et', 'fi', 'fil', 'fr', 'fr-CA', 'hr', 'hu', 'id', 'it', 'ja', 'ko', 'lt', 'lv', 'ms', 'mt', 'nb', 'nl', 'pl', 'pt', 'pt-BR', 'ro', 'ru', 'sk', 'sl', 'sv', 'th', 'tr', 'vi', 'zh', 'zh-HK', 'zh-TW']|None"
            ]
            on_behalf_of: NotRequired["str|None"]
            return_url: NotRequired["str|None"]

        class CreateParamsFlowData(TypedDict):
            after_completion: NotRequired[
                "Session.CreateParamsFlowDataAfterCompletion|None"
            ]
            subscription_cancel: NotRequired[
                "Session.CreateParamsFlowDataSubscriptionCancel|None"
            ]
            subscription_update: NotRequired[
                "Session.CreateParamsFlowDataSubscriptionUpdate|None"
            ]
            subscription_update_confirm: NotRequired[
                "Session.CreateParamsFlowDataSubscriptionUpdateConfirm|None"
            ]
            type: Literal[
                "payment_method_update",
                "subscription_cancel",
                "subscription_update",
                "subscription_update_confirm",
            ]

        class CreateParamsFlowDataSubscriptionUpdateConfirm(TypedDict):
            discounts: NotRequired[
                "List[Session.CreateParamsFlowDataSubscriptionUpdateConfirmDiscount]|None"
            ]
            items: List[
                "Session.CreateParamsFlowDataSubscriptionUpdateConfirmItem"
            ]
            subscription: str

        class CreateParamsFlowDataSubscriptionUpdateConfirmItem(TypedDict):
            id: str
            price: NotRequired["str|None"]
            quantity: NotRequired["int|None"]

        class CreateParamsFlowDataSubscriptionUpdateConfirmDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            promotion_code: NotRequired["str|None"]

        class CreateParamsFlowDataSubscriptionUpdate(TypedDict):
            subscription: str

        class CreateParamsFlowDataSubscriptionCancel(TypedDict):
            retention: NotRequired[
                "Session.CreateParamsFlowDataSubscriptionCancelRetention|None"
            ]
            subscription: str

        class CreateParamsFlowDataSubscriptionCancelRetention(TypedDict):
            coupon_offer: "Session.CreateParamsFlowDataSubscriptionCancelRetentionCouponOffer"
            type: Literal["coupon_offer"]

        class CreateParamsFlowDataSubscriptionCancelRetentionCouponOffer(
            TypedDict,
        ):
            coupon: str

        class CreateParamsFlowDataAfterCompletion(TypedDict):
            hosted_confirmation: NotRequired[
                "Session.CreateParamsFlowDataAfterCompletionHostedConfirmation|None"
            ]
            redirect: NotRequired[
                "Session.CreateParamsFlowDataAfterCompletionRedirect|None"
            ]
            type: Literal["hosted_confirmation", "portal_homepage", "redirect"]

        class CreateParamsFlowDataAfterCompletionRedirect(TypedDict):
            return_url: str

        class CreateParamsFlowDataAfterCompletionHostedConfirmation(TypedDict):
            custom_message: NotRequired["str|None"]

    configuration: ExpandableField["Configuration"]
    created: int
    customer: str
    flow: Optional[StripeObject]
    id: str
    livemode: bool
    locale: Optional[
        Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-SG",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ]
    object: Literal["billing_portal.session"]
    on_behalf_of: Optional[str]
    return_url: Optional[str]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.CreateParams"]
    ) -> "Session":
        return cast(
            "Session",
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
