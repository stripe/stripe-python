# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class SourceTransaction(StripeObject):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    OBJECT_NAME = "source_transaction"

    class AchCreditTransfer(StripeObject):
        customer_data: Optional[str]
        fingerprint: Optional[str]
        last4: Optional[str]
        routing_number: Optional[str]

    class ChfCreditTransfer(StripeObject):
        reference: Optional[str]
        sender_address_country: Optional[str]
        sender_address_line1: Optional[str]
        sender_iban: Optional[str]
        sender_name: Optional[str]

    class GbpCreditTransfer(StripeObject):
        fingerprint: Optional[str]
        funding_method: Optional[str]
        last4: Optional[str]
        reference: Optional[str]
        sender_account_number: Optional[str]
        sender_name: Optional[str]
        sender_sort_code: Optional[str]

    class PaperCheck(StripeObject):
        available_at: Optional[str]
        invoices: Optional[str]

    class SepaCreditTransfer(StripeObject):
        reference: Optional[str]
        sender_iban: Optional[str]
        sender_name: Optional[str]

    ach_credit_transfer: Optional[AchCreditTransfer]
    amount: int
    chf_credit_transfer: Optional[ChfCreditTransfer]
    created: int
    currency: str
    gbp_credit_transfer: Optional[GbpCreditTransfer]
    id: str
    livemode: bool
    object: Literal["source_transaction"]
    paper_check: Optional[PaperCheck]
    sepa_credit_transfer: Optional[SepaCreditTransfer]
    source: str
    status: str
    type: Literal[
        "ach_credit_transfer",
        "ach_debit",
        "alipay",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ]

    _inner_class_types = {
        "ach_credit_transfer": AchCreditTransfer,
        "chf_credit_transfer": ChfCreditTransfer,
        "gbp_credit_transfer": GbpCreditTransfer,
        "paper_check": PaperCheck,
        "sepa_credit_transfer": SepaCreditTransfer,
    }
