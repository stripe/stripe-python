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
            Optional["Subscription.CancelParamsCancellationDetails"]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_now: NotRequired[Optional[bool]]
        prorate: NotRequired[Optional[bool]]

    class CancelParamsCancellationDetails(TypedDict):
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
            Optional[List["Subscription.CreateParamsAddInvoiceItem"]]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["Subscription.CreateParamsAutomaticTax"]
        ]
        backdate_start_date: NotRequired[Optional[int]]
        billing_cycle_anchor: NotRequired[Optional[int]]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsItemBillingThresholds",
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
        items: NotRequired[Optional[List["Subscription.CreateParamsItem"]]]
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
            Optional["Subscription.CreateParamsPaymentSettings"]
        ]
        pending_invoice_item_interval: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPendingInvoiceItemInterval",
                ]
            ]
        ]
        promotion_code: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        transfer_data: NotRequired[
            Optional["Subscription.CreateParamsTransferData"]
        ]
        trial_end: NotRequired[Optional[Union[Literal["now"], int]]]
        trial_from_plan: NotRequired[Optional[bool]]
        trial_period_days: NotRequired[Optional[int]]
        trial_settings: NotRequired[
            Optional["Subscription.CreateParamsTrialSettings"]
        ]

    class CreateParamsTrialSettings(TypedDict):
        end_behavior: "Subscription.CreateParamsTrialSettingsEndBehavior"

    class CreateParamsTrialSettingsEndBehavior(TypedDict):
        missing_payment_method: Literal["cancel", "create_invoice", "pause"]

    class CreateParamsTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateParamsPendingInvoiceItemInterval(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateParamsPaymentSettings(TypedDict):
        payment_method_options: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptions"
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

    class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
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

    class CreateParamsPaymentSettingsPaymentMethodOptionsKonbini(TypedDict):
        pass

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
            ]
        ]
        type: NotRequired[Optional[str]]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions"
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

    class CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
        TypedDict,
    ):
        amount: NotRequired[Optional[int]]
        amount_type: NotRequired[Optional[Literal["fixed", "maximum"]]]
        description: NotRequired[Optional[str]]

    class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
        TypedDict,
    ):
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class CreateParamsItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.CreateParamsItemBillingThresholds",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        plan: NotRequired[Optional[str]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.CreateParamsItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateParamsItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "Subscription.CreateParamsItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateParamsItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateParamsItemBillingThresholds(TypedDict):
        usage_gte: int

    class CreateParamsBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool

    class CreateParamsAddInvoiceItem(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.CreateParamsAddInvoiceItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class CreateParamsAddInvoiceItemPriceData(TypedDict):
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
            Optional["Subscription.ListParamsAutomaticTax"]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        created: NotRequired[
            Optional[Union["Subscription.ListParamsCreated", int]]
        ]
        current_period_end: NotRequired[
            Optional[Union["Subscription.ListParamsCurrentPeriodEnd", int]]
        ]
        current_period_start: NotRequired[
            Optional[Union["Subscription.ListParamsCurrentPeriodStart", int]]
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

    class ListParamsCurrentPeriodStart(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCurrentPeriodEnd(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsAutomaticTax(TypedDict):
        enabled: bool

    class ModifyParams(RequestOptions):
        add_invoice_items: NotRequired[
            Optional[List["Subscription.ModifyParamsAddInvoiceItem"]]
        ]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["Subscription.ModifyParamsAutomaticTax"]
        ]
        billing_cycle_anchor: NotRequired[
            Optional[Literal["now", "unchanged"]]
        ]
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsItemBillingThresholds",
                ]
            ]
        ]
        cancel_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancel_at_period_end: NotRequired[Optional[bool]]
        cancellation_details: NotRequired[
            Optional["Subscription.ModifyParamsCancellationDetails"]
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
        items: NotRequired[Optional[List["Subscription.ModifyParamsItem"]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        off_session: NotRequired[Optional[bool]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        pause_collection: NotRequired[
            Optional[
                Union[Literal[""], "Subscription.ModifyParamsPauseCollection"]
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
            Optional["Subscription.ModifyParamsPaymentSettings"]
        ]
        pending_invoice_item_interval: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPendingInvoiceItemInterval",
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
                Union[Literal[""], "Subscription.ModifyParamsTransferData"]
            ]
        ]
        trial_end: NotRequired[Optional[Union[Literal["now"], int]]]
        trial_from_plan: NotRequired[Optional[bool]]
        trial_settings: NotRequired[
            Optional["Subscription.ModifyParamsTrialSettings"]
        ]

    class ModifyParamsTrialSettings(TypedDict):
        end_behavior: "Subscription.ModifyParamsTrialSettingsEndBehavior"

    class ModifyParamsTrialSettingsEndBehavior(TypedDict):
        missing_payment_method: Literal["cancel", "create_invoice", "pause"]

    class ModifyParamsTransferData(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class ModifyParamsPendingInvoiceItemInterval(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyParamsPaymentSettings(TypedDict):
        payment_method_options: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions"
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

    class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
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

    class ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini(TypedDict):
        pass

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
            ]
        ]
        type: NotRequired[Optional[str]]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions"
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

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
        TypedDict,
    ):
        amount: NotRequired[Optional[int]]
        amount_type: NotRequired[Optional[Literal["fixed", "maximum"]]]
        description: NotRequired[Optional[str]]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
        TypedDict,
    ):
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ModifyParamsPauseCollection(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        resumes_at: NotRequired[Optional[int]]

    class ModifyParamsItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Subscription.ModifyParamsItemBillingThresholds",
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
            Optional["Subscription.ModifyParamsItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyParamsItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "Subscription.ModifyParamsItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class ModifyParamsItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class ModifyParamsItemBillingThresholds(TypedDict):
        usage_gte: int

    class ModifyParamsCancellationDetails(TypedDict):
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

    class ModifyParamsBillingThresholds(TypedDict):
        amount_gte: NotRequired[Optional[int]]
        reset_billing_cycle_anchor: NotRequired[Optional[bool]]

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool

    class ModifyParamsAddInvoiceItem(TypedDict):
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Subscription.ModifyParamsAddInvoiceItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class ModifyParamsAddInvoiceItemPriceData(TypedDict):
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
