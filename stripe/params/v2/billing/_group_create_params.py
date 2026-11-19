# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class GroupCreateParams(TypedDict):
    billing_settings: NotRequired["GroupCreateParamsBillingSettings"]
    """
    Billing setting overrides for the group. If omitted, the applicable defaults are used.
    """
    customer: str
    """
    The ID of the Customer object whose invoices are grouped.
    """
    default_payment_method: NotRequired[str]
    """
    The ID of the PaymentMethod object used by default. If unset, the customer's default payment method is used.
    """
    grouping_behavior: NotRequired["GroupCreateParamsGroupingBehavior"]
    """
    The strategy used to group member invoices.
    """
    include: NotRequired[
        List[Union[Literal["billing_settings", "invoice_discount_rules"], str]]
    ]
    """
    Additional fields to include in the response.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to find a particular billing group. Maximum length of 200 characters.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs that you can attach to an object for storing additional structured information.
    """


class GroupCreateParamsBillingSettings(TypedDict):
    collection_method: NotRequired[
        Literal["charge_automatically", "send_invoice"]
    ]
    """
    How Stripe collects payment.
    """
    email_delivery: NotRequired[
        "GroupCreateParamsBillingSettingsEmailDelivery"
    ]
    """
    Email delivery setting.
    """
    invoice_presentation: NotRequired[
        "GroupCreateParamsBillingSettingsInvoicePresentation"
    ]
    """
    Settings for invoice presentation.
    """
    invoice_time_until_due: NotRequired[
        "GroupCreateParamsBillingSettingsInvoiceTimeUntilDue"
    ]
    """
    The amount of time until the invoice is overdue for payment.
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the payment method configuration, which controls which payment methods are displayed to your customers.
    """
    payment_method_options: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptions"
    ]
    """
    Payment Method specific configuration to be stored on the object.
    """
    tax: NotRequired["GroupCreateParamsBillingSettingsTax"]
    """
    Settings for calculating tax.
    """


class GroupCreateParamsBillingSettingsEmailDelivery(TypedDict):
    payment_due: NotRequired[
        "GroupCreateParamsBillingSettingsEmailDeliveryPaymentDue"
    ]
    """
    Controls emails for when the payment is due. Omit to use the applicable default.
    """


class GroupCreateParamsBillingSettingsEmailDeliveryPaymentDue(TypedDict):
    enabled: NotRequired[bool]
    """
    If true an email for the invoice would be generated and sent out.
    """
    include_payment_link: NotRequired[bool]
    """
    If true the payment link to hosted invoice page would be included in email and PDF of the invoice.
    """


class GroupCreateParamsBillingSettingsInvoicePresentation(TypedDict):
    invoice_rendering_template: NotRequired[str]
    """
    The ID of the invoice rendering template to be used when generating invoices. Omit to use the applicable default.
    """


class GroupCreateParamsBillingSettingsInvoiceTimeUntilDue(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit for the time until due.
    """
    interval_count: int
    """
    The number of interval units. For example, if interval=day and interval_count=30, the invoice is due in 30 days.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebit"
    ]
    """
    This sub-hash contains details about the Canadian pre-authorized debit payment method options.
    """
    bancontact: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsBancontact"
    ]
    """
    This sub-hash contains details about the Bancontact payment method.
    """
    card: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains details about the Card payment method options.
    """
    customer_balance: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalance"
    ]
    """
    This sub-hash contains details about the Bank transfer payment method options.
    """
    konbini: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsKonbini"
    ]
    """
    This sub-hash contains details about the Konbini payment method options.
    """
    sepa_debit: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsSepaDebit"
    ]
    """
    This sub-hash contains details about the SEPA Direct Debit payment method options.
    """
    us_bank_account: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccount"
    ]
    """
    This sub-hash contains details about the ACH direct debit payment method options.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebit(TypedDict):
    mandate_options: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation.
    """
    verification_method: NotRequired[
        "Literal['automatic', 'instant', 'microdeposits']|str"
    ]
    """
    Verification method.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    transaction_type: NotRequired["Literal['business', 'personal']|str"]
    """
    Transaction type of the mandate.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsBancontact(
    TypedDict
):
    preferred_language: NotRequired["Literal['de', 'en', 'fr', 'nl']|str"]
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsCard(TypedDict):
    mandate_options: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions"
    ]
    """
    Configuration options for setting up an eMandate for cards issued in India.
    """
    network: NotRequired[str]
    """
    Selected network to process the payment on. Depends on the available networks of the card.
    """
    request_three_d_secure: NotRequired[
        "Literal['any', 'automatic', 'challenge']|str"
    ]
    """
    An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
    for authentication based on risk level and [other requirements](https://docs.stripe.com/strong-customer-authentication).
    However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
    Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount to be charged for future payments.
    """
    amount_type: NotRequired["Literal['fixed', 'maximum']|str"]
    """
    The AmountType for the mandate. One of `fixed` or `maximum`.
    """
    description: NotRequired[str]
    """
    A description of the mandate that is meant to be displayed to the customer.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalance(
    TypedDict,
):
    bank_transfer: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
    ]
    """
    Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
    """
    funding_type: NotRequired["Literal['bank_transfer']|str"]
    """
    The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
    ]
    """
    Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
    """
    type: NotRequired[
        "Literal['eu_bank_transfer', 'gb_bank_transfer', 'jp_bank_transfer', 'mx_bank_transfer', 'us_bank_transfer']|str"
    ]
    """
    The bank transfer type that can be used for funding.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: Union[Literal["BE", "DE", "ES", "FR", "IE", "NL"], str]
    """
    The desired country code of the bank account information.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsKonbini(TypedDict):
    pass


class GroupCreateParamsBillingSettingsPaymentMethodOptionsSepaDebit(TypedDict):
    pass


class GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccount(
    TypedDict,
):
    financial_connections: "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
    """
    Additional fields for Financial Connections Session creation.
    """
    verification_method: Union[
        Literal["automatic", "instant", "microdeposits"], str
    ]
    """
    Verification method.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    permissions: NotRequired[
        List[
            Union[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ],
                str,
            ]
        ]
    ]
    """
    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
    """
    prefetch: NotRequired[
        List[Union[Literal["balances", "ownership", "transactions"], str]]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """


class GroupCreateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[
        List[Union[Literal["checking", "savings"], str]]
    ]
    """
    The account subcategories to use to filter for selectable accounts.
    """


class GroupCreateParamsBillingSettingsTax(TypedDict):
    type: NotRequired["Literal['automatic', 'manual']|str"]
    """
    Determines if tax is calculated automatically based on a product tax code or manually based on rules defined by the business. Omit to use the applicable default.
    """


class GroupCreateParamsGroupingBehavior(TypedDict):
    by_cadence: NotRequired["GroupCreateParamsGroupingBehaviorByCadence"]
    """
    The cadence configuration when type is `by_cadence`.
    """
    type: Union[Literal["by_cadence"], str]
    """
    The grouping strategy.
    """


class GroupCreateParamsGroupingBehaviorByCadence(TypedDict):
    billing_cycle_anchor: NotRequired[str]
    """
    Timestamp that anchors the recurring grouping cadence.
    """
    day: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceDay"]
    """
    Daily cadence details.
    """
    interval_count: NotRequired[int]
    """
    The number of interval units between groups. Defaults to 1.
    """
    month: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceMonth"]
    """
    Monthly cadence details.
    """
    type: Union[Literal["day", "month", "week", "year"], str]
    """
    The interval unit for the cadence.
    """
    week: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceWeek"]
    """
    Weekly cadence details.
    """
    year: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceYear"]
    """
    Yearly cadence details.
    """


class GroupCreateParamsGroupingBehaviorByCadenceDay(TypedDict):
    time: "GroupCreateParamsGroupingBehaviorByCadenceDayTime"
    """
    The time at which the daily grouping interval begins.
    """


class GroupCreateParamsGroupingBehaviorByCadenceDayTime(TypedDict):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class GroupCreateParamsGroupingBehaviorByCadenceMonth(TypedDict):
    day_of_month: int
    """
    The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
    """
    month_of_year: NotRequired[int]
    """
    The month of year, from 1 through 12, from which occurrences are calculated. Defaults to the month when the billing group was created.
    """
    time: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceMonthTime"]
    """
    The time at which the monthly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class GroupCreateParamsGroupingBehaviorByCadenceMonthTime(TypedDict):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class GroupCreateParamsGroupingBehaviorByCadenceWeek(TypedDict):
    day_of_week: int
    """
    The ISO-8601 day of week, from 1 for Monday through 7 for Sunday.
    """
    time: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceWeekTime"]
    """
    The time at which the weekly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class GroupCreateParamsGroupingBehaviorByCadenceWeekTime(TypedDict):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """


class GroupCreateParamsGroupingBehaviorByCadenceYear(TypedDict):
    day_of_month: int
    """
    The day of month, from 1 through 31. For shorter months, the cadence anchors to the month's last day.
    """
    month_of_year: int
    """
    The month of year, from 1 through 12.
    """
    time: NotRequired["GroupCreateParamsGroupingBehaviorByCadenceYearTime"]
    """
    The time at which the yearly grouping interval begins. Defaults to the time the billing group is created, in UTC.
    """


class GroupCreateParamsGroupingBehaviorByCadenceYearTime(TypedDict):
    hour: int
    """
    The hour, from 0 through 23.
    """
    minute: int
    """
    The minute, from 0 through 59.
    """
    second: int
    """
    The second, from 0 through 59.
    """
