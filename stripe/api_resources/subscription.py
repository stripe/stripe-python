# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.subscription_item import SubscriptionItem
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.account import Account
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.subscription_schedule import SubscriptionSchedule
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Subscription(
    CreateableAPIResource["Subscription"],
    DeletableAPIResource["Subscription"],
    ListableAPIResource["Subscription"],
    SearchableAPIResource["Subscription"],
    UpdateableAPIResource["Subscription"],
):
    """
    Subscriptions allow you to charge a customer on a recurring basis.

    Related guide: [Creating subscriptions](https://stripe.com/docs/billing/subscriptions/creating)
    """

    OBJECT_NAME = "subscription"
    application: Optional[ExpandableField[Any]]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    billing_cycle_anchor: str
    billing_thresholds: Optional[StripeObject]
    cancel_at: Optional[str]
    cancel_at_period_end: bool
    canceled_at: Optional[str]
    cancellation_details: Optional[StripeObject]
    collection_method: str
    created: str
    currency: str
    current_period_end: str
    current_period_start: str
    customer: ExpandableField[Any]
    days_until_due: Optional[int]
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    default_source: Optional[ExpandableField[Any]]
    default_tax_rates: Optional[List["TaxRate"]]
    description: Optional[str]
    discount: Optional["Discount"]
    ended_at: Optional[str]
    id: str
    items: ListObject["SubscriptionItem"]
    latest_invoice: Optional[ExpandableField["Invoice"]]
    livemode: bool
    metadata: Dict[str, str]
    next_pending_invoice_item_invoice: Optional[str]
    object: Literal["subscription"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    pause_collection: Optional[StripeObject]
    payment_settings: Optional[StripeObject]
    pending_invoice_item_interval: Optional[StripeObject]
    pending_setup_intent: Optional[ExpandableField["SetupIntent"]]
    pending_update: Optional[StripeObject]
    schedule: Optional[ExpandableField["SubscriptionSchedule"]]
    start_date: str
    status: str
    test_clock: Optional[ExpandableField["TestClock"]]
    transfer_data: Optional[StripeObject]
    trial_end: Optional[str]
    trial_settings: Optional[StripeObject]
    trial_start: Optional[str]

    @classmethod
    def _cls_cancel(
        cls,
        subscription_exposed_id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}".format(
                subscription_exposed_id=util.sanitize_id(
                    subscription_exposed_id
                )
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}".format(
                subscription_exposed_id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        subscription_exposed_id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                subscription_exposed_id=util.sanitize_id(
                    subscription_exposed_id
                )
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_delete_discount")
    def delete_discount(self, idempotency_key=None, **params):
        return self._request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                subscription_exposed_id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_resume(
        cls,
        subscription,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/subscriptions/{subscription}/resume".format(
                subscription=util.sanitize_id(subscription)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_resume")
    def resume(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/subscriptions/{subscription}/resume".format(
                subscription=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(
            search_url="/v1/subscriptions/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
