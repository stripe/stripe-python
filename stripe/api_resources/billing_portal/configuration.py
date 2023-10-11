# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        business_profile: "Configuration.CreateBusinessProfileParams"
        default_return_url: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]
        features: "Configuration.CreateFeaturesParams"
        login_page: NotRequired[
            Optional["Configuration.CreateLoginPageParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]

    class CreateLoginPageParams(TypedDict):
        enabled: bool

    class CreateFeaturesParams(TypedDict):
        customer_update: NotRequired[
            Optional["Configuration.CreateFeaturesCustomerUpdateParams"]
        ]
        invoice_history: NotRequired[
            Optional["Configuration.CreateFeaturesInvoiceHistoryParams"]
        ]
        payment_method_update: NotRequired[
            Optional["Configuration.CreateFeaturesPaymentMethodUpdateParams"]
        ]
        subscription_cancel: NotRequired[
            Optional["Configuration.CreateFeaturesSubscriptionCancelParams"]
        ]
        subscription_pause: NotRequired[
            Optional["Configuration.CreateFeaturesSubscriptionPauseParams"]
        ]
        subscription_update: NotRequired[
            Optional["Configuration.CreateFeaturesSubscriptionUpdateParams"]
        ]

    class CreateFeaturesSubscriptionUpdateParams(TypedDict):
        default_allowed_updates: Union[
            Literal[""], List[Literal["price", "promotion_code", "quantity"]]
        ]
        enabled: bool
        products: Union[
            Literal[""],
            List[
                "Configuration.CreateFeaturesSubscriptionUpdateProductParams"
            ],
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class CreateFeaturesSubscriptionUpdateProductParams(TypedDict):
        prices: List[str]
        product: str

    class CreateFeaturesSubscriptionPauseParams(TypedDict):
        enabled: NotRequired[Optional[bool]]

    class CreateFeaturesSubscriptionCancelParams(TypedDict):
        cancellation_reason: NotRequired[
            Optional[
                "Configuration.CreateFeaturesSubscriptionCancelCancellationReasonParams"
            ]
        ]
        enabled: bool
        mode: NotRequired[Optional[Literal["at_period_end", "immediately"]]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class CreateFeaturesSubscriptionCancelCancellationReasonParams(TypedDict):
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

    class CreateFeaturesPaymentMethodUpdateParams(TypedDict):
        enabled: bool

    class CreateFeaturesInvoiceHistoryParams(TypedDict):
        enabled: bool

    class CreateFeaturesCustomerUpdateParams(TypedDict):
        allowed_updates: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        Literal[
                            "address",
                            "email",
                            "name",
                            "phone",
                            "shipping",
                            "tax_id",
                        ]
                    ],
                ]
            ]
        ]
        enabled: bool

    class CreateBusinessProfileParams(TypedDict):
        headline: NotRequired[Optional[Union[Literal[""], str]]]
        privacy_policy_url: NotRequired[Optional[str]]
        terms_of_service_url: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        is_default: NotRequired[Optional[bool]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        business_profile: NotRequired[
            Optional["Configuration.ModifyBusinessProfileParams"]
        ]
        default_return_url: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[Optional["Configuration.ModifyFeaturesParams"]]
        login_page: NotRequired[
            Optional["Configuration.ModifyLoginPageParams"]
        ]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ModifyLoginPageParams(TypedDict):
        enabled: bool

    class ModifyFeaturesParams(TypedDict):
        customer_update: NotRequired[
            Optional["Configuration.ModifyFeaturesCustomerUpdateParams"]
        ]
        invoice_history: NotRequired[
            Optional["Configuration.ModifyFeaturesInvoiceHistoryParams"]
        ]
        payment_method_update: NotRequired[
            Optional["Configuration.ModifyFeaturesPaymentMethodUpdateParams"]
        ]
        subscription_cancel: NotRequired[
            Optional["Configuration.ModifyFeaturesSubscriptionCancelParams"]
        ]
        subscription_pause: NotRequired[
            Optional["Configuration.ModifyFeaturesSubscriptionPauseParams"]
        ]
        subscription_update: NotRequired[
            Optional["Configuration.ModifyFeaturesSubscriptionUpdateParams"]
        ]

    class ModifyFeaturesSubscriptionUpdateParams(TypedDict):
        default_allowed_updates: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[Literal["price", "promotion_code", "quantity"]],
                ]
            ]
        ]
        enabled: NotRequired[Optional[bool]]
        products: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "Configuration.ModifyFeaturesSubscriptionUpdateProductParams"
                    ],
                ]
            ]
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class ModifyFeaturesSubscriptionUpdateProductParams(TypedDict):
        prices: List[str]
        product: str

    class ModifyFeaturesSubscriptionPauseParams(TypedDict):
        enabled: NotRequired[Optional[bool]]

    class ModifyFeaturesSubscriptionCancelParams(TypedDict):
        cancellation_reason: NotRequired[
            Optional[
                "Configuration.ModifyFeaturesSubscriptionCancelCancellationReasonParams"
            ]
        ]
        enabled: NotRequired[Optional[bool]]
        mode: NotRequired[Optional[Literal["at_period_end", "immediately"]]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class ModifyFeaturesSubscriptionCancelCancellationReasonParams(TypedDict):
        enabled: bool
        options: NotRequired[
            Optional[
                Union[
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
            ]
        ]

    class ModifyFeaturesPaymentMethodUpdateParams(TypedDict):
        enabled: bool

    class ModifyFeaturesInvoiceHistoryParams(TypedDict):
        enabled: bool

    class ModifyFeaturesCustomerUpdateParams(TypedDict):
        allowed_updates: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        Literal[
                            "address",
                            "email",
                            "name",
                            "phone",
                            "shipping",
                            "tax_id",
                        ]
                    ],
                ]
            ]
        ]
        enabled: NotRequired[Optional[bool]]

    class ModifyBusinessProfileParams(TypedDict):
        headline: NotRequired[Optional[Union[Literal[""], str]]]
        privacy_policy_url: NotRequired[Optional[Union[Literal[""], str]]]
        terms_of_service_url: NotRequired[Optional[Union[Literal[""], str]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
