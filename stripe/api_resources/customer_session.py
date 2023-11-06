# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer


class CustomerSession(CreateableAPIResource["CustomerSession"]):
    """
    A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
    control over a customer.
    """

    OBJECT_NAME: ClassVar[Literal["customer_session"]] = "customer_session"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            customer: str
            """
            The ID of an existing customer for which to create the customer session.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

    client_secret: str
    """
    The client secret of this customer session. Used on the client to set up secure access to the given `customer`.

    The client secret can be used to provide access to `customer` from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.
    """
    customer: ExpandableField["Customer"]
    """
    The customer the customer session was created for.
    """
    expires_at: int
    """
    The timestamp at which this customer session will expire.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["customer_session"]
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
        **params: Unpack["CustomerSession.CreateParams"]
    ) -> "CustomerSession":
        """
        Creates a customer session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.
        """
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
