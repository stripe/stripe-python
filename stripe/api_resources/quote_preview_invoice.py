# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.invoice_line_item import InvoiceLineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.quote import Quote
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class QuotePreviewInvoice(ListableAPIResource["QuotePreviewInvoice"]):
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

    OBJECT_NAME = "quote_preview_invoice"
    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    applies_to: StripeObject
    attempt_count: int
    attempted: bool
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
    collection_method: Literal["charge_automatically", "send_invoice"]
    created: int
    currency: str
    custom_fields: Optional[List[StripeObject]]
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
    id: str
    issuer: Optional[StripeObject]
    last_finalization_error: Optional[StripeObject]
    latest_revision: Optional[ExpandableField["Invoice"]]
    lines: ListObject["InvoiceLineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[int]
    number: Optional[str]
    object: Literal["quote_preview_invoice"]
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

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["QuotePreviewInvoice"]:
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
