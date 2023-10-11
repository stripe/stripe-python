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
            Optional["SubscriptionSchedule.CreateParamsDefaultSettings"]
        ]
        end_behavior: NotRequired[
            Optional[Literal["cancel", "none", "release", "renew"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        from_subscription: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        phases: NotRequired[
            Optional[List["SubscriptionSchedule.CreateParamsPhase"]]
        ]
        start_date: NotRequired[Optional[Union[int, Literal["now"]]]]

    class CreateParamsPhase(TypedDict):
        add_invoice_items: NotRequired[
            Optional[
                List["SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem"]
            ]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["SubscriptionSchedule.CreateParamsPhaseAutomaticTax"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateParamsPhaseItemBillingThresholds",
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
            Optional["SubscriptionSchedule.CreateParamsPhaseInvoiceSettings"]
        ]
        items: List["SubscriptionSchedule.CreateParamsPhaseItem"]
        iterations: NotRequired[Optional[int]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        transfer_data: NotRequired[
            Optional["SubscriptionSchedule.CreateParamsPhaseTransferData"]
        ]
        trial: NotRequired[Optional[bool]]
        trial_end: NotRequired[Optional[int]]

    class CreateParamsPhaseTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateParamsPhaseItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateParamsPhaseItemBillingThresholds",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionSchedule.CreateParamsPhaseItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateParamsPhaseItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionSchedule.CreateParamsPhaseItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsPhaseItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateParamsPhaseItemBillingThresholds(TypedDict):
        usage_gte: int

    class CreateParamsPhaseInvoiceSettings(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class CreateParamsPhaseBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreateParamsPhaseAutomaticTax(TypedDict):
        enabled: bool

    class CreateParamsPhaseAddInvoiceItem(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemPriceData"
            ]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateParamsPhaseAddInvoiceItemPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsDefaultSettings(TypedDict):
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional[
                "SubscriptionSchedule.CreateParamsDefaultSettingsAutomaticTax"
            ]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateParamsDefaultSettingsBillingThresholds",
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
                "SubscriptionSchedule.CreateParamsDefaultSettingsInvoiceSettings"
            ]
        ]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        transfer_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.CreateParamsDefaultSettingsTransferData",
                ]
            ]
        ]

    class CreateParamsDefaultSettingsTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateParamsDefaultSettingsInvoiceSettings(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class CreateParamsDefaultSettingsBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreateParamsDefaultSettingsAutomaticTax(TypedDict):
        enabled: bool

    class ListParams(RequestOptions):
        canceled_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListParamsCanceledAt", int]]
        ]
        completed_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListParamsCompletedAt", int]]
        ]
        created: NotRequired[
            Optional[Union["SubscriptionSchedule.ListParamsCreated", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        released_at: NotRequired[
            Optional[Union["SubscriptionSchedule.ListParamsReleasedAt", int]]
        ]
        scheduled: NotRequired[Optional[bool]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsReleasedAt(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCompletedAt(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCanceledAt(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        default_settings: NotRequired[
            Optional["SubscriptionSchedule.ModifyParamsDefaultSettings"]
        ]
        end_behavior: NotRequired[
            Optional[Literal["cancel", "none", "release", "renew"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        phases: NotRequired[
            Optional[List["SubscriptionSchedule.ModifyParamsPhase"]]
        ]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]

    class ModifyParamsPhase(TypedDict):
        add_invoice_items: NotRequired[
            Optional[
                List["SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem"]
            ]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["SubscriptionSchedule.ModifyParamsPhaseAutomaticTax"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyParamsPhaseItemBillingThresholds",
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
            Optional["SubscriptionSchedule.ModifyParamsPhaseInvoiceSettings"]
        ]
        items: List["SubscriptionSchedule.ModifyParamsPhaseItem"]
        iterations: NotRequired[Optional[int]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        start_date: NotRequired[Optional[Union[int, Literal["now"]]]]
        transfer_data: NotRequired[
            Optional["SubscriptionSchedule.ModifyParamsPhaseTransferData"]
        ]
        trial: NotRequired[Optional[bool]]
        trial_end: NotRequired[Optional[Union[int, Literal["now"]]]]

    class ModifyParamsPhaseTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyParamsPhaseItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyParamsPhaseItemBillingThresholds",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["SubscriptionSchedule.ModifyParamsPhaseItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyParamsPhaseItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "SubscriptionSchedule.ModifyParamsPhaseItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsPhaseItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyParamsPhaseItemBillingThresholds(TypedDict):
        usage_gte: int

    class ModifyParamsPhaseInvoiceSettings(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class ModifyParamsPhaseBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyParamsPhaseAutomaticTax(TypedDict):
        enabled: bool

    class ModifyParamsPhaseAddInvoiceItem(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemPriceData"
            ]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyParamsPhaseAddInvoiceItemPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsDefaultSettings(TypedDict):
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsAutomaticTax"
            ]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["automatic", "phase_start"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyParamsDefaultSettingsBillingThresholds",
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
                "SubscriptionSchedule.ModifyParamsDefaultSettingsInvoiceSettings"
            ]
        ]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        transfer_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SubscriptionSchedule.ModifyParamsDefaultSettingsTransferData",
                ]
            ]
        ]

    class ModifyParamsDefaultSettingsTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyParamsDefaultSettingsInvoiceSettings(TypedDict):
        days_until_due: NotRequired[Optional[int]]

    class ModifyParamsDefaultSettingsBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyParamsDefaultSettingsAutomaticTax(TypedDict):
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
