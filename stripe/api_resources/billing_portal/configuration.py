# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.application import Application


class Configuration(
    CreateableAPIResource["Configuration"],
    ListableAPIResource["Configuration"],
    UpdateableAPIResource["Configuration"],
):
    """
    A portal configuration describes the functionality and behavior of a portal session.
    """

    OBJECT_NAME = "billing_portal.configuration"

    class BusinessProfile(StripeObject):
        headline: Optional[str]
        privacy_policy_url: Optional[str]
        terms_of_service_url: Optional[str]

    class Features(StripeObject):
        class CustomerUpdate(StripeObject):
            allowed_updates: List[
                Literal[
                    "address", "email", "name", "phone", "shipping", "tax_id"
                ]
            ]
            enabled: bool

        class InvoiceHistory(StripeObject):
            enabled: bool

        class PaymentMethodUpdate(StripeObject):
            enabled: bool

        class SubscriptionCancel(StripeObject):
            class CancellationReason(StripeObject):
                enabled: bool
                options: List[
                    Literal[
                        "customer_service",
                        "low_quality",
                        "missing_features",
                        "other",
                        "switched_service",
                        "too_complex",
                        "too_expensive",
                        "unused",
                    ]
                ]

            cancellation_reason: CancellationReason
            enabled: bool
            mode: Literal["at_period_end", "immediately"]
            proration_behavior: Literal[
                "always_invoice", "create_prorations", "none"
            ]
            _inner_class_types = {"cancellation_reason": CancellationReason}

        class SubscriptionPause(StripeObject):
            enabled: bool

        class SubscriptionUpdate(StripeObject):
            class Product(StripeObject):
                prices: List[str]
                product: str

            default_allowed_updates: List[
                Literal["price", "promotion_code", "quantity"]
            ]
            enabled: bool
            products: Optional[List[Product]]
            proration_behavior: Literal[
                "always_invoice", "create_prorations", "none"
            ]
            _inner_class_types = {"products": Product}

        customer_update: CustomerUpdate
        invoice_history: InvoiceHistory
        payment_method_update: PaymentMethodUpdate
        subscription_cancel: SubscriptionCancel
        subscription_pause: SubscriptionPause
        subscription_update: SubscriptionUpdate
        _inner_class_types = {
            "customer_update": CustomerUpdate,
            "invoice_history": InvoiceHistory,
            "payment_method_update": PaymentMethodUpdate,
            "subscription_cancel": SubscriptionCancel,
            "subscription_pause": SubscriptionPause,
            "subscription_update": SubscriptionUpdate,
        }

    class LoginPage(StripeObject):
        enabled: bool
        url: Optional[str]

    active: bool
    application: Optional[ExpandableField["Application"]]
    business_profile: BusinessProfile
    created: int
    default_return_url: Optional[str]
    features: Features
    id: str
    is_default: bool
    livemode: bool
    login_page: LoginPage
    metadata: Optional[Dict[str, str]]
    object: Literal["billing_portal.configuration"]
    updated: int

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Configuration":
        return cast(
            "Configuration",
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

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Configuration"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Any) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Configuration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Configuration":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "business_profile": BusinessProfile,
        "features": Features,
        "login_page": LoginPage,
    }
