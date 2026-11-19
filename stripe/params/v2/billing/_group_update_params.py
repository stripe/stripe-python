# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class GroupUpdateParams(TypedDict):
    billing_settings: NotRequired["GroupUpdateParamsBillingSettings"]
    """
    Billing setting overrides to update. Set to null to restore all applicable defaults.
    """
    default_payment_method: NotRequired[str]
    """
    The ID of the default PaymentMethod object. Set to null to use the customer's default payment method.
    """
    include: NotRequired[
        List[Union[Literal["billing_settings", "invoice_discount_rules"], str]]
    ]
    """
    Additional fields to include in the response.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to find a particular billing group. Set to null to clear it. Maximum length of 200 characters.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs to add, update, or remove.
    """


class GroupUpdateParamsBillingSettings(TypedDict):
    collection_method: NotRequired[
        Literal["charge_automatically", "send_invoice"]
    ]
    """
    How Stripe collects payment. Set to null to restore the applicable default.
    """
    email_delivery: NotRequired[
        "GroupUpdateParamsBillingSettingsEmailDelivery"
    ]
    """
    Email delivery setting. Set to null to restore the applicable default.
    """
    invoice_presentation: NotRequired[
        "GroupUpdateParamsBillingSettingsInvoicePresentation"
    ]
    """
    Settings for invoice presentation. Set to null to restore the applicable defaults.
    """
    invoice_time_until_due: NotRequired[
        "GroupUpdateParamsBillingSettingsInvoiceTimeUntilDue"
    ]
    """
    The amount of time until the invoice is overdue for payment. Set to null to restore the applicable default.
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the payment method configuration, which controls which payment methods are displayed to your customers. Set to null to restore the applicable default.
    """
    payment_method_options: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptions"
    ]
    """
    Payment Method specific configuration to be stored on the object. Set to null to clear the stored value.
    """
    tax: NotRequired["GroupUpdateParamsBillingSettingsTax"]
    """
    Tax calculation settings. Set to null to restore the applicable default.
    """


class GroupUpdateParamsBillingSettingsEmailDelivery(TypedDict):
    payment_due: NotRequired[
        "GroupUpdateParamsBillingSettingsEmailDeliveryPaymentDue"
    ]
    """
    Controls emails for when the payment is due. Omit to leave unchanged. Set to null to restore the applicable default.
    """


class GroupUpdateParamsBillingSettingsEmailDeliveryPaymentDue(TypedDict):
    enabled: NotRequired[bool]
    """
    If true an email for the invoice would be generated and sent out. Omit to leave unchanged. Set to null to restore the applicable default.
    """
    include_payment_link: NotRequired[bool]
    """
    If true the payment link to hosted invoice page would be included in email and PDF of the invoice. Omit to leave unchanged. Set to null to restore the applicable default.
    """


class GroupUpdateParamsBillingSettingsInvoicePresentation(TypedDict):
    invoice_rendering_template: NotRequired[str]
    """
    The ID of the invoice rendering template to be used when generating invoices. Set to null to use no template.
    """


class GroupUpdateParamsBillingSettingsInvoiceTimeUntilDue(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit for the time until due.
    """
    interval_count: int
    """
    The number of interval units. For example, if interval=day and interval_count=30, the invoice is due in 30 days.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebit"
    ]
    """
    This sub-hash contains details about the Canadian pre-authorized debit payment method options.
    """
    bancontact: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsBancontact"
    ]
    """
    This sub-hash contains details about the Bancontact payment method.
    """
    card: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains details about the Card payment method options.
    """
    customer_balance: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalance"
    ]
    """
    This sub-hash contains details about the Bank transfer payment method options.
    """
    konbini: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsKonbini"
    ]
    """
    This sub-hash contains details about the Konbini payment method options.
    """
    sepa_debit: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsSepaDebit"
    ]
    """
    This sub-hash contains details about the SEPA Direct Debit payment method options.
    """
    us_bank_account: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccount"
    ]
    """
    This sub-hash contains details about the ACH direct debit payment method options.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebit(TypedDict):
    mandate_options: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions"
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


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    transaction_type: NotRequired["Literal['business', 'personal']|str"]
    """
    Transaction type of the mandate.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsBancontact(
    TypedDict
):
    preferred_language: NotRequired["Literal['de', 'en', 'fr', 'nl']|str"]
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsCard(TypedDict):
    mandate_options: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions"
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


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsCardMandateOptions(
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


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalance(
    TypedDict,
):
    bank_transfer: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
    ]
    """
    Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
    """
    funding_type: NotRequired["Literal['bank_transfer']|str"]
    """
    The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: Union[Literal["BE", "DE", "ES", "FR", "IE", "NL"], str]
    """
    The desired country code of the bank account information.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsKonbini(TypedDict):
    pass


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsSepaDebit(TypedDict):
    pass


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccount(
    TypedDict,
):
    financial_connections: "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections"
    """
    Additional fields for Financial Connections Session creation.
    """
    verification_method: Union[
        Literal["automatic", "instant", "microdeposits"], str
    ]
    """
    Verification method.
    """


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
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


class GroupUpdateParamsBillingSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[
        List[Union[Literal["checking", "savings"], str]]
    ]
    """
    The account subcategories to use to filter for selectable accounts.
    """


class GroupUpdateParamsBillingSettingsTax(TypedDict):
    type: Union[Literal["automatic", "manual"], str]
    """
    Determines if tax is calculated automatically based on a product tax code or manually based on rules defined by the business.
    """
