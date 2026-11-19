# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Group(StripeObject):
    """
    A Billing Group combines member invoices into a consolidated invoice according to shared grouping behavior.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.group"]] = "v2.billing.group"

    class BillingSettings(StripeObject):
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

            payment_due: PaymentDue
            """
            Controls emails for when the payment is due.
            """
            _inner_class_types = {"payment_due": PaymentDue}

        class InvoicePresentation(StripeObject):
            invoice_rendering_template: Optional[str]
            """
            The ID of the invoice rendering template to be used when generating invoices.
            """

        class InvoiceTimeUntilDue(StripeObject):
            interval: Literal["day", "month", "week", "year"]
            """
            The interval unit for the time until due.
            """
            interval_count: int
            """
            The number of interval units. For example, if interval=day and interval_count=30, the invoice is due in 30 days.
            """

        class PaymentMethodOptions(StripeObject):
            class AcssDebit(StripeObject):
                class MandateOptions(StripeObject):
                    transaction_type: Optional[
                        Union[Literal["business", "personal"], str]
                    ]
                    """
                    Transaction type of the mandate.
                    """

                mandate_options: Optional[MandateOptions]
                """
                Additional fields for Mandate creation.
                """
                verification_method: Optional[
                    Union[
                        Literal["automatic", "instant", "microdeposits"], str
                    ]
                ]
                """
                Verification method.
                """
                _inner_class_types = {"mandate_options": MandateOptions}

            class Bancontact(StripeObject):
                preferred_language: Optional[
                    Union[Literal["de", "en", "fr", "nl"], str]
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
                    amount_type: Optional[
                        Union[Literal["fixed", "maximum"], str]
                    ]
                    """
                    The AmountType for the mandate. One of `fixed` or `maximum`.
                    """
                    description: Optional[str]
                    """
                    A description of the mandate that is meant to be displayed to the customer.
                    """
                    _field_encodings = {"amount": "int64_string"}

                mandate_options: Optional[MandateOptions]
                """
                Configuration options for setting up an eMandate for cards issued in India.
                """
                network: Optional[str]
                """
                Selected network to process the payment on. Depends on the available networks of the card.
                """
                request_three_d_secure: Optional[
                    Union[Literal["any", "automatic", "challenge"], str]
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
                        country: Union[
                            Literal["BE", "DE", "ES", "FR", "IE", "NL"], str
                        ]
                        """
                        The desired country code of the bank account information.
                        """

                    eu_bank_transfer: Optional[EuBankTransfer]
                    """
                    Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
                    """
                    type: Optional[
                        Union[
                            Literal[
                                "eu_bank_transfer",
                                "gb_bank_transfer",
                                "jp_bank_transfer",
                                "mx_bank_transfer",
                                "us_bank_transfer",
                            ],
                            str,
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
                funding_type: Optional[Union[Literal["bank_transfer"], str]]
                """
                The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
                """
                _inner_class_types = {"bank_transfer": BankTransfer}

            class Konbini(StripeObject):
                pass

            class SepaDebit(StripeObject):
                pass

            class UsBankAccount(StripeObject):
                class FinancialConnections(StripeObject):
                    class Filters(StripeObject):
                        account_subcategories: List[
                            Union[Literal["checking", "savings"], str]
                        ]
                        """
                        The account subcategories to use to filter for selectable accounts.
                        """

                    filters: Optional[Filters]
                    """
                    Provide filters for the linked accounts that the customer can select for the payment method.
                    """
                    permissions: List[
                        Union[
                            Literal[
                                "balances",
                                "ownership",
                                "payment_method",
                                "transactions",
                            ],
                            str,
                        ]
                    ]
                    """
                    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
                    """
                    prefetch: List[
                        Union[
                            Literal["balances", "ownership", "transactions"],
                            str,
                        ]
                    ]
                    """
                    List of data features that you would like to retrieve upon account creation.
                    """
                    _inner_class_types = {"filters": Filters}

                financial_connections: FinancialConnections
                """
                Additional fields for Financial Connections Session creation.
                """
                verification_method: Union[
                    Literal["automatic", "instant", "microdeposits"], str
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
            konbini: Optional[Konbini]
            """
            This sub-hash contains details about the Konbini payment method options.
            """
            sepa_debit: Optional[SepaDebit]
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
                "konbini": Konbini,
                "sepa_debit": SepaDebit,
                "us_bank_account": UsBankAccount,
            }

        class Tax(StripeObject):
            type: Union[Literal["automatic", "manual"], str]
            """
            Determines if tax is calculated automatically based on a product tax code or manually based on rules defined by the business.
            """

        collection_method: Literal["charge_automatically", "send_invoice"]
        """
        How Stripe collects payment.
        """
        email_delivery: EmailDelivery
        """
        Email delivery setting.
        """
        invoice_presentation: Optional[InvoicePresentation]
        """
        Settings for invoice presentation.
        """
        invoice_time_until_due: InvoiceTimeUntilDue
        """
        The amount of time until the invoice is overdue for payment.
        """
        payment_method_configuration: Optional[str]
        """
        The ID of the payment method configuration, which controls which payment methods are displayed to your customers.
        """
        payment_method_options: Optional[PaymentMethodOptions]
        """
        Payment Method specific configuration to be stored on the object.
        """
        tax: Tax
        """
        Settings for calculating tax.
        """
        _inner_class_types = {
            "email_delivery": EmailDelivery,
            "invoice_presentation": InvoicePresentation,
            "invoice_time_until_due": InvoiceTimeUntilDue,
            "payment_method_options": PaymentMethodOptions,
            "tax": Tax,
        }

    class GroupingBehavior(StripeObject):
        class ByCadence(StripeObject):
            class Day(StripeObject):
                class Time(StripeObject):
                    hour: int
                    """
                    The hour, from 0 through 23.
                    """
                    minute: int
                    """
                    The minute, from 0 through 59.
                    """
                    second: Optional[int]
                    """
                    The second, from 0 through 59. Defaults to 0.
                    """

                time: Time
                """
                The time at which the daily grouping interval begins.
                """
                _inner_class_types = {"time": Time}

            class Month(StripeObject):
                class Time(StripeObject):
                    hour: int
                    """
                    The hour, from 0 through 23.
                    """
                    minute: int
                    """
                    The minute, from 0 through 59.
                    """
                    second: Optional[int]
                    """
                    The second, from 0 through 59. Defaults to 0.
                    """

                day_of_month: Optional[int]
                """
                The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
                """
                month_of_year: Optional[int]
                """
                The month of year, from 1 through 12, from which occurrences are calculated.
                """
                time: Time
                """
                The time at which the monthly grouping interval begins. Defaults to the time the billing group was created, in UTC.
                """
                _inner_class_types = {"time": Time}

            class Week(StripeObject):
                class Time(StripeObject):
                    hour: int
                    """
                    The hour, from 0 through 23.
                    """
                    minute: int
                    """
                    The minute, from 0 through 59.
                    """
                    second: Optional[int]
                    """
                    The second, from 0 through 59. Defaults to 0.
                    """

                day_of_week: Optional[int]
                """
                The ISO-8601 day of week, from 1 for Monday through 7 for Sunday.
                """
                time: Time
                """
                The time at which the weekly grouping interval begins.
                """
                _inner_class_types = {"time": Time}

            class Year(StripeObject):
                class Time(StripeObject):
                    hour: int
                    """
                    The hour, from 0 through 23.
                    """
                    minute: int
                    """
                    The minute, from 0 through 59.
                    """
                    second: Optional[int]
                    """
                    The second, from 0 through 59. Defaults to 0.
                    """

                day_of_month: Optional[int]
                """
                The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
                """
                month_of_year: Optional[int]
                """
                The month of year, from 1 through 12.
                """
                time: Time
                """
                The time at which the yearly grouping interval begins. Defaults to the time the billing group was created, in UTC.
                """
                _inner_class_types = {"time": Time}

            billing_cycle_anchor: Optional[str]
            """
            Timestamp that anchors the recurring grouping cadence.
            """
            day: Optional[Day]
            """
            Daily cadence details.
            """
            interval_count: int
            """
            The number of interval units between groups.
            """
            month: Optional[Month]
            """
            Monthly cadence details.
            """
            type: Union[Literal["day", "month", "week", "year"], str]
            """
            The interval unit for the cadence.
            """
            week: Optional[Week]
            """
            Weekly cadence details.
            """
            year: Optional[Year]
            """
            Yearly cadence details.
            """
            _inner_class_types = {
                "day": Day,
                "month": Month,
                "week": Week,
                "year": Year,
            }

        by_cadence: Optional[ByCadence]
        """
        The cadence configuration when type is `by_cadence`.
        """
        type: Union[Literal["by_cadence"], str]
        """
        The grouping strategy.
        """
        _inner_class_types = {"by_cadence": ByCadence}

    class InvoiceDiscountRule(StripeObject):
        class PercentOff(StripeObject):
            class MaximumApplications(StripeObject):
                times: Optional[int]
                """
                The number of times this discount can be applied when the type is `times`.
                """
                type: Union[Literal["indefinite", "times"], str]
                """
                Max applications type of this discount, ex: indefinite.
                """

            maximum_applications: MaximumApplications
            """
            The maximum applications configuration for this discount.
            """
            percent_off: Decimal
            """
            Percent that is taken off the amount. For example, a percent_off of 50.0 reduces a 100 USD amount to 50 USD.
            """
            _inner_class_types = {"maximum_applications": MaximumApplications}
            _field_encodings = {"percent_off": "decimal_string"}

        id: str
        """
        Unique identifier for the object.
        """
        percent_off: Optional[PercentOff]
        """
        Details if the discount is a percentage off.
        """
        type: Union[Literal["percent_off"], str]
        """
        The type of the discount.
        """
        _inner_class_types = {"percent_off": PercentOff}

    class StatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        Timestamp of when the billing group became active.
        """
        canceled_at: Optional[str]
        """
        Timestamp of when the billing group was canceled.
        """

    billing_settings: Optional[BillingSettings]
    """
    The effective billing settings for the group. Returned only when `billing_settings` is included in the request.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    customer: str
    """
    The ID of the Customer object whose invoices are grouped.
    """
    default_payment_method: Optional[str]
    """
    The ID of the PaymentMethod object used by default. If unset, the customer's default payment method is used.
    """
    grouping_behavior: GroupingBehavior
    """
    The strategy used to group member invoices.
    """
    id: str
    """
    The ID of the BillingGroup object.
    """
    invoice_discount_rules: Optional[List[InvoiceDiscountRule]]
    """
    The discount rules applied to all invoices for the group's underlying cadence. Returned only when `invoice_discount_rules` is included in the request.
    """
    livemode: bool
    """
    Whether the billing group exists in live mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to find a particular billing group. Maximum length of 200 characters.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object for storing additional structured information.
    """
    next_billing_date: str
    """
    The date when the billing group will next create a consolidated invoice.
    """
    object: Literal["v2.billing.group"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Union[Literal["active", "canceled"], str]
    """
    The current status of the billing group.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for the billing group's status transitions.
    """
    test_clock: Optional[str]
    """
    The ID of the TestClock object associated with the billing group.
    """
    _inner_class_types = {
        "billing_settings": BillingSettings,
        "grouping_behavior": GroupingBehavior,
        "invoice_discount_rules": InvoiceDiscountRule,
        "status_transitions": StatusTransitions,
    }
