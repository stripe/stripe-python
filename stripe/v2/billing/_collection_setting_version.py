# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class CollectionSettingVersion(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.collection_setting_version"]] = (
        "v2.billing.collection_setting_version"
    )

    class EmailDelivery(StripeObject):
        class PaymentDue(StripeObject):
            enabled: bool
            """
            If true an email for the invoice would be generated and sent out.
            """
            include_payment_link: bool
            """
            If true the payment link to hosted invoice page would be included in email and PDF of the invoice.
            """

        payment_due: Optional[PaymentDue]
        """
        Controls emails for when the payment is due. For example after the invoice is finalized and transitions to Open state.
        """
        _inner_class_types = {"payment_due": PaymentDue}

    class PaymentMethodOptions(StripeObject):
        class AcssDebit(StripeObject):
            class MandateOptions(StripeObject):
                transaction_type: Optional[Literal["business", "personal"]]
                """
                Transaction type of the mandate.
                """

            mandate_options: Optional[MandateOptions]
            """
            Additional fields for Mandate creation.
            """
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            """
            Verification method.
            """
            _inner_class_types = {"mandate_options": MandateOptions}

        class Bancontact(StripeObject):
            preferred_language: Optional[Literal["de", "en", "fr", "nl"]]
            """
            Preferred language of the Bancontact authorization page that the customer is redirected to.
            """

        class Card(StripeObject):
            class MandateOptions(StripeObject):
                amount: Optional[int]
                """
                Amount to be charged for future payments.
                """
                amount_type: Optional[Literal["fixed", "maximum"]]
                """
                The AmountType for the mandate. One of `fixed` or `maximum`.
                """
                description: Optional[str]
                """
                A description of the mandate that is meant to be displayed to the customer.
                """

            mandate_options: Optional[MandateOptions]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            network: Optional[str]
            """
            Selected network to process the payment on. Depends on the available networks of the card.
            """
            request_three_d_secure: Optional[
                Literal["any", "automatic", "challenge"]
            ]
            """
            An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
            for authentication based on risk level and [other requirements](https://docs.stripe.com/strong-customer-authentication).
            However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
            Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """
            _inner_class_types = {"mandate_options": MandateOptions}

        class CustomerBalance(StripeObject):
            class BankTransfer(StripeObject):
                class EuBankTransfer(StripeObject):
                    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
                    """
                    The desired country code of the bank account information.
                    """

                eu_bank_transfer: Optional[EuBankTransfer]
                """
                Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
                """
                type: Optional[
                    Literal[
                        "eu_bank_transfer",
                        "gb_bank_transfer",
                        "jp_bank_transfer",
                        "mx_bank_transfer",
                        "us_bank_transfer",
                    ]
                ]
                """
                The bank transfer type that can be used for funding.
                """
                _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

            bank_transfer: Optional[BankTransfer]
            """
            Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
            """
            funding_type: Optional[Literal["bank_transfer"]]
            """
            The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
            """
            _inner_class_types = {"bank_transfer": BankTransfer}

        class UsBankAccount(StripeObject):
            class FinancialConnections(StripeObject):
                class Filters(StripeObject):
                    account_subcategories: List[Literal["checking", "savings"]]
                    """
                    The account subcategories to use to filter for selectable accounts.
                    """

                filters: Optional[Filters]
                """
                Provide filters for the linked accounts that the customer can select for the payment method.
                """
                permissions: List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
                """
                The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
                """
                prefetch: List[
                    Literal["balances", "ownership", "transactions"]
                ]
                """
                List of data features that you would like to retrieve upon account creation.
                """
                _inner_class_types = {"filters": Filters}

            financial_connections: FinancialConnections
            """
            Additional fields for Financial Connections Session creation.
            """
            verification_method: Literal[
                "automatic", "instant", "microdeposits"
            ]
            """
            Verification method.
            """
            _inner_class_types = {
                "financial_connections": FinancialConnections
            }

        acss_debit: Optional[AcssDebit]
        """
        This sub-hash contains details about the Canadian pre-authorized debit payment method options.
        """
        bancontact: Optional[Bancontact]
        """
        This sub-hash contains details about the Bancontact payment method.
        """
        card: Optional[Card]
        """
        This sub-hash contains details about the Card payment method options.
        """
        customer_balance: Optional[CustomerBalance]
        """
        This sub-hash contains details about the Bank transfer payment method options.
        """
        konbini: Optional[Dict[str, "Any"]]
        """
        This sub-hash contains details about the Konbini payment method options.
        """
        sepa_debit: Optional[Dict[str, "Any"]]
        """
        This sub-hash contains details about the SEPA Direct Debit payment method options.
        """
        us_bank_account: Optional[UsBankAccount]
        """
        This sub-hash contains details about the ACH direct debit payment method options.
        """
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "bancontact": Bancontact,
            "card": Card,
            "customer_balance": CustomerBalance,
            "us_bank_account": UsBankAccount,
        }

    collection_method: Optional[Literal["automatic", "send_invoice"]]
    """
    Either automatic, or send_invoice. When charging automatically, Stripe will attempt to pay this
    bill at the end of the period using the payment method attached to the payer profile. When sending an invoice,
    Stripe will email your payer profile an invoice with payment instructions.
    Defaults to automatic.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    email_delivery: Optional[EmailDelivery]
    """
    Email delivery settings.
    """
    id: str
    """
    The ID of the CollectionSettingVersion object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.collection_setting_version"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payment_method_configuration: Optional[str]
    """
    The ID of the PaymentMethodConfiguration object, which controls which payment methods are displayed to your customers.
    """
    payment_method_options: Optional[PaymentMethodOptions]
    """
    Payment Method specific configuration stored on the object.
    """
    _inner_class_types = {
        "email_delivery": EmailDelivery,
        "payment_method_options": PaymentMethodOptions,
    }
