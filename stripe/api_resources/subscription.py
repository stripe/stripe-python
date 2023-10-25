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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, Iterator, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card as CardResource
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.source import Source
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

    OBJECT_NAME: ClassVar[Literal["subscription"]] = "subscription"

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

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            cancellation_details: NotRequired[
                "Subscription.CancelParamsCancellationDetails|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_now: NotRequired["bool|None"]
            prorate: NotRequired["bool|None"]

        class CancelParamsCancellationDetails(TypedDict):
            comment: NotRequired["Literal['']|str|None"]
            feedback: NotRequired[
                "Literal['']|Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']|None"
            ]

        class CreateParams(RequestOptions):
            add_invoice_items: NotRequired[
                "List[Subscription.CreateParamsAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "Subscription.CreateParamsAutomaticTax|None"
            ]
            backdate_start_date: NotRequired["int|None"]
            billing_cycle_anchor: NotRequired["int|None"]
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.CreateParamsBillingThresholds|None"
            ]
            cancel_at: NotRequired["int|None"]
            cancel_at_period_end: NotRequired["bool|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            customer: str
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Subscription.CreateParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_settings: NotRequired[
                "Subscription.CreateParamsInvoiceSettings|None"
            ]
            items: NotRequired["List[Subscription.CreateParamsItem]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            off_session: NotRequired["bool|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            payment_settings: NotRequired[
                "Subscription.CreateParamsPaymentSettings|None"
            ]
            pending_invoice_item_interval: NotRequired[
                "Literal['']|Subscription.CreateParamsPendingInvoiceItemInterval|None"
            ]
            prebilling: NotRequired["Subscription.CreateParamsPrebilling|None"]
            promotion_code: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            transfer_data: NotRequired[
                "Subscription.CreateParamsTransferData|None"
            ]
            trial_end: NotRequired["Literal['now']|int|None"]
            trial_from_plan: NotRequired["bool|None"]
            trial_period_days: NotRequired["int|None"]
            trial_settings: NotRequired[
                "Subscription.CreateParamsTrialSettings|None"
            ]

        class CreateParamsTrialSettings(TypedDict):
            end_behavior: "Subscription.CreateParamsTrialSettingsEndBehavior"

        class CreateParamsTrialSettingsEndBehavior(TypedDict):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]

        class CreateParamsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsPrebilling(TypedDict):
            iterations: int
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]

        class CreateParamsPendingInvoiceItemInterval(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsPaymentSettings(TypedDict):
            payment_method_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            save_default_payment_method: NotRequired[
                "Literal['off', 'on_subscription']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions|None"
            ]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
            TypedDict,
        ):
            amount: NotRequired["int|None"]
            amount_type: NotRequired["Literal['fixed', 'maximum']|None"]
            description: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.CreateParamsItemBillingThresholds|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[Subscription.CreateParamsItemDiscount]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Subscription.CreateParamsItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            trial: NotRequired["Subscription.CreateParamsItemTrial|None"]

        class CreateParamsItemTrial(TypedDict):
            converts_to: NotRequired["List[str]|None"]
            type: Literal["free", "paid"]

        class CreateParamsItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Subscription.CreateParamsItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["str|None"]

        class CreateParamsItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.CreateParamsItemDiscountDiscountEnd|None"
            ]

        class CreateParamsItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsItemBillingThresholds(TypedDict):
            usage_gte: int

        class CreateParamsInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "Subscription.CreateParamsInvoiceSettingsIssuer|None"
            ]

        class CreateParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.CreateParamsDiscountDiscountEnd|None"
            ]

        class CreateParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Subscription.CreateParamsAutomaticTaxLiability|None"
            ]

        class CreateParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[Subscription.CreateParamsAddInvoiceItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["str|None"]

        class CreateParamsAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemDiscountDiscountEnd|None"
            ]

        class CreateParamsAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.CreateParamsAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsAddInvoiceItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class DeleteDiscountParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            automatic_tax: NotRequired[
                "Subscription.ListParamsAutomaticTax|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            created: NotRequired["Subscription.ListParamsCreated|int|None"]
            current_period_end: NotRequired[
                "Subscription.ListParamsCurrentPeriodEnd|int|None"
            ]
            current_period_start: NotRequired[
                "Subscription.ListParamsCurrentPeriodStart|int|None"
            ]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['active', 'all', 'canceled', 'ended', 'incomplete', 'incomplete_expired', 'past_due', 'paused', 'trialing', 'unpaid']|None"
            ]
            test_clock: NotRequired["str|None"]

        class ListParamsCurrentPeriodStart(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCurrentPeriodEnd(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsAutomaticTax(TypedDict):
            enabled: bool

        class ModifyParams(RequestOptions):
            add_invoice_items: NotRequired[
                "List[Subscription.ModifyParamsAddInvoiceItem]|None"
            ]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "Subscription.ModifyParamsAutomaticTax|None"
            ]
            billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|None"
            ]
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.ModifyParamsBillingThresholds|None"
            ]
            cancel_at: NotRequired["Literal['']|int|None"]
            cancel_at_period_end: NotRequired["bool|None"]
            cancellation_details: NotRequired[
                "Subscription.ModifyParamsCancellationDetails|None"
            ]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            coupon: NotRequired["str|None"]
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["Literal['']|str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[Subscription.ModifyParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_settings: NotRequired[
                "Subscription.ModifyParamsInvoiceSettings|None"
            ]
            items: NotRequired["List[Subscription.ModifyParamsItem]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            off_session: NotRequired["bool|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            pause_collection: NotRequired[
                "Literal['']|Subscription.ModifyParamsPauseCollection|None"
            ]
            payment_behavior: NotRequired[
                "Literal['allow_incomplete', 'default_incomplete', 'error_if_incomplete', 'pending_if_incomplete']|None"
            ]
            payment_settings: NotRequired[
                "Subscription.ModifyParamsPaymentSettings|None"
            ]
            pending_invoice_item_interval: NotRequired[
                "Literal['']|Subscription.ModifyParamsPendingInvoiceItemInterval|None"
            ]
            prebilling: NotRequired["Subscription.ModifyParamsPrebilling|None"]
            promotion_code: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            proration_date: NotRequired["int|None"]
            transfer_data: NotRequired[
                "Literal['']|Subscription.ModifyParamsTransferData|None"
            ]
            trial_end: NotRequired["Literal['now']|int|None"]
            trial_from_plan: NotRequired["bool|None"]
            trial_settings: NotRequired[
                "Subscription.ModifyParamsTrialSettings|None"
            ]

        class ModifyParamsTrialSettings(TypedDict):
            end_behavior: "Subscription.ModifyParamsTrialSettingsEndBehavior"

        class ModifyParamsTrialSettingsEndBehavior(TypedDict):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]

        class ModifyParamsTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class ModifyParamsPrebilling(TypedDict):
            iterations: int
            update_behavior: NotRequired["Literal['prebill', 'reset']|None"]

        class ModifyParamsPendingInvoiceItemInterval(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsPaymentSettings(TypedDict):
            payment_method_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            save_default_payment_method: NotRequired[
                "Literal['off', 'on_subscription']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions|None"
            ]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardMandateOptions(
            TypedDict,
        ):
            amount: NotRequired["int|None"]
            amount_type: NotRequired["Literal['fixed', 'maximum']|None"]
            description: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ModifyParamsPauseCollection(TypedDict):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            resumes_at: NotRequired["int|None"]

        class ModifyParamsItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Subscription.ModifyParamsItemBillingThresholds|None"
            ]
            clear_usage: NotRequired["bool|None"]
            deleted: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Subscription.ModifyParamsItemDiscount]|None"
            ]
            id: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Subscription.ModifyParamsItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Subscription.ModifyParamsItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["str|None"]

        class ModifyParamsItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class ModifyParamsItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.ModifyParamsItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsItemBillingThresholds(TypedDict):
            usage_gte: int

        class ModifyParamsInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "Subscription.ModifyParamsInvoiceSettingsIssuer|None"
            ]

        class ModifyParamsInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.ModifyParamsDiscountDiscountEnd|None"
            ]

        class ModifyParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsCancellationDetails(TypedDict):
            comment: NotRequired["Literal['']|str|None"]
            feedback: NotRequired[
                "Literal['']|Literal['customer_service', 'low_quality', 'missing_features', 'other', 'switched_service', 'too_complex', 'too_expensive', 'unused']|None"
            ]

        class ModifyParamsBillingThresholds(TypedDict):
            amount_gte: NotRequired["int|None"]
            reset_billing_cycle_anchor: NotRequired["bool|None"]

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Subscription.ModifyParamsAutomaticTaxLiability|None"
            ]

        class ModifyParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsAddInvoiceItem(TypedDict):
            discounts: NotRequired[
                "List[Subscription.ModifyParamsAddInvoiceItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsAddInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["str|None"]

        class ModifyParamsAddInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemDiscountDiscountEnd|None"
            ]

        class ModifyParamsAddInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Subscription.ModifyParamsAddInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsAddInvoiceItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ResumeParams(RequestOptions):
            billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|None"
            ]
            expand: NotRequired["List[str]|None"]
            proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            proration_date: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
            query: str

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
    default_source: Optional[
        ExpandableField[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
    ]
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
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            cls._static_request(
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
            ),
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.CancelParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            self._request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}".format(
                    subscription_exposed_id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
    ) -> "Discount":
        return cast(
            "Discount",
            cls._static_request(
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
            ),
        )

    @util.class_method_variant("_cls_delete_discount")
    def delete_discount(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.DeleteDiscountParams"]
    ) -> "Discount":
        return cast(
            "Discount",
            self._request(
                "delete",
                "/v1/subscriptions/{subscription_exposed_id}/discount".format(
                    subscription_exposed_id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
        cls, id: str, **params: Unpack["Subscription.ModifyParams"]
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
    ) -> "Subscription":
        return cast(
            "Subscription",
            cls._static_request(
                "post",
                "/v1/subscriptions/{subscription}/resume".format(
                    subscription=util.sanitize_id(subscription)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @util.class_method_variant("_cls_resume")
    def resume(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Subscription.ResumeParams"]
    ) -> "Subscription":
        return cast(
            "Subscription",
            self._request(
                "post",
                "/v1/subscriptions/{subscription}/resume".format(
                    subscription=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Subscription.SearchParams"]
    ) -> Iterator["Subscription"]:
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
