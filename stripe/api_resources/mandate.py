# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class Mandate(APIResource["Mandate"]):
    """
    A Mandate is a record of the permission that your customer gives you to debit their payment method.
    """

    OBJECT_NAME: ClassVar[Literal["mandate"]] = "mandate"

    class CustomerAcceptance(StripeObject):
        class Offline(StripeObject):
            pass

        class Online(StripeObject):
            ip_address: Optional[str]
            """
            The customer accepts the mandate from this IP address.
            """
            user_agent: Optional[str]
            """
            The customer accepts the mandate using the user agent of the browser.
            """

        accepted_at: Optional[int]
        """
        The time that the customer accepts the mandate.
        """
        offline: Optional[Offline]
        online: Optional[Online]
        type: Literal["offline", "online"]
        """
        The mandate includes the type of customer acceptance information, such as: `online` or `offline`.
        """
        _inner_class_types = {"offline": Offline, "online": Online}

    class MultiUse(StripeObject):
        pass

    class PaymentMethodDetails(StripeObject):
        class AcssDebit(StripeObject):
            default_for: Optional[List[Literal["invoice", "subscription"]]]
            """
            List of Stripe products where this mandate can be selected automatically.
            """
            interval_description: Optional[str]
            """
            Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'.
            """
            payment_schedule: Literal["combined", "interval", "sporadic"]
            """
            Payment schedule for the mandate.
            """
            transaction_type: Literal["business", "personal"]
            """
            Transaction type of the mandate.
            """

        class AuBecsDebit(StripeObject):
            url: str
            """
            The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.
            """

        class BacsDebit(StripeObject):
            network_status: Literal[
                "accepted", "pending", "refused", "revoked"
            ]
            """
            The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`.
            """
            reference: str
            """
            The unique reference identifying the mandate on the Bacs network.
            """
            url: str
            """
            The URL that will contain the mandate that the customer has signed.
            """

        class Card(StripeObject):
            pass

        class Cashapp(StripeObject):
            pass

        class Link(StripeObject):
            pass

        class Paypal(StripeObject):
            billing_agreement_id: Optional[str]
            """
            The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
            """
            payer_id: Optional[str]
            """
            PayPal account PayerID. This identifier uniquely identifies the PayPal customer.
            """

        class SepaDebit(StripeObject):
            reference: str
            """
            The unique reference of the mandate.
            """
            url: str
            """
            The URL of the mandate. This URL generally contains sensitive information about the customer and should be shared with them exclusively.
            """

        class UsBankAccount(StripeObject):
            pass

        acss_debit: Optional[AcssDebit]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        card: Optional[Card]
        cashapp: Optional[Cashapp]
        link: Optional[Link]
        paypal: Optional[Paypal]
        sepa_debit: Optional[SepaDebit]
        type: str
        """
        This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that's specific to that payment method.
        """
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "au_becs_debit": AuBecsDebit,
            "bacs_debit": BacsDebit,
            "card": Card,
            "cashapp": Cashapp,
            "link": Link,
            "paypal": Paypal,
            "sepa_debit": SepaDebit,
            "us_bank_account": UsBankAccount,
        }

    class SingleUse(StripeObject):
        amount: int
        """
        The amount of the payment on a single use mandate.
        """
        currency: str
        """
        The currency of the payment on a single use mandate.
        """

    if TYPE_CHECKING:

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

    customer_acceptance: CustomerAcceptance
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    multi_use: Optional[MultiUse]
    object: Literal["mandate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[str]
    """
    The account (if any) that the mandate is intended for.
    """
    payment_method: ExpandableField["PaymentMethod"]
    """
    ID of the payment method associated with this mandate.
    """
    payment_method_details: PaymentMethodDetails
    single_use: Optional[SingleUse]
    status: Literal["active", "inactive", "pending"]
    """
    The mandate status indicates whether or not you can use it to initiate a payment.
    """
    type: Literal["multi_use", "single_use"]
    """
    The type of the mandate.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Mandate.RetrieveParams"]
    ) -> "Mandate":
        """
        Retrieves a Mandate object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "customer_acceptance": CustomerAcceptance,
        "multi_use": MultiUse,
        "payment_method_details": PaymentMethodDetails,
        "single_use": SingleUse,
    }
