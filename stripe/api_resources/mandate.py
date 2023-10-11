# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class Mandate(APIResource["Mandate"]):
    """
    A Mandate is a record of the permission that your customer gives you to debit their payment method.
    """

    OBJECT_NAME = "mandate"

    class CustomerAcceptance(StripeObject):
        class Offline(StripeObject):
            pass

        class Online(StripeObject):
            ip_address: Optional[str]
            user_agent: Optional[str]

        accepted_at: Optional[int]
        offline: Optional[Offline]
        online: Optional[Online]
        type: Literal["offline", "online"]
        _inner_class_types = {"offline": Offline, "online": Online}

    class MultiUse(StripeObject):
        pass

    class PaymentMethodDetails(StripeObject):
        class AcssDebit(StripeObject):
            default_for: Optional[List[Literal["invoice", "subscription"]]]
            interval_description: Optional[str]
            payment_schedule: Literal["combined", "interval", "sporadic"]
            transaction_type: Literal["business", "personal"]

        class AuBecsDebit(StripeObject):
            url: str

        class BacsDebit(StripeObject):
            network_status: Literal[
                "accepted", "pending", "refused", "revoked"
            ]
            reference: str
            url: str

        class Card(StripeObject):
            pass

        class Cashapp(StripeObject):
            pass

        class Link(StripeObject):
            pass

        class Paypal(StripeObject):
            billing_agreement_id: Optional[str]
            fingerprint: Optional[str]
            payer_id: Optional[str]
            verified_email: Optional[str]

        class SepaDebit(StripeObject):
            reference: str
            url: str

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
        currency: str

    customer_acceptance: CustomerAcceptance
    id: str
    livemode: bool
    multi_use: Optional[MultiUse]
    object: Literal["mandate"]
    on_behalf_of: Optional[str]
    payment_method: ExpandableField["PaymentMethod"]
    payment_method_details: PaymentMethodDetails
    single_use: Optional[SingleUse]
    status: Literal["active", "inactive", "pending"]
    type: Literal["multi_use", "single_use"]

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Mandate":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "customer_acceptance": CustomerAcceptance,
        "multi_use": MultiUse,
        "payment_method_details": PaymentMethodDetails,
        "single_use": SingleUse,
    }
