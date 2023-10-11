# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CancelParams(RequestOptions):
        cancellation_details: NotRequired[
            Optional["Subscription.CancelCancellationDetailsParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_now: NotRequired[Optional[bool]]
        prorate: NotRequired[Optional[bool]]

    class CancelCancellationDetailsParams(TypedDict):
        comment: NotRequired[Optional[Union[Literal[""], str]]]
        feedback: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal[
                        "customer_service",
                        "low_quality",
                        "missing_features",
                        "other",
                        "switched_service",
                        "too_complex",
                        "too_expensive",
                        "unused",
                    ],
                ]
            ]
        ]

    class CreateParams(RequestOptions):
        add_invoice_items: NotRequired[
            Optional[List["Subscription.CreateAddInvoiceItemParams"]]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["Subscription.CreateAutomaticTaxParams"]
        ]
        backdate_start_date: NotRequired[Optional[int]]
        billing_cycle_anchor: NotRequired[Optional[int]]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateItemBillingThresholdsParams",
                ]
            ]
        ]
        cancel_at: NotRequired[Optional[int]]
        cancel_at_period_end: NotRequired[Optional[bool]]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        coupon: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        customer: str
        days_until_due: NotRequired[Optional[int]]
        default_payment_method: NotRequired[Optional[str]]
        default_source: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        items: NotRequired[Optional[List["Subscription.CreateItemParams"]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        off_session: NotRequired[Optional[bool]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        payment_behavior: NotRequired[
            Optional[
                Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ]
        ]
        payment_settings: NotRequired[
            Optional["Subscription.CreatePaymentSettingsParams"]
        ]
        pending_invoice_item_interval: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePendingInvoiceItemIntervalParams",
                ]
            ]
        ]
        promotion_code: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        transfer_data: NotRequired[
            Optional["Subscription.CreateTransferDataParams"]
        ]
        trial_end: NotRequired[Optional[Union[Literal["now"], int]]]
        trial_from_plan: NotRequired[Optional[bool]]
        trial_period_days: NotRequired[Optional[int]]
        trial_settings: NotRequired[
            Optional["Subscription.CreateTrialSettingsParams"]
        ]

    class CreateTrialSettingsParams(TypedDict):
        end_behavior: "Subscription.CreateTrialSettingsEndBehaviorParams"

    class CreateTrialSettingsEndBehaviorParams(TypedDict):
        missing_payment_method: Literal["cancel", "create_invoice", "pause"]

    class CreateTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreatePendingInvoiceItemIntervalParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreatePaymentSettingsParams(TypedDict):
        payment_method_options: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsParams"
            ]
        ]
        payment_method_types: NotRequired[
            Optional[
                Union[
                    Literal[""],
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
                    ],
                ]
            ]
        ]
        save_default_payment_method: NotRequired[
            Optional[Literal["off", "on_subscription"]]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsAcssDebitParams",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsBancontactParams",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsCardParams",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceParams",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsKonbiniParams",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreatePaymentSettingsPaymentMethodOptionsUsBankAccountParams",
                ]
            ]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsUsBankAccountParams(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
        TypedDict,
    ):
        permissions: NotRequired[
            Optional[
                List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
            ]
        ]
        prefetch: NotRequired[Optional[List[Literal["balances"]]]]

    class CreatePaymentSettingsPaymentMethodOptionsKonbiniParams(TypedDict):
        pass

    class CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceParams(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
            ]
        ]
        type: NotRequired[Optional[str]]

    class CreatePaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams(
        TypedDict,
    ):
        country: str

    class CreatePaymentSettingsPaymentMethodOptionsCardParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsCardMandateOptionsParams"
            ]
        ]
        network: NotRequired[
            Optional[
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
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsCardMandateOptionsParams(
        TypedDict,
    ):
        amount: NotRequired[Optional[int]]
        amount_type: NotRequired[Optional[Literal["fixed", "maximum"]]]
        description: NotRequired[Optional[str]]

    class CreatePaymentSettingsPaymentMethodOptionsBancontactParams(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsAcssDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.CreatePaymentSettingsPaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreatePaymentSettingsPaymentMethodOptionsAcssDebitMandateOptionsParams(
        TypedDict,
    ):
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class CreateItemParams(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateItemBillingThresholdsParams",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.CreateItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "Subscription.CreateItemPriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateItemBillingThresholdsParams(TypedDict):
        usage_gte: int

    class CreateBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreateAutomaticTaxParams(TypedDict):
        enabled: bool

    class CreateAddInvoiceItemParams(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.CreateAddInvoiceItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateAddInvoiceItemPriceDataParams(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class DeleteDiscountParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        automatic_tax: NotRequired[
            Optional["Subscription.ListAutomaticTaxParams"]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        created: NotRequired[
            Optional[Union["Subscription.ListCreatedParams", int]]
        ]
        current_period_end: NotRequired[
            Optional[Union["Subscription.ListCurrentPeriodEndParams", int]]
        ]
        current_period_start: NotRequired[
            Optional[Union["Subscription.ListCurrentPeriodStartParams", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[
                Literal[
                    "active",
                    "all",
                    "canceled",
                    "ended",
                    "incomplete",
                    "incomplete_expired",
                    "past_due",
                    "paused",
                    "trialing",
                    "unpaid",
                ]
            ]
        ]
        test_clock: NotRequired[Optional[str]]

    class ListCurrentPeriodStartParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCurrentPeriodEndParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListAutomaticTaxParams(TypedDict):
        enabled: bool

    class ModifyParams(RequestOptions):
        add_invoice_items: NotRequired[
            Optional[List["Subscription.ModifyAddInvoiceItemParams"]]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["Subscription.ModifyAutomaticTaxParams"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["now", "unchanged"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyItemBillingThresholdsParams",
                ]
            ]
        ]
        cancel_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancel_at_period_end: NotRequired[Optional[bool]]
        cancellation_details: NotRequired[
            Optional["Subscription.ModifyCancellationDetailsParams"]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        coupon: NotRequired[Optional[str]]
        days_until_due: NotRequired[Optional[int]]
        default_payment_method: NotRequired[Optional[str]]
        default_source: NotRequired[Optional[Union[Literal[""], str]]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]
        items: NotRequired[Optional[List["Subscription.ModifyItemParams"]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        off_session: NotRequired[Optional[bool]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        pause_collection: NotRequired[
            Optional[
                Union[Literal[""], "Subscription.ModifyPauseCollectionParams"]
            ]
        ]
        payment_behavior: NotRequired[
            Optional[
                Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ]
        ]
        payment_settings: NotRequired[
            Optional["Subscription.ModifyPaymentSettingsParams"]
        ]
        pending_invoice_item_interval: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPendingInvoiceItemIntervalParams",
                ]
            ]
        ]
        promotion_code: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        proration_date: NotRequired[Optional[int]]
        transfer_data: NotRequired[
            Optional[
                Union[Literal[""], "Subscription.ModifyTransferDataParams"]
            ]
        ]
        trial_end: NotRequired[Optional[Union[Literal["now"], int]]]
        trial_from_plan: NotRequired[Optional[bool]]
        trial_settings: NotRequired[
            Optional["Subscription.ModifyTrialSettingsParams"]
        ]

    class ModifyTrialSettingsParams(TypedDict):
        end_behavior: "Subscription.ModifyTrialSettingsEndBehaviorParams"

    class ModifyTrialSettingsEndBehaviorParams(TypedDict):
        missing_payment_method: Literal["cancel", "create_invoice", "pause"]

    class ModifyTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyPendingInvoiceItemIntervalParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyPaymentSettingsParams(TypedDict):
        payment_method_options: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsParams"
            ]
        ]
        payment_method_types: NotRequired[
            Optional[
                Union[
                    Literal[""],
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
                    ],
                ]
            ]
        ]
        save_default_payment_method: NotRequired[
            Optional[Literal["off", "on_subscription"]]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsAcssDebitParams",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsBancontactParams",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsCardParams",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceParams",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsKonbiniParams",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyPaymentSettingsPaymentMethodOptionsUsBankAccountParams",
                ]
            ]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsUsBankAccountParams(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
        TypedDict,
    ):
        permissions: NotRequired[
            Optional[
                List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
            ]
        ]
        prefetch: NotRequired[Optional[List[Literal["balances"]]]]

    class ModifyPaymentSettingsPaymentMethodOptionsKonbiniParams(TypedDict):
        pass

    class ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceParams(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
            ]
        ]
        type: NotRequired[Optional[str]]

    class ModifyPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams(
        TypedDict,
    ):
        country: str

    class ModifyPaymentSettingsPaymentMethodOptionsCardParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsCardMandateOptionsParams"
            ]
        ]
        network: NotRequired[
            Optional[
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
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsCardMandateOptionsParams(
        TypedDict,
    ):
        amount: NotRequired[Optional[int]]
        amount_type: NotRequired[Optional[Literal["fixed", "maximum"]]]
        description: NotRequired[Optional[str]]

    class ModifyPaymentSettingsPaymentMethodOptionsBancontactParams(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsAcssDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.ModifyPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptionsParams(
        TypedDict,
    ):
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ModifyPauseCollectionParams(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        resumes_at: NotRequired[Optional[int]]

    class ModifyItemParams(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyItemBillingThresholdsParams",
                ]
            ]
        ]
        clear_usage: NotRequired[Optional[bool]]
        deleted: NotRequired[Optional[bool]]
        id: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.ModifyItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyItemPriceDataParams(TypedDict):
        currency: str
        product: str
        recurring: "Subscription.ModifyItemPriceDataRecurringParams"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyItemBillingThresholdsParams(TypedDict):
        usage_gte: int

    class ModifyCancellationDetailsParams(TypedDict):
        comment: NotRequired[Optional[Union[Literal[""], str]]]
        feedback: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal[
                        "customer_service",
                        "low_quality",
                        "missing_features",
                        "other",
                        "switched_service",
                        "too_complex",
                        "too_expensive",
                        "unused",
                    ],
                ]
            ]
        ]

    class ModifyBillingThresholdsParams(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyAutomaticTaxParams(TypedDict):
        enabled: bool

    class ModifyAddInvoiceItemParams(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.ModifyAddInvoiceItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyAddInvoiceItemPriceDataParams(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ResumeParams(RequestOptions):
        billing_cycle_anchor: NotRequired[
            Optional[Literal["now", "unchanged"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        proration_date: NotRequired[Optional[int]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
        query: str

    application: Optional[ExpandableField["Application"]]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    billing_cycle_anchor: int
    billing_thresholds: Optional[StripeObject]
    cancel_at: Optional[int]
    cancel_at_period_end: bool
    canceled_at: Optional[int]
    cancellation_details: Optional[StripeObject]
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
    ended_at: Optional[int]
    id: str
    items: ListObject["SubscriptionItem"]
    latest_invoice: Optional[ExpandableField["Invoice"]]
    livemode: bool
    metadata: Dict[str, str]
    next_pending_invoice_item_invoice: Optional[int]
    object: Literal["subscription"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    pause_collection: Optional[StripeObject]
    payment_settings: Optional[StripeObject]
    pending_invoice_item_interval: Optional[StripeObject]
    pending_setup_intent: Optional[ExpandableField["SetupIntent"]]
    pending_update: Optional[StripeObject]
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
    transfer_data: Optional[StripeObject]
    trial_end: Optional[int]
    trial_settings: Optional[StripeObject]
    trial_start: Optional[int]

    @classmethod
    def _cls_cancel(
        cls,
        subscription_exposed_id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
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
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ):
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
        **params: Unpack["Subscription.CreateParams"]
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
        **params: Unpack["Subscription.DeleteDiscountParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
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
        **params: Unpack["Subscription.ListParams"]
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
    def modify(
        cls, id, **params: Unpack["Subscription.ModifyParams"]
    ) -> "Subscription":
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
        **params: Unpack["Subscription.ResumeParams"]
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
    def resume(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ):
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
        cls, id: str, **params: Unpack["Subscription.RetrieveParams"]
    ) -> "Subscription":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Subscription.SearchParams"]
    ) -> SearchResultObject["Subscription"]:
        return cls._search(
            search_url="/v1/subscriptions/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
