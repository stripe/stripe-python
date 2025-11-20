# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class Cadence(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.cadence"]] = "v2.billing.cadence"

    class BillingCycle(StripeObject):
        class Day(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Month(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_month: int
            """
            The day to anchor the billing on for a type="month" billing cycle from 1-31.
            If this number is greater than the number of days in the month being billed,
            this will anchor to the last day of the month.
            """
            month_of_year: Optional[int]
            """
            The month to anchor the billing on for a type="month" billing cycle from
            1-12. Occurrences are calculated from the month anchor.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Week(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_week: int
            """
            The day of the week to bill the type=week billing cycle on.
            Numbered from 1-7 for Monday to Sunday respectively, based on the ISO-8601 week day numbering.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Year(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_month: int
            """
            The day to anchor the billing on for a type="month" billing cycle from 1-31.
            If this number is greater than the number of days in the month being billed,
            this will anchor to the last day of the month.
            """
            month_of_year: int
            """
            The month to bill on from 1-12. If not provided, this will default to the month the cadence was created.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        day: Optional[Day]
        """
        Specific configuration for determining billing dates when type=day.
        """
        interval_count: int
        """
        The number of intervals (specified in the interval attribute) between cadence billings. For example, type=month and interval_count=3 bills every 3 months.
        """
        month: Optional[Month]
        """
        Specific configuration for determining billing dates when type=month.
        """
        type: Literal["day", "month", "week", "year"]
        """
        The frequency at which a cadence bills.
        """
        week: Optional[Week]
        """
        Specific configuration for determining billing dates when type=week.
        """
        year: Optional[Year]
        """
        Specific configuration for determining billing dates when type=year.
        """
        _inner_class_types = {
            "day": Day,
            "month": Month,
            "week": Week,
            "year": Year,
        }

    class InvoiceDiscountRule(StripeObject):
        class PercentOff(StripeObject):
            class MaximumApplications(StripeObject):
                type: Literal["indefinite"]
                """
                Max applications type of this discount, ex: indefinite.
                """

            maximum_applications: MaximumApplications
            """
            The maximum applications configuration for this discount.
            """
            percent_off: str
            """
            Percent that will be taken off of the amount. For example, percent_off of 50.0 will make $100 amount $50 instead.
            """
            _inner_class_types = {"maximum_applications": MaximumApplications}

        id: str
        """
        Unique identifier for the object.
        """
        percent_off: Optional[PercentOff]
        """
        Details if the discount is a percentage off.
        """
        type: Literal["percent_off"]
        """
        The type of the discount.
        """
        _inner_class_types = {"percent_off": PercentOff}

    class Payer(StripeObject):
        billing_profile: str
        """
        The ID of the Billing Profile object which determines how a bill will be paid.
        """
        customer: Optional[str]
        """
        The ID of the Customer object.
        """
        type: Literal["customer"]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class Settings(StripeObject):
        class Bill(StripeObject):
            id: str
            """
            The ID of the referenced settings object.
            """
            version: Optional[str]
            """
            Returns the Settings Version when the cadence is pinned to a specific version.
            """

        class Collection(StripeObject):
            id: str
            """
            The ID of the referenced settings object.
            """
            version: Optional[str]
            """
            Returns the Settings Version when the cadence is pinned to a specific version.
            """

        bill: Optional[Bill]
        """
        Settings that configure bills generation, which includes calculating totals, tax, and presenting invoices.
        """
        collection: Optional[Collection]
        """
        Settings that configure and manage the behavior of collecting payments.
        """
        _inner_class_types = {"bill": Bill, "collection": Collection}

    class SettingsData(StripeObject):
        class Bill(StripeObject):
            class Calculation(StripeObject):
                class Tax(StripeObject):
                    type: Literal["automatic", "manual"]
                    """
                    Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
                    """

                tax: Optional[Tax]
                """
                Settings for calculating tax.
                """
                _inner_class_types = {"tax": Tax}

            class Invoice(StripeObject):
                class TimeUntilDue(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    The interval unit for the time until due.
                    """
                    interval_count: int
                    """
                    The number of interval units. For example, if interval=day and interval_count=30,
                    the invoice will be due in 30 days.
                    """

                time_until_due: Optional[TimeUntilDue]
                """
                The amount of time until the invoice will be overdue for payment.
                """
                _inner_class_types = {"time_until_due": TimeUntilDue}

            calculation: Calculation
            """
            Settings related to calculating a bill.
            """
            invoice: Invoice
            """
            Settings related to invoice behavior.
            """
            invoice_rendering_template: Optional[str]
            """
            The ID of the invoice rendering template to be used when generating invoices.
            """
            _inner_class_types = {
                "calculation": Calculation,
                "invoice": Invoice,
            }

        class Collection(StripeObject):
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
                        transaction_type: Optional[
                            Literal["business", "personal"]
                        ]
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
                    preferred_language: Optional[
                        Literal["de", "en", "fr", "nl"]
                    ]
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
                            country: Literal[
                                "BE", "DE", "ES", "FR", "IE", "NL"
                            ]
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
                        _inner_class_types = {
                            "eu_bank_transfer": EuBankTransfer,
                        }

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
                            account_subcategories: List[
                                Literal["checking", "savings"]
                            ]
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
                        "financial_connections": FinancialConnections,
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

            collection_method: Literal["automatic", "send_invoice"]
            """
            Either automatic, or send_invoice. When charging automatically, Stripe will attempt to pay this
            bill at the end of the period using the payment method attached to the payer profile. When sending an invoice,
            Stripe will email your payer profile an invoice with payment instructions.
            Defaults to automatic.
            """
            email_delivery: EmailDelivery
            """
            Email delivery settings.
            """
            payment_method_configuration: str
            """
            The ID of the PaymentMethodConfiguration object, which controls which payment methods are displayed to your customers.
            """
            payment_method_options: PaymentMethodOptions
            """
            Payment Method specific configuration stored on the object.
            """
            _inner_class_types = {
                "email_delivery": EmailDelivery,
                "payment_method_options": PaymentMethodOptions,
            }

        bill: Bill
        """
        Expanded bill settings data with actual configuration values.
        """
        collection: Collection
        """
        Expanded collection settings data with actual configuration values.
        """
        _inner_class_types = {"bill": Bill, "collection": Collection}

    billing_cycle: BillingCycle
    """
    The billing cycle is the object that defines future billing cycle dates.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_discount_rules: Optional[List[InvoiceDiscountRule]]
    """
    The discount rules applied to all invoices for the cadence.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    A lookup key used to retrieve cadences dynamically from a static string. Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_billing_date: Optional[str]
    """
    The date that the billing cadence will next bill. Null if the cadence is not active.
    """
    object: Literal["v2.billing.cadence"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payer: Payer
    """
    The payer determines the entity financially responsible for the bill.
    """
    settings: Optional[Settings]
    """
    The settings associated with the cadence.
    """
    settings_data: Optional[SettingsData]
    """
    Settings data that contains expanded billing settings configuration with actual values.
    """
    status: Literal["active", "canceled"]
    """
    The current status of the cadence.
    """
    test_clock: Optional[str]
    """
    The ID of the Test Clock.
    """
    _inner_class_types = {
        "billing_cycle": BillingCycle,
        "invoice_discount_rules": InvoiceDiscountRule,
        "payer": Payer,
        "settings": Settings,
        "settings_data": SettingsData,
    }
