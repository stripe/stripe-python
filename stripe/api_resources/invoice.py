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
from typing import Dict, List, Optional, Union, cast
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
    from stripe.api_resources.card import Card
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice_line_item import InvoiceLineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.quote import Quote
    from stripe.api_resources.source import Source
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Invoice(
    CreateableAPIResource["Invoice"],
    DeletableAPIResource["Invoice"],
    ListableAPIResource["Invoice"],
    SearchableAPIResource["Invoice"],
    UpdateableAPIResource["Invoice"],
):
    """
    Invoices are statements of amounts owed by a customer, and are either
    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://stripe.com/docs/billing/customer/balance).

    Related guide: [Send invoices to customers](https://stripe.com/docs/billing/invoices/sending)
    """

    OBJECT_NAME = "invoice"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            application_fee_amount: NotRequired["int|None"]
            auto_advance: NotRequired["bool|None"]
            automatic_tax: NotRequired["Invoice.CreateParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            currency: NotRequired["str|None"]
            custom_fields: NotRequired[
                "Literal['']|List[Invoice.CreateParamsCustomField]|None"
            ]
            customer: NotRequired["str|None"]
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["str|None"]
            default_tax_rates: NotRequired["List[str]|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.CreateParamsDiscount]|None"
            ]
            due_date: NotRequired["int|None"]
            effective_at: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            footer: NotRequired["str|None"]
            from_invoice: NotRequired["Invoice.CreateParamsFromInvoice|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            payment_settings: NotRequired[
                "Invoice.CreateParamsPaymentSettings|None"
            ]
            pending_invoice_items_behavior: NotRequired[
                "Literal['exclude', 'include', 'include_and_require']|None"
            ]
            rendering: NotRequired["Invoice.CreateParamsRendering|None"]
            rendering_options: NotRequired[
                "Literal['']|Invoice.CreateParamsRenderingOptions|None"
            ]
            shipping_cost: NotRequired["Invoice.CreateParamsShippingCost|None"]
            shipping_details: NotRequired[
                "Invoice.CreateParamsShippingDetails|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            transfer_data: NotRequired["Invoice.CreateParamsTransferData|None"]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsShippingDetails(TypedDict):
            address: "Invoice.CreateParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateData|None"
            ]

        class CreateParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class CreateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Invoice.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class CreateParamsRendering(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            pdf: NotRequired["Invoice.CreateParamsRenderingPdf|None"]

        class CreateParamsRenderingPdf(TypedDict):
            page_size: NotRequired["Literal['a4', 'auto', 'letter']|None"]

        class CreateParamsPaymentSettings(TypedDict):
            default_mandate: NotRequired["Literal['']|str|None"]
            payment_method_options: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
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
            prefetch: NotRequired["List[Literal['balances']]|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            installments: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
            TypedDict,
        ):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
            TypedDict,
        ):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

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
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
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

        class CreateParamsFromInvoice(TypedDict):
            action: Literal["revision"]
            invoice: str

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class CreateParamsCustomField(TypedDict):
            name: str
            value: str

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool

        class DeleteParams(RequestOptions):
            pass

        class FinalizeInvoiceParams(RequestOptions):
            auto_advance: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            created: NotRequired["Invoice.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            due_date: NotRequired["Invoice.ListParamsDueDate|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['draft', 'open', 'paid', 'uncollectible', 'void']|None"
            ]
            subscription: NotRequired["str|None"]

        class ListParamsDueDate(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class MarkUncollectibleParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyParams(RequestOptions):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            application_fee_amount: NotRequired["int|None"]
            auto_advance: NotRequired["bool|None"]
            automatic_tax: NotRequired["Invoice.ModifyParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            custom_fields: NotRequired[
                "Literal['']|List[Invoice.ModifyParamsCustomField]|None"
            ]
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["Literal['']|str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.ModifyParamsDiscount]|None"
            ]
            due_date: NotRequired["int|None"]
            effective_at: NotRequired["Literal['']|int|None"]
            expand: NotRequired["List[str]|None"]
            footer: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            payment_settings: NotRequired[
                "Invoice.ModifyParamsPaymentSettings|None"
            ]
            rendering: NotRequired["Invoice.ModifyParamsRendering|None"]
            rendering_options: NotRequired[
                "Literal['']|Invoice.ModifyParamsRenderingOptions|None"
            ]
            shipping_cost: NotRequired[
                "Literal['']|Invoice.ModifyParamsShippingCost|None"
            ]
            shipping_details: NotRequired[
                "Literal['']|Invoice.ModifyParamsShippingDetails|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Literal['']|Invoice.ModifyParamsTransferData|None"
            ]

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class ModifyParamsShippingDetails(TypedDict):
            address: "Invoice.ModifyParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateData|None"
            ]

        class ModifyParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class ModifyParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Invoice.ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class ModifyParamsRendering(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            pdf: NotRequired["Invoice.ModifyParamsRenderingPdf|None"]

        class ModifyParamsRenderingPdf(TypedDict):
            page_size: NotRequired["Literal['a4', 'auto', 'letter']|None"]

        class ModifyParamsPaymentSettings(TypedDict):
            default_mandate: NotRequired["Literal['']|str|None"]
            payment_method_options: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
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
            prefetch: NotRequired["List[Literal['balances']]|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            installments: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
            TypedDict,
        ):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
            TypedDict,
        ):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

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
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
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

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class ModifyParamsCustomField(TypedDict):
            name: str
            value: str

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool

        class PayParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            forgive: NotRequired["bool|None"]
            mandate: NotRequired["Literal['']|str|None"]
            off_session: NotRequired["bool|None"]
            paid_out_of_band: NotRequired["bool|None"]
            payment_method: NotRequired["str|None"]
            source: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SendInvoiceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class UpcomingParams(RequestOptions):
            automatic_tax: NotRequired[
                "Invoice.UpcomingParamsAutomaticTax|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Invoice.UpcomingParamsCustomerDetails|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_items: NotRequired[
                "List[Invoice.UpcomingParamsInvoiceItem]|None"
            ]
            schedule: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            subscription_billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|int|None"
            ]
            subscription_cancel_at: NotRequired["Literal['']|int|None"]
            subscription_cancel_at_period_end: NotRequired["bool|None"]
            subscription_cancel_now: NotRequired["bool|None"]
            subscription_default_tax_rates: NotRequired[
                "Literal['']|List[str]|None"
            ]
            subscription_items: NotRequired[
                "List[Invoice.UpcomingParamsSubscriptionItem]|None"
            ]
            subscription_proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            subscription_proration_date: NotRequired["int|None"]
            subscription_resume_at: NotRequired["Literal['now']|None"]
            subscription_start_date: NotRequired["int|None"]
            subscription_trial_end: NotRequired["Literal['now']|int|None"]
            subscription_trial_from_plan: NotRequired["bool|None"]

        class UpcomingParamsSubscriptionItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Invoice.UpcomingParamsSubscriptionItemBillingThresholds|None"
            ]
            clear_usage: NotRequired["bool|None"]
            deleted: NotRequired["bool|None"]
            id: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingParamsSubscriptionItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class UpcomingParamsSubscriptionItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Invoice.UpcomingParamsSubscriptionItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsSubscriptionItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class UpcomingParamsSubscriptionItemBillingThresholds(TypedDict):
            usage_gte: int

        class UpcomingParamsInvoiceItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingParamsInvoiceItemDiscount]|None"
            ]
            invoiceitem: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired["Invoice.UpcomingParamsInvoiceItemPeriod|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingParamsInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsInvoiceItemPeriod(TypedDict):
            end: int
            start: int

        class UpcomingParamsInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class UpcomingParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class UpcomingParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Literal['']|Invoice.UpcomingParamsCustomerDetailsAddress|None"
            ]
            shipping: NotRequired[
                "Literal['']|Invoice.UpcomingParamsCustomerDetailsShipping|None"
            ]
            tax: NotRequired["Invoice.UpcomingParamsCustomerDetailsTax|None"]
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Invoice.UpcomingParamsCustomerDetailsTaxId]|None"
            ]

        class UpcomingParamsCustomerDetailsTaxId(TypedDict):
            type: Literal[
                "ad_nrt",
                "ae_trn",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "bg_uic",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "ch_vat",
                "cl_tin",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "hk_br",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kr_brn",
                "li_uid",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "no_vat",
                "nz_gst",
                "pe_ruc",
                "ph_tin",
                "ro_tin",
                "rs_pib",
                "ru_inn",
                "ru_kpp",
                "sa_vat",
                "sg_gst",
                "sg_uen",
                "si_tin",
                "sv_nit",
                "th_vat",
                "tr_tin",
                "tw_vat",
                "ua_vat",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class UpcomingParamsCustomerDetailsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]

        class UpcomingParamsCustomerDetailsShipping(TypedDict):
            address: "Invoice.UpcomingParamsCustomerDetailsShippingAddress"
            name: str
            phone: NotRequired["str|None"]

        class UpcomingParamsCustomerDetailsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingParamsAutomaticTax(TypedDict):
            enabled: bool

        class UpcomingLinesParams(RequestOptions):
            automatic_tax: NotRequired[
                "Invoice.UpcomingLinesParamsAutomaticTax|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Invoice.UpcomingLinesParamsCustomerDetails|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingLinesParamsDiscount]|None"
            ]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            invoice_items: NotRequired[
                "List[Invoice.UpcomingLinesParamsInvoiceItem]|None"
            ]
            limit: NotRequired["int|None"]
            schedule: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            subscription_billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|int|None"
            ]
            subscription_cancel_at: NotRequired["Literal['']|int|None"]
            subscription_cancel_at_period_end: NotRequired["bool|None"]
            subscription_cancel_now: NotRequired["bool|None"]
            subscription_default_tax_rates: NotRequired[
                "Literal['']|List[str]|None"
            ]
            subscription_items: NotRequired[
                "List[Invoice.UpcomingLinesParamsSubscriptionItem]|None"
            ]
            subscription_proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            subscription_proration_date: NotRequired["int|None"]
            subscription_resume_at: NotRequired["Literal['now']|None"]
            subscription_start_date: NotRequired["int|None"]
            subscription_trial_end: NotRequired["Literal['now']|int|None"]
            subscription_trial_from_plan: NotRequired["bool|None"]

        class UpcomingLinesParamsSubscriptionItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsSubscriptionItemBillingThresholds|None"
            ]
            clear_usage: NotRequired["bool|None"]
            deleted: NotRequired["bool|None"]
            id: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingLinesParamsSubscriptionItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class UpcomingLinesParamsSubscriptionItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Invoice.UpcomingLinesParamsSubscriptionItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsSubscriptionItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class UpcomingLinesParamsSubscriptionItemBillingThresholds(TypedDict):
            usage_gte: int

        class UpcomingLinesParamsInvoiceItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingLinesParamsInvoiceItemDiscount]|None"
            ]
            invoiceitem: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemPeriod|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsInvoiceItemPeriod(TypedDict):
            end: int
            start: int

        class UpcomingLinesParamsInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class UpcomingLinesParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class UpcomingLinesParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsCustomerDetailsAddress|None"
            ]
            shipping: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsCustomerDetailsShipping|None"
            ]
            tax: NotRequired[
                "Invoice.UpcomingLinesParamsCustomerDetailsTax|None"
            ]
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Invoice.UpcomingLinesParamsCustomerDetailsTaxId]|None"
            ]

        class UpcomingLinesParamsCustomerDetailsTaxId(TypedDict):
            type: Literal[
                "ad_nrt",
                "ae_trn",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "bg_uic",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "ch_vat",
                "cl_tin",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "hk_br",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kr_brn",
                "li_uid",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "no_vat",
                "nz_gst",
                "pe_ruc",
                "ph_tin",
                "ro_tin",
                "rs_pib",
                "ru_inn",
                "ru_kpp",
                "sa_vat",
                "sg_gst",
                "sg_uen",
                "si_tin",
                "sv_nit",
                "th_vat",
                "tr_tin",
                "tw_vat",
                "ua_vat",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class UpcomingLinesParamsCustomerDetailsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]

        class UpcomingLinesParamsCustomerDetailsShipping(TypedDict):
            address: "Invoice.UpcomingLinesParamsCustomerDetailsShippingAddress"
            name: str
            phone: NotRequired["str|None"]

        class UpcomingLinesParamsCustomerDetailsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingLinesParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingLinesParamsAutomaticTax(TypedDict):
            enabled: bool

        class VoidInvoiceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
            query: str

    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    attempt_count: int
    attempted: bool
    auto_advance: Optional[bool]
    automatic_tax: StripeObject
    billing_reason: Optional[
        Literal[
            "automatic_pending_invoice_item_invoice",
            "manual",
            "quote_accept",
            "subscription",
            "subscription_create",
            "subscription_cycle",
            "subscription_threshold",
            "subscription_update",
            "upcoming",
        ]
    ]
    charge: Optional[ExpandableField["Charge"]]
    collection_method: Literal["charge_automatically", "send_invoice"]
    created: int
    currency: str
    custom_fields: Optional[List[StripeObject]]
    customer: Optional[ExpandableField["Customer"]]
    customer_address: Optional[StripeObject]
    customer_email: Optional[str]
    customer_name: Optional[str]
    customer_phone: Optional[str]
    customer_shipping: Optional[StripeObject]
    customer_tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    customer_tax_ids: Optional[List[StripeObject]]
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    default_source: Optional[
        ExpandableField[Union["Account", "BankAccount", "Card", "Source"]]
    ]
    default_tax_rates: List["TaxRate"]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[ExpandableField["Discount"]]]
    due_date: Optional[int]
    effective_at: Optional[int]
    ending_balance: Optional[int]
    footer: Optional[str]
    from_invoice: Optional[StripeObject]
    hosted_invoice_url: Optional[str]
    id: Optional[str]
    invoice_pdf: Optional[str]
    last_finalization_error: Optional[StripeObject]
    latest_revision: Optional[ExpandableField["Invoice"]]
    lines: ListObject["InvoiceLineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[int]
    number: Optional[str]
    object: Literal["invoice"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    paid: bool
    paid_out_of_band: bool
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_settings: StripeObject
    period_end: int
    period_start: int
    post_payment_credit_notes_amount: int
    pre_payment_credit_notes_amount: int
    quote: Optional[ExpandableField["Quote"]]
    receipt_number: Optional[str]
    rendering: Optional[StripeObject]
    rendering_options: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    starting_balance: int
    statement_descriptor: Optional[str]
    status: Optional[Literal["draft", "open", "paid", "uncollectible", "void"]]
    status_transitions: StripeObject
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_details: Optional[StripeObject]
    subscription_proration_date: Optional[int]
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax: Optional[int]
    test_clock: Optional[ExpandableField["TestClock"]]
    threshold_reason: Optional[StripeObject]
    total: int
    total_discount_amounts: Optional[List[StripeObject]]
    total_excluding_tax: Optional[int]
    total_tax_amounts: List[StripeObject]
    transfer_data: Optional[StripeObject]
    webhooks_delivered_at: Optional[int]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.CreateParams"]
    ) -> "Invoice":
        return cast(
            "Invoice",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Invoice.DeleteParams"]
    ) -> "Invoice":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Invoice",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Invoice.DeleteParams"]) -> "Invoice":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def _cls_finalize_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.FinalizeInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_finalize_invoice")
    def finalize_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.FinalizeInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(self.get("id"))
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
        **params: Unpack["Invoice.ListParams"]
    ) -> ListObject["Invoice"]:
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
    def _cls_mark_uncollectible(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.MarkUncollectibleParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_uncollectible")
    def mark_uncollectible(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.MarkUncollectibleParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Unpack["Invoice.ModifyParams"]) -> "Invoice":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Invoice",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_pay(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.PayParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_pay")
    def pay(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.PayParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Invoice.RetrieveParams"]
    ) -> "Invoice":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_send_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.SendInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/send".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_send_invoice")
    def send_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.SendInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/send".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def upcoming(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.UpcomingParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/invoices/upcoming",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def upcoming_lines(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.UpcomingLinesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/invoices/upcoming/lines",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def _cls_void_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.VoidInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_void_invoice")
    def void_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.VoidInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Invoice.SearchParams"]
    ) -> SearchResultObject["Invoice"]:
        return cls._search(search_url="/v1/invoices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Invoice.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()
