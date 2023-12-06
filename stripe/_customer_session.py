# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._customer import Customer


class CustomerSession(CreateableAPIResource["CustomerSession"]):
    """
    A customer session allows you to grant client access to Stripe's frontend SDKs (like StripeJs)
    control over a customer.
    """

    OBJECT_NAME: ClassVar[Literal["customer_session"]] = "customer_session"

    class Components(StripeObject):
        class PaymentElement(StripeObject):
            class Features(StripeObject):
                payment_method_remove: Literal["auto", "never"]
                """
                Controls whether the Payment Element allows the removal of a saved payment method.
                """
                payment_method_save: Literal["auto", "never"]
                """
                Controls whether the Payment Element offers to save a new payment method.
                """
                payment_method_set_as_default: Literal["auto", "never"]
                """
                Controls whether the Payment Element offers to set a payment method as the default.
                """
                payment_method_update: Literal["auto", "never"]
                """
                Controls whether the Payment Element allows the updating of a saved payment method.
                """

            enabled: bool
            """
            Whether the payment element is enabled.
            """
            features: Optional[Features]
            """
            This hash defines whether the payment element supports certain features.
            """
            _inner_class_types = {"features": Features}

        class PricingTable(StripeObject):
            enabled: bool
            """
            Whether the pricing table is enabled.
            """

        payment_element: Optional[PaymentElement]
        """
        This hash contains whether the payment element is enabled and the features it supports.
        """
        pricing_table: Optional[PricingTable]
        """
        This hash contains whether the pricing table is enabled.
        """
        _inner_class_types = {
            "payment_element": PaymentElement,
            "pricing_table": PricingTable,
        }

    class CreateParams(RequestOptions):
        components: "CustomerSession.CreateParamsComponents"
        """
        Configuration for each component.
        """
        customer: str
        """
        The ID of an existing customer for which to create the customer session.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParamsComponents(TypedDict):
        payment_element: NotRequired[
            "CustomerSession.CreateParamsComponentsPaymentElement"
        ]
        """
        Configuration for the payment element.
        """
        pricing_table: NotRequired[
            "CustomerSession.CreateParamsComponentsPricingTable"
        ]
        """
        Configuration for the pricing table.
        """

    class CreateParamsComponentsPricingTable(TypedDict):
        enabled: bool
        """
        Whether the pricing table is enabled.
        """

    class CreateParamsComponentsPaymentElement(TypedDict):
        enabled: bool
        """
        Whether the payment element is enabled.
        """
        features: NotRequired[
            "CustomerSession.CreateParamsComponentsPaymentElementFeatures"
        ]
        """
        This hash defines whether the payment element supports certain features.
        """

    class CreateParamsComponentsPaymentElementFeatures(TypedDict):
        payment_method_remove: NotRequired["Literal['auto', 'never']"]
        """
        Controls whether the Payment Element allows the removal of a saved payment method.
        """
        payment_method_save: NotRequired["Literal['auto', 'never']"]
        """
        Controls whether the Payment Element offers to save a new payment method.
        """
        payment_method_set_as_default: NotRequired["Literal['auto', 'never']"]
        """
        Controls whether the Payment Element offers to set a payment method as the default.
        """
        payment_method_update: NotRequired["Literal['auto', 'never']"]
        """
        Controls whether the Payment Element allows the updating of a saved payment method.
        """

    client_secret: str
    """
    The client secret of this customer session. Used on the client to set up secure access to the given `customer`.

    The client secret can be used to provide access to `customer` from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.
    """
    components: Optional[Components]
    """
    Configuration for the components supported by this customer session.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
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
        **params: Unpack[
            "CustomerSession.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
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

    _inner_class_types = {"components": Components}
