# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._charge import Charge
    from stripe._invoice import Invoice
    from stripe._payment_intent import PaymentIntent
    from stripe._payment_record import PaymentRecord


class InvoicePayment(StripeObject):
    """
    Invoice Payments represent payments made against invoices. Invoice Payments can
    be accessed in two ways:
    1. By expanding the `payments` field on the [Invoice](https://stripe.com/docs/api#invoice) resource.
    2. By using the Invoice Payment retrieve and list endpoints.

    Invoice Payments include the mapping between payment objects, such as Payment Intent, and Invoices.
    This resource and its endpoints allows you to easily track if a payment is associated with a specific invoice and
    monitor the allocation details of the payments.
    """

    OBJECT_NAME: ClassVar[Literal["invoice_payment"]] = "invoice_payment"

    class Payment(StripeObject):
        charge: Optional[ExpandableField["Charge"]]
        """
        ID of the successful charge for this payment when `type` is `charge`.Note: charge is only surfaced if the charge object is not associated with a payment intent. If the charge object does have a payment intent, the Invoice Payment surfaces the payment intent instead.
        """
        payment_intent: Optional[ExpandableField["PaymentIntent"]]
        """
        ID of the PaymentIntent associated with this payment when `type` is `payment_intent`. Note: This property is only populated for invoices finalized on or after March 15th, 2019.
        """
        payment_record: Optional[ExpandableField["PaymentRecord"]]
        """
        ID of the PaymentRecord associated with this payment when `type` is `payment_record`.
        """
        type: Literal["charge", "payment_intent"]
        """
        Type of payment object associated with this invoice payment.
        """

    class StatusTransitions(StripeObject):
        canceled_at: Optional[int]
        """
        The time that the payment was canceled.
        """
        paid_at: Optional[int]
        """
        The time that the payment succeeded.
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
    is_default: bool
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
