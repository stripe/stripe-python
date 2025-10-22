# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Dict, List, Optional
from typing_extensions import Literal, NotRequired, TypedDict


class AccountUpdateParams(TypedDict):
    configuration: NotRequired["AccountUpdateParamsConfiguration"]
    """
    An Account Configuration which allows the Account to take on a key persona across Stripe products.
    """
    contact_email: NotRequired[str]
    """
    The default contact email address for the Account. Required when configuring the account as a merchant or recipient.
    """
    dashboard: NotRequired[Literal["express", "full", "none"]]
    """
    A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.
    """
    defaults: NotRequired["AccountUpdateParamsDefaults"]
    """
    Default values to be used on Account Configurations.
    """
    display_name: NotRequired[str]
    """
    A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
    """
    identity: NotRequired["AccountUpdateParamsIdentity"]
    """
    Information about the company, individual, and business represented by the Account.
    """
    include: NotRequired[
        List[
            Literal[
                "configuration.card_creator",
                "configuration.customer",
                "configuration.merchant",
                "configuration.recipient",
                "configuration.storer",
                "defaults",
                "identity",
                "requirements",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """


class AccountUpdateParamsConfiguration(TypedDict):
    card_creator: NotRequired["AccountUpdateParamsConfigurationCardCreator"]
    """
    The CardCreator Configuration allows the Account to create and issue cards to users.
    """
    customer: NotRequired["AccountUpdateParamsConfigurationCustomer"]
    """
    The Customer Configuration allows the Account to be charged.
    """
    merchant: NotRequired["AccountUpdateParamsConfigurationMerchant"]
    """
    The Merchant configuration allows the Account to act as a connected account and collect payments facilitated by a Connect platform. You can add this configuration to your connected accounts only if you've completed onboarding as a Connect platform.
    """
    recipient: NotRequired["AccountUpdateParamsConfigurationRecipient"]
    """
    The Recipient Configuration allows the Account to receive funds.
    """
    storer: NotRequired["AccountUpdateParamsConfigurationStorer"]
    """
    The Storer Configuration allows the Account to store and move funds using stored-value FinancialAccounts.
    """


class AccountUpdateParamsConfigurationCardCreator(TypedDict):
    applied: NotRequired[bool]
    """
    Represents the state of the configuration, and can be updated to deactivate or re-apply a configuration.
    """
    capabilities: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilities"
    ]
    """
    Capabilities to request on the CardCreator Configuration.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilities(TypedDict):
    commercial: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercial"
    ]
    """
    Can create cards for commercial issuing use cases.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercial(
    TypedDict,
):
    celtic: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCeltic"
    ]
    """
    Can create commercial issuing cards with Celtic as BIN sponsor.
    """
    cross_river_bank: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBank"
    ]
    """
    Can create commercial issuing cards with Cross River Bank as BIN sponsor.
    """
    stripe: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripe"
    ]
    """
    Can create commercial issuing cards with Stripe as BIN sponsor.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCeltic(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCelticChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Celtic as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCelticSpendCard"
    ]
    """
    Can create commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCelticChargeCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCelticSpendCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBank(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankSpendCard"
    ]
    """
    Can create commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankChargeCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankSpendCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripe(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripeChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Stripe as BIN sponsor.
    """
    prepaid_card: NotRequired[
        "AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripePrepaidCard"
    ]
    """
    Can create commercial issuing prepaid cards with Stripe as BIN sponsor.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripeChargeCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCardCreatorCapabilitiesCommercialStripePrepaidCard(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCustomer(TypedDict):
    applied: NotRequired[bool]
    """
    Represents the state of the configuration, and can be updated to deactivate or re-apply a configuration.
    """
    automatic_indirect_tax: NotRequired[
        "AccountUpdateParamsConfigurationCustomerAutomaticIndirectTax"
    ]
    """
    Automatic indirect tax settings to be used when automatic tax calculation is enabled on the customer's invoices, subscriptions, checkout sessions, or payment links. Surfaces if automatic tax calculation is possible given the current customer location information.
    """
    billing: NotRequired["AccountUpdateParamsConfigurationCustomerBilling"]
    """
    Billing settings - default settings used for this customer in Billing flows such as Invoices and Subscriptions.
    """
    capabilities: NotRequired[
        "AccountUpdateParamsConfigurationCustomerCapabilities"
    ]
    """
    Capabilities that have been requested on the Customer Configuration.
    """
    shipping: NotRequired["AccountUpdateParamsConfigurationCustomerShipping"]
    """
    The customer's shipping information. Appears on invoices emailed to this customer.
    """
    test_clock: NotRequired[str]
    """
    ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.
    """


class AccountUpdateParamsConfigurationCustomerAutomaticIndirectTax(TypedDict):
    exempt: NotRequired[Literal["exempt", "none", "reverse"]]
    """
    Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to reverse, invoice and receipt PDFs include the following text: “Reverse charge”.
    """
    ip_address: NotRequired[str]
    """
    A recent IP address of the customer used for tax reporting and tax location inference.
    """
    location_source: NotRequired[
        Literal[
            "identity_address",
            "ip_address",
            "payment_method",
            "shipping_address",
        ]
    ]
    """
    The data source used to identify the customer's tax location - defaults to 'identity_address'. Will only be used for automatic tax calculation on the customer's Invoices and Subscriptions.
    """
    validate_location: NotRequired[Literal["auto", "deferred", "immediately"]]
    """
    A per-request flag that indicates when Stripe should validate the customer tax location - defaults to 'auto'.
    """


class AccountUpdateParamsConfigurationCustomerBilling(TypedDict):
    default_payment_method: NotRequired[str]
    """
    ID of a payment method that's attached to the customer, to be used as the customer's default payment method for invoices and subscriptions.
    """
    invoice: NotRequired[
        "AccountUpdateParamsConfigurationCustomerBillingInvoice"
    ]
    """
    Default settings used on invoices for this customer.
    """


class AccountUpdateParamsConfigurationCustomerBillingInvoice(TypedDict):
    custom_fields: NotRequired[
        List[
            "AccountUpdateParamsConfigurationCustomerBillingInvoiceCustomField"
        ]
    ]
    """
    The list of up to 4 default custom fields to be displayed on invoices for this customer.
    """
    footer: NotRequired[str]
    """
    Default footer to be displayed on invoices for this customer.
    """
    next_sequence: NotRequired[int]
    """
    The sequence to be used on the customer's next invoice. Defaults to 1.
    """
    prefix: NotRequired[str]
    """
    The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
    """
    rendering: NotRequired[
        "AccountUpdateParamsConfigurationCustomerBillingInvoiceRendering"
    ]
    """
    Default options for invoice PDF rendering for this customer.
    """


class AccountUpdateParamsConfigurationCustomerBillingInvoiceCustomField(
    TypedDict,
):
    name: str
    """
    The name of the custom field. This may be up to 40 characters.
    """
    value: str
    """
    The value of the custom field. This may be up to 140 characters. When updating, pass an empty string to remove previously-defined values.
    """


class AccountUpdateParamsConfigurationCustomerBillingInvoiceRendering(
    TypedDict,
):
    amount_tax_display: NotRequired[
        Literal["exclude_tax", "include_inclusive_tax"]
    ]
    """
    How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of exclude_tax or include_inclusive_tax. include_inclusive_tax will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. exclude_tax will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
    """
    template: NotRequired[str]
    """
    ID of the invoice rendering template to use for future invoices.
    """


class AccountUpdateParamsConfigurationCustomerCapabilities(TypedDict):
    automatic_indirect_tax: NotRequired[
        "AccountUpdateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax"
    ]
    """
    Generates requirements for enabling automatic indirect tax calculation on this customer's invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer's invoices or subscriptions. Uses the `location_source` field.
    """


class AccountUpdateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationCustomerShipping(TypedDict):
    address: NotRequired[
        "AccountUpdateParamsConfigurationCustomerShippingAddress"
    ]
    """
    Customer shipping address.
    """
    name: NotRequired[str]
    """
    Customer name.
    """
    phone: NotRequired[str]
    """
    Customer phone (including extension).
    """


class AccountUpdateParamsConfigurationCustomerShippingAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """


class AccountUpdateParamsConfigurationMerchant(TypedDict):
    applied: NotRequired[bool]
    """
    Represents the state of the configuration, and can be updated to deactivate or re-apply a configuration.
    """
    bacs_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantBacsDebitPayments"
    ]
    """
    Settings used for Bacs debit payments.
    """
    branding: NotRequired["AccountUpdateParamsConfigurationMerchantBranding"]
    """
    Settings used to apply the merchant's branding to email receipts, invoices, Checkout, and other products.
    """
    capabilities: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilities"
    ]
    """
    Capabilities to request on the Merchant Configuration.
    """
    card_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCardPayments"
    ]
    """
    Card payments settings.
    """
    mcc: NotRequired[str]
    """
    The merchant category code for the merchant. MCCs are used to classify businesses based on the goods or services they provide.
    """
    statement_descriptor: NotRequired[
        "AccountUpdateParamsConfigurationMerchantStatementDescriptor"
    ]
    """
    Statement descriptor.
    """
    support: NotRequired["AccountUpdateParamsConfigurationMerchantSupport"]
    """
    Publicly available contact information for sending support issues to.
    """


class AccountUpdateParamsConfigurationMerchantBacsDebitPayments(TypedDict):
    display_name: NotRequired[str]
    """
    Display name for Bacs debit payments.
    """


class AccountUpdateParamsConfigurationMerchantBranding(TypedDict):
    icon: NotRequired[str]
    """
    ID of a [file upload](https://docs.stripe.com/api/persons/update#create_file): An icon for the merchant. Must be square and at least 128px x 128px.
    """
    logo: NotRequired[str]
    """
    ID of a [file upload](https://docs.stripe.com/api/persons/update#create_file): A logo for the merchant that will be used in Checkout instead of the icon and without the merchant's name next to it if provided. Must be at least 128px x 128px.
    """
    primary_color: NotRequired[str]
    """
    A CSS hex color value representing the primary branding color for the merchant.
    """
    secondary_color: NotRequired[str]
    """
    A CSS hex color value representing the secondary branding color for the merchant.
    """


class AccountUpdateParamsConfigurationMerchantCapabilities(TypedDict):
    ach_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAchDebitPayments"
    ]
    """
    Allow the merchant to process ACH debit payments.
    """
    acss_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAcssDebitPayments"
    ]
    """
    Allow the merchant to process ACSS debit payments.
    """
    affirm_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAffirmPayments"
    ]
    """
    Allow the merchant to process Affirm payments.
    """
    afterpay_clearpay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments"
    ]
    """
    Allow the merchant to process Afterpay/Clearpay payments.
    """
    alma_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAlmaPayments"
    ]
    """
    Allow the merchant to process Alma payments.
    """
    amazon_pay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAmazonPayPayments"
    ]
    """
    Allow the merchant to process Amazon Pay payments.
    """
    au_becs_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments"
    ]
    """
    Allow the merchant to process Australian BECS Direct Debit payments.
    """
    bacs_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesBacsDebitPayments"
    ]
    """
    Allow the merchant to process BACS Direct Debit payments.
    """
    bancontact_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesBancontactPayments"
    ]
    """
    Allow the merchant to process Bancontact payments.
    """
    blik_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesBlikPayments"
    ]
    """
    Allow the merchant to process BLIK payments.
    """
    boleto_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesBoletoPayments"
    ]
    """
    Allow the merchant to process Boleto payments.
    """
    card_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesCardPayments"
    ]
    """
    Allow the merchant to collect card payments.
    """
    cartes_bancaires_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments"
    ]
    """
    Allow the merchant to process Cartes Bancaires payments.
    """
    cashapp_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesCashappPayments"
    ]
    """
    Allow the merchant to process Cash App payments.
    """
    eps_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesEpsPayments"
    ]
    """
    Allow the merchant to process EPS payments.
    """
    fpx_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesFpxPayments"
    ]
    """
    Allow the merchant to process FPX payments.
    """
    gb_bank_transfer_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments"
    ]
    """
    Allow the merchant to process UK bank transfer payments.
    """
    grabpay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesGrabpayPayments"
    ]
    """
    Allow the merchant to process GrabPay payments.
    """
    ideal_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesIdealPayments"
    ]
    """
    Allow the merchant to process iDEAL payments.
    """
    jcb_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesJcbPayments"
    ]
    """
    Allow the merchant to process JCB card payments.
    """
    jp_bank_transfer_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments"
    ]
    """
    Allow the merchant to process Japanese bank transfer payments.
    """
    kakao_pay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesKakaoPayPayments"
    ]
    """
    Allow the merchant to process Kakao Pay payments.
    """
    klarna_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesKlarnaPayments"
    ]
    """
    Allow the merchant to process Klarna payments.
    """
    konbini_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesKonbiniPayments"
    ]
    """
    Allow the merchant to process Konbini convenience store payments.
    """
    kr_card_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesKrCardPayments"
    ]
    """
    Allow the merchant to process Korean card payments.
    """
    link_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesLinkPayments"
    ]
    """
    Allow the merchant to process Link payments.
    """
    mobilepay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesMobilepayPayments"
    ]
    """
    Allow the merchant to process MobilePay payments.
    """
    multibanco_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesMultibancoPayments"
    ]
    """
    Allow the merchant to process Multibanco payments.
    """
    mx_bank_transfer_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments"
    ]
    """
    Allow the merchant to process Mexican bank transfer payments.
    """
    naver_pay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesNaverPayPayments"
    ]
    """
    Allow the merchant to process Naver Pay payments.
    """
    oxxo_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesOxxoPayments"
    ]
    """
    Allow the merchant to process OXXO payments.
    """
    p24_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesP24Payments"
    ]
    """
    Allow the merchant to process Przelewy24 (P24) payments.
    """
    pay_by_bank_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesPayByBankPayments"
    ]
    """
    Allow the merchant to process Pay by Bank payments.
    """
    payco_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesPaycoPayments"
    ]
    """
    Allow the merchant to process PAYCO payments.
    """
    paynow_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesPaynowPayments"
    ]
    """
    Allow the merchant to process PayNow payments.
    """
    promptpay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesPromptpayPayments"
    ]
    """
    Allow the merchant to process PromptPay payments.
    """
    revolut_pay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesRevolutPayPayments"
    ]
    """
    Allow the merchant to process Revolut Pay payments.
    """
    samsung_pay_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesSamsungPayPayments"
    ]
    """
    Allow the merchant to process Samsung Pay payments.
    """
    sepa_bank_transfer_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments"
    ]
    """
    Allow the merchant to process SEPA bank transfer payments.
    """
    sepa_debit_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesSepaDebitPayments"
    ]
    """
    Allow the merchant to process SEPA Direct Debit payments.
    """
    swish_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesSwishPayments"
    ]
    """
    Allow the merchant to process Swish payments.
    """
    twint_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesTwintPayments"
    ]
    """
    Allow the merchant to process TWINT payments.
    """
    us_bank_transfer_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments"
    ]
    """
    Allow the merchant to process US bank transfer payments.
    """
    zip_payments: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCapabilitiesZipPayments"
    ]
    """
    Allow the merchant to process Zip payments.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAchDebitPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAcssDebitPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAffirmPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAlmaPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAmazonPayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesBacsDebitPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesBancontactPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesBlikPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesBoletoPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesCardPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesCashappPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesEpsPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesFpxPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesGrabpayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesIdealPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesJcbPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesKakaoPayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesKlarnaPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesKonbiniPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesKrCardPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesLinkPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesMobilepayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesMultibancoPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesNaverPayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesOxxoPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesP24Payments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesPayByBankPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesPaycoPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesPaynowPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesPromptpayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesRevolutPayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesSamsungPayPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesSepaDebitPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesSwishPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesTwintPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCapabilitiesZipPayments(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationMerchantCardPayments(TypedDict):
    decline_on: NotRequired[
        "AccountUpdateParamsConfigurationMerchantCardPaymentsDeclineOn"
    ]
    """
    Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
    """


class AccountUpdateParamsConfigurationMerchantCardPaymentsDeclineOn(TypedDict):
    avs_failure: NotRequired[bool]
    """
    Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
    """
    cvc_failure: NotRequired[bool]
    """
    Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
    """


class AccountUpdateParamsConfigurationMerchantStatementDescriptor(TypedDict):
    descriptor: NotRequired[str]
    """
    The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don't set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
    """
    prefix: NotRequired[str]
    """
    Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don't specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
    """


class AccountUpdateParamsConfigurationMerchantSupport(TypedDict):
    address: NotRequired[
        "AccountUpdateParamsConfigurationMerchantSupportAddress"
    ]
    """
    A publicly available mailing address for sending support issues to.
    """
    email: NotRequired[str]
    """
    A publicly available email address for sending support issues to.
    """
    phone: NotRequired[str]
    """
    A publicly available phone number to call with support issues.
    """
    url: NotRequired[str]
    """
    A publicly available website for handling support issues.
    """


class AccountUpdateParamsConfigurationMerchantSupportAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsConfigurationRecipient(TypedDict):
    applied: NotRequired[bool]
    """
    Represents the state of the configuration, and can be updated to deactivate or re-apply a configuration.
    """
    capabilities: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilities"
    ]
    """
    Capabilities to request on the Recipient Configuration.
    """
    default_outbound_destination: NotRequired[str]
    """
    The payout method id to be used as a default outbound destination. This will allow the PayoutMethod to be omitted on OutboundPayments made through API or sending payouts via dashboard. Can also be explicitly set to `null` to clear the existing default outbound destination. For further details about creating an Outbound Destination, see [Collect recipient's payment details](https://docs.corp.stripe.com/global-payouts-private-preview/quickstart?dashboard-or-api=api#collect-bank-account-details).
    """


class AccountUpdateParamsConfigurationRecipientCapabilities(TypedDict):
    bank_accounts: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccounts"
    ]
    """
    Capabilities that enable OutboundPayments to a bank account linked to this Account.
    """
    cards: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesCards"
    ]
    """
    Capability that enable OutboundPayments to a debit card linked to this Account.
    """
    crypto_wallets: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesCryptoWallets"
    ]
    """
    Capabilities that enable OutboundPayments to a crypto wallet linked to this Account.
    """
    stripe_balance: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesStripeBalance"
    ]
    """
    Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccounts(
    TypedDict,
):
    local: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccountsLocal"
    ]
    """
    Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
    """
    wire: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccountsWire"
    ]
    """
    Enables this Account to receive OutboundPayments to linked bank accounts over wire.
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccountsLocal(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesBankAccountsWire(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesCards(TypedDict):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesCryptoWallets(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesStripeBalance(
    TypedDict,
):
    stripe_transfers: NotRequired[
        "AccountUpdateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers"
    ]
    """
    Allows the account to receive /v1/transfers into their Stripe Balance (/v1/balance).
    """


class AccountUpdateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorer(TypedDict):
    applied: NotRequired[bool]
    """
    Represents the state of the configuration, and can be updated to deactivate or re-apply a configuration.
    """
    capabilities: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilities"
    ]
    """
    Capabilities to request on the Storer Configuration.
    """


class AccountUpdateParamsConfigurationStorerCapabilities(TypedDict):
    financial_addresses: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesFinancialAddresses"
    ]
    """
    Can provision a financial address to credit/debit a FinancialAccount.
    """
    holds_currencies: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrencies"
    ]
    """
    Can hold storage-type funds on Stripe.
    """
    inbound_transfers: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesInboundTransfers"
    ]
    """
    Can pull funds from an external source, owned by yourself, to a FinancialAccount.
    """
    outbound_payments: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPayments"
    ]
    """
    Can send funds from a FinancialAccount to a destination owned by someone else.
    """
    outbound_transfers: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfers"
    ]
    """
    Can send funds from a FinancialAccount to a destination owned by yourself.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesFinancialAddresses(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts"
    ]
    """
    Can provision a bank-account-like financial address (VBAN) to credit/debit a FinancialAccount.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrencies(
    TypedDict,
):
    gbp: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp"
    ]
    """
    Can hold storage-type funds on Stripe in GBP.
    """
    usd: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesUsd"
    ]
    """
    Can hold storage-type funds on Stripe in USD.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesUsd(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesInboundTransfers(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts"
    ]
    """
    Can pull funds from an external bank account owned by yourself to a FinancialAccount.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPayments(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts"
    ]
    """
    Can send funds from a FinancialAccount to a bank account owned by someone else.
    """
    cards: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards"
    ]
    """
    Can send funds from a FinancialAccount to a debit card owned by someone else.
    """
    financial_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts"
    ]
    """
    Can send funds from a FinancialAccount to another FinancialAccount owned by someone else.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfers(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts"
    ]
    """
    Can send funds from a FinancialAccount to a bank account owned by yourself.
    """
    financial_accounts: NotRequired[
        "AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts"
    ]
    """
    Can send funds from a FinancialAccount to another FinancialAccount owned by yourself.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts(
    TypedDict,
):
    requested: NotRequired[bool]
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountUpdateParamsDefaults(TypedDict):
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    locales: NotRequired[
        List[
            Literal[
                "ar-SA",
                "bg",
                "bg-BG",
                "cs",
                "cs-CZ",
                "da",
                "da-DK",
                "de",
                "de-DE",
                "el",
                "el-GR",
                "en",
                "en-AU",
                "en-CA",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-NZ",
                "en-SG",
                "en-US",
                "es",
                "es-419",
                "es-ES",
                "et",
                "et-EE",
                "fi",
                "fil",
                "fil-PH",
                "fi-FI",
                "fr",
                "fr-CA",
                "fr-FR",
                "he-IL",
                "hr",
                "hr-HR",
                "hu",
                "hu-HU",
                "id",
                "id-ID",
                "it",
                "it-IT",
                "ja",
                "ja-JP",
                "ko",
                "ko-KR",
                "lt",
                "lt-LT",
                "lv",
                "lv-LV",
                "ms",
                "ms-MY",
                "mt",
                "mt-MT",
                "nb",
                "nb-NO",
                "nl",
                "nl-NL",
                "pl",
                "pl-PL",
                "pt",
                "pt-BR",
                "pt-PT",
                "ro",
                "ro-RO",
                "ru",
                "ru-RU",
                "sk",
                "sk-SK",
                "sl",
                "sl-SI",
                "sv",
                "sv-SE",
                "th",
                "th-TH",
                "tr",
                "tr-TR",
                "vi",
                "vi-VN",
                "zh",
                "zh-Hans",
                "zh-Hant-HK",
                "zh-Hant-TW",
                "zh-HK",
                "zh-TW",
            ]
        ]
    ]
    """
    The Account's preferred locales (languages), ordered by preference.
    """
    profile: NotRequired["AccountUpdateParamsDefaultsProfile"]
    """
    Account profile information.
    """
    responsibilities: NotRequired[
        "AccountUpdateParamsDefaultsResponsibilities"
    ]
    """
    Default responsibilities held by either Stripe or the platform.
    """


class AccountUpdateParamsDefaultsProfile(TypedDict):
    business_url: NotRequired[str]
    """
    The business's publicly-available website.
    """
    doing_business_as: NotRequired[str]
    """
    The name which is used by the business.
    """
    product_description: NotRequired[str]
    """
    Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
    """


class AccountUpdateParamsDefaultsResponsibilities(TypedDict):
    fees_collector: Literal[
        "application", "application_custom", "application_express", "stripe"
    ]
    """
    A value indicating the party responsible for collecting fees from this account.
    """
    losses_collector: Literal["application", "stripe"]
    """
    A value indicating who is responsible for losses when this Account can't pay back negative balances from payments.
    """


class AccountUpdateParamsIdentity(TypedDict):
    attestations: NotRequired["AccountUpdateParamsIdentityAttestations"]
    """
    Attestations from the identity's key people, e.g. owners, executives, directors, representatives.
    """
    business_details: NotRequired["AccountUpdateParamsIdentityBusinessDetails"]
    """
    Information about the company or business.
    """
    country: NotRequired[str]
    """
    The country in which the account holder resides, or in which the business is legally established. This should be an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.
    """
    entity_type: NotRequired[
        Literal["company", "government_entity", "individual", "non_profit"]
    ]
    """
    The entity type.
    """
    individual: NotRequired["AccountUpdateParamsIdentityIndividual"]
    """
    Information about the individual represented by the Account. This property is `null` unless `entity_type` is set to `individual`.
    """


class AccountUpdateParamsIdentityAttestations(TypedDict):
    directorship_declaration: NotRequired[
        "AccountUpdateParamsIdentityAttestationsDirectorshipDeclaration"
    ]
    """
    This hash is used to attest that the directors information provided to Stripe is both current and correct.
    """
    ownership_declaration: NotRequired[
        "AccountUpdateParamsIdentityAttestationsOwnershipDeclaration"
    ]
    """
    This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
    """
    persons_provided: NotRequired[
        "AccountUpdateParamsIdentityAttestationsPersonsProvided"
    ]
    """
    Attestation that all Persons with a specific Relationship value have been provided.
    """
    representative_declaration: NotRequired[
        "AccountUpdateParamsIdentityAttestationsRepresentativeDeclaration"
    ]
    """
    This hash is used to attest that the representative is authorized to act as the representative of their legal entity.
    """
    terms_of_service: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfService"
    ]
    """
    Attestations of accepted terms of service agreements.
    """


class AccountUpdateParamsIdentityAttestationsDirectorshipDeclaration(
    TypedDict
):
    date: NotRequired[str]
    """
    The time marking when the director attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the director attestation was made.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the director attestation was made.
    """


class AccountUpdateParamsIdentityAttestationsOwnershipDeclaration(TypedDict):
    date: NotRequired[str]
    """
    The time marking when the beneficial owner attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the beneficial owner attestation was made.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the beneficial owner attestation was made.
    """


class AccountUpdateParamsIdentityAttestationsPersonsProvided(TypedDict):
    directors: NotRequired[bool]
    """
    Whether the company's directors have been provided. Set this Boolean to true after creating all the company's directors with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    executives: NotRequired[bool]
    """
    Whether the company's executives have been provided. Set this Boolean to true after creating all the company's executives with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    owners: NotRequired[bool]
    """
    Whether the company's owners have been provided. Set this Boolean to true after creating all the company's owners with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    ownership_exemption_reason: NotRequired[
        Literal[
            "qualified_entity_exceeds_ownership_threshold",
            "qualifies_as_financial_institution",
        ]
    ]
    """
    Reason for why the company is exempt from providing ownership information.
    """


class AccountUpdateParamsIdentityAttestationsRepresentativeDeclaration(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time marking when the representative attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the representative attestation was made.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the representative attestation was made.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfService(TypedDict):
    account: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceAccount"
    ]
    """
    Details on the Account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance).
    """
    card_creator: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreator"
    ]
    """
    Details on the Account's acceptance of Issuing-specific terms of service.
    """
    storer: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceStorer"
    ]
    """
    Details on the Account's acceptance of Treasury-specific terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceAccount(TypedDict):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreator(
    TypedDict,
):
    commercial: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercial"
    ]
    """
    Terms of service acceptances to create cards for commercial issuing use cases.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercial(
    TypedDict,
):
    account_holder: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialAccountHolder"
    ]
    """
    Terms of service acceptances for Stripe commercial card issuing.
    """
    celtic: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCeltic"
    ]
    """
    Terms of service acceptances for commercial issuing cards with Celtic as BIN sponsor.
    """
    cross_river_bank: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBank"
    ]
    """
    Terms of service acceptances for commercial issuing cards with Cross River Bank as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialAccountHolder(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCeltic(
    TypedDict,
):
    apple_pay: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticApplePay"
    ]
    """
    Terms of service acceptances for commercial issuing Apple Pay cards with Celtic as BIN sponsor.
    """
    charge_card: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCard"
    ]
    """
    Terms of service acceptances for commercial issuing charge cards with Celtic as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCard"
    ]
    """
    Terms of service acceptances for commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticApplePay(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing charge cards with Celtic as BIN sponsor.
    """
    platform: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing charge cards with Celtic as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardBankTerms(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardPlatform(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """
    platform: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardBankTerms(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardFinancingDisclosures(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardPlatform(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBank(
    TypedDict,
):
    apple_pay: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankApplePay"
    ]
    """
    Terms of service acceptances for commercial issuing Apple Pay cards with Cross River Bank as BIN sponsor.
    """
    charge_card: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCard"
    ]
    """
    Terms of service acceptances for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCard"
    ]
    """
    Terms of service acceptances for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankApplePay(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    platform: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardBankTerms(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardFinancingDisclosures(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardPlatform(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardBankTerms(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardFinancingDisclosures(
    TypedDict,
):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityAttestationsTermsOfServiceStorer(TypedDict):
    date: NotRequired[str]
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: NotRequired[str]
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountUpdateParamsIdentityBusinessDetails(TypedDict):
    address: NotRequired["AccountUpdateParamsIdentityBusinessDetailsAddress"]
    """
    The business registration address of the business entity.
    """
    annual_revenue: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsAnnualRevenue"
    ]
    """
    The business gross annual revenue for its preceding fiscal year.
    """
    documents: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocuments"
    ]
    """
    A document verifying the business.
    """
    estimated_worker_count: NotRequired[int]
    """
    An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
    """
    id_numbers: NotRequired[
        List["AccountUpdateParamsIdentityBusinessDetailsIdNumber"]
    ]
    """
    The ID numbers of a business entity.
    """
    monthly_estimated_revenue: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue"
    ]
    """
    An estimate of the monthly revenue of the business.
    """
    phone: NotRequired[str]
    """
    The phone number of the Business Entity.
    """
    registered_name: NotRequired[str]
    """
    The business legal name.
    """
    script_addresses: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptAddresses"
    ]
    """
    The business registration address of the business entity in non latin script.
    """
    script_names: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptNames"
    ]
    """
    The business legal name in non latin script.
    """
    structure: NotRequired[
        Literal[
            "cooperative",
            "free_zone_establishment",
            "free_zone_llc",
            "governmental_unit",
            "government_instrumentality",
            "incorporated_association",
            "incorporated_non_profit",
            "incorporated_partnership",
            "limited_liability_partnership",
            "llc",
            "multi_member_llc",
            "private_company",
            "private_corporation",
            "private_partnership",
            "public_company",
            "public_corporation",
            "public_listed_corporation",
            "public_partnership",
            "registered_charity",
            "single_member_llc",
            "sole_establishment",
            "sole_proprietorship",
            "tax_exempt_government_instrumentality",
            "trust",
            "unincorporated_association",
            "unincorporated_non_profit",
            "unincorporated_partnership",
        ]
    ]
    """
    The category identifying the legal structure of the business.
    """


class AccountUpdateParamsIdentityBusinessDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityBusinessDetailsAnnualRevenue(TypedDict):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """
    fiscal_year_end: NotRequired[str]
    """
    The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocuments(TypedDict):
    bank_account_ownership_verification: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification"
    ]
    """
    One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
    """
    company_license: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyLicense"
    ]
    """
    One or more documents that demonstrate proof of a company's license to operate.
    """
    company_memorandum_of_association: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation"
    ]
    """
    One or more documents showing the company's Memorandum of Association.
    """
    company_ministerial_decree: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree"
    ]
    """
    Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
    """
    company_registration_verification: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
    """
    company_tax_id_verification: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's tax ID.
    """
    primary_verification: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerification"
    ]
    """
    A document verifying the business.
    """
    proof_of_address: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfAddress"
    ]
    """
    One or more documents that demonstrate proof of address.
    """
    proof_of_registration: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfRegistration"
    ]
    """
    One or more documents showing the company's proof of registration with the national business registry.
    """
    proof_of_ultimate_beneficial_ownership: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership"
    ]
    """
    One or more documents that demonstrate proof of ultimate beneficial ownership.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyLicense(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountUpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfAddress(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfRegistration(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityBusinessDetailsIdNumber(TypedDict):
    registrar: NotRequired[str]
    """
    The registrar of the ID number (Only valid for DE ID number types).
    """
    type: Literal[
        "ae_crn",
        "ae_vat",
        "ao_nif",
        "at_fn",
        "au_abn",
        "au_acn",
        "au_in",
        "az_tin",
        "bd_etin",
        "be_cbe",
        "bg_uic",
        "br_cnpj",
        "ca_cn",
        "ca_crarr",
        "ca_neq",
        "ca_rid",
        "ch_chid",
        "ch_uid",
        "cr_cpj",
        "cr_nite",
        "cy_tic",
        "cz_ico",
        "de_hrn",
        "de_vat",
        "dk_cvr",
        "do_rcn",
        "ee_rk",
        "es_cif",
        "fi_yt",
        "fr_siren",
        "fr_vat",
        "gb_crn",
        "gi_crn",
        "gr_gemi",
        "gt_nit",
        "hk_br",
        "hk_cr",
        "hk_mbs",
        "hu_cjs",
        "ie_crn",
        "it_rea",
        "it_vat",
        "jp_cn",
        "kz_bin",
        "li_uid",
        "lt_ccrn",
        "lu_rcs",
        "lv_urn",
        "mt_crn",
        "mx_rfc",
        "my_brn",
        "my_coid",
        "my_sst",
        "mz_nuit",
        "nl_kvk",
        "no_orgnr",
        "nz_bn",
        "pe_ruc",
        "pk_ntn",
        "pl_regon",
        "pt_vat",
        "ro_cui",
        "sa_crn",
        "sa_tin",
        "se_orgnr",
        "sg_uen",
        "si_msp",
        "sk_ico",
        "th_crn",
        "th_prn",
        "th_tin",
        "us_ein",
    ]
    """
    Open Enum. The ID number type of a business entity.
    """
    value: str
    """
    The value of the ID number.
    """


class AccountUpdateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue(
    TypedDict,
):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptAddresses(TypedDict):
    kana: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptAddressesKana(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptAddressesKanji(
    TypedDict
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptNames(TypedDict):
    kana: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptNamesKana"
    ]
    """
    Kana name.
    """
    kanji: NotRequired[
        "AccountUpdateParamsIdentityBusinessDetailsScriptNamesKanji"
    ]
    """
    Kanji name.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptNamesKana(TypedDict):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountUpdateParamsIdentityBusinessDetailsScriptNamesKanji(TypedDict):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountUpdateParamsIdentityIndividual(TypedDict):
    additional_addresses: NotRequired[
        List["AccountUpdateParamsIdentityIndividualAdditionalAddress"]
    ]
    """
    Additional addresses associated with the individual.
    """
    additional_names: NotRequired[
        List["AccountUpdateParamsIdentityIndividualAdditionalName"]
    ]
    """
    Additional names (e.g. aliases) associated with the individual.
    """
    address: NotRequired["AccountUpdateParamsIdentityIndividualAddress"]
    """
    The individual's residential address.
    """
    date_of_birth: NotRequired[
        "AccountUpdateParamsIdentityIndividualDateOfBirth"
    ]
    """
    The individual's date of birth.
    """
    documents: NotRequired["AccountUpdateParamsIdentityIndividualDocuments"]
    """
    Documents that may be submitted to satisfy various informational requests.
    """
    email: NotRequired[str]
    """
    The individual's email address.
    """
    given_name: NotRequired[str]
    """
    The individual's first name.
    """
    id_numbers: NotRequired[
        List["AccountUpdateParamsIdentityIndividualIdNumber"]
    ]
    """
    The identification numbers (e.g., SSN) associated with the individual.
    """
    legal_gender: NotRequired[Literal["female", "male"]]
    """
    The individual's gender (International regulations require either "male" or "female").
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationalities: NotRequired[List[str]]
    """
    The countries where the individual is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    phone: NotRequired[str]
    """
    The individual's phone number.
    """
    political_exposure: NotRequired[Literal["existing", "none"]]
    """
    The individual's political exposure.
    """
    relationship: NotRequired[
        "AccountUpdateParamsIdentityIndividualRelationship"
    ]
    """
    The relationship that this individual has with the account's identity.
    """
    script_addresses: NotRequired[
        "AccountUpdateParamsIdentityIndividualScriptAddresses"
    ]
    """
    The script addresses (e.g., non-Latin characters) associated with the individual.
    """
    script_names: NotRequired[
        "AccountUpdateParamsIdentityIndividualScriptNames"
    ]
    """
    The individuals primary name in non latin script.
    """
    surname: NotRequired[str]
    """
    The individual's last name.
    """


class AccountUpdateParamsIdentityIndividualAdditionalAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    purpose: Literal["registered"]
    """
    Purpose of additional address.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityIndividualAdditionalName(TypedDict):
    full_name: NotRequired[str]
    """
    The person's full name.
    """
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    purpose: Literal["alias", "maiden"]
    """
    The purpose or type of the additional name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class AccountUpdateParamsIdentityIndividualAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityIndividualDateOfBirth(TypedDict):
    day: int
    """
    The day of the birth.
    """
    month: int
    """
    The month of birth.
    """
    year: int
    """
    The year of birth.
    """


class AccountUpdateParamsIdentityIndividualDocuments(TypedDict):
    company_authorization: NotRequired[
        "AccountUpdateParamsIdentityIndividualDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired[
        "AccountUpdateParamsIdentityIndividualDocumentsPassport"
    ]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    primary_verification: NotRequired[
        "AccountUpdateParamsIdentityIndividualDocumentsPrimaryVerification"
    ]
    """
    An identifying document showing the person's name, either a passport or local ID card.
    """
    secondary_verification: NotRequired[
        "AccountUpdateParamsIdentityIndividualDocumentsSecondaryVerification"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    visa: NotRequired["AccountUpdateParamsIdentityIndividualDocumentsVisa"]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class AccountUpdateParamsIdentityIndividualDocumentsCompanyAuthorization(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityIndividualDocumentsPassport(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityIndividualDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountUpdateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountUpdateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountUpdateParamsIdentityIndividualDocumentsSecondaryVerification(
    TypedDict,
):
    front_back: "AccountUpdateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountUpdateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountUpdateParamsIdentityIndividualDocumentsVisa(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountUpdateParamsIdentityIndividualIdNumber(TypedDict):
    type: Literal[
        "ae_eid",
        "ao_nif",
        "az_tin",
        "bd_brc",
        "bd_etin",
        "bd_nid",
        "br_cpf",
        "cr_cpf",
        "cr_dimex",
        "cr_nite",
        "de_stn",
        "do_rcn",
        "gt_nit",
        "hk_id",
        "kz_iin",
        "mx_rfc",
        "my_nric",
        "mz_nuit",
        "nl_bsn",
        "pe_dni",
        "pk_cnic",
        "pk_snic",
        "sa_tin",
        "sg_fin",
        "sg_nric",
        "th_lc",
        "th_pin",
        "us_itin",
        "us_itin_last_4",
        "us_ssn",
        "us_ssn_last_4",
    ]
    """
    The ID number type of an individual.
    """
    value: str
    """
    The value of the ID number.
    """


class AccountUpdateParamsIdentityIndividualRelationship(TypedDict):
    director: NotRequired[bool]
    """
    Whether the person is a director of the account's identity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
    """
    executive: NotRequired[bool]
    """
    Whether the person has significant responsibility to control, manage, or direct the organization.
    """
    owner: NotRequired[bool]
    """
    Whether the person is an owner of the account's identity.
    """
    percent_ownership: NotRequired[str]
    """
    The percent owned by the person of the account's legal entity.
    """
    title: NotRequired[str]
    """
    The person's title (e.g., CEO, Support Engineer).
    """


class AccountUpdateParamsIdentityIndividualScriptAddresses(TypedDict):
    kana: NotRequired[
        "AccountUpdateParamsIdentityIndividualScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountUpdateParamsIdentityIndividualScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountUpdateParamsIdentityIndividualScriptAddressesKana(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityIndividualScriptAddressesKanji(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountUpdateParamsIdentityIndividualScriptNames(TypedDict):
    kana: NotRequired["AccountUpdateParamsIdentityIndividualScriptNamesKana"]
    """
    Persons name in kana script.
    """
    kanji: NotRequired["AccountUpdateParamsIdentityIndividualScriptNamesKanji"]
    """
    Persons name in kanji script.
    """


class AccountUpdateParamsIdentityIndividualScriptNamesKana(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class AccountUpdateParamsIdentityIndividualScriptNamesKanji(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """
