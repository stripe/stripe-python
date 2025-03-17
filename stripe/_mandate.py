# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._expandable_field import ExpandableField
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_method import PaymentMethod


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

        class AmazonPay(StripeObject):
            pass

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
            revocation_reason: Optional[
                Literal[
                    "account_closed",
                    "bank_account_restricted",
                    "bank_ownership_changed",
                    "could_not_process",
                    "debit_not_authorized",
                ]
            ]
            """
            When the mandate is revoked on the Bacs network this field displays the reason for the revocation.
            """
            url: str
            """
            The URL that will contain the mandate that the customer has signed.
            """

        class Card(StripeObject):
            pass

        class Cashapp(StripeObject):
            pass

        class KakaoPay(StripeObject):
            pass

        class KrCard(StripeObject):
            pass

        class Link(StripeObject):
            pass

        class NaverPay(StripeObject):
            pass

        class Paypal(StripeObject):
            billing_agreement_id: Optional[str]
            """
            The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
            """
            fingerprint: Optional[str]
            """
            Uniquely identifies this particular PayPal account. You can use this attribute to check whether two PayPal accounts are the same.
            """
            payer_id: Optional[str]
            """
            PayPal account PayerID. This identifier uniquely identifies the PayPal customer.
            """
            verified_email: Optional[str]
            """
            Owner's verified email. Values are verified or provided by PayPal directly
            (if supported) at the time of authorization or settlement. They cannot be set or mutated.
            """

        class Payto(StripeObject):
            amount: Optional[int]
            """
            Amount that will be collected. It is required when `amount_type` is `fixed`.
            """
            amount_type: Literal["fixed", "maximum"]
            """
            The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively.
            """
            end_date: Optional[str]
            """
            Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.
            """
            payment_schedule: Literal[
                "adhoc",
                "annual",
                "daily",
                "fortnightly",
                "monthly",
                "quarterly",
                "semi_annual",
                "weekly",
            ]
            """
            The periodicity at which payments will be collected.
            """
            payments_per_period: Optional[int]
            """
            The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.
            """
            purpose: Optional[
                Literal[
                    "dependant_support",
                    "government",
                    "loan",
                    "mortgage",
                    "other",
                    "pension",
                    "personal",
                    "retail",
                    "salary",
                    "tax",
                    "utility",
                ]
            ]
            """
            The purpose for which payments are made. Defaults to retail.
            """
            start_date: Optional[str]
            """
            Date, in YYYY-MM-DD format, from which payments will be collected. Defaults to confirmation time.
            """

        class RevolutPay(StripeObject):
            pass

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
            collection_method: Optional[Literal["paper"]]
            """
            Mandate collection method
            """

        acss_debit: Optional[AcssDebit]
        amazon_pay: Optional[AmazonPay]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        card: Optional[Card]
        cashapp: Optional[Cashapp]
        kakao_pay: Optional[KakaoPay]
        kr_card: Optional[KrCard]
        link: Optional[Link]
        naver_pay: Optional[NaverPay]
        paypal: Optional[Paypal]
        payto: Optional[Payto]
        revolut_pay: Optional[RevolutPay]
        sepa_debit: Optional[SepaDebit]
        type: str
        """
        This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that's specific to that payment method.
        """
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "amazon_pay": AmazonPay,
            "au_becs_debit": AuBecsDebit,
            "bacs_debit": BacsDebit,
            "card": Card,
            "cashapp": Cashapp,
            "kakao_pay": KakaoPay,
            "kr_card": KrCard,
            "link": Link,
            "naver_pay": NaverPay,
            "paypal": Paypal,
            "payto": Payto,
            "revolut_pay": RevolutPay,
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

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
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

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Mandate.RetrieveParams"]
    ) -> "Mandate":
        """
        Retrieves a Mandate object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "customer_acceptance": CustomerAcceptance,
        "multi_use": MultiUse,
        "payment_method_details": PaymentMethodDetails,
        "single_use": SingleUse,
    }
