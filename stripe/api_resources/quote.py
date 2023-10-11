# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.subscription_schedule import (
        SubscriptionSchedule as SubscriptionScheduleResource,
    )
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


@nested_resource_class_methods("preview_invoice")
@nested_resource_class_methods("preview_subscription_schedule")
class Quote(
    CreateableAPIResource["Quote"],
    ListableAPIResource["Quote"],
    UpdateableAPIResource["Quote"],
):
    """
    A Quote is a way to model prices that you'd like to provide to a customer.
    Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    """

    OBJECT_NAME = "quote"

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        _inner_class_types = {"liability": Liability}

    class Computed(StripeObject):
        class Recurring(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        discount: "DiscountResource"

                    class Tax(StripeObject):
                        amount: int
                        rate: "TaxRate"
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        taxable_amount: Optional[int]

                    discounts: List[Discount]
                    taxes: List[Tax]
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                amount_shipping: Optional[int]
                amount_tax: int
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            amount_total: int
            interval: Literal["day", "month", "week", "year"]
            interval_count: int
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        class Upfront(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        discount: "DiscountResource"

                    class Tax(StripeObject):
                        amount: int
                        rate: "TaxRate"
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        taxable_amount: Optional[int]

                    discounts: List[Discount]
                    taxes: List[Tax]
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                amount_shipping: Optional[int]
                amount_tax: int
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            amount_total: int
            line_items: Optional[ListObject["LineItem"]]
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        recurring: Optional[Recurring]
        updated_at: Optional[int]
        upfront: Upfront
        _inner_class_types = {"recurring": Recurring, "upfront": Upfront}

    class FromQuote(StripeObject):
        is_revision: bool
        quote: ExpandableField["Quote"]

    class InvoiceSettings(StripeObject):
        class Issuer(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        days_until_due: Optional[int]
        issuer: Optional[Issuer]
        _inner_class_types = {"issuer": Issuer}

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Optional[
                Literal[
                    "canceled",
                    "quote_accepted",
                    "quote_expired",
                    "quote_superseded",
                    "subscription_canceled",
                ]
            ]
            transitioned_at: Optional[int]

        class Stale(StripeObject):
            class LastReason(StripeObject):
                class SubscriptionChanged(StripeObject):
                    previous_subscription: Optional["Subscription"]

                class SubscriptionScheduleChanged(StripeObject):
                    previous_subscription_schedule: Optional[
                        "SubscriptionScheduleResource"
                    ]

                line_invalid: Optional[str]
                marked_stale: Optional[str]
                subscription_canceled: Optional[str]
                subscription_changed: Optional[SubscriptionChanged]
                subscription_expired: Optional[str]
                subscription_schedule_canceled: Optional[str]
                subscription_schedule_changed: Optional[
                    SubscriptionScheduleChanged
                ]
                subscription_schedule_released: Optional[str]
                type: Optional[
                    Literal[
                        "bill_on_acceptance_invalid",
                        "line_invalid",
                        "marked_stale",
                        "subscription_canceled",
                        "subscription_changed",
                        "subscription_expired",
                        "subscription_schedule_canceled",
                        "subscription_schedule_changed",
                        "subscription_schedule_released",
                    ]
                ]
                _inner_class_types = {
                    "subscription_changed": SubscriptionChanged,
                    "subscription_schedule_changed": SubscriptionScheduleChanged,
                }

            expires_at: Optional[int]
            last_reason: Optional[LastReason]
            last_updated_at: Optional[int]
            transitioned_at: Optional[int]
            _inner_class_types = {"last_reason": LastReason}

        canceled: Optional[Canceled]
        stale: Optional[Stale]
        _inner_class_types = {"canceled": Canceled, "stale": Stale}

    class StatusTransitions(StripeObject):
        accepted_at: Optional[int]
        canceled_at: Optional[int]
        finalized_at: Optional[int]

    class SubscriptionData(StripeObject):
        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str

                computed: Optional[int]
                line_starts_at: Optional[LineStartsAt]
                timestamp: Optional[int]
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    interval_count: int

                class LineEndsAt(StripeObject):
                    id: str

                computed: Optional[int]
                duration: Optional[Duration]
                line_ends_at: Optional[LineEndsAt]
                timestamp: Optional[int]
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            bill_until: Optional[BillUntil]
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        class Prebilling(StripeObject):
            iterations: int

        bill_on_acceptance: Optional[BillOnAcceptance]
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        billing_cycle_anchor: Optional[Literal["reset"]]
        description: Optional[str]
        effective_date: Optional[int]
        end_behavior: Optional[Literal["cancel", "release"]]
        from_schedule: Optional[
            ExpandableField["SubscriptionScheduleResource"]
        ]
        from_subscription: Optional[ExpandableField["Subscription"]]
        prebilling: Optional[Prebilling]
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        trial_period_days: Optional[int]
        _inner_class_types = {
            "bill_on_acceptance": BillOnAcceptance,
            "prebilling": Prebilling,
        }

    class SubscriptionDataOverride(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            subscription_schedule: Optional[str]
            type: Literal["new_reference", "subscription_schedule"]

        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str

                computed: Optional[int]
                line_starts_at: Optional[LineStartsAt]
                timestamp: Optional[int]
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    interval_count: int

                class LineEndsAt(StripeObject):
                    id: str

                computed: Optional[int]
                duration: Optional[Duration]
                line_ends_at: Optional[LineEndsAt]
                timestamp: Optional[int]
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            bill_until: Optional[BillUntil]
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        applies_to: AppliesTo
        bill_on_acceptance: Optional[BillOnAcceptance]
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        customer: Optional[str]
        description: Optional[str]
        end_behavior: Optional[Literal["cancel", "release"]]
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        _inner_class_types = {
            "applies_to": AppliesTo,
            "bill_on_acceptance": BillOnAcceptance,
        }

    class SubscriptionSchedule(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            subscription_schedule: Optional[str]
            type: Literal["new_reference", "subscription_schedule"]

        applies_to: AppliesTo
        subscription_schedule: str
        _inner_class_types = {"applies_to": AppliesTo}

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                discount: "DiscountResource"

            class Tax(StripeObject):
                amount: int
                rate: "TaxRate"
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                taxable_amount: Optional[int]

            discounts: List[Discount]
            taxes: List[Tax]
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        amount_shipping: Optional[int]
        amount_tax: int
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    class TransferData(StripeObject):
        amount: Optional[int]
        amount_percent: Optional[float]
        destination: ExpandableField["Account"]

    allow_backdated_lines: Optional[bool]
    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: AutomaticTax
    collection_method: Literal["charge_automatically", "send_invoice"]
    computed: Computed
    created: int
    currency: Optional[str]
    customer: Optional[ExpandableField["Customer"]]
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    description: Optional[str]
    discounts: List[ExpandableField["DiscountResource"]]
    expires_at: int
    footer: Optional[str]
    from_quote: Optional[FromQuote]
    header: Optional[str]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_settings: Optional[InvoiceSettings]
    line_items: Optional[ListObject["LineItem"]]
    lines: Optional[List[str]]
    livemode: bool
    metadata: Dict[str, str]
    number: Optional[str]
    object: Literal["quote"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    status: Literal[
        "accepted", "accepting", "canceled", "draft", "open", "stale"
    ]
    status_details: Optional[StatusDetails]
    status_transitions: StatusTransitions
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_data: SubscriptionData
    subscription_data_overrides: Optional[List[SubscriptionDataOverride]]
    subscription_schedule: Optional[
        ExpandableField["SubscriptionScheduleResource"]
    ]
    subscription_schedules: Optional[List[SubscriptionSchedule]]
    test_clock: Optional[ExpandableField["TestClock"]]
    total_details: TotalDetails
    transfer_data: Optional[TransferData]

    @classmethod
    def _cls_accept(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/accept".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_accept")
    def accept(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/quotes/{quote}/accept".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/cancel".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/quotes/{quote}/cancel".format(
                quote=util.sanitize_id(self.get("id"))
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
        **params: Any
    ) -> "Quote":
        return cast(
            "Quote",
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
    def _cls_finalize_quote(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/finalize".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_finalize_quote")
    def finalize_quote(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/quotes/{quote}/finalize".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Quote"]:
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
    def _cls_list_computed_upfront_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/computed_upfront_line_items".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_computed_upfront_line_items")
    def list_computed_upfront_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/computed_upfront_line_items".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/line_items".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/line_items".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_lines(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/lines".format(quote=util.sanitize_id(quote)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_lines")
    def list_lines(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "get",
            "/v1/quotes/{quote}/lines".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_preview_invoice_lines(
        cls,
        quote: str,
        preview_invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                quote=util.sanitize_id(quote),
                preview_invoice=util.sanitize_id(preview_invoice),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_preview_invoice_lines")
    def list_preview_invoice_lines(
        self,
        preview_invoice: str,
        idempotency_key: Optional[str] = None,
        **params: Any
    ):
        return self._request(
            "get",
            "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                quote=util.sanitize_id(self.get("id")),
                preview_invoice=util.sanitize_id(preview_invoice),
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_mark_draft(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/mark_draft".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_draft")
    def mark_draft(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/quotes/{quote}/mark_draft".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_mark_stale(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/mark_stale".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_stale")
    def mark_stale(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/quotes/{quote}/mark_stale".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "Quote":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Quote",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_reestimate(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/quotes/{quote}/reestimate".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reestimate")
    def reestimate(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/quotes/{quote}/reestimate".format(
                quote=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Quote":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(sid),
            "pdf",
        )
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @util.class_method_variant("_cls_pdf")
    def pdf(
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)

    @classmethod
    def list_preview_invoices(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_invoices".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_preview_subscription_schedules(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quotes/{quote}/preview_subscription_schedules".format(
                quote=util.sanitize_id(quote)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "computed": Computed,
        "from_quote": FromQuote,
        "invoice_settings": InvoiceSettings,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "subscription_data": SubscriptionData,
        "subscription_data_overrides": SubscriptionDataOverride,
        "subscription_schedules": SubscriptionSchedule,
        "total_details": TotalDetails,
        "transfer_data": TransferData,
    }
