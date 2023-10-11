# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.subscription_item import SubscriptionItem
    from stripe.api_resources.subscription_schedule import SubscriptionSchedule
    from stripe.api_resources.tax_rate import TaxRate
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

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        _inner_class_types = {"liability": Liability}

    class BillingThresholds(StripeObject):
        amount_gte: Optional[int]
        reset_billing_cycle_anchor: Optional[bool]

    class CancellationDetails(StripeObject):
        comment: Optional[str]
        feedback: Optional[
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
        ]
        reason: Optional[
            Literal[
                "cancellation_requested", "payment_disputed", "payment_failed"
            ]
        ]

    class PauseCollection(StripeObject):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        resumes_at: Optional[int]

    class PaymentSettings(StripeObject):
        class PaymentMethodOptions(StripeObject):
            class AcssDebit(StripeObject):
                class MandateOptions(StripeObject):
                    transaction_type: Optional[Literal["business", "personal"]]

                mandate_options: Optional[MandateOptions]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                _inner_class_types = {"mandate_options": MandateOptions}

            class Bancontact(StripeObject):
                preferred_language: Literal["de", "en", "fr", "nl"]

            class Card(StripeObject):
                class MandateOptions(StripeObject):
                    amount: Optional[int]
                    amount_type: Optional[Literal["fixed", "maximum"]]
                    description: Optional[str]

                mandate_options: Optional[MandateOptions]
                network: Optional[
                    Literal[
                        "amex",
                        "cartes_bancaires",
                        "diners",
                        "discover",
                        "eftpos_au",
                        "interac",
                        "jcb",
                        "mastercard",
                        "unionpay",
                        "unknown",
                        "visa",
                    ]
                ]
                request_three_d_secure: Optional[Literal["any", "automatic"]]
                _inner_class_types = {"mandate_options": MandateOptions}

            class CustomerBalance(StripeObject):
                class BankTransfer(StripeObject):
                    class EuBankTransfer(StripeObject):
                        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]

                    eu_bank_transfer: Optional[EuBankTransfer]
                    type: Optional[str]
                    _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

                bank_transfer: Optional[BankTransfer]
                funding_type: Optional[Literal["bank_transfer"]]
                _inner_class_types = {"bank_transfer": BankTransfer}

            class Konbini(StripeObject):
                pass

            class UsBankAccount(StripeObject):
                class FinancialConnections(StripeObject):
                    permissions: Optional[
                        List[
                            Literal[
                                "balances",
                                "ownership",
                                "payment_method",
                                "transactions",
                            ]
                        ]
                    ]
                    prefetch: Optional[
                        List[
                            Literal[
                                "balances",
                                "inferred_balances",
                                "ownership",
                                "transactions",
                            ]
                        ]
                    ]

                financial_connections: Optional[FinancialConnections]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                _inner_class_types = {
                    "financial_connections": FinancialConnections,
                }

            acss_debit: Optional[AcssDebit]
            bancontact: Optional[Bancontact]
            card: Optional[Card]
            customer_balance: Optional[CustomerBalance]
            konbini: Optional[Konbini]
            us_bank_account: Optional[UsBankAccount]
            _inner_class_types = {
                "acss_debit": AcssDebit,
                "bancontact": Bancontact,
                "card": Card,
                "customer_balance": CustomerBalance,
                "konbini": Konbini,
                "us_bank_account": UsBankAccount,
            }

        payment_method_options: Optional[PaymentMethodOptions]
        payment_method_types: Optional[
            List[
                Literal[
                    "ach_credit_transfer",
                    "ach_debit",
                    "acss_debit",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "konbini",
                    "link",
                    "paynow",
                    "paypal",
                    "promptpay",
                    "sepa_credit_transfer",
                    "sepa_debit",
                    "sofort",
                    "us_bank_account",
                    "wechat_pay",
                ]
            ]
        ]
        save_default_payment_method: Optional[
            Literal["off", "on_subscription"]
        ]
        _inner_class_types = {"payment_method_options": PaymentMethodOptions}

    class PendingInvoiceItemInterval(StripeObject):
        interval: Literal["day", "month", "week", "year"]
        interval_count: int

    class PendingUpdate(StripeObject):
        billing_cycle_anchor: Optional[int]
        expires_at: int
        prebilling_iterations: Optional[int]
        subscription_items: Optional[List["SubscriptionItem"]]
        trial_end: Optional[int]
        trial_from_plan: Optional[bool]

    class Prebilling(StripeObject):
        invoice: ExpandableField["Invoice"]
        period_end: int
        period_start: int
        update_behavior: Optional[Literal["prebill", "reset"]]

    class TransferData(StripeObject):
        amount_percent: Optional[float]
        destination: ExpandableField["Account"]

    class TrialSettings(StripeObject):
        class EndBehavior(StripeObject):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]

        end_behavior: EndBehavior
        _inner_class_types = {"end_behavior": EndBehavior}

    application: Optional[ExpandableField["Application"]]
    application_fee_percent: Optional[float]
    automatic_tax: AutomaticTax
    billing_cycle_anchor: int
    billing_thresholds: Optional[BillingThresholds]
    cancel_at: Optional[int]
    cancel_at_period_end: bool
    canceled_at: Optional[int]
    cancellation_details: Optional[CancellationDetails]
    collection_method: Literal["charge_automatically", "send_invoice"]
    created: int
    currency: str
    current_period_end: int
    current_period_start: int
    customer: ExpandableField["Customer"]
    days_until_due: Optional[int]
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    default_source: Optional[ExpandableField[Any]]
    default_tax_rates: Optional[List["TaxRate"]]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[ExpandableField["Discount"]]]
    ended_at: Optional[int]
    id: str
    items: ListObject["SubscriptionItem"]
    latest_invoice: Optional[ExpandableField["Invoice"]]
    livemode: bool
    metadata: Dict[str, str]
    next_pending_invoice_item_invoice: Optional[int]
    object: Literal["subscription"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    pause_collection: Optional[PauseCollection]
    payment_settings: Optional[PaymentSettings]
    pending_invoice_item_interval: Optional[PendingInvoiceItemInterval]
    pending_setup_intent: Optional[ExpandableField["SetupIntent"]]
    pending_update: Optional[PendingUpdate]
    prebilling: Optional[Prebilling]
    schedule: Optional[ExpandableField["SubscriptionSchedule"]]
    start_date: int
    status: Literal[
        "active",
        "canceled",
        "incomplete",
        "incomplete_expired",
        "past_due",
        "paused",
        "trialing",
        "unpaid",
    ]
    test_clock: Optional[ExpandableField["TestClock"]]
    transfer_data: Optional[TransferData]
    trial_end: Optional[int]
    trial_settings: Optional[TrialSettings]
    trial_start: Optional[int]

    @classmethod
    def _cls_cancel(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}".format(
                subscription_exposed_id=util.sanitize_id(self.get("id"))
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
    ) -> "Subscription":
        return cast(
            "Subscription",
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
    def _cls_delete_discount(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def delete_discount(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "delete",
            "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                subscription_exposed_id=util.sanitize_id(self.get("id"))
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
    ) -> ListObject["Subscription"]:
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
    def modify(cls, id, **params: Any) -> "Subscription":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Subscription",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_resume(
        cls,
        subscription: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def resume(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/subscriptions/{subscription}/resume".format(
                subscription=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Subscription":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(cls, *args, **kwargs) -> SearchResultObject["Subscription"]:
        return cls._search(
            search_url="/v1/subscriptions/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "billing_thresholds": BillingThresholds,
        "cancellation_details": CancellationDetails,
        "pause_collection": PauseCollection,
        "payment_settings": PaymentSettings,
        "pending_invoice_item_interval": PendingInvoiceItemInterval,
        "pending_update": PendingUpdate,
        "prebilling": Prebilling,
        "transfer_data": TransferData,
        "trial_settings": TrialSettings,
    }
