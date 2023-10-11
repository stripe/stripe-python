# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
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
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.test_helpers.test_clock import TestClock


class SubscriptionSchedule(
    CreateableAPIResource["SubscriptionSchedule"],
    ListableAPIResource["SubscriptionSchedule"],
    UpdateableAPIResource["SubscriptionSchedule"],
):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)
    """

    OBJECT_NAME = "subscription_schedule"

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        invoice_now: NotRequired[Optional[bool]]
        prorate: NotRequired[Optional[bool]]

    class CreateParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        default_settings: NotRequired[
            Optional["SubscriptionSchedule.CreateDefaultSettingsParams"]
        ]
        end_behavior: NotRequired[
            Optional[Literal["cancel", "none", "release", "renew"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        from_subscription: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        phases: NotRequired[
            Optional[List["SubscriptionSchedule.CreatePhaseParams"]]
        ]
        start_date: NotRequired[Optional[Union[int, Literal["now"]]]]

    class CreatePhaseParams(TypedDict):
        add_invoice_items: NotRequired[
            Optional[
                List["SubscriptionSchedule.CreatePhaseAddInvoiceItemParams"]
            ]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["SubscriptionSchedule.CreatePhaseAutomaticTaxParams"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreatePhaseItemBillingThresholdsParams",
                ]
            ]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        coupon: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        default_payment_method: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        end_date: NotRequired[Optional[int]]
        invoice_settings: NotRequired[
            Optional["SubscriptionSchedule.CreatePhaseInvoiceSettingsParams"]
        ]
        items: List["SubscriptionSchedule.CreatePhaseItemParams"]
        iterations: NotRequired[Optional[int]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        transfer_data: NotRequired[
            Optional["SubscriptionSchedule.CreatePhaseTransferDataParams"]
        ]
        trial: NotRequired[Optional[bool]]
        trial_end: NotRequired[Optional[int]]

    class CreatePhaseTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreatePhaseItemParams(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreatePhaseItemBillingThresholdsParams",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionSchedule.CreatePhaseItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreatePhaseItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionSchedule.CreatePhaseItemPriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreatePhaseItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreatePhaseItemBillingThresholdsParams(TypedDict):
        usage_gte: int

    class CreatePhaseInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class CreatePhaseBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreatePhaseAutomaticTaxParams(TypedDict):
        enabled: bool

    class CreatePhaseAddInvoiceItemParams(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional[
                "SubscriptionSchedule.CreatePhaseAddInvoiceItemPriceDataParams"
            ]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreatePhaseAddInvoiceItemPriceDataParams(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateDefaultSettingsParams(TypedDict):
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional[
                "SubscriptionSchedule.CreateDefaultSettingsAutomaticTaxParams"
            ]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateDefaultSettingsBillingThresholdsParams",
                ]
            ]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        default_payment_method: NotRequired[Optional[str]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        invoice_settings: NotRequired[
            Optional[
                "SubscriptionSchedule.CreateDefaultSettingsInvoiceSettingsParams"
            ]
        ]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        transfer_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateDefaultSettingsTransferDataParams",
                ]
            ]
        ]

    class CreateDefaultSettingsTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateDefaultSettingsInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class CreateDefaultSettingsBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreateDefaultSettingsAutomaticTaxParams(TypedDict):
        enabled: bool

    class ListParams(RequestOptions):
        canceled_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListCanceledAtParams", int]]
        ]
        completed_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListCompletedAtParams", int]]
        ]
        created: NotRequired[
            Optional[Union["SubscriptionSchedule.ListCreatedParams", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        released_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListReleasedAtParams", int]]
        ]
        scheduled: NotRequired[Optional[bool]]
        starting_after: NotRequired[Optional[str]]

    class ListReleasedAtParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCompletedAtParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCanceledAtParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        default_settings: NotRequired[
            Optional["SubscriptionSchedule.ModifyDefaultSettingsParams"]
        ]
        end_behavior: NotRequired[
            Optional[Literal["cancel", "none", "release", "renew"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        phases: NotRequired[
            Optional[List["SubscriptionSchedule.ModifyPhaseParams"]]
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class ModifyPhaseParams(TypedDict):
        add_invoice_items: NotRequired[
            Optional[
                List["SubscriptionSchedule.ModifyPhaseAddInvoiceItemParams"]
            ]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["SubscriptionSchedule.ModifyPhaseAutomaticTaxParams"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyPhaseItemBillingThresholdsParams",
                ]
            ]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        coupon: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        default_payment_method: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        end_date: NotRequired[Optional[Union[int, Literal["now"]]]]
        invoice_settings: NotRequired[
            Optional["SubscriptionSchedule.ModifyPhaseInvoiceSettingsParams"]
        ]
        items: List["SubscriptionSchedule.ModifyPhaseItemParams"]
        iterations: NotRequired[Optional[int]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        start_date: NotRequired[Optional[Union[int, Literal["now"]]]]
        transfer_data: NotRequired[
            Optional["SubscriptionSchedule.ModifyPhaseTransferDataParams"]
        ]
        trial: NotRequired[Optional[bool]]
        trial_end: NotRequired[Optional[Union[int, Literal["now"]]]]

    class ModifyPhaseTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyPhaseItemParams(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyPhaseItemBillingThresholdsParams",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionSchedule.ModifyPhaseItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyPhaseItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionSchedule.ModifyPhaseItemPriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyPhaseItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyPhaseItemBillingThresholdsParams(TypedDict):
        usage_gte: int

    class ModifyPhaseInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class ModifyPhaseBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyPhaseAutomaticTaxParams(TypedDict):
        enabled: bool

    class ModifyPhaseAddInvoiceItemParams(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional[
                "SubscriptionSchedule.ModifyPhaseAddInvoiceItemPriceDataParams"
            ]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyPhaseAddInvoiceItemPriceDataParams(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyDefaultSettingsParams(TypedDict):
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional[
                "SubscriptionSchedule.ModifyDefaultSettingsAutomaticTaxParams"
            ]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyDefaultSettingsBillingThresholdsParams",
                ]
            ]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        default_payment_method: NotRequired[Optional[str]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        invoice_settings: NotRequired[
            Optional[
                "SubscriptionSchedule.ModifyDefaultSettingsInvoiceSettingsParams"
            ]
        ]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        transfer_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyDefaultSettingsTransferDataParams",
                ]
            ]
        ]

    class ModifyDefaultSettingsTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyDefaultSettingsInvoiceSettingsParams(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class ModifyDefaultSettingsBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyDefaultSettingsAutomaticTaxParams(TypedDict):
        enabled: bool

    class ReleaseParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        preserve_cancel_date: NotRequired[Optional[bool]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    application: Optional[ExpandableField["Application"]]
    canceled_at: Optional[int]
    completed_at: Optional[int]
    created: int
    current_phase: Optional[StripeObject]
    customer: ExpandableField["Customer"]
    default_settings: StripeObject
    end_behavior: Literal["cancel", "none", "release", "renew"]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["subscription_schedule"]
    phases: List[StripeObject]
    released_at: Optional[int]
    released_subscription: Optional[str]
    status: Literal[
        "active", "canceled", "completed", "not_started", "released"
    ]
    subscription: Optional[ExpandableField["Subscription"]]
    test_clock: Optional[ExpandableField["TestClock"]]

    @classmethod
    def _cls_cancel(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/cancel".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.CreateParams"]
    ) -> "SubscriptionSchedule":
        return cast(
            "SubscriptionSchedule",
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
        **params: Unpack["SubscriptionSchedule.ListParams"]
    ) -> ListObject["SubscriptionSchedule"]:
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
        cls, id, **params: Unpack["SubscriptionSchedule.ModifyParams"]
    ) -> "SubscriptionSchedule":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SubscriptionSchedule",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_release(
        cls,
        schedule: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(schedule)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_release")
    def release(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SubscriptionSchedule.ReleaseParams"]
    ):
        return self._request(
            "post",
            "/v1/subscription_schedules/{schedule}/release".format(
                schedule=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SubscriptionSchedule.RetrieveParams"]
    ) -> "SubscriptionSchedule":
        instance = cls(id, **params)
        instance.refresh()
        return instance
