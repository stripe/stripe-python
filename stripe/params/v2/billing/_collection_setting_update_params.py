# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Any, Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class CollectionSettingUpdateParams(TypedDict):
    collection_method: NotRequired[Literal["automatic", "send_invoice"]]
    """
    Either automatic, or send_invoice. When charging automatically, Stripe will attempt to pay this
    bill at the end of the period using the payment method attached to the payer profile. When sending an invoice,
    Stripe will email your payer profile an invoice with payment instructions.
    """
    display_name: NotRequired[str]
    """
    An optional customer-facing display name for the CollectionSetting object.
    To remove the display name, set it to an empty string in the request.
    Maximum length of 250 characters.
    """
    email_delivery: NotRequired["CollectionSettingUpdateParamsEmailDelivery"]
    """
    Email delivery settings.
    """
    live_version: NotRequired[str]
    """
    Optionally change the live version of the CollectionSetting. Billing Cadences and other objects that refer to this
    CollectionSetting will use this version when no overrides are set. Providing `live_version = "latest"` will set the
    CollectionSetting's `live_version` to its latest version.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key used to retrieve settings dynamically from a static string.
    This may be up to 200 characters.
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the PaymentMethodConfiguration object, which controls which payment methods are displayed to your customers.
    """
    payment_method_options: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptions"
    ]
    """
    Payment Method specific configuration to be stored on the object.
    """


class CollectionSettingUpdateParamsEmailDelivery(TypedDict):
    payment_due: NotRequired[
        "CollectionSettingUpdateParamsEmailDeliveryPaymentDue"
    ]
    """
    Controls emails for when the payment is due. For example after the invoice is finalized and transitions to Open state.
    """


class CollectionSettingUpdateParamsEmailDeliveryPaymentDue(TypedDict):
    enabled: bool
    """
    If true an email for the invoice would be generated and sent out.
    """
    include_payment_link: bool
    """
    If true the payment link to hosted invoice page would be included in email and PDF of the invoice.
    """


class CollectionSettingUpdateParamsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebit"
    ]
    """
    This sub-hash contains details about the Canadian pre-authorized debit payment method options.
    """
    bancontact: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsBancontact"
    ]
    """
    This sub-hash contains details about the Bancontact payment method.
    """
    card: NotRequired["CollectionSettingUpdateParamsPaymentMethodOptionsCard"]
    """
    This sub-hash contains details about the Card payment method options.
    """
    customer_balance: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalance"
    ]
    """
    This sub-hash contains details about the Bank transfer payment method options.
    """
    konbini: NotRequired[Dict[str, "Any"]]
    """
    This sub-hash contains details about the Konbini payment method options.
    """
    sepa_debit: NotRequired[Dict[str, "Any"]]
    """
    This sub-hash contains details about the SEPA Direct Debit payment method options.
    """
    us_bank_account: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount"
    ]
    """
    This sub-hash contains details about the ACH direct debit payment method options.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebit(TypedDict):
    mandate_options: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation.
    """
    verification_method: NotRequired[
        Literal["automatic", "instant", "microdeposits"]
    ]
    """
    Verification method.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    transaction_type: NotRequired[Literal["business", "personal"]]
    """
    Transaction type of the mandate.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsBancontact(TypedDict):
    preferred_language: NotRequired[Literal["de", "en", "fr", "nl"]]
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsCard(TypedDict):
    mandate_options: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsCardMandateOptions"
    ]
    """
    Configuration options for setting up an eMandate for cards issued in India.
    """
    network: NotRequired[str]
    """
    Selected network to process the payment on. Depends on the available networks of the card.
    """
    request_three_d_secure: NotRequired[
        Literal["any", "automatic", "challenge"]
    ]
    """
    An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
    for authentication based on risk level and [other requirements](https://docs.stripe.com/strong-customer-authentication).
    However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
    Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsCardMandateOptions(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount to be charged for future payments.
    """
    amount_type: NotRequired[Literal["fixed", "maximum"]]
    """
    The AmountType for the mandate. One of `fixed` or `maximum`.
    """
    description: NotRequired[str]
    """
    A description of the mandate that is meant to be displayed to the customer.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalance(
    TypedDict,
):
    bank_transfer: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
    ]
    """
    Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
    """
    funding_type: NotRequired[Literal["bank_transfer"]]
    """
    The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
    ]
    """
    Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
    """
    type: NotRequired[
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


class CollectionSettingUpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
    """
    The desired country code of the bank account information.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccount(
    TypedDict
):
    financial_connections: "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
    """
    Additional fields for Financial Connections Session creation.
    """
    verification_method: Literal["automatic", "instant", "microdeposits"]
    """
    Verification method.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    permissions: NotRequired[
        List[
            Literal["balances", "ownership", "payment_method", "transactions"]
        ]
    ]
    """
    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
    """
    prefetch: NotRequired[
        List[Literal["balances", "ownership", "transactions"]]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """


class CollectionSettingUpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[List[Literal["checking", "savings"]]]
    """
    The account subcategories to use to filter for selectable accounts.
    """
