# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceAttachPaymentParams(RequestOptions):
    amount_requested: NotRequired[int]
    """
    The portion of the `amount` on the PaymentIntent or out of band payment to apply to this invoice. It defaults to the entire amount.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_intent: NotRequired[str]
    """
    The ID of the PaymentIntent to attach to the invoice.
    """
    payment_record: NotRequired[str]
    """
    The ID of the PaymentRecord to attach to the invoice.
    """
    payment_record_data: NotRequired[
        "InvoiceAttachPaymentParamsPaymentRecordData"
    ]
    """
    The PaymentRecord data for attaching an out of band payment to the invoice.
    """


class InvoiceAttachPaymentParamsPaymentRecordData(TypedDict):
    amount: int
    """
    The amount that was paid out of band.
    """
    currency: str
    """
    The currency that was paid out of band.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    money_movement_type: str
    """
    The type of money movement for this out of band payment record.
    """
    paid_at: NotRequired[int]
    """
    The timestamp when this out of band payment was paid.
    """
    payment_reference: NotRequired[str]
    """
    The reference for this out of band payment record.
    """
