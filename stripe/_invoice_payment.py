# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._charge import Charge
    from stripe._invoice import Invoice
    from stripe._payment_intent import PaymentIntent


class InvoicePayment(StripeObject):
    """
    The invoice payment object
    """

    OBJECT_NAME: ClassVar[Literal["invoice_payment"]] = "invoice_payment"

    class Payment(StripeObject):
        class OutOfBandPayment(StripeObject):
            amount: int
            """
            Amount paid on this out of band payment, in cents (or local equivalent)
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            money_movement_type: str
            """
            The type of money movement for this out of band payment record.
            """
            paid_at: Optional[int]
            """
            The timestamp when this out of band payment was paid.
            """
            payment_reference: Optional[str]
            """
            The reference for this out of band payment record.
            """

        charge: Optional[ExpandableField["Charge"]]
        """
        ID of the successful charge for this payment when `type` is `charge`.
        """
        out_of_band_payment: Optional[OutOfBandPayment]
        payment_intent: Optional[ExpandableField["PaymentIntent"]]
        """
        ID of the PaymentIntent associated with this payment when `type` is `payment_intent`. Note: This property is only populated for invoices finalized on or after March 15th, 2019.
        """
        type: Literal["charge", "out_of_band_payment", "payment_intent"]
        """
        Type of payment object associated with this invoice payment.
        """
        _inner_class_types = {"out_of_band_payment": OutOfBandPayment}

    class StatusTransitions(StripeObject):
        canceled_at: Optional[int]
        """
        The time that the payment was canceled.
        """
        paid_at: Optional[int]
        """
        The time that the payment succeeded.
        """

    amount_overpaid: Optional[int]
    """
    Excess payment that was received for this invoice and credited to the customer's `invoice_credit_balance`. This field is null until the payment is `paid`. Overpayment can happen when you attach more than one PaymentIntent to the invoice, and each of them succeeds. To avoid overpayment, cancel any PaymentIntents that you do not need before attaching more.
    """
    amount_paid: Optional[int]
    """
    Amount that was actually paid for this invoice, in cents (or local equivalent). This field is null until the payment is `paid`. This amount can be less than the `amount_requested` if the PaymentIntent's `amount_received` is not sufficient to pay all of the invoices that it is attached to.
    """
    amount_requested: int
    """
    Amount intended to be paid toward this invoice, in cents (or local equivalent)
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice: ExpandableField["Invoice"]
    """
    The invoice that was paid.
    """
    is_default: Optional[bool]
    """
    Stripe automatically creates a default InvoicePayment when the invoice is finalized, and keeps it synchronized with the invoice's `amount_remaining`. The PaymentIntent associated with the default payment can't be edited or canceled directly.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["invoice_payment"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment: Payment
    status: str
    """
    The status of the payment, one of `open`, `paid`, or `canceled`.
    """
    status_transitions: StatusTransitions
    _inner_class_types = {
        "payment": Payment,
        "status_transitions": StatusTransitions,
    }
