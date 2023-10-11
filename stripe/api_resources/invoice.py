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
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice_line_item import InvoiceLineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.quote import Quote
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

    class CreateParams(RequestOptions):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        application_fee_amount: NotRequired[Optional[int]]
        auto_advance: NotRequired[Optional[bool]]
        automatic_tax: NotRequired[
            Optional["Invoice.CreateParamsAutomaticTax"]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        currency: NotRequired[Optional[str]]
        custom_fields: NotRequired[
            Optional[
                Union[Literal[""], List["Invoice.CreateParamsCustomField"]]
            ]
        ]
        customer: NotRequired[Optional[str]]
        days_until_due: NotRequired[Optional[int]]
        default_payment_method: NotRequired[Optional[str]]
        default_source: NotRequired[Optional[str]]
        default_tax_rates: NotRequired[Optional[List[str]]]
        description: NotRequired[Optional[str]]
        discounts: NotRequired[
            Optional[Union[Literal[""], List["Invoice.CreateParamsDiscount"]]]
        ]
        due_date: NotRequired[Optional[int]]
        effective_at: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        footer: NotRequired[Optional[str]]
        from_invoice: NotRequired[Optional["Invoice.CreateParamsFromInvoice"]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        on_behalf_of: NotRequired[Optional[str]]
        payment_settings: NotRequired[
            Optional["Invoice.CreateParamsPaymentSettings"]
        ]
        pending_invoice_items_behavior: NotRequired[
            Optional[Literal["exclude", "include", "include_and_require"]]
        ]
        rendering: NotRequired[Optional["Invoice.CreateParamsRendering"]]
        rendering_options: NotRequired[
            Optional[
                Union[Literal[""], "Invoice.CreateParamsRenderingOptions"]
            ]
        ]
        shipping_cost: NotRequired[
            Optional["Invoice.CreateParamsShippingCost"]
        ]
        shipping_details: NotRequired[
            Optional["Invoice.CreateParamsShippingDetails"]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        subscription: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["Invoice.CreateParamsTransferData"]
        ]

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreateParamsShippingDetails(TypedDict):
        address: "Invoice.CreateParamsShippingDetailsAddress"
        name: str
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsShippingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsShippingCost(TypedDict):
        shipping_rate: NotRequired[Optional[str]]
        shipping_rate_data: NotRequired[
            Optional["Invoice.CreateParamsShippingCostShippingRateData"]
        ]

    class CreateParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            Optional[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimate"
            ]
        ]
        display_name: str
        fixed_amount: NotRequired[
            Optional[
                "Invoice.CreateParamsShippingCostShippingRateDataFixedAmount"
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["fixed_amount"]]]

    class CreateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
        amount: int
        currency: str
        currency_options: NotRequired[
            Optional[
                Dict[
                    str,
                    "Invoice.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions",
                ]
            ]
        ]

    class CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
        TypedDict,
    ):
        amount: int
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class CreateParamsShippingCostShippingRateDataDeliveryEstimate(TypedDict):
        maximum: NotRequired[
            Optional[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
            ]
        ]
        minimum: NotRequired[
            Optional[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
            ]
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
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class CreateParamsRendering(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]
        pdf: NotRequired[Optional["Invoice.CreateParamsRenderingPdf"]]

    class CreateParamsRenderingPdf(TypedDict):
        page_size: NotRequired[Optional[Literal["a4", "auto", "letter"]]]

    class CreateParamsPaymentSettings(TypedDict):
        default_mandate: NotRequired[Optional[Union[Literal[""], str]]]
        payment_method_options: NotRequired[
            Optional["Invoice.CreateParamsPaymentSettingsPaymentMethodOptions"]
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

    class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCard",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
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
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
            ]
        ]
        type: NotRequired[Optional[str]]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        installments: NotRequired[
            Optional[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments"
            ]
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
        TypedDict,
    ):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan",
                ]
            ]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
        TypedDict,
    ):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
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

    class CreateParamsFromInvoice(TypedDict):
        action: Literal["revision"]
        invoice: str

    class CreateParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class CreateParamsCustomField(TypedDict):
        name: str
        value: str

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool

    class DeleteParams(RequestOptions):
        pass

    class FinalizeInvoiceParams(RequestOptions):
        auto_advance: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]

    class ListParams(RequestOptions):
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        created: NotRequired[Optional[Union["Invoice.ListParamsCreated", int]]]
        customer: NotRequired[Optional[str]]
        due_date: NotRequired[
            Optional[Union["Invoice.ListParamsDueDate", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[Literal["draft", "open", "paid", "uncollectible", "void"]]
        ]
        subscription: NotRequired[Optional[str]]

    class ListParamsDueDate(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class MarkUncollectibleParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyParams(RequestOptions):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        application_fee_amount: NotRequired[Optional[int]]
        auto_advance: NotRequired[Optional[bool]]
        automatic_tax: NotRequired[
            Optional["Invoice.ModifyParamsAutomaticTax"]
        ]
        collection_method: NotRequired[
            Optional[Literal["charge_automatically", "send_invoice"]]
        ]
        custom_fields: NotRequired[
            Optional[
                Union[Literal[""], List["Invoice.ModifyParamsCustomField"]]
            ]
        ]
        days_until_due: NotRequired[Optional[int]]
        default_payment_method: NotRequired[Optional[str]]
        default_source: NotRequired[Optional[Union[Literal[""], str]]]
        default_tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        description: NotRequired[Optional[str]]
        discounts: NotRequired[
            Optional[Union[Literal[""], List["Invoice.ModifyParamsDiscount"]]]
        ]
        due_date: NotRequired[Optional[int]]
        effective_at: NotRequired[Optional[Union[Literal[""], int]]]
        expand: NotRequired[Optional[List[str]]]
        footer: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        on_behalf_of: NotRequired[Optional[Union[Literal[""], str]]]
        payment_settings: NotRequired[
            Optional["Invoice.ModifyParamsPaymentSettings"]
        ]
        rendering: NotRequired[Optional["Invoice.ModifyParamsRendering"]]
        rendering_options: NotRequired[
            Optional[
                Union[Literal[""], "Invoice.ModifyParamsRenderingOptions"]
            ]
        ]
        shipping_cost: NotRequired[
            Optional[Union[Literal[""], "Invoice.ModifyParamsShippingCost"]]
        ]
        shipping_details: NotRequired[
            Optional[Union[Literal[""], "Invoice.ModifyParamsShippingDetails"]]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional[Union[Literal[""], "Invoice.ModifyParamsTransferData"]]
        ]

    class ModifyParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class ModifyParamsShippingDetails(TypedDict):
        address: "Invoice.ModifyParamsShippingDetailsAddress"
        name: str
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsShippingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyParamsShippingCost(TypedDict):
        shipping_rate: NotRequired[Optional[str]]
        shipping_rate_data: NotRequired[
            Optional["Invoice.ModifyParamsShippingCostShippingRateData"]
        ]

    class ModifyParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            Optional[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimate"
            ]
        ]
        display_name: str
        fixed_amount: NotRequired[
            Optional[
                "Invoice.ModifyParamsShippingCostShippingRateDataFixedAmount"
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["fixed_amount"]]]

    class ModifyParamsShippingCostShippingRateDataFixedAmount(TypedDict):
        amount: int
        currency: str
        currency_options: NotRequired[
            Optional[
                Dict[
                    str,
                    "Invoice.ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions",
                ]
            ]
        ]

    class ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
        TypedDict,
    ):
        amount: int
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class ModifyParamsShippingCostShippingRateDataDeliveryEstimate(TypedDict):
        maximum: NotRequired[
            Optional[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
            ]
        ]
        minimum: NotRequired[
            Optional[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
            ]
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
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class ModifyParamsRendering(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]
        pdf: NotRequired[Optional["Invoice.ModifyParamsRenderingPdf"]]

    class ModifyParamsRenderingPdf(TypedDict):
        page_size: NotRequired[Optional[Literal["a4", "auto", "letter"]]]

    class ModifyParamsPaymentSettings(TypedDict):
        default_mandate: NotRequired[Optional[Union[Literal[""], str]]]
        payment_method_options: NotRequired[
            Optional["Invoice.ModifyParamsPaymentSettingsPaymentMethodOptions"]
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

    class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCard",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
        TypedDict,
    ):
        financial_connections: NotRequired[
            Optional[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
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
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[str]]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
            ]
        ]
        type: NotRequired[Optional[str]]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        installments: NotRequired[
            Optional[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments"
            ]
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
        TypedDict,
    ):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan",
                ]
            ]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
        TypedDict,
    ):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
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

    class ModifyParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class ModifyParamsCustomField(TypedDict):
        name: str
        value: str

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool

    class PayParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        forgive: NotRequired[Optional[bool]]
        mandate: NotRequired[Optional[Union[Literal[""], str]]]
        off_session: NotRequired[Optional[bool]]
        paid_out_of_band: NotRequired[Optional[bool]]
        payment_method: NotRequired[Optional[str]]
        source: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SendInvoiceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class UpcomingParams(RequestOptions):
        automatic_tax: NotRequired[
            Optional["Invoice.UpcomingParamsAutomaticTax"]
        ]
        coupon: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        customer: NotRequired[Optional[str]]
        customer_details: NotRequired[
            Optional["Invoice.UpcomingParamsCustomerDetails"]
        ]
        discounts: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Invoice.UpcomingParamsInvoiceItemDiscount"],
                ]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_items: NotRequired[
            Optional[List["Invoice.UpcomingParamsInvoiceItem"]]
        ]
        schedule: NotRequired[Optional[str]]
        subscription: NotRequired[Optional[str]]
        subscription_billing_cycle_anchor: NotRequired[
            Optional[Union[Literal["now", "unchanged"], int]]
        ]
        subscription_cancel_at: NotRequired[Optional[Union[Literal[""], int]]]
        subscription_cancel_at_period_end: NotRequired[Optional[bool]]
        subscription_cancel_now: NotRequired[Optional[bool]]
        subscription_default_tax_rates: NotRequired[
            Optional[Union[Literal[""], List[str]]]
        ]
        subscription_items: NotRequired[
            Optional[List["Invoice.UpcomingParamsSubscriptionItem"]]
        ]
        subscription_proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        subscription_proration_date: NotRequired[Optional[int]]
        subscription_resume_at: NotRequired[Optional[Literal["now"]]]
        subscription_start_date: NotRequired[Optional[int]]
        subscription_trial_end: NotRequired[
            Optional[Union[Literal["now"], int]]
        ]
        subscription_trial_from_plan: NotRequired[Optional[bool]]

    class UpcomingParamsSubscriptionItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingParamsSubscriptionItemBillingThresholds",
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
            Optional["Invoice.UpcomingParamsSubscriptionItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class UpcomingParamsSubscriptionItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "Invoice.UpcomingParamsSubscriptionItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingParamsSubscriptionItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class UpcomingParamsSubscriptionItemBillingThresholds(TypedDict):
        usage_gte: int

    class UpcomingParamsInvoiceItem(TypedDict):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        discountable: NotRequired[Optional[bool]]
        discounts: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Invoice.UpcomingParamsInvoiceItemDiscount"],
                ]
            ]
        ]
        invoiceitem: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        period: NotRequired[
            Optional["Invoice.UpcomingParamsInvoiceItemPeriod"]
        ]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Invoice.UpcomingParamsInvoiceItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[Union[Literal[""], str]]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingParamsInvoiceItemPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingParamsInvoiceItemPeriod(TypedDict):
        end: int
        start: int

    class UpcomingParamsInvoiceItemDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class UpcomingParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class UpcomingParamsCustomerDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingParamsCustomerDetailsShippingAddress",
                ]
            ]
        ]
        shipping: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingParamsCustomerDetailsShipping",
                ]
            ]
        ]
        tax: NotRequired[Optional["Invoice.UpcomingParamsCustomerDetailsTax"]]
        tax_exempt: NotRequired[
            Optional[Union[Literal[""], Literal["exempt", "none", "reverse"]]]
        ]
        tax_ids: NotRequired[
            Optional[List["Invoice.UpcomingParamsCustomerDetailsTaxId"]]
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
        ip_address: NotRequired[Optional[Union[Literal[""], str]]]

    class UpcomingParamsCustomerDetailsShipping(TypedDict):
        address: "Invoice.UpcomingParamsCustomerDetailsShippingAddress"
        name: str
        phone: NotRequired[Optional[str]]

    class UpcomingParamsCustomerDetailsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class UpcomingParamsCustomerDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class UpcomingParamsAutomaticTax(TypedDict):
        enabled: bool

    class UpcomingLinesParams(RequestOptions):
        automatic_tax: NotRequired[
            Optional["Invoice.UpcomingLinesParamsAutomaticTax"]
        ]
        coupon: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        customer: NotRequired[Optional[str]]
        customer_details: NotRequired[
            Optional["Invoice.UpcomingLinesParamsCustomerDetails"]
        ]
        discounts: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Invoice.UpcomingLinesParamsInvoiceItemDiscount"],
                ]
            ]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice_items: NotRequired[
            Optional[List["Invoice.UpcomingLinesParamsInvoiceItem"]]
        ]
        limit: NotRequired[Optional[int]]
        schedule: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]
        subscription: NotRequired[Optional[str]]
        subscription_billing_cycle_anchor: NotRequired[
            Optional[Union[Literal["now", "unchanged"], int]]
        ]
        subscription_cancel_at: NotRequired[Optional[Union[Literal[""], int]]]
        subscription_cancel_at_period_end: NotRequired[Optional[bool]]
        subscription_cancel_now: NotRequired[Optional[bool]]
        subscription_default_tax_rates: NotRequired[
            Optional[Union[Literal[""], List[str]]]
        ]
        subscription_items: NotRequired[
            Optional[List["Invoice.UpcomingLinesParamsSubscriptionItem"]]
        ]
        subscription_proration_behavior: NotRequired[
            Optional[Literal["always_invoice", "create_prorations", "none"]]
        ]
        subscription_proration_date: NotRequired[Optional[int]]
        subscription_resume_at: NotRequired[Optional[Literal["now"]]]
        subscription_start_date: NotRequired[Optional[int]]
        subscription_trial_end: NotRequired[
            Optional[Union[Literal["now"], int]]
        ]
        subscription_trial_from_plan: NotRequired[Optional[bool]]

    class UpcomingLinesParamsSubscriptionItem(TypedDict):
        billing_thresholds: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingLinesParamsSubscriptionItemBillingThresholds",
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
            Optional["Invoice.UpcomingLinesParamsSubscriptionItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]

    class UpcomingLinesParamsSubscriptionItemPriceData(TypedDict):
        currency: str
        product: str
        recurring: "Invoice.UpcomingLinesParamsSubscriptionItemPriceDataRecurring"
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingLinesParamsSubscriptionItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class UpcomingLinesParamsSubscriptionItemBillingThresholds(TypedDict):
        usage_gte: int

    class UpcomingLinesParamsInvoiceItem(TypedDict):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        discountable: NotRequired[Optional[bool]]
        discounts: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Invoice.UpcomingLinesParamsInvoiceItemDiscount"],
                ]
            ]
        ]
        invoiceitem: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        period: NotRequired[
            Optional["Invoice.UpcomingLinesParamsInvoiceItemPeriod"]
        ]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Invoice.UpcomingLinesParamsInvoiceItemPriceData"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[Union[Literal[""], str]]]
        tax_rates: NotRequired[Optional[Union[Literal[""], List[str]]]]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingLinesParamsInvoiceItemPriceData(TypedDict):
        currency: str
        product: str
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class UpcomingLinesParamsInvoiceItemPeriod(TypedDict):
        end: int
        start: int

    class UpcomingLinesParamsInvoiceItemDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class UpcomingLinesParamsDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        discount: NotRequired[Optional[str]]

    class UpcomingLinesParamsCustomerDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingLinesParamsCustomerDetailsShippingAddress",
                ]
            ]
        ]
        shipping: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Invoice.UpcomingLinesParamsCustomerDetailsShipping",
                ]
            ]
        ]
        tax: NotRequired[
            Optional["Invoice.UpcomingLinesParamsCustomerDetailsTax"]
        ]
        tax_exempt: NotRequired[
            Optional[Union[Literal[""], Literal["exempt", "none", "reverse"]]]
        ]
        tax_ids: NotRequired[
            Optional[List["Invoice.UpcomingLinesParamsCustomerDetailsTaxId"]]
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
        ip_address: NotRequired[Optional[Union[Literal[""], str]]]

    class UpcomingLinesParamsCustomerDetailsShipping(TypedDict):
        address: "Invoice.UpcomingLinesParamsCustomerDetailsShippingAddress"
        name: str
        phone: NotRequired[Optional[str]]

    class UpcomingLinesParamsCustomerDetailsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class UpcomingLinesParamsCustomerDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class UpcomingLinesParamsAutomaticTax(TypedDict):
        enabled: bool

    class VoidInvoiceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
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
    default_source: Optional[ExpandableField[Any]]
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
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
