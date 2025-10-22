# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountCreateParams(TypedDict):
    configuration: NotRequired["AccountCreateParamsConfiguration"]
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
    defaults: NotRequired["AccountCreateParamsDefaults"]
    """
    Default values to be used on Account Configurations.
    """
    display_name: NotRequired[str]
    """
    A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
    """
    identity: NotRequired["AccountCreateParamsIdentity"]
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
    metadata: NotRequired[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """


class AccountCreateParamsConfiguration(TypedDict):
    card_creator: NotRequired["AccountCreateParamsConfigurationCardCreator"]
    """
    The CardCreator Configuration allows the Account to create and issue cards to users.
    """
    customer: NotRequired["AccountCreateParamsConfigurationCustomer"]
    """
    The Customer Configuration allows the Account to be used in inbound payment flows.
    """
    merchant: NotRequired["AccountCreateParamsConfigurationMerchant"]
    """
    The Merchant configuration allows the Account to act as a connected account and collect payments facilitated by a Connect platform. You can add this configuration to your connected accounts only if you've completed onboarding as a Connect platform.
    """
    recipient: NotRequired["AccountCreateParamsConfigurationRecipient"]
    """
    The Recipient Configuration allows the Account to receive funds.
    """
    storer: NotRequired["AccountCreateParamsConfigurationStorer"]
    """
    The Storer Configuration allows the Account to store and move funds using stored-value FinancialAccounts.
    """


class AccountCreateParamsConfigurationCardCreator(TypedDict):
    capabilities: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilities"
    ]
    """
    Capabilities to request on the CardCreator Configuration.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilities(TypedDict):
    commercial: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercial"
    ]
    """
    Can create cards for commercial issuing use cases.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercial(
    TypedDict,
):
    celtic: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCeltic"
    ]
    """
    Can create commercial issuing cards with Celtic as BIN sponsor.
    """
    cross_river_bank: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBank"
    ]
    """
    Can create commercial issuing cards with Cross River Bank as BIN sponsor.
    """
    stripe: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripe"
    ]
    """
    Can create commercial issuing cards with Stripe as BIN sponsor.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCeltic(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCelticChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Celtic as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCelticSpendCard"
    ]
    """
    Can create commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCelticChargeCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCelticSpendCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBank(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankSpendCard"
    ]
    """
    Can create commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankChargeCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialCrossRiverBankSpendCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripe(
    TypedDict,
):
    charge_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripeChargeCard"
    ]
    """
    Can create commercial issuing charge cards with Stripe as BIN sponsor.
    """
    prepaid_card: NotRequired[
        "AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripePrepaidCard"
    ]
    """
    Can create commercial issuing prepaid cards with Stripe as BIN sponsor.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripeChargeCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCardCreatorCapabilitiesCommercialStripePrepaidCard(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCustomer(TypedDict):
    automatic_indirect_tax: NotRequired[
        "AccountCreateParamsConfigurationCustomerAutomaticIndirectTax"
    ]
    """
    Automatic indirect tax settings to be used when automatic tax calculation is enabled on the customer's invoices, subscriptions, checkout sessions, or payment links. Surfaces if automatic tax calculation is possible given the current customer location information.
    """
    billing: NotRequired["AccountCreateParamsConfigurationCustomerBilling"]
    """
    Billing settings - default settings used for this customer in Billing flows such as Invoices and Subscriptions.
    """
    capabilities: NotRequired[
        "AccountCreateParamsConfigurationCustomerCapabilities"
    ]
    """
    Capabilities that have been requested on the Customer Configuration.
    """
    shipping: NotRequired["AccountCreateParamsConfigurationCustomerShipping"]
    """
    The customer's shipping information. Appears on invoices emailed to this customer.
    """
    test_clock: NotRequired[str]
    """
    ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.
    """


class AccountCreateParamsConfigurationCustomerAutomaticIndirectTax(TypedDict):
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


class AccountCreateParamsConfigurationCustomerBilling(TypedDict):
    invoice: NotRequired[
        "AccountCreateParamsConfigurationCustomerBillingInvoice"
    ]
    """
    Default settings used on invoices for this customer.
    """


class AccountCreateParamsConfigurationCustomerBillingInvoice(TypedDict):
    custom_fields: NotRequired[
        List[
            "AccountCreateParamsConfigurationCustomerBillingInvoiceCustomField"
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
        "AccountCreateParamsConfigurationCustomerBillingInvoiceRendering"
    ]
    """
    Default options for invoice PDF rendering for this customer.
    """


class AccountCreateParamsConfigurationCustomerBillingInvoiceCustomField(
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


class AccountCreateParamsConfigurationCustomerBillingInvoiceRendering(
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


class AccountCreateParamsConfigurationCustomerCapabilities(TypedDict):
    automatic_indirect_tax: NotRequired[
        "AccountCreateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax"
    ]
    """
    Generates requirements for enabling automatic indirect tax calculation on this customer's invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer's invoices or subscriptions. Uses the `location_source` field.
    """


class AccountCreateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationCustomerShipping(TypedDict):
    address: NotRequired[
        "AccountCreateParamsConfigurationCustomerShippingAddress"
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


class AccountCreateParamsConfigurationCustomerShippingAddress(TypedDict):
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


class AccountCreateParamsConfigurationMerchant(TypedDict):
    bacs_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantBacsDebitPayments"
    ]
    """
    Settings used for Bacs debit payments.
    """
    branding: NotRequired["AccountCreateParamsConfigurationMerchantBranding"]
    """
    Settings used to apply the merchant's branding to email receipts, invoices, Checkout, and other products.
    """
    capabilities: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilities"
    ]
    """
    Capabilities to request on the Merchant Configuration.
    """
    card_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCardPayments"
    ]
    """
    Card payments settings.
    """
    mcc: NotRequired[str]
    """
    The merchant category code for the Merchant Configuration. MCCs are used to classify businesses based on the goods or services they provide.
    """
    statement_descriptor: NotRequired[
        "AccountCreateParamsConfigurationMerchantStatementDescriptor"
    ]
    """
    Statement descriptor.
    """
    support: NotRequired["AccountCreateParamsConfigurationMerchantSupport"]
    """
    Publicly available contact information for sending support issues to.
    """


class AccountCreateParamsConfigurationMerchantBacsDebitPayments(TypedDict):
    display_name: NotRequired[str]
    """
    Display name for Bacs debit payments.
    """


class AccountCreateParamsConfigurationMerchantBranding(TypedDict):
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


class AccountCreateParamsConfigurationMerchantCapabilities(TypedDict):
    ach_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAchDebitPayments"
    ]
    """
    Allow the merchant to process ACH debit payments.
    """
    acss_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAcssDebitPayments"
    ]
    """
    Allow the merchant to process ACSS debit payments.
    """
    affirm_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAffirmPayments"
    ]
    """
    Allow the merchant to process Affirm payments.
    """
    afterpay_clearpay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments"
    ]
    """
    Allow the merchant to process Afterpay/Clearpay payments.
    """
    alma_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAlmaPayments"
    ]
    """
    Allow the merchant to process Alma payments.
    """
    amazon_pay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAmazonPayPayments"
    ]
    """
    Allow the merchant to process Amazon Pay payments.
    """
    au_becs_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments"
    ]
    """
    Allow the merchant to process Australian BECS Direct Debit payments.
    """
    bacs_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesBacsDebitPayments"
    ]
    """
    Allow the merchant to process BACS Direct Debit payments.
    """
    bancontact_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesBancontactPayments"
    ]
    """
    Allow the merchant to process Bancontact payments.
    """
    blik_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesBlikPayments"
    ]
    """
    Allow the merchant to process BLIK payments.
    """
    boleto_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesBoletoPayments"
    ]
    """
    Allow the merchant to process Boleto payments.
    """
    card_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesCardPayments"
    ]
    """
    Allow the merchant to collect card payments.
    """
    cartes_bancaires_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments"
    ]
    """
    Allow the merchant to process Cartes Bancaires payments.
    """
    cashapp_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesCashappPayments"
    ]
    """
    Allow the merchant to process Cash App payments.
    """
    eps_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesEpsPayments"
    ]
    """
    Allow the merchant to process EPS payments.
    """
    fpx_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesFpxPayments"
    ]
    """
    Allow the merchant to process FPX payments.
    """
    gb_bank_transfer_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments"
    ]
    """
    Allow the merchant to process UK bank transfer payments.
    """
    grabpay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesGrabpayPayments"
    ]
    """
    Allow the merchant to process GrabPay payments.
    """
    ideal_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesIdealPayments"
    ]
    """
    Allow the merchant to process iDEAL payments.
    """
    jcb_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesJcbPayments"
    ]
    """
    Allow the merchant to process JCB card payments.
    """
    jp_bank_transfer_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments"
    ]
    """
    Allow the merchant to process Japanese bank transfer payments.
    """
    kakao_pay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesKakaoPayPayments"
    ]
    """
    Allow the merchant to process Kakao Pay payments.
    """
    klarna_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesKlarnaPayments"
    ]
    """
    Allow the merchant to process Klarna payments.
    """
    konbini_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesKonbiniPayments"
    ]
    """
    Allow the merchant to process Konbini convenience store payments.
    """
    kr_card_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesKrCardPayments"
    ]
    """
    Allow the merchant to process Korean card payments.
    """
    link_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesLinkPayments"
    ]
    """
    Allow the merchant to process Link payments.
    """
    mobilepay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesMobilepayPayments"
    ]
    """
    Allow the merchant to process MobilePay payments.
    """
    multibanco_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesMultibancoPayments"
    ]
    """
    Allow the merchant to process Multibanco payments.
    """
    mx_bank_transfer_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments"
    ]
    """
    Allow the merchant to process Mexican bank transfer payments.
    """
    naver_pay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesNaverPayPayments"
    ]
    """
    Allow the merchant to process Naver Pay payments.
    """
    oxxo_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesOxxoPayments"
    ]
    """
    Allow the merchant to process OXXO payments.
    """
    p24_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesP24Payments"
    ]
    """
    Allow the merchant to process Przelewy24 (P24) payments.
    """
    pay_by_bank_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesPayByBankPayments"
    ]
    """
    Allow the merchant to process Pay by Bank payments.
    """
    payco_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesPaycoPayments"
    ]
    """
    Allow the merchant to process PAYCO payments.
    """
    paynow_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesPaynowPayments"
    ]
    """
    Allow the merchant to process PayNow payments.
    """
    promptpay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesPromptpayPayments"
    ]
    """
    Allow the merchant to process PromptPay payments.
    """
    revolut_pay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesRevolutPayPayments"
    ]
    """
    Allow the merchant to process Revolut Pay payments.
    """
    samsung_pay_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesSamsungPayPayments"
    ]
    """
    Allow the merchant to process Samsung Pay payments.
    """
    sepa_bank_transfer_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments"
    ]
    """
    Allow the merchant to process SEPA bank transfer payments.
    """
    sepa_debit_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesSepaDebitPayments"
    ]
    """
    Allow the merchant to process SEPA Direct Debit payments.
    """
    swish_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesSwishPayments"
    ]
    """
    Allow the merchant to process Swish payments.
    """
    twint_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesTwintPayments"
    ]
    """
    Allow the merchant to process TWINT payments.
    """
    us_bank_transfer_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments"
    ]
    """
    Allow the merchant to process US bank transfer payments.
    """
    zip_payments: NotRequired[
        "AccountCreateParamsConfigurationMerchantCapabilitiesZipPayments"
    ]
    """
    Allow the merchant to process Zip payments.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAchDebitPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAcssDebitPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAffirmPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAlmaPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAmazonPayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesBacsDebitPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesBancontactPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesBlikPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesBoletoPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesCardPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesCashappPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesEpsPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesFpxPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesGrabpayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesIdealPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesJcbPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesKakaoPayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesKlarnaPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesKonbiniPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesKrCardPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesLinkPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesMobilepayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesMultibancoPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesNaverPayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesOxxoPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesP24Payments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesPayByBankPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesPaycoPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesPaynowPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesPromptpayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesRevolutPayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesSamsungPayPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesSepaDebitPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesSwishPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesTwintPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCapabilitiesZipPayments(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationMerchantCardPayments(TypedDict):
    decline_on: NotRequired[
        "AccountCreateParamsConfigurationMerchantCardPaymentsDeclineOn"
    ]
    """
    Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
    """


class AccountCreateParamsConfigurationMerchantCardPaymentsDeclineOn(TypedDict):
    avs_failure: NotRequired[bool]
    """
    Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
    """
    cvc_failure: NotRequired[bool]
    """
    Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
    """


class AccountCreateParamsConfigurationMerchantStatementDescriptor(TypedDict):
    descriptor: NotRequired[str]
    """
    The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don't set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
    """
    prefix: NotRequired[str]
    """
    Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don't specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
    """


class AccountCreateParamsConfigurationMerchantSupport(TypedDict):
    address: NotRequired[
        "AccountCreateParamsConfigurationMerchantSupportAddress"
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


class AccountCreateParamsConfigurationMerchantSupportAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsConfigurationRecipient(TypedDict):
    capabilities: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilities"
    ]
    """
    Capabilities to be requested on the Recipient Configuration.
    """


class AccountCreateParamsConfigurationRecipientCapabilities(TypedDict):
    bank_accounts: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesBankAccounts"
    ]
    """
    Capabilities that enable OutboundPayments to a bank account linked to this Account.
    """
    cards: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesCards"
    ]
    """
    Capabilities that enable OutboundPayments to a card linked to this Account.
    """
    crypto_wallets: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesCryptoWallets"
    ]
    """
    Capabilities that enable OutboundPayments to a crypto wallet linked to this Account.
    """
    stripe_balance: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesStripeBalance"
    ]
    """
    Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesBankAccounts(
    TypedDict,
):
    local: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesBankAccountsLocal"
    ]
    """
    Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
    """
    wire: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesBankAccountsWire"
    ]
    """
    Enables this Account to receive OutboundPayments to linked bank accounts over wire.
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesBankAccountsLocal(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesBankAccountsWire(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesCards(TypedDict):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesCryptoWallets(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesStripeBalance(
    TypedDict,
):
    stripe_transfers: NotRequired[
        "AccountCreateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers"
    ]
    """
    Allows the account to receive /v1/transfers into their Stripe Balance (/v1/balance).
    """


class AccountCreateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorer(TypedDict):
    capabilities: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilities"
    ]
    """
    Capabilities to request on the Storer Configuration.
    """


class AccountCreateParamsConfigurationStorerCapabilities(TypedDict):
    financial_addresses: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesFinancialAddresses"
    ]
    """
    Can provision a financial address to credit/debit a FinancialAccount.
    """
    holds_currencies: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrencies"
    ]
    """
    Can hold storage-type funds on Stripe.
    """
    inbound_transfers: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesInboundTransfers"
    ]
    """
    Can pull funds from an external source, owned by yourself, to a FinancialAccount.
    """
    outbound_payments: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundPayments"
    ]
    """
    Can send funds from a FinancialAccount to a destination owned by someone else.
    """
    outbound_transfers: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfers"
    ]
    """
    Can send funds from a FinancialAccount to a destination owned by yourself.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesFinancialAddresses(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts"
    ]
    """
    Can provision a bank-account-like financial address (VBAN) to credit/debit a FinancialAccount.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrencies(
    TypedDict,
):
    gbp: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp"
    ]
    """
    Can hold storage-type funds on Stripe in GBP.
    """
    usd: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesUsd"
    ]
    """
    Can hold storage-type funds on Stripe in USD.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesUsd(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesInboundTransfers(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts"
    ]
    """
    Can pull funds from an external bank account owned by yourself to a FinancialAccount.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundPayments(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts"
    ]
    """
    Can send funds from a FinancialAccount to a bank account owned by someone else.
    """
    cards: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards"
    ]
    """
    Can send funds from a FinancialAccount to a debit card owned by someone else.
    """
    financial_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts"
    ]
    """
    Can send funds from a FinancialAccount to another FinancialAccount owned by someone else.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfers(
    TypedDict,
):
    bank_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts"
    ]
    """
    Can send funds from a FinancialAccount to a bank account owned by yourself.
    """
    financial_accounts: NotRequired[
        "AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts"
    ]
    """
    Can send funds from a FinancialAccount to another FinancialAccount owned by yourself.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts(
    TypedDict,
):
    requested: bool
    """
    To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
    """


class AccountCreateParamsDefaults(TypedDict):
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
    profile: NotRequired["AccountCreateParamsDefaultsProfile"]
    """
    Account profile information.
    """
    responsibilities: NotRequired[
        "AccountCreateParamsDefaultsResponsibilities"
    ]
    """
    Default responsibilities held by either Stripe or the platform.
    """


class AccountCreateParamsDefaultsProfile(TypedDict):
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


class AccountCreateParamsDefaultsResponsibilities(TypedDict):
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


class AccountCreateParamsIdentity(TypedDict):
    attestations: NotRequired["AccountCreateParamsIdentityAttestations"]
    """
    Attestations from the identity's key people, e.g. owners, executives, directors, representatives.
    """
    business_details: NotRequired["AccountCreateParamsIdentityBusinessDetails"]
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
    individual: NotRequired["AccountCreateParamsIdentityIndividual"]
    """
    Information about the person represented by the account.
    """


class AccountCreateParamsIdentityAttestations(TypedDict):
    directorship_declaration: NotRequired[
        "AccountCreateParamsIdentityAttestationsDirectorshipDeclaration"
    ]
    """
    This hash is used to attest that the directors information provided to Stripe is both current and correct.
    """
    ownership_declaration: NotRequired[
        "AccountCreateParamsIdentityAttestationsOwnershipDeclaration"
    ]
    """
    This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
    """
    persons_provided: NotRequired[
        "AccountCreateParamsIdentityAttestationsPersonsProvided"
    ]
    """
    Attestation that all Persons with a specific Relationship value have been provided.
    """
    representative_declaration: NotRequired[
        "AccountCreateParamsIdentityAttestationsRepresentativeDeclaration"
    ]
    """
    This hash is used to attest that the representative is authorized to act as the representative of their legal entity.
    """
    terms_of_service: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfService"
    ]
    """
    Attestations of accepted terms of service agreements.
    """


class AccountCreateParamsIdentityAttestationsDirectorshipDeclaration(
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


class AccountCreateParamsIdentityAttestationsOwnershipDeclaration(TypedDict):
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


class AccountCreateParamsIdentityAttestationsPersonsProvided(TypedDict):
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


class AccountCreateParamsIdentityAttestationsRepresentativeDeclaration(
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


class AccountCreateParamsIdentityAttestationsTermsOfService(TypedDict):
    account: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceAccount"
    ]
    """
    Details on the Account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance).
    """
    card_creator: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreator"
    ]
    """
    Details on the Account's acceptance of Issuing-specific terms of service.
    """
    storer: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceStorer"
    ]
    """
    Details on the Account's acceptance of Treasury-specific terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceAccount(TypedDict):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreator(
    TypedDict,
):
    commercial: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercial"
    ]
    """
    Terms of service acceptances to create cards for commercial issuing use cases.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercial(
    TypedDict,
):
    account_holder: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialAccountHolder"
    ]
    """
    Terms of service acceptances for Stripe commercial card issuing.
    """
    celtic: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCeltic"
    ]
    """
    Terms of service acceptances for commercial issuing cards with Celtic as BIN sponsor.
    """
    cross_river_bank: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBank"
    ]
    """
    Terms of service acceptances for commercial issuing cards with Cross River Bank as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialAccountHolder(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCeltic(
    TypedDict,
):
    apple_pay: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticApplePay"
    ]
    """
    Terms of service acceptances for commercial issuing Apple Pay cards with Celtic as BIN sponsor.
    """
    charge_card: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCard"
    ]
    """
    Terms of service acceptances for commercial issuing charge cards with Celtic as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCard"
    ]
    """
    Terms of service acceptances for commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticApplePay(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing charge cards with Celtic as BIN sponsor.
    """
    platform: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing charge cards with Celtic as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardBankTerms(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticChargeCardPlatform(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """
    platform: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing spend cards with Celtic as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardBankTerms(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardFinancingDisclosures(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCelticSpendCardPlatform(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBank(
    TypedDict,
):
    apple_pay: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankApplePay"
    ]
    """
    Terms of service acceptances for commercial issuing Apple Pay cards with Cross River Bank as BIN sponsor.
    """
    charge_card: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCard"
    ]
    """
    Terms of service acceptances for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    spend_card: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCard"
    ]
    """
    Terms of service acceptances for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankApplePay(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """
    platform: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardPlatform"
    ]
    """
    Platform terms of service acceptance for commercial issuing charge cards with Cross River Bank as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardBankTerms(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardFinancingDisclosures(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankChargeCardPlatform(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCard(
    TypedDict,
):
    bank_terms: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardBankTerms"
    ]
    """
    Bank terms of service acceptance for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """
    financing_disclosures: NotRequired[
        "AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardFinancingDisclosures"
    ]
    """
    Financial disclosures terms of service acceptance for commercial issuing spend cards with Cross River Bank as BIN sponsor.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardBankTerms(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceCardCreatorCommercialCrossRiverBankSpendCardFinancingDisclosures(
    TypedDict,
):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityAttestationsTermsOfServiceStorer(TypedDict):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class AccountCreateParamsIdentityBusinessDetails(TypedDict):
    address: NotRequired["AccountCreateParamsIdentityBusinessDetailsAddress"]
    """
    The business registration address of the business entity.
    """
    annual_revenue: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsAnnualRevenue"
    ]
    """
    The business gross annual revenue for its preceding fiscal year.
    """
    documents: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocuments"
    ]
    """
    A document verifying the business.
    """
    estimated_worker_count: NotRequired[int]
    """
    An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
    """
    id_numbers: NotRequired[
        List["AccountCreateParamsIdentityBusinessDetailsIdNumber"]
    ]
    """
    The ID numbers of a business entity.
    """
    monthly_estimated_revenue: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue"
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
        "AccountCreateParamsIdentityBusinessDetailsScriptAddresses"
    ]
    """
    The business registration address of the business entity in non latin script.
    """
    script_names: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsScriptNames"
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


class AccountCreateParamsIdentityBusinessDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityBusinessDetailsAnnualRevenue(TypedDict):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """
    fiscal_year_end: NotRequired[str]
    """
    The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
    """


class AccountCreateParamsIdentityBusinessDetailsDocuments(TypedDict):
    bank_account_ownership_verification: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification"
    ]
    """
    One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
    """
    company_license: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyLicense"
    ]
    """
    One or more documents that demonstrate proof of a company's license to operate.
    """
    company_memorandum_of_association: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation"
    ]
    """
    One or more documents showing the company's Memorandum of Association.
    """
    company_ministerial_decree: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree"
    ]
    """
    Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
    """
    company_registration_verification: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
    """
    company_tax_id_verification: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's tax ID.
    """
    primary_verification: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification"
    ]
    """
    A document verifying the business.
    """
    proof_of_address: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfAddress"
    ]
    """
    One or more documents that demonstrate proof of address.
    """
    proof_of_registration: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration"
    ]
    """
    One or more documents showing the company's proof of registration with the national business registry.
    """
    proof_of_ultimate_beneficial_ownership: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership"
    ]
    """
    One or more documents that demonstrate proof of ultimate beneficial ownership.
    """


class AccountCreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyLicense(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: str
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfAddress(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration(
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


class AccountCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership(
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


class AccountCreateParamsIdentityBusinessDetailsIdNumber(TypedDict):
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


class AccountCreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue(
    TypedDict,
):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """


class AccountCreateParamsIdentityBusinessDetailsScriptAddresses(TypedDict):
    kana: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountCreateParamsIdentityBusinessDetailsScriptAddressesKana(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityBusinessDetailsScriptAddressesKanji(
    TypedDict
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityBusinessDetailsScriptNames(TypedDict):
    kana: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsScriptNamesKana"
    ]
    """
    Kana name.
    """
    kanji: NotRequired[
        "AccountCreateParamsIdentityBusinessDetailsScriptNamesKanji"
    ]
    """
    Kanji name.
    """


class AccountCreateParamsIdentityBusinessDetailsScriptNamesKana(TypedDict):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountCreateParamsIdentityBusinessDetailsScriptNamesKanji(TypedDict):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountCreateParamsIdentityIndividual(TypedDict):
    additional_addresses: NotRequired[
        List["AccountCreateParamsIdentityIndividualAdditionalAddress"]
    ]
    """
    Additional addresses associated with the individual.
    """
    additional_names: NotRequired[
        List["AccountCreateParamsIdentityIndividualAdditionalName"]
    ]
    """
    Additional names (e.g. aliases) associated with the individual.
    """
    address: NotRequired["AccountCreateParamsIdentityIndividualAddress"]
    """
    The individual's residential address.
    """
    date_of_birth: NotRequired[
        "AccountCreateParamsIdentityIndividualDateOfBirth"
    ]
    """
    The individual's date of birth.
    """
    documents: NotRequired["AccountCreateParamsIdentityIndividualDocuments"]
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
        List["AccountCreateParamsIdentityIndividualIdNumber"]
    ]
    """
    The identification numbers (e.g., SSN) associated with the individual.
    """
    legal_gender: NotRequired[Literal["female", "male"]]
    """
    The individual's gender (International regulations require either "male" or "female").
    """
    metadata: NotRequired[Dict[str, str]]
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
        "AccountCreateParamsIdentityIndividualRelationship"
    ]
    """
    The relationship that this individual has with the account's identity.
    """
    script_addresses: NotRequired[
        "AccountCreateParamsIdentityIndividualScriptAddresses"
    ]
    """
    The script addresses (e.g., non-Latin characters) associated with the individual.
    """
    script_names: NotRequired[
        "AccountCreateParamsIdentityIndividualScriptNames"
    ]
    """
    The individuals primary name in non latin script.
    """
    surname: NotRequired[str]
    """
    The individual's last name.
    """


class AccountCreateParamsIdentityIndividualAdditionalAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityIndividualAdditionalName(TypedDict):
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


class AccountCreateParamsIdentityIndividualAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityIndividualDateOfBirth(TypedDict):
    day: int
    """
    The day of birth.
    """
    month: int
    """
    The month of birth.
    """
    year: int
    """
    The year of birth.
    """


class AccountCreateParamsIdentityIndividualDocuments(TypedDict):
    company_authorization: NotRequired[
        "AccountCreateParamsIdentityIndividualDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired[
        "AccountCreateParamsIdentityIndividualDocumentsPassport"
    ]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    primary_verification: NotRequired[
        "AccountCreateParamsIdentityIndividualDocumentsPrimaryVerification"
    ]
    """
    An identifying document showing the person's name, either a passport or local ID card.
    """
    secondary_verification: NotRequired[
        "AccountCreateParamsIdentityIndividualDocumentsSecondaryVerification"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    visa: NotRequired["AccountCreateParamsIdentityIndividualDocumentsVisa"]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class AccountCreateParamsIdentityIndividualDocumentsCompanyAuthorization(
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


class AccountCreateParamsIdentityIndividualDocumentsPassport(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountCreateParamsIdentityIndividualDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountCreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountCreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: str
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountCreateParamsIdentityIndividualDocumentsSecondaryVerification(
    TypedDict,
):
    front_back: "AccountCreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountCreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: str
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountCreateParamsIdentityIndividualDocumentsVisa(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountCreateParamsIdentityIndividualIdNumber(TypedDict):
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


class AccountCreateParamsIdentityIndividualRelationship(TypedDict):
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


class AccountCreateParamsIdentityIndividualScriptAddresses(TypedDict):
    kana: NotRequired[
        "AccountCreateParamsIdentityIndividualScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountCreateParamsIdentityIndividualScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountCreateParamsIdentityIndividualScriptAddressesKana(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityIndividualScriptAddressesKanji(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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


class AccountCreateParamsIdentityIndividualScriptNames(TypedDict):
    kana: NotRequired["AccountCreateParamsIdentityIndividualScriptNamesKana"]
    """
    Persons name in kana script.
    """
    kanji: NotRequired["AccountCreateParamsIdentityIndividualScriptNamesKanji"]
    """
    Persons name in kanji script.
    """


class AccountCreateParamsIdentityIndividualScriptNamesKana(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class AccountCreateParamsIdentityIndividualScriptNamesKanji(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """
