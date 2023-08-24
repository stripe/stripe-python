# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.discount import Discount


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
    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[Any]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[Any]
    application_fee_amount: Optional[int]
    attempt_count: int
    attempted: bool
    auto_advance: bool
    automatic_tax: Any
    billing_reason: Optional[str]
    charge: Optional[Any]
    collection_method: str
    created: str
    currency: str
    custom_fields: Optional[List[Any]]
    customer: Optional[Any]
    customer_address: Optional[Any]
    customer_email: Optional[str]
    customer_name: Optional[str]
    customer_phone: Optional[str]
    customer_shipping: Optional[Any]
    customer_tax_exempt: Optional[str]
    customer_tax_ids: Optional[List[Any]]
    default_payment_method: Optional[Any]
    default_source: Optional[Any]
    default_tax_rates: List["TaxRate"]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[Any]]
    due_date: Optional[str]
    effective_at: Optional[str]
    ending_balance: Optional[int]
    footer: Optional[str]
    from_invoice: Optional[Any]
    hosted_invoice_url: Optional[str]
    id: str
    invoice_pdf: Optional[str]
    last_finalization_error: Optional[Any]
    latest_revision: Optional[Any]
    lines: Any
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[str]
    number: Optional[str]
    object: Literal["invoice"]
    on_behalf_of: Optional[Any]
    paid: bool
    paid_out_of_band: bool
    payment_intent: Optional[Any]
    payment_settings: Any
    period_end: str
    period_start: str
    post_payment_credit_notes_amount: int
    pre_payment_credit_notes_amount: int
    quote: Optional[Any]
    receipt_number: Optional[str]
    rendering_options: Optional[Any]
    shipping_cost: Optional[Any]
    shipping_details: Optional[Any]
    starting_balance: int
    statement_descriptor: Optional[str]
    status: Optional[str]
    status_transitions: Any
    subscription: Optional[Any]
    subscription_details: Optional[Any]
    subscription_proration_date: int
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax: Optional[int]
    test_clock: Optional[Any]
    threshold_reason: Any
    total: int
    total_discount_amounts: Optional[List[Any]]
    total_excluding_tax: Optional[int]
    total_tax_amounts: List[Any]
    transfer_data: Optional[Any]
    webhooks_delivered_at: Optional[str]

    @classmethod
    def _cls_finalize_invoice(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def finalize_invoice(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_mark_uncollectible(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def mark_uncollectible(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_pay(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def pay(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_send_invoice(
        cls,
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def send_invoice(self, idempotency_key=None, **params):
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
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
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
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
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
        invoice,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def void_invoice(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/invoices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
