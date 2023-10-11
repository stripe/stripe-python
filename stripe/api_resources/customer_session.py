# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from typing import Any, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer


class CustomerSession(CreateableAPIResource["CustomerSession"]):
    """
    A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
    control over a customer.
    """

    OBJECT_NAME = "customer_session"
    client_secret: str
    customer: ExpandableField["Customer"]
    expires_at: int
    livemode: bool
    object: Literal["customer_session"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "CustomerSession":
        return cast(
            "CustomerSession",
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
