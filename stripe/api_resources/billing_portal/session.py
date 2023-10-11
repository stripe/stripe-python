# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

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

    class Flow(StripeObject):
        class AfterCompletion(StripeObject):
            class HostedConfirmation(StripeObject):
                custom_message: Optional[str]

            class Redirect(StripeObject):
                return_url: str

            hosted_confirmation: Optional[HostedConfirmation]
            redirect: Optional[Redirect]
            type: Literal["hosted_confirmation", "portal_homepage", "redirect"]
            _inner_class_types = {
                "hosted_confirmation": HostedConfirmation,
                "redirect": Redirect,
            }

        class SubscriptionCancel(StripeObject):
            class Retention(StripeObject):
                class CouponOffer(StripeObject):
                    coupon: str

                coupon_offer: Optional[CouponOffer]
                type: Literal["coupon_offer"]
                _inner_class_types = {"coupon_offer": CouponOffer}

            retention: Optional[Retention]
            subscription: str
            _inner_class_types = {"retention": Retention}

        class SubscriptionUpdate(StripeObject):
            subscription: str

        class SubscriptionUpdateConfirm(StripeObject):
            class Discount(StripeObject):
                coupon: Optional[str]
                promotion_code: Optional[str]

            class Item(StripeObject):
                id: Optional[str]
                price: Optional[str]
                quantity: Optional[int]

            discounts: Optional[List[Discount]]
            items: List[Item]
            subscription: str
            _inner_class_types = {"discounts": Discount, "items": Item}

        after_completion: AfterCompletion
        subscription_cancel: Optional[SubscriptionCancel]
        subscription_update: Optional[SubscriptionUpdate]
        subscription_update_confirm: Optional[SubscriptionUpdateConfirm]
        type: Literal[
            "payment_method_update",
            "subscription_cancel",
            "subscription_update",
            "subscription_update_confirm",
        ]
        _inner_class_types = {
            "after_completion": AfterCompletion,
            "subscription_cancel": SubscriptionCancel,
            "subscription_update": SubscriptionUpdate,
            "subscription_update_confirm": SubscriptionUpdateConfirm,
        }

    configuration: ExpandableField["Configuration"]
    created: int
    customer: str
    flow: Optional[Flow]
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
        **params: Any
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

    _inner_class_types = {"flow": Flow}
