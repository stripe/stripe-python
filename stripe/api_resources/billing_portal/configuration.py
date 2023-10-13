# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            business_profile: "Configuration.CreateParamsBusinessProfile"
            default_return_url: NotRequired["Literal['']|str|None"]
            expand: NotRequired["List[str]|None"]
            features: "Configuration.CreateParamsFeatures"
            login_page: NotRequired["Configuration.CreateParamsLoginPage|None"]
            metadata: NotRequired["Dict[str, str]|None"]

        class CreateParamsLoginPage(TypedDict):
            enabled: bool

        class CreateParamsFeatures(TypedDict):
            customer_update: NotRequired[
                "Configuration.CreateParamsFeaturesCustomerUpdate|None"
            ]
            invoice_history: NotRequired[
                "Configuration.CreateParamsFeaturesInvoiceHistory|None"
            ]
            payment_method_update: NotRequired[
                "Configuration.CreateParamsFeaturesPaymentMethodUpdate|None"
            ]
            subscription_cancel: NotRequired[
                "Configuration.CreateParamsFeaturesSubscriptionCancel|None"
            ]
            subscription_pause: NotRequired[
                "Configuration.CreateParamsFeaturesSubscriptionPause|None"
            ]
            subscription_update: NotRequired[
                "Configuration.CreateParamsFeaturesSubscriptionUpdate|None"
            ]

        class CreateParamsFeaturesSubscriptionUpdate(TypedDict):
            default_allowed_updates: Union[
                Literal[""],
                List[Literal["price", "promotion_code", "quantity"]],
            ]
            enabled: bool
            products: Union[
                Literal[""],
                List[
                    "Configuration.CreateParamsFeaturesSubscriptionUpdateProduct"
                ],
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class CreateParamsFeaturesSubscriptionUpdateProduct(TypedDict):
            prices: List[str]
            product: str

        class CreateParamsFeaturesSubscriptionPause(TypedDict):
            enabled: NotRequired["bool|None"]

        class CreateParamsFeaturesSubscriptionCancel(TypedDict):
            cancellation_reason: NotRequired[
                "Configuration.CreateParamsFeaturesSubscriptionCancelCancellationReason|None"
            ]
            enabled: bool
            mode: NotRequired["Literal['at_period_end', 'immediately']|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class CreateParamsFeaturesSubscriptionCancelCancellationReason(
            TypedDict,
        ):
            enabled: bool
            options: Union[
                Literal[""],
                List[
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
                ],
            ]

        class CreateParamsFeaturesPaymentMethodUpdate(TypedDict):
            enabled: bool

        class CreateParamsFeaturesInvoiceHistory(TypedDict):
            enabled: bool

        class CreateParamsFeaturesCustomerUpdate(TypedDict):
            allowed_updates: NotRequired[
                "Literal['']|List[Literal['address', 'email', 'name', 'phone', 'shipping', 'tax_id']]|None"
            ]
            enabled: bool

        class CreateParamsBusinessProfile(TypedDict):
            headline: NotRequired["Literal['']|str|None"]
            privacy_policy_url: NotRequired["str|None"]
            terms_of_service_url: NotRequired["str|None"]

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            is_default: NotRequired["bool|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            business_profile: NotRequired[
                "Configuration.ModifyParamsBusinessProfile|None"
            ]
            default_return_url: NotRequired["Literal['']|str|None"]
            expand: NotRequired["List[str]|None"]
            features: NotRequired["Configuration.ModifyParamsFeatures|None"]
            login_page: NotRequired["Configuration.ModifyParamsLoginPage|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ModifyParamsLoginPage(TypedDict):
            enabled: bool

        class ModifyParamsFeatures(TypedDict):
            customer_update: NotRequired[
                "Configuration.ModifyParamsFeaturesCustomerUpdate|None"
            ]
            invoice_history: NotRequired[
                "Configuration.ModifyParamsFeaturesInvoiceHistory|None"
            ]
            payment_method_update: NotRequired[
                "Configuration.ModifyParamsFeaturesPaymentMethodUpdate|None"
            ]
            subscription_cancel: NotRequired[
                "Configuration.ModifyParamsFeaturesSubscriptionCancel|None"
            ]
            subscription_pause: NotRequired[
                "Configuration.ModifyParamsFeaturesSubscriptionPause|None"
            ]
            subscription_update: NotRequired[
                "Configuration.ModifyParamsFeaturesSubscriptionUpdate|None"
            ]

        class ModifyParamsFeaturesSubscriptionUpdate(TypedDict):
            default_allowed_updates: NotRequired[
                "Literal['']|List[Literal['price', 'promotion_code', 'quantity']]|None"
            ]
            enabled: NotRequired["bool|None"]
            products: NotRequired[
                "Literal['']|List[Configuration.ModifyParamsFeaturesSubscriptionUpdateProduct]|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class ModifyParamsFeaturesSubscriptionUpdateProduct(TypedDict):
            prices: List[str]
            product: str

        class ModifyParamsFeaturesSubscriptionPause(TypedDict):
            enabled: NotRequired["bool|None"]

        class ModifyParamsFeaturesSubscriptionCancel(TypedDict):
            cancellation_reason: NotRequired[
                "Configuration.ModifyParamsFeaturesSubscriptionCancelCancellationReason|None"
            ]
            enabled: NotRequired["bool|None"]
            mode: NotRequired["Literal['at_period_end', 'immediately']|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class ModifyParamsFeaturesSubscriptionCancelCancellationReason(
            TypedDict,
        ):
            enabled: bool
            options: NotRequired[
                "Literal['']|List[Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']]|None"
            ]

        class ModifyParamsFeaturesPaymentMethodUpdate(TypedDict):
            enabled: bool

        class ModifyParamsFeaturesInvoiceHistory(TypedDict):
            enabled: bool

        class ModifyParamsFeaturesCustomerUpdate(TypedDict):
            allowed_updates: NotRequired[
                "Literal['']|List[Literal['address', 'email', 'name', 'phone', 'shipping', 'tax_id']]|None"
            ]
            enabled: NotRequired["bool|None"]

        class ModifyParamsBusinessProfile(TypedDict):
            headline: NotRequired["Literal['']|str|None"]
            privacy_policy_url: NotRequired["Literal['']|str|None"]
            terms_of_service_url: NotRequired["Literal['']|str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    active: bool
    application: Optional[ExpandableField["Application"]]
    business_profile: StripeObject
    created: int
    default_return_url: Optional[str]
    features: StripeObject
    id: str
    is_default: bool
    livemode: bool
    login_page: StripeObject
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
        **params: Unpack["Configuration.CreateParams"]
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
        **params: Unpack["Configuration.ListParams"]
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
    def modify(
        cls, id, **params: Unpack["Configuration.ModifyParams"]
    ) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Configuration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Configuration.RetrieveParams"]
    ) -> "Configuration":
        instance = cls(id, **params)
        instance.refresh()
        return instance
