# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, cast
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
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            invoice_now: NotRequired["bool|None"]
            prorate: NotRequired["bool|None"]

        class CreateParams(RequestOptions):
            customer: NotRequired["str|None"]
            default_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettings|None"
            ]
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            expand: NotRequired["List[str]|None"]
            from_subscription: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            phases: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhase]|None"
            ]
            start_date: NotRequired["int|Literal['now']|None"]

        class CreateParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            default_payment_method: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            end_date: NotRequired["int|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseInvoiceSettings|None"
            ]
            items: List["SubscriptionSchedule.CreateParamsPhaseItem"]
            iterations: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            transfer_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseTransferData|None"
            ]
            trial: NotRequired["bool|None"]
            trial_end: NotRequired["int|None"]

        class CreateParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsPhaseItemBillingThresholds|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsPhaseItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionSchedule.CreateParamsPhaseItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int

        class CreateParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class CreateParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class CreateParamsPhaseAutomaticTax(TypedDict):
            enabled: bool

        class CreateParamsPhaseAddInvoiceItem(TypedDict):
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.CreateParamsPhaseAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_payment_method: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.CreateParamsDefaultSettingsInvoiceSettings|None"
            ]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.CreateParamsDefaultSettingsTransferData|None"
            ]

        class CreateParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class CreateParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class CreateParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool

        class ListParams(RequestOptions):
            canceled_at: NotRequired[
                "SubscriptionSchedule.ListParamsCanceledAt|int|None"
            ]
            completed_at: NotRequired[
                "SubscriptionSchedule.ListParamsCompletedAt|int|None"
            ]
            created: NotRequired[
                "SubscriptionSchedule.ListParamsCreated|int|None"
            ]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            released_at: NotRequired[
                "SubscriptionSchedule.ListParamsReleasedAt|int|None"
            ]
            scheduled: NotRequired["bool|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsReleasedAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCompletedAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCanceledAt(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            default_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettings|None"
            ]
            end_behavior: NotRequired[
                "Literal['cancel', 'none', 'release', 'renew']|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            phases: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhase]|None"
            ]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]

        class ModifyParamsPhase(TypedDict):
            add_invoice_items: NotRequired[
                "List[SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            default_payment_method: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            end_date: NotRequired["int|Literal['now']|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseInvoiceSettings|None"
            ]
            items: List["SubscriptionSchedule.ModifyParamsPhaseItem"]
            iterations: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            start_date: NotRequired["int|Literal['now']|None"]
            transfer_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseTransferData|None"
            ]
            trial: NotRequired["bool|None"]
            trial_end: NotRequired["int|Literal['now']|None"]

        class ModifyParamsPhaseTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsPhaseItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsPhaseItemBillingThresholds|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsPhaseItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "SubscriptionSchedule.ModifyParamsPhaseItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsPhaseItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsPhaseItemBillingThresholds(TypedDict):
            usage_gte: int

        class ModifyParamsPhaseInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class ModifyParamsPhaseBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class ModifyParamsPhaseAutomaticTax(TypedDict):
            enabled: bool

        class ModifyParamsPhaseAddInvoiceItem(TypedDict):
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsPhaseAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsDefaultSettings(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['automatic', 'phase_start']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsBillingThresholds|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            default_payment_method: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            invoice_settings: NotRequired[
                "SubscriptionSchedule.ModifyParamsDefaultSettingsInvoiceSettings|None"
            ]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            transfer_data: NotRequired[
                "Literal['']|SubscriptionSchedule.ModifyParamsDefaultSettingsTransferData|None"
            ]

        class ModifyParamsDefaultSettingsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsDefaultSettingsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]

        class ModifyParamsDefaultSettingsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class ModifyParamsDefaultSettingsAutomaticTax(TypedDict):
            enabled: bool

        class ReleaseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            preserve_cancel_date: NotRequired["bool|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
