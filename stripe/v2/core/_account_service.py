# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._list_object import ListObject
from stripe.v2.core._account import Account
from stripe.v2.core.accounts._person_service import PersonService
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class AccountService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.persons = PersonService(self._requestor)

    class CloseParams(TypedDict):
        applied_configurations: NotRequired[
            List[Literal["customer", "merchant", "recipient", "storer"]]
        ]
        """
        Configurations on the Account to be closed. All configurations on the Account must be passed in for this request to succeed.
        """

    class CreateParams(TypedDict):
        configuration: NotRequired["AccountService.CreateParamsConfiguration"]
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
        defaults: NotRequired["AccountService.CreateParamsDefaults"]
        """
        Default values to be used on Account Configurations.
        """
        display_name: NotRequired[str]
        """
        A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
        """
        identity: NotRequired["AccountService.CreateParamsIdentity"]
        """
        Information about the company, individual, and business represented by the Account.
        """
        include: NotRequired[
            List[
                Literal[
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

    class CreateParamsConfiguration(TypedDict):
        customer: NotRequired[
            "AccountService.CreateParamsConfigurationCustomer"
        ]
        """
        The Customer Configuration allows the Account to be used in inbound payment flows.
        """
        merchant: NotRequired[
            "AccountService.CreateParamsConfigurationMerchant"
        ]
        """
        The Merchant configuration allows the Account to act as a connected account and collect payments facilitated by a Connect platform. You can add this configuration to your connected accounts only if you've completed onboarding as a Connect platform.
        """
        recipient: NotRequired[
            "AccountService.CreateParamsConfigurationRecipient"
        ]
        """
        The Recipient Configuration allows the Account to receive funds.
        """
        storer: NotRequired["AccountService.CreateParamsConfigurationStorer"]
        """
        The Storer Configuration allows the Account to store and move funds using stored-value FinancialAccounts.
        """

    class CreateParamsConfigurationCustomer(TypedDict):
        automatic_indirect_tax: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerAutomaticIndirectTax"
        ]
        """
        Automatic indirect tax settings to be used when automatic tax calculation is enabled on the customer's invoices, subscriptions, checkout sessions, or payment links. Surfaces if automatic tax calculation is possible given the current customer location information.
        """
        billing: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerBilling"
        ]
        """
        Billing settings - default settings used for this customer in Billing flows such as Invoices and Subscriptions.
        """
        capabilities: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerCapabilities"
        ]
        """
        Capabilities that have been requested on the Customer Configuration.
        """
        shipping: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerShipping"
        ]
        """
        The customer's shipping information. Appears on invoices emailed to this customer.
        """
        test_clock: NotRequired[str]
        """
        ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.
        """

    class CreateParamsConfigurationCustomerAutomaticIndirectTax(TypedDict):
        exempt: NotRequired[Literal["exempt", "none", "reverse"]]
        """
        Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to reverse, invoice and receipt PDFs include the following text: “Reverse charge”.
        """
        ip_address: NotRequired[str]
        """
        A recent IP address of the customer used for tax reporting and tax location inference.
        """
        location_source: NotRequired[
            Literal["identity_address", "ip_address", "shipping_address"]
        ]
        """
        The data source used to identify the customer's tax location - defaults to 'identity_address'. Will only be used for automatic tax calculation on the customer's Invoices and Subscriptions.
        """

    class CreateParamsConfigurationCustomerBilling(TypedDict):
        invoice: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerBillingInvoice"
        ]
        """
        Default settings used on invoices for this customer.
        """

    class CreateParamsConfigurationCustomerBillingInvoice(TypedDict):
        custom_fields: NotRequired[
            List[
                "AccountService.CreateParamsConfigurationCustomerBillingInvoiceCustomField"
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
            "AccountService.CreateParamsConfigurationCustomerBillingInvoiceRendering"
        ]
        """
        Default options for invoice PDF rendering for this customer.
        """

    class CreateParamsConfigurationCustomerBillingInvoiceCustomField(
        TypedDict
    ):
        name: str
        """
        The name of the custom field. This may be up to 40 characters.
        """
        value: str
        """
        The value of the custom field. This may be up to 140 characters. When updating, pass an empty string to remove previously-defined values.
        """

    class CreateParamsConfigurationCustomerBillingInvoiceRendering(TypedDict):
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

    class CreateParamsConfigurationCustomerCapabilities(TypedDict):
        automatic_indirect_tax: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax"
        ]
        """
        Generates requirements for enabling automatic indirect tax calculation on this customer's invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer's invoices or subscriptions. Uses the `location_source` field.
        """

    class CreateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationCustomerShipping(TypedDict):
        address: NotRequired[
            "AccountService.CreateParamsConfigurationCustomerShippingAddress"
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

    class CreateParamsConfigurationCustomerShippingAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Literal[
                "ad",
                "ae",
                "af",
                "ag",
                "ai",
                "al",
                "am",
                "ao",
                "aq",
                "ar",
                "as",
                "at",
                "au",
                "aw",
                "ax",
                "az",
                "ba",
                "bb",
                "bd",
                "be",
                "bf",
                "bg",
                "bh",
                "bi",
                "bj",
                "bl",
                "bm",
                "bn",
                "bo",
                "bq",
                "br",
                "bs",
                "bt",
                "bv",
                "bw",
                "by",
                "bz",
                "ca",
                "cc",
                "cd",
                "cf",
                "cg",
                "ch",
                "ci",
                "ck",
                "cl",
                "cm",
                "cn",
                "co",
                "cr",
                "cu",
                "cv",
                "cw",
                "cx",
                "cy",
                "cz",
                "de",
                "dj",
                "dk",
                "dm",
                "do",
                "dz",
                "ec",
                "ee",
                "eg",
                "eh",
                "er",
                "es",
                "et",
                "fi",
                "fj",
                "fk",
                "fm",
                "fo",
                "fr",
                "ga",
                "gb",
                "gd",
                "ge",
                "gf",
                "gg",
                "gh",
                "gi",
                "gl",
                "gm",
                "gn",
                "gp",
                "gq",
                "gr",
                "gs",
                "gt",
                "gu",
                "gw",
                "gy",
                "hk",
                "hm",
                "hn",
                "hr",
                "ht",
                "hu",
                "id",
                "ie",
                "il",
                "im",
                "in",
                "io",
                "iq",
                "ir",
                "is",
                "it",
                "je",
                "jm",
                "jo",
                "jp",
                "ke",
                "kg",
                "kh",
                "ki",
                "km",
                "kn",
                "kp",
                "kr",
                "kw",
                "ky",
                "kz",
                "la",
                "lb",
                "lc",
                "li",
                "lk",
                "lr",
                "ls",
                "lt",
                "lu",
                "lv",
                "ly",
                "ma",
                "mc",
                "md",
                "me",
                "mf",
                "mg",
                "mh",
                "mk",
                "ml",
                "mm",
                "mn",
                "mo",
                "mp",
                "mq",
                "mr",
                "ms",
                "mt",
                "mu",
                "mv",
                "mw",
                "mx",
                "my",
                "mz",
                "na",
                "nc",
                "ne",
                "nf",
                "ng",
                "ni",
                "nl",
                "no",
                "np",
                "nr",
                "nu",
                "nz",
                "om",
                "pa",
                "pe",
                "pf",
                "pg",
                "ph",
                "pk",
                "pl",
                "pm",
                "pn",
                "pr",
                "ps",
                "pt",
                "pw",
                "py",
                "qa",
                "qz",
                "re",
                "ro",
                "rs",
                "ru",
                "rw",
                "sa",
                "sb",
                "sc",
                "sd",
                "se",
                "sg",
                "sh",
                "si",
                "sj",
                "sk",
                "sl",
                "sm",
                "sn",
                "so",
                "sr",
                "ss",
                "st",
                "sv",
                "sx",
                "sy",
                "sz",
                "tc",
                "td",
                "tf",
                "tg",
                "th",
                "tj",
                "tk",
                "tl",
                "tm",
                "tn",
                "to",
                "tr",
                "tt",
                "tv",
                "tw",
                "tz",
                "ua",
                "ug",
                "um",
                "us",
                "uy",
                "uz",
                "va",
                "vc",
                "ve",
                "vg",
                "vi",
                "vn",
                "vu",
                "wf",
                "ws",
                "xx",
                "ye",
                "yt",
                "za",
                "zm",
                "zw",
            ]
        ]
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

    class CreateParamsConfigurationMerchant(TypedDict):
        bacs_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantBacsDebitPayments"
        ]
        """
        Settings used for Bacs debit payments.
        """
        branding: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantBranding"
        ]
        """
        Settings used to apply the merchant's branding to email receipts, invoices, Checkout, and other products.
        """
        capabilities: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilities"
        ]
        """
        Capabilities to request on the Merchant Configuration.
        """
        card_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCardPayments"
        ]
        """
        Card payments settings.
        """
        mcc: NotRequired[str]
        """
        The merchant category code for the Merchant Configuration. MCCs are used to classify businesses based on the goods or services they provide.
        """
        statement_descriptor: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantStatementDescriptor"
        ]
        """
        Statement descriptor.
        """
        support: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantSupport"
        ]
        """
        Publicly available contact information for sending support issues to.
        """

    class CreateParamsConfigurationMerchantBacsDebitPayments(TypedDict):
        display_name: NotRequired[str]
        """
        Display name for Bacs debit payments.
        """

    class CreateParamsConfigurationMerchantBranding(TypedDict):
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

    class CreateParamsConfigurationMerchantCapabilities(TypedDict):
        ach_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAchDebitPayments"
        ]
        """
        Allow the merchant to process ACH debit payments.
        """
        acss_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAcssDebitPayments"
        ]
        """
        Allow the merchant to process ACSS debit payments.
        """
        affirm_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAffirmPayments"
        ]
        """
        Allow the merchant to process Affirm payments.
        """
        afterpay_clearpay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments"
        ]
        """
        Allow the merchant to process Afterpay/Clearpay payments.
        """
        alma_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAlmaPayments"
        ]
        """
        Allow the merchant to process Alma payments.
        """
        amazon_pay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAmazonPayPayments"
        ]
        """
        Allow the merchant to process Amazon Pay payments.
        """
        au_becs_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments"
        ]
        """
        Allow the merchant to process Australian BECS Direct Debit payments.
        """
        bacs_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesBacsDebitPayments"
        ]
        """
        Allow the merchant to process BACS Direct Debit payments.
        """
        bancontact_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesBancontactPayments"
        ]
        """
        Allow the merchant to process Bancontact payments.
        """
        blik_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesBlikPayments"
        ]
        """
        Allow the merchant to process BLIK payments.
        """
        boleto_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesBoletoPayments"
        ]
        """
        Allow the merchant to process Boleto payments.
        """
        card_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesCardPayments"
        ]
        """
        Allow the merchant to collect card payments.
        """
        cartes_bancaires_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments"
        ]
        """
        Allow the merchant to process Cartes Bancaires payments.
        """
        cashapp_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesCashappPayments"
        ]
        """
        Allow the merchant to process Cash App payments.
        """
        eps_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesEpsPayments"
        ]
        """
        Allow the merchant to process EPS payments.
        """
        fpx_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesFpxPayments"
        ]
        """
        Allow the merchant to process FPX payments.
        """
        gb_bank_transfer_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments"
        ]
        """
        Allow the merchant to process UK bank transfer payments.
        """
        grabpay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesGrabpayPayments"
        ]
        """
        Allow the merchant to process GrabPay payments.
        """
        ideal_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesIdealPayments"
        ]
        """
        Allow the merchant to process iDEAL payments.
        """
        jcb_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesJcbPayments"
        ]
        """
        Allow the merchant to process JCB card payments.
        """
        jp_bank_transfer_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments"
        ]
        """
        Allow the merchant to process Japanese bank transfer payments.
        """
        kakao_pay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesKakaoPayPayments"
        ]
        """
        Allow the merchant to process Kakao Pay payments.
        """
        klarna_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesKlarnaPayments"
        ]
        """
        Allow the merchant to process Klarna payments.
        """
        konbini_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesKonbiniPayments"
        ]
        """
        Allow the merchant to process Konbini convenience store payments.
        """
        kr_card_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesKrCardPayments"
        ]
        """
        Allow the merchant to process Korean card payments.
        """
        link_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesLinkPayments"
        ]
        """
        Allow the merchant to process Link payments.
        """
        mobilepay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesMobilepayPayments"
        ]
        """
        Allow the merchant to process MobilePay payments.
        """
        multibanco_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesMultibancoPayments"
        ]
        """
        Allow the merchant to process Multibanco payments.
        """
        mx_bank_transfer_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments"
        ]
        """
        Allow the merchant to process Mexican bank transfer payments.
        """
        naver_pay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesNaverPayPayments"
        ]
        """
        Allow the merchant to process Naver Pay payments.
        """
        oxxo_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesOxxoPayments"
        ]
        """
        Allow the merchant to process OXXO payments.
        """
        p24_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesP24Payments"
        ]
        """
        Allow the merchant to process Przelewy24 (P24) payments.
        """
        pay_by_bank_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesPayByBankPayments"
        ]
        """
        Allow the merchant to process Pay by Bank payments.
        """
        payco_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesPaycoPayments"
        ]
        """
        Allow the merchant to process PAYCO payments.
        """
        paynow_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesPaynowPayments"
        ]
        """
        Allow the merchant to process PayNow payments.
        """
        promptpay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesPromptpayPayments"
        ]
        """
        Allow the merchant to process PromptPay payments.
        """
        revolut_pay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesRevolutPayPayments"
        ]
        """
        Allow the merchant to process Revolut Pay payments.
        """
        samsung_pay_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesSamsungPayPayments"
        ]
        """
        Allow the merchant to process Samsung Pay payments.
        """
        sepa_bank_transfer_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments"
        ]
        """
        Allow the merchant to process SEPA bank transfer payments.
        """
        sepa_debit_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesSepaDebitPayments"
        ]
        """
        Allow the merchant to process SEPA Direct Debit payments.
        """
        swish_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesSwishPayments"
        ]
        """
        Allow the merchant to process Swish payments.
        """
        twint_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesTwintPayments"
        ]
        """
        Allow the merchant to process TWINT payments.
        """
        us_bank_transfer_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments"
        ]
        """
        Allow the merchant to process US bank transfer payments.
        """
        zip_payments: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCapabilitiesZipPayments"
        ]
        """
        Allow the merchant to process Zip payments.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAchDebitPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAcssDebitPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAffirmPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAlmaPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAmazonPayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesBacsDebitPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesBancontactPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesBlikPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesBoletoPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesCardPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesCashappPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesEpsPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesFpxPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesGrabpayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesIdealPayments(
        TypedDict
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesJcbPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesKakaoPayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesKlarnaPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesKonbiniPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesKrCardPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesLinkPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesMobilepayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesMultibancoPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesNaverPayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesOxxoPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesP24Payments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesPayByBankPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesPaycoPayments(
        TypedDict
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesPaynowPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesPromptpayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesRevolutPayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesSamsungPayPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesSepaDebitPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesSwishPayments(
        TypedDict
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesTwintPayments(
        TypedDict
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCapabilitiesZipPayments(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationMerchantCardPayments(TypedDict):
        decline_on: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantCardPaymentsDeclineOn"
        ]
        """
        Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
        """

    class CreateParamsConfigurationMerchantCardPaymentsDeclineOn(TypedDict):
        avs_failure: NotRequired[bool]
        """
        Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
        """
        cvc_failure: NotRequired[bool]
        """
        Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
        """

    class CreateParamsConfigurationMerchantStatementDescriptor(TypedDict):
        descriptor: NotRequired[str]
        """
        The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don't set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
        """
        prefix: NotRequired[str]
        """
        Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don't specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
        """

    class CreateParamsConfigurationMerchantSupport(TypedDict):
        address: NotRequired[
            "AccountService.CreateParamsConfigurationMerchantSupportAddress"
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

    class CreateParamsConfigurationMerchantSupportAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsConfigurationRecipient(TypedDict):
        capabilities: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilities"
        ]
        """
        Capabilities to be requested on the Recipient Configuration.
        """

    class CreateParamsConfigurationRecipientCapabilities(TypedDict):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesBankAccounts"
        ]
        """
        Capabilities that enable OutboundPayments to a bank account linked to this Account.
        """
        cards: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesCards"
        ]
        """
        Capabilities that enable OutboundPayments to a card linked to this Account.
        """
        stripe_balance: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesStripeBalance"
        ]
        """
        Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).
        """

    class CreateParamsConfigurationRecipientCapabilitiesBankAccounts(
        TypedDict
    ):
        local: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesBankAccountsLocal"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
        """
        wire: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesBankAccountsWire"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over wire.
        """

    class CreateParamsConfigurationRecipientCapabilitiesBankAccountsLocal(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationRecipientCapabilitiesBankAccountsWire(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationRecipientCapabilitiesCards(TypedDict):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationRecipientCapabilitiesStripeBalance(
        TypedDict,
    ):
        stripe_transfers: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers"
        ]
        """
        Allows the account to receive /v1/transfers into their Stripe Balance (/v1/balance).
        """

    class CreateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorer(TypedDict):
        capabilities: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilities"
        ]
        """
        Capabilities to request on the Storer Configuration.
        """

    class CreateParamsConfigurationStorerCapabilities(TypedDict):
        financial_addresses: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesFinancialAddresses"
        ]
        """
        Can provision a financial address to credit/debit a FinancialAccount.
        """
        holds_currencies: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesHoldsCurrencies"
        ]
        """
        Can hold storage-type funds on Stripe.
        """
        inbound_transfers: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesInboundTransfers"
        ]
        """
        Can pull funds from an external source, owned by yourself, to a FinancialAccount.
        """
        outbound_payments: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundPayments"
        ]
        """
        Can send funds from a FinancialAccount to a destination owned by someone else.
        """
        outbound_transfers: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundTransfers"
        ]
        """
        Can send funds from a FinancialAccount to a destination owned by yourself.
        """

    class CreateParamsConfigurationStorerCapabilitiesFinancialAddresses(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts"
        ]
        """
        Can provision a bank-account-like financial address (VBAN) to credit/debit a FinancialAccount.
        """

    class CreateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesHoldsCurrencies(
        TypedDict
    ):
        gbp: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp"
        ]
        """
        Can hold storage-type funds on Stripe in GBP.
        """

    class CreateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesInboundTransfers(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts"
        ]
        """
        Can pull funds from an external bank account owned by yourself to a FinancialAccount.
        """

    class CreateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundPayments(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts"
        ]
        """
        Can send funds from a FinancialAccount to a bank account owned by someone else.
        """
        cards: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards"
        ]
        """
        Can send funds from a FinancialAccount to a debit card owned by someone else.
        """
        financial_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts"
        ]
        """
        Can send funds from a FinancialAccount to another FinancialAccount owned by someone else.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundTransfers(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts"
        ]
        """
        Can send funds from a FinancialAccount to a bank account owned by yourself.
        """
        financial_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts"
        ]
        """
        Can send funds from a FinancialAccount to another FinancialAccount owned by yourself.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts(
        TypedDict,
    ):
        requested: bool
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class CreateParamsDefaults(TypedDict):
        currency: NotRequired[
            Literal[
                "aed",
                "afn",
                "all",
                "amd",
                "ang",
                "aoa",
                "ars",
                "aud",
                "awg",
                "azn",
                "bam",
                "bbd",
                "bdt",
                "bgn",
                "bhd",
                "bif",
                "bmd",
                "bnd",
                "bob",
                "bov",
                "brl",
                "bsd",
                "btn",
                "bwp",
                "byn",
                "byr",
                "bzd",
                "cad",
                "cdf",
                "che",
                "chf",
                "chw",
                "clf",
                "clp",
                "cny",
                "cop",
                "cou",
                "crc",
                "cuc",
                "cup",
                "cve",
                "czk",
                "djf",
                "dkk",
                "dop",
                "dzd",
                "eek",
                "egp",
                "ern",
                "etb",
                "eur",
                "fjd",
                "fkp",
                "gbp",
                "gel",
                "ghc",
                "ghs",
                "gip",
                "gmd",
                "gnf",
                "gtq",
                "gyd",
                "hkd",
                "hnl",
                "hrk",
                "htg",
                "huf",
                "idr",
                "ils",
                "inr",
                "iqd",
                "irr",
                "isk",
                "jmd",
                "jod",
                "jpy",
                "kes",
                "kgs",
                "khr",
                "kmf",
                "kpw",
                "krw",
                "kwd",
                "kyd",
                "kzt",
                "lak",
                "lbp",
                "lkr",
                "lrd",
                "lsl",
                "ltl",
                "lvl",
                "lyd",
                "mad",
                "mdl",
                "mga",
                "mkd",
                "mmk",
                "mnt",
                "mop",
                "mro",
                "mru",
                "mur",
                "mvr",
                "mwk",
                "mxn",
                "mxv",
                "myr",
                "mzn",
                "nad",
                "ngn",
                "nio",
                "nok",
                "npr",
                "nzd",
                "omr",
                "pab",
                "pen",
                "pgk",
                "php",
                "pkr",
                "pln",
                "pyg",
                "qar",
                "ron",
                "rsd",
                "rub",
                "rwf",
                "sar",
                "sbd",
                "scr",
                "sdg",
                "sek",
                "sgd",
                "shp",
                "sle",
                "sll",
                "sos",
                "srd",
                "ssp",
                "std",
                "stn",
                "svc",
                "syp",
                "szl",
                "thb",
                "tjs",
                "tmt",
                "tnd",
                "top",
                "try",
                "ttd",
                "twd",
                "tzs",
                "uah",
                "ugx",
                "usd",
                "usdb",
                "usdc",
                "usn",
                "uyi",
                "uyu",
                "uzs",
                "vef",
                "ves",
                "vnd",
                "vuv",
                "wst",
                "xaf",
                "xcd",
                "xcg",
                "xof",
                "xpf",
                "yer",
                "zar",
                "zmk",
                "zmw",
                "zwd",
                "zwg",
                "zwl",
            ]
        ]
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
        responsibilities: NotRequired[
            "AccountService.CreateParamsDefaultsResponsibilities"
        ]
        """
        Default responsibilities held by either Stripe or the platform.
        """

    class CreateParamsDefaultsResponsibilities(TypedDict):
        fees_collector: Literal["application", "stripe"]
        """
        A value indicating the party responsible for collecting fees from this account.
        """
        losses_collector: Literal["application", "stripe"]
        """
        A value indicating who is responsible for losses when this Account can't pay back negative balances from payments.
        """

    class CreateParamsIdentity(TypedDict):
        attestations: NotRequired[
            "AccountService.CreateParamsIdentityAttestations"
        ]
        """
        Attestations from the identity's key people, e.g. owners, executives, directors.
        """
        business_details: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetails"
        ]
        """
        Information about the company or business.
        """
        country: NotRequired[
            Literal[
                "ad",
                "ae",
                "af",
                "ag",
                "ai",
                "al",
                "am",
                "ao",
                "aq",
                "ar",
                "as",
                "at",
                "au",
                "aw",
                "ax",
                "az",
                "ba",
                "bb",
                "bd",
                "be",
                "bf",
                "bg",
                "bh",
                "bi",
                "bj",
                "bl",
                "bm",
                "bn",
                "bo",
                "bq",
                "br",
                "bs",
                "bt",
                "bv",
                "bw",
                "by",
                "bz",
                "ca",
                "cc",
                "cd",
                "cf",
                "cg",
                "ch",
                "ci",
                "ck",
                "cl",
                "cm",
                "cn",
                "co",
                "cr",
                "cu",
                "cv",
                "cw",
                "cx",
                "cy",
                "cz",
                "de",
                "dj",
                "dk",
                "dm",
                "do",
                "dz",
                "ec",
                "ee",
                "eg",
                "eh",
                "er",
                "es",
                "et",
                "fi",
                "fj",
                "fk",
                "fm",
                "fo",
                "fr",
                "ga",
                "gb",
                "gd",
                "ge",
                "gf",
                "gg",
                "gh",
                "gi",
                "gl",
                "gm",
                "gn",
                "gp",
                "gq",
                "gr",
                "gs",
                "gt",
                "gu",
                "gw",
                "gy",
                "hk",
                "hm",
                "hn",
                "hr",
                "ht",
                "hu",
                "id",
                "ie",
                "il",
                "im",
                "in",
                "io",
                "iq",
                "ir",
                "is",
                "it",
                "je",
                "jm",
                "jo",
                "jp",
                "ke",
                "kg",
                "kh",
                "ki",
                "km",
                "kn",
                "kp",
                "kr",
                "kw",
                "ky",
                "kz",
                "la",
                "lb",
                "lc",
                "li",
                "lk",
                "lr",
                "ls",
                "lt",
                "lu",
                "lv",
                "ly",
                "ma",
                "mc",
                "md",
                "me",
                "mf",
                "mg",
                "mh",
                "mk",
                "ml",
                "mm",
                "mn",
                "mo",
                "mp",
                "mq",
                "mr",
                "ms",
                "mt",
                "mu",
                "mv",
                "mw",
                "mx",
                "my",
                "mz",
                "na",
                "nc",
                "ne",
                "nf",
                "ng",
                "ni",
                "nl",
                "no",
                "np",
                "nr",
                "nu",
                "nz",
                "om",
                "pa",
                "pe",
                "pf",
                "pg",
                "ph",
                "pk",
                "pl",
                "pm",
                "pn",
                "pr",
                "ps",
                "pt",
                "pw",
                "py",
                "qa",
                "qz",
                "re",
                "ro",
                "rs",
                "ru",
                "rw",
                "sa",
                "sb",
                "sc",
                "sd",
                "se",
                "sg",
                "sh",
                "si",
                "sj",
                "sk",
                "sl",
                "sm",
                "sn",
                "so",
                "sr",
                "ss",
                "st",
                "sv",
                "sx",
                "sy",
                "sz",
                "tc",
                "td",
                "tf",
                "tg",
                "th",
                "tj",
                "tk",
                "tl",
                "tm",
                "tn",
                "to",
                "tr",
                "tt",
                "tv",
                "tw",
                "tz",
                "ua",
                "ug",
                "um",
                "us",
                "uy",
                "uz",
                "va",
                "vc",
                "ve",
                "vg",
                "vi",
                "vn",
                "vu",
                "wf",
                "ws",
                "xx",
                "ye",
                "yt",
                "za",
                "zm",
                "zw",
            ]
        ]
        """
        The country in which the account holder resides, or in which the business is legally established. This should be an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.
        """
        entity_type: NotRequired[
            Literal["company", "government_entity", "individual", "non_profit"]
        ]
        """
        The entity type.
        """
        individual: NotRequired[
            "AccountService.CreateParamsIdentityIndividual"
        ]
        """
        Information about the person represented by the account.
        """

    class CreateParamsIdentityAttestations(TypedDict):
        directorship_declaration: NotRequired[
            "AccountService.CreateParamsIdentityAttestationsDirectorshipDeclaration"
        ]
        """
        This hash is used to attest that the directors information provided to Stripe is both current and correct.
        """
        ownership_declaration: NotRequired[
            "AccountService.CreateParamsIdentityAttestationsOwnershipDeclaration"
        ]
        """
        This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
        """
        persons_provided: NotRequired[
            "AccountService.CreateParamsIdentityAttestationsPersonsProvided"
        ]
        """
        Attestation that all Persons with a specific Relationship value have been provided.
        """
        terms_of_service: NotRequired[
            "AccountService.CreateParamsIdentityAttestationsTermsOfService"
        ]
        """
        Attestations of accepted terms of service agreements.
        """

    class CreateParamsIdentityAttestationsDirectorshipDeclaration(TypedDict):
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

    class CreateParamsIdentityAttestationsOwnershipDeclaration(TypedDict):
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

    class CreateParamsIdentityAttestationsPersonsProvided(TypedDict):
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

    class CreateParamsIdentityAttestationsTermsOfService(TypedDict):
        account: NotRequired[
            "AccountService.CreateParamsIdentityAttestationsTermsOfServiceAccount"
        ]
        """
        Details on the Account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance).
        """

    class CreateParamsIdentityAttestationsTermsOfServiceAccount(TypedDict):
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

    class CreateParamsIdentityBusinessDetails(TypedDict):
        address: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsAddress"
        ]
        """
        The business registration address of the business entity.
        """
        annual_revenue: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsAnnualRevenue"
        ]
        """
        The business gross annual revenue for its preceding fiscal year.
        """
        documents: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocuments"
        ]
        """
        A document verifying the business.
        """
        doing_business_as: NotRequired[str]
        """
        The name which is used by the business.
        """
        estimated_worker_count: NotRequired[int]
        """
        An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
        """
        id_numbers: NotRequired[
            List["AccountService.CreateParamsIdentityBusinessDetailsIdNumber"]
        ]
        """
        The ID numbers of a business entity.
        """
        monthly_estimated_revenue: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue"
        ]
        """
        An estimate of the monthly revenue of the business.
        """
        phone: NotRequired[str]
        """
        The phone number of the Business Entity.
        """
        product_description: NotRequired[str]
        """
        Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
        """
        registered_name: NotRequired[str]
        """
        The business legal name.
        """
        script_addresses: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptAddresses"
        ]
        """
        The business registration address of the business entity in non latin script.
        """
        script_names: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptNames"
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
        url: NotRequired[str]
        """
        The business's publicly available website.
        """

    class CreateParamsIdentityBusinessDetailsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityBusinessDetailsAnnualRevenue(TypedDict):
        amount: NotRequired[AmountParam]
        """
        A non-negative integer representing the amount in the smallest currency unit.
        """
        fiscal_year_end: NotRequired[str]
        """
        The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
        """

    class CreateParamsIdentityBusinessDetailsDocuments(TypedDict):
        bank_account_ownership_verification: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification"
        ]
        """
        One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
        """
        company_license: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsCompanyLicense"
        ]
        """
        One or more documents that demonstrate proof of a company's license to operate.
        """
        company_memorandum_of_association: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation"
        ]
        """
        One or more documents showing the company's Memorandum of Association.
        """
        company_ministerial_decree: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree"
        ]
        """
        Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
        """
        company_registration_verification: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification"
        ]
        """
        One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
        """
        company_tax_id_verification: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification"
        ]
        """
        One or more documents that demonstrate proof of a company's tax ID.
        """
        primary_verification: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification"
        ]
        """
        A document verifying the business.
        """
        proof_of_address: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsProofOfAddress"
        ]
        """
        One or more documents that demonstrate proof of address.
        """
        proof_of_registration: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration"
        ]
        """
        One or more documents showing the company's proof of registration with the national business registry.
        """
        proof_of_ultimate_beneficial_ownership: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership"
        ]
        """
        One or more documents that demonstrate proof of ultimate beneficial ownership.
        """

    class CreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification(
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

    class CreateParamsIdentityBusinessDetailsDocumentsCompanyLicense(
        TypedDict
    ):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation(
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

    class CreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree(
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

    class CreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification(
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

    class CreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification(
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

    class CreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification(
        TypedDict,
    ):
        front_back: "AccountService.CreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class CreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack(
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

    class CreateParamsIdentityBusinessDetailsDocumentsProofOfAddress(
        TypedDict
    ):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration(
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

    class CreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership(
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

    class CreateParamsIdentityBusinessDetailsIdNumber(TypedDict):
        registrar: NotRequired[str]
        """
        The registrar of the ID number (Only valid for DE ID number types).
        """
        type: Literal[
            "ae_crn",
            "ae_vat",
            "at_fn",
            "au_abn",
            "au_acn",
            "au_in",
            "be_cbe",
            "bg_uic",
            "br_cnpj",
            "ca_cn",
            "ca_crarr",
            "ca_neq",
            "ca_rid",
            "ch_chid",
            "ch_uid",
            "cy_tic",
            "cz_ico",
            "de_hrn",
            "de_vat",
            "dk_cvr",
            "ee_rk",
            "es_cif",
            "fi_yt",
            "fr_siren",
            "fr_vat",
            "gb_crn",
            "gi_crn",
            "gr_gemi",
            "hk_br",
            "hk_cr",
            "hk_mbs",
            "hu_cjs",
            "ie_crn",
            "it_rea",
            "it_vat",
            "jp_cn",
            "li_uid",
            "lt_ccrn",
            "lu_rcs",
            "lv_urn",
            "mt_crn",
            "mx_rfc",
            "my_brn",
            "my_coid",
            "my_sst",
            "nl_kvk",
            "no_orgnr",
            "nz_bn",
            "pl_regon",
            "pt_vat",
            "ro_cui",
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

    class CreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue(
        TypedDict
    ):
        amount: NotRequired[AmountParam]
        """
        A non-negative integer representing the amount in the smallest currency unit.
        """

    class CreateParamsIdentityBusinessDetailsScriptAddresses(TypedDict):
        kana: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptAddressesKana"
        ]
        """
        Kana Address.
        """
        kanji: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptAddressesKanji"
        ]
        """
        Kanji Address.
        """

    class CreateParamsIdentityBusinessDetailsScriptAddressesKana(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityBusinessDetailsScriptAddressesKanji(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityBusinessDetailsScriptNames(TypedDict):
        kana: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptNamesKana"
        ]
        """
        Kana name.
        """
        kanji: NotRequired[
            "AccountService.CreateParamsIdentityBusinessDetailsScriptNamesKanji"
        ]
        """
        Kanji name.
        """

    class CreateParamsIdentityBusinessDetailsScriptNamesKana(TypedDict):
        registered_name: NotRequired[str]
        """
        Registered name of the business.
        """

    class CreateParamsIdentityBusinessDetailsScriptNamesKanji(TypedDict):
        registered_name: NotRequired[str]
        """
        Registered name of the business.
        """

    class CreateParamsIdentityIndividual(TypedDict):
        additional_addresses: NotRequired[
            List[
                "AccountService.CreateParamsIdentityIndividualAdditionalAddress"
            ]
        ]
        """
        Additional addresses associated with the individual.
        """
        additional_names: NotRequired[
            List["AccountService.CreateParamsIdentityIndividualAdditionalName"]
        ]
        """
        Additional names (e.g. aliases) associated with the individual.
        """
        address: NotRequired[
            "AccountService.CreateParamsIdentityIndividualAddress"
        ]
        """
        The individual's residential address.
        """
        date_of_birth: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDateOfBirth"
        ]
        """
        The individual's date of birth.
        """
        documents: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocuments"
        ]
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
            List["AccountService.CreateParamsIdentityIndividualIdNumber"]
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
        nationalities: NotRequired[
            List[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
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
            "AccountService.CreateParamsIdentityIndividualRelationship"
        ]
        """
        The relationship that this individual has with the account's identity.
        """
        script_addresses: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptAddresses"
        ]
        """
        The script addresses (e.g., non-Latin characters) associated with the individual.
        """
        script_names: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptNames"
        ]
        """
        The individuals primary name in non latin script.
        """
        surname: NotRequired[str]
        """
        The individual's last name.
        """

    class CreateParamsIdentityIndividualAdditionalAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityIndividualAdditionalName(TypedDict):
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

    class CreateParamsIdentityIndividualAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityIndividualDateOfBirth(TypedDict):
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

    class CreateParamsIdentityIndividualDocuments(TypedDict):
        company_authorization: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocumentsCompanyAuthorization"
        ]
        """
        One or more documents that demonstrate proof that this person is authorized to represent the company.
        """
        passport: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocumentsPassport"
        ]
        """
        One or more documents showing the person's passport page with photo and personal data.
        """
        primary_verification: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocumentsPrimaryVerification"
        ]
        """
        An identifying document showing the person's name, either a passport or local ID card.
        """
        secondary_verification: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocumentsSecondaryVerification"
        ]
        """
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
        """
        visa: NotRequired[
            "AccountService.CreateParamsIdentityIndividualDocumentsVisa"
        ]
        """
        One or more documents showing the person's visa required for living in the country where they are residing.
        """

    class CreateParamsIdentityIndividualDocumentsCompanyAuthorization(
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

    class CreateParamsIdentityIndividualDocumentsPassport(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsIdentityIndividualDocumentsPrimaryVerification(
        TypedDict
    ):
        front_back: "AccountService.CreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class CreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack(
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

    class CreateParamsIdentityIndividualDocumentsSecondaryVerification(
        TypedDict,
    ):
        front_back: "AccountService.CreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class CreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack(
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

    class CreateParamsIdentityIndividualDocumentsVisa(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsIdentityIndividualIdNumber(TypedDict):
        type: Literal[
            "ae_eid",
            "br_cpf",
            "de_stn",
            "hk_id",
            "mx_rfc",
            "my_nric",
            "nl_bsn",
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

    class CreateParamsIdentityIndividualRelationship(TypedDict):
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

    class CreateParamsIdentityIndividualScriptAddresses(TypedDict):
        kana: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptAddressesKana"
        ]
        """
        Kana Address.
        """
        kanji: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptAddressesKanji"
        ]
        """
        Kanji Address.
        """

    class CreateParamsIdentityIndividualScriptAddressesKana(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityIndividualScriptAddressesKanji(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsIdentityIndividualScriptNames(TypedDict):
        kana: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptNamesKana"
        ]
        """
        Persons name in kana script.
        """
        kanji: NotRequired[
            "AccountService.CreateParamsIdentityIndividualScriptNamesKanji"
        ]
        """
        Persons name in kanji script.
        """

    class CreateParamsIdentityIndividualScriptNamesKana(TypedDict):
        given_name: NotRequired[str]
        """
        The person's first or given name.
        """
        surname: NotRequired[str]
        """
        The person's last or family name.
        """

    class CreateParamsIdentityIndividualScriptNamesKanji(TypedDict):
        given_name: NotRequired[str]
        """
        The person's first or given name.
        """
        surname: NotRequired[str]
        """
        The person's last or family name.
        """

    class ListParams(TypedDict):
        applied_configurations: NotRequired[List[str]]
        """
        Filter only accounts that have all of the configurations specified. If omitted, returns all accounts regardless of which configurations they have.
        """
        limit: NotRequired[int]
        """
        The upper limit on the number of accounts returned by the List Account request.
        """

    class RetrieveParams(TypedDict):
        include: NotRequired[
            List[
                Literal[
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

    class UpdateParams(TypedDict):
        configuration: NotRequired["AccountService.UpdateParamsConfiguration"]
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
        defaults: NotRequired["AccountService.UpdateParamsDefaults"]
        """
        Default values to be used on Account Configurations.
        """
        display_name: NotRequired[str]
        """
        A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
        """
        identity: NotRequired["AccountService.UpdateParamsIdentity"]
        """
        Information about the company, individual, and business represented by the Account.
        """
        include: NotRequired[
            List[
                Literal[
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

    class UpdateParamsConfiguration(TypedDict):
        customer: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomer"
        ]
        """
        The Customer Configuration allows the Account to be charged.
        """
        merchant: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchant"
        ]
        """
        The Merchant configuration allows the Account to act as a connected account and collect payments facilitated by a Connect platform. You can add this configuration to your connected accounts only if you've completed onboarding as a Connect platform.
        """
        recipient: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipient"
        ]
        """
        The Recipient Configuration allows the Account to receive funds.
        """
        storer: NotRequired["AccountService.UpdateParamsConfigurationStorer"]
        """
        The Storer Configuration allows the Account to store and move funds using stored-value FinancialAccounts.
        """

    class UpdateParamsConfigurationCustomer(TypedDict):
        automatic_indirect_tax: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerAutomaticIndirectTax"
        ]
        """
        Automatic indirect tax settings to be used when automatic tax calculation is enabled on the customer's invoices, subscriptions, checkout sessions, or payment links. Surfaces if automatic tax calculation is possible given the current customer location information.
        """
        billing: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerBilling"
        ]
        """
        Billing settings - default settings used for this customer in Billing flows such as Invoices and Subscriptions.
        """
        capabilities: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerCapabilities"
        ]
        """
        Capabilities that have been requested on the Customer Configuration.
        """
        shipping: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerShipping"
        ]
        """
        The customer's shipping information. Appears on invoices emailed to this customer.
        """
        test_clock: NotRequired[str]
        """
        ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.
        """

    class UpdateParamsConfigurationCustomerAutomaticIndirectTax(TypedDict):
        exempt: NotRequired[Literal["exempt", "none", "reverse"]]
        """
        Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to reverse, invoice and receipt PDFs include the following text: “Reverse charge”.
        """
        ip_address: NotRequired[str]
        """
        A recent IP address of the customer used for tax reporting and tax location inference.
        """
        location_source: NotRequired[
            Literal["identity_address", "ip_address", "shipping_address"]
        ]
        """
        The data source used to identify the customer's tax location - defaults to 'identity_address'. Will only be used for automatic tax calculation on the customer's Invoices and Subscriptions.
        """
        validate_location: NotRequired[
            Literal["auto", "deferred", "immediately"]
        ]
        """
        A per-request flag that indicates when Stripe should validate the customer tax location - defaults to 'auto'.
        """

    class UpdateParamsConfigurationCustomerBilling(TypedDict):
        default_payment_method: NotRequired[str]
        """
        ID of a payment method that's attached to the customer, to be used as the customer's default payment method for invoices and subscriptions.
        """
        invoice: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerBillingInvoice"
        ]
        """
        Default settings used on invoices for this customer.
        """

    class UpdateParamsConfigurationCustomerBillingInvoice(TypedDict):
        custom_fields: NotRequired[
            List[
                "AccountService.UpdateParamsConfigurationCustomerBillingInvoiceCustomField"
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
            "AccountService.UpdateParamsConfigurationCustomerBillingInvoiceRendering"
        ]
        """
        Default options for invoice PDF rendering for this customer.
        """

    class UpdateParamsConfigurationCustomerBillingInvoiceCustomField(
        TypedDict
    ):
        name: str
        """
        The name of the custom field. This may be up to 40 characters.
        """
        value: str
        """
        The value of the custom field. This may be up to 140 characters. When updating, pass an empty string to remove previously-defined values.
        """

    class UpdateParamsConfigurationCustomerBillingInvoiceRendering(TypedDict):
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

    class UpdateParamsConfigurationCustomerCapabilities(TypedDict):
        automatic_indirect_tax: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax"
        ]
        """
        Generates requirements for enabling automatic indirect tax calculation on this customer's invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer's invoices or subscriptions. Uses the `location_source` field.
        """

    class UpdateParamsConfigurationCustomerCapabilitiesAutomaticIndirectTax(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationCustomerShipping(TypedDict):
        address: NotRequired[
            "AccountService.UpdateParamsConfigurationCustomerShippingAddress"
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

    class UpdateParamsConfigurationCustomerShippingAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Literal[
                "ad",
                "ae",
                "af",
                "ag",
                "ai",
                "al",
                "am",
                "ao",
                "aq",
                "ar",
                "as",
                "at",
                "au",
                "aw",
                "ax",
                "az",
                "ba",
                "bb",
                "bd",
                "be",
                "bf",
                "bg",
                "bh",
                "bi",
                "bj",
                "bl",
                "bm",
                "bn",
                "bo",
                "bq",
                "br",
                "bs",
                "bt",
                "bv",
                "bw",
                "by",
                "bz",
                "ca",
                "cc",
                "cd",
                "cf",
                "cg",
                "ch",
                "ci",
                "ck",
                "cl",
                "cm",
                "cn",
                "co",
                "cr",
                "cu",
                "cv",
                "cw",
                "cx",
                "cy",
                "cz",
                "de",
                "dj",
                "dk",
                "dm",
                "do",
                "dz",
                "ec",
                "ee",
                "eg",
                "eh",
                "er",
                "es",
                "et",
                "fi",
                "fj",
                "fk",
                "fm",
                "fo",
                "fr",
                "ga",
                "gb",
                "gd",
                "ge",
                "gf",
                "gg",
                "gh",
                "gi",
                "gl",
                "gm",
                "gn",
                "gp",
                "gq",
                "gr",
                "gs",
                "gt",
                "gu",
                "gw",
                "gy",
                "hk",
                "hm",
                "hn",
                "hr",
                "ht",
                "hu",
                "id",
                "ie",
                "il",
                "im",
                "in",
                "io",
                "iq",
                "ir",
                "is",
                "it",
                "je",
                "jm",
                "jo",
                "jp",
                "ke",
                "kg",
                "kh",
                "ki",
                "km",
                "kn",
                "kp",
                "kr",
                "kw",
                "ky",
                "kz",
                "la",
                "lb",
                "lc",
                "li",
                "lk",
                "lr",
                "ls",
                "lt",
                "lu",
                "lv",
                "ly",
                "ma",
                "mc",
                "md",
                "me",
                "mf",
                "mg",
                "mh",
                "mk",
                "ml",
                "mm",
                "mn",
                "mo",
                "mp",
                "mq",
                "mr",
                "ms",
                "mt",
                "mu",
                "mv",
                "mw",
                "mx",
                "my",
                "mz",
                "na",
                "nc",
                "ne",
                "nf",
                "ng",
                "ni",
                "nl",
                "no",
                "np",
                "nr",
                "nu",
                "nz",
                "om",
                "pa",
                "pe",
                "pf",
                "pg",
                "ph",
                "pk",
                "pl",
                "pm",
                "pn",
                "pr",
                "ps",
                "pt",
                "pw",
                "py",
                "qa",
                "qz",
                "re",
                "ro",
                "rs",
                "ru",
                "rw",
                "sa",
                "sb",
                "sc",
                "sd",
                "se",
                "sg",
                "sh",
                "si",
                "sj",
                "sk",
                "sl",
                "sm",
                "sn",
                "so",
                "sr",
                "ss",
                "st",
                "sv",
                "sx",
                "sy",
                "sz",
                "tc",
                "td",
                "tf",
                "tg",
                "th",
                "tj",
                "tk",
                "tl",
                "tm",
                "tn",
                "to",
                "tr",
                "tt",
                "tv",
                "tw",
                "tz",
                "ua",
                "ug",
                "um",
                "us",
                "uy",
                "uz",
                "va",
                "vc",
                "ve",
                "vg",
                "vi",
                "vn",
                "vu",
                "wf",
                "ws",
                "xx",
                "ye",
                "yt",
                "za",
                "zm",
                "zw",
            ]
        ]
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

    class UpdateParamsConfigurationMerchant(TypedDict):
        bacs_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantBacsDebitPayments"
        ]
        """
        Settings used for Bacs debit payments.
        """
        branding: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantBranding"
        ]
        """
        Settings used to apply the merchant's branding to email receipts, invoices, Checkout, and other products.
        """
        capabilities: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilities"
        ]
        """
        Capabilities to request on the Merchant Configuration.
        """
        card_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCardPayments"
        ]
        """
        Card payments settings.
        """
        mcc: NotRequired[str]
        """
        The merchant category code for the merchant. MCCs are used to classify businesses based on the goods or services they provide.
        """
        statement_descriptor: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantStatementDescriptor"
        ]
        """
        Statement descriptor.
        """
        support: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantSupport"
        ]
        """
        Publicly available contact information for sending support issues to.
        """

    class UpdateParamsConfigurationMerchantBacsDebitPayments(TypedDict):
        display_name: NotRequired[str]
        """
        Display name for Bacs debit payments.
        """

    class UpdateParamsConfigurationMerchantBranding(TypedDict):
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

    class UpdateParamsConfigurationMerchantCapabilities(TypedDict):
        ach_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAchDebitPayments"
        ]
        """
        Allow the merchant to process ACH debit payments.
        """
        acss_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAcssDebitPayments"
        ]
        """
        Allow the merchant to process ACSS debit payments.
        """
        affirm_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAffirmPayments"
        ]
        """
        Allow the merchant to process Affirm payments.
        """
        afterpay_clearpay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments"
        ]
        """
        Allow the merchant to process Afterpay/Clearpay payments.
        """
        alma_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAlmaPayments"
        ]
        """
        Allow the merchant to process Alma payments.
        """
        amazon_pay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAmazonPayPayments"
        ]
        """
        Allow the merchant to process Amazon Pay payments.
        """
        au_becs_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments"
        ]
        """
        Allow the merchant to process Australian BECS Direct Debit payments.
        """
        bacs_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesBacsDebitPayments"
        ]
        """
        Allow the merchant to process BACS Direct Debit payments.
        """
        bancontact_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesBancontactPayments"
        ]
        """
        Allow the merchant to process Bancontact payments.
        """
        blik_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesBlikPayments"
        ]
        """
        Allow the merchant to process BLIK payments.
        """
        boleto_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesBoletoPayments"
        ]
        """
        Allow the merchant to process Boleto payments.
        """
        card_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesCardPayments"
        ]
        """
        Allow the merchant to collect card payments.
        """
        cartes_bancaires_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments"
        ]
        """
        Allow the merchant to process Cartes Bancaires payments.
        """
        cashapp_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesCashappPayments"
        ]
        """
        Allow the merchant to process Cash App payments.
        """
        eps_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesEpsPayments"
        ]
        """
        Allow the merchant to process EPS payments.
        """
        fpx_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesFpxPayments"
        ]
        """
        Allow the merchant to process FPX payments.
        """
        gb_bank_transfer_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments"
        ]
        """
        Allow the merchant to process UK bank transfer payments.
        """
        grabpay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesGrabpayPayments"
        ]
        """
        Allow the merchant to process GrabPay payments.
        """
        ideal_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesIdealPayments"
        ]
        """
        Allow the merchant to process iDEAL payments.
        """
        jcb_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesJcbPayments"
        ]
        """
        Allow the merchant to process JCB card payments.
        """
        jp_bank_transfer_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments"
        ]
        """
        Allow the merchant to process Japanese bank transfer payments.
        """
        kakao_pay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesKakaoPayPayments"
        ]
        """
        Allow the merchant to process Kakao Pay payments.
        """
        klarna_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesKlarnaPayments"
        ]
        """
        Allow the merchant to process Klarna payments.
        """
        konbini_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesKonbiniPayments"
        ]
        """
        Allow the merchant to process Konbini convenience store payments.
        """
        kr_card_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesKrCardPayments"
        ]
        """
        Allow the merchant to process Korean card payments.
        """
        link_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesLinkPayments"
        ]
        """
        Allow the merchant to process Link payments.
        """
        mobilepay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesMobilepayPayments"
        ]
        """
        Allow the merchant to process MobilePay payments.
        """
        multibanco_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesMultibancoPayments"
        ]
        """
        Allow the merchant to process Multibanco payments.
        """
        mx_bank_transfer_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments"
        ]
        """
        Allow the merchant to process Mexican bank transfer payments.
        """
        naver_pay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesNaverPayPayments"
        ]
        """
        Allow the merchant to process Naver Pay payments.
        """
        oxxo_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesOxxoPayments"
        ]
        """
        Allow the merchant to process OXXO payments.
        """
        p24_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesP24Payments"
        ]
        """
        Allow the merchant to process Przelewy24 (P24) payments.
        """
        pay_by_bank_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesPayByBankPayments"
        ]
        """
        Allow the merchant to process Pay by Bank payments.
        """
        payco_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesPaycoPayments"
        ]
        """
        Allow the merchant to process PAYCO payments.
        """
        paynow_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesPaynowPayments"
        ]
        """
        Allow the merchant to process PayNow payments.
        """
        promptpay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesPromptpayPayments"
        ]
        """
        Allow the merchant to process PromptPay payments.
        """
        revolut_pay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesRevolutPayPayments"
        ]
        """
        Allow the merchant to process Revolut Pay payments.
        """
        samsung_pay_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesSamsungPayPayments"
        ]
        """
        Allow the merchant to process Samsung Pay payments.
        """
        sepa_bank_transfer_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments"
        ]
        """
        Allow the merchant to process SEPA bank transfer payments.
        """
        sepa_debit_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesSepaDebitPayments"
        ]
        """
        Allow the merchant to process SEPA Direct Debit payments.
        """
        swish_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesSwishPayments"
        ]
        """
        Allow the merchant to process Swish payments.
        """
        twint_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesTwintPayments"
        ]
        """
        Allow the merchant to process TWINT payments.
        """
        us_bank_transfer_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments"
        ]
        """
        Allow the merchant to process US bank transfer payments.
        """
        zip_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCapabilitiesZipPayments"
        ]
        """
        Allow the merchant to process Zip payments.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAchDebitPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAcssDebitPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAffirmPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAfterpayClearpayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAlmaPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAmazonPayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesAuBecsDebitPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesBacsDebitPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesBancontactPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesBlikPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesBoletoPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesCardPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesCartesBancairesPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesCashappPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesEpsPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesFpxPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesGbBankTransferPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesGrabpayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesIdealPayments(
        TypedDict
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesJcbPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesJpBankTransferPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesKakaoPayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesKlarnaPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesKonbiniPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesKrCardPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesLinkPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesMobilepayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesMultibancoPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesMxBankTransferPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesNaverPayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesOxxoPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesP24Payments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesPayByBankPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesPaycoPayments(
        TypedDict
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesPaynowPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesPromptpayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesRevolutPayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesSamsungPayPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesSepaBankTransferPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesSepaDebitPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesSwishPayments(
        TypedDict
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesTwintPayments(
        TypedDict
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesUsBankTransferPayments(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCapabilitiesZipPayments(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationMerchantCardPayments(TypedDict):
        decline_on: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantCardPaymentsDeclineOn"
        ]
        """
        Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
        """

    class UpdateParamsConfigurationMerchantCardPaymentsDeclineOn(TypedDict):
        avs_failure: NotRequired[bool]
        """
        Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
        """
        cvc_failure: NotRequired[bool]
        """
        Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
        """

    class UpdateParamsConfigurationMerchantStatementDescriptor(TypedDict):
        descriptor: NotRequired[str]
        """
        The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don't set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
        """
        prefix: NotRequired[str]
        """
        Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don't specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
        """

    class UpdateParamsConfigurationMerchantSupport(TypedDict):
        address: NotRequired[
            "AccountService.UpdateParamsConfigurationMerchantSupportAddress"
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

    class UpdateParamsConfigurationMerchantSupportAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsConfigurationRecipient(TypedDict):
        capabilities: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilities"
        ]
        """
        Capabilities to request on the Recipient Configuration.
        """
        default_outbound_destination: NotRequired[str]
        """
        The payout method id to be used as a default outbound destination. This will allow the PayoutMethod to be omitted on OutboundPayments made through API or sending payouts via dashboard. Can also be explicitly set to `null` to clear the existing default outbound destination.
        """

    class UpdateParamsConfigurationRecipientCapabilities(TypedDict):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesBankAccounts"
        ]
        """
        Capabilities that enable OutboundPayments to a bank account linked to this Account.
        """
        cards: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesCards"
        ]
        """
        Capability that enable OutboundPayments to a debit card linked to this Account.
        """
        stripe_balance: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesStripeBalance"
        ]
        """
        Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).
        """

    class UpdateParamsConfigurationRecipientCapabilitiesBankAccounts(
        TypedDict
    ):
        local: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesBankAccountsLocal"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
        """
        wire: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesBankAccountsWire"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over wire.
        """

    class UpdateParamsConfigurationRecipientCapabilitiesBankAccountsLocal(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationRecipientCapabilitiesBankAccountsWire(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationRecipientCapabilitiesCards(TypedDict):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationRecipientCapabilitiesStripeBalance(
        TypedDict,
    ):
        stripe_transfers: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers"
        ]
        """
        Allows the account to receive /v1/transfers into their Stripe Balance (/v1/balance).
        """

    class UpdateParamsConfigurationRecipientCapabilitiesStripeBalanceStripeTransfers(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorer(TypedDict):
        capabilities: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilities"
        ]
        """
        Capabilities to request on the Storer Configuration.
        """

    class UpdateParamsConfigurationStorerCapabilities(TypedDict):
        financial_addresses: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesFinancialAddresses"
        ]
        """
        Can provision a financial address to credit/debit a FinancialAccount.
        """
        holds_currencies: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesHoldsCurrencies"
        ]
        """
        Can hold storage-type funds on Stripe.
        """
        inbound_transfers: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesInboundTransfers"
        ]
        """
        Can pull funds from an external source, owned by yourself, to a FinancialAccount.
        """
        outbound_payments: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundPayments"
        ]
        """
        Can send funds from a FinancialAccount to a destination owned by someone else.
        """
        outbound_transfers: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundTransfers"
        ]
        """
        Can send funds from a FinancialAccount to a destination owned by yourself.
        """

    class UpdateParamsConfigurationStorerCapabilitiesFinancialAddresses(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts"
        ]
        """
        Can provision a bank-account-like financial address (VBAN) to credit/debit a FinancialAccount.
        """

    class UpdateParamsConfigurationStorerCapabilitiesFinancialAddressesBankAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesHoldsCurrencies(
        TypedDict
    ):
        gbp: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp"
        ]
        """
        Can hold storage-type funds on Stripe in GBP.
        """

    class UpdateParamsConfigurationStorerCapabilitiesHoldsCurrenciesGbp(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesInboundTransfers(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts"
        ]
        """
        Can pull funds from an external bank account owned by yourself to a FinancialAccount.
        """

    class UpdateParamsConfigurationStorerCapabilitiesInboundTransfersBankAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundPayments(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts"
        ]
        """
        Can send funds from a FinancialAccount to a bank account owned by someone else.
        """
        cards: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards"
        ]
        """
        Can send funds from a FinancialAccount to a debit card owned by someone else.
        """
        financial_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts"
        ]
        """
        Can send funds from a FinancialAccount to another FinancialAccount owned by someone else.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsBankAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsCards(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundPaymentsFinancialAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundTransfers(
        TypedDict,
    ):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts"
        ]
        """
        Can send funds from a FinancialAccount to a bank account owned by yourself.
        """
        financial_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts"
        ]
        """
        Can send funds from a FinancialAccount to another FinancialAccount owned by yourself.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundTransfersBankAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsConfigurationStorerCapabilitiesOutboundTransfersFinancialAccounts(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        To request a new Capability for an account, pass true. There can be a delay before the requested Capability becomes active.
        """

    class UpdateParamsDefaults(TypedDict):
        currency: NotRequired[
            Literal[
                "aed",
                "afn",
                "all",
                "amd",
                "ang",
                "aoa",
                "ars",
                "aud",
                "awg",
                "azn",
                "bam",
                "bbd",
                "bdt",
                "bgn",
                "bhd",
                "bif",
                "bmd",
                "bnd",
                "bob",
                "bov",
                "brl",
                "bsd",
                "btn",
                "bwp",
                "byn",
                "byr",
                "bzd",
                "cad",
                "cdf",
                "che",
                "chf",
                "chw",
                "clf",
                "clp",
                "cny",
                "cop",
                "cou",
                "crc",
                "cuc",
                "cup",
                "cve",
                "czk",
                "djf",
                "dkk",
                "dop",
                "dzd",
                "eek",
                "egp",
                "ern",
                "etb",
                "eur",
                "fjd",
                "fkp",
                "gbp",
                "gel",
                "ghc",
                "ghs",
                "gip",
                "gmd",
                "gnf",
                "gtq",
                "gyd",
                "hkd",
                "hnl",
                "hrk",
                "htg",
                "huf",
                "idr",
                "ils",
                "inr",
                "iqd",
                "irr",
                "isk",
                "jmd",
                "jod",
                "jpy",
                "kes",
                "kgs",
                "khr",
                "kmf",
                "kpw",
                "krw",
                "kwd",
                "kyd",
                "kzt",
                "lak",
                "lbp",
                "lkr",
                "lrd",
                "lsl",
                "ltl",
                "lvl",
                "lyd",
                "mad",
                "mdl",
                "mga",
                "mkd",
                "mmk",
                "mnt",
                "mop",
                "mro",
                "mru",
                "mur",
                "mvr",
                "mwk",
                "mxn",
                "mxv",
                "myr",
                "mzn",
                "nad",
                "ngn",
                "nio",
                "nok",
                "npr",
                "nzd",
                "omr",
                "pab",
                "pen",
                "pgk",
                "php",
                "pkr",
                "pln",
                "pyg",
                "qar",
                "ron",
                "rsd",
                "rub",
                "rwf",
                "sar",
                "sbd",
                "scr",
                "sdg",
                "sek",
                "sgd",
                "shp",
                "sle",
                "sll",
                "sos",
                "srd",
                "ssp",
                "std",
                "stn",
                "svc",
                "syp",
                "szl",
                "thb",
                "tjs",
                "tmt",
                "tnd",
                "top",
                "try",
                "ttd",
                "twd",
                "tzs",
                "uah",
                "ugx",
                "usd",
                "usdb",
                "usdc",
                "usn",
                "uyi",
                "uyu",
                "uzs",
                "vef",
                "ves",
                "vnd",
                "vuv",
                "wst",
                "xaf",
                "xcd",
                "xcg",
                "xof",
                "xpf",
                "yer",
                "zar",
                "zmk",
                "zmw",
                "zwd",
                "zwg",
                "zwl",
            ]
        ]
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
        responsibilities: NotRequired[
            "AccountService.UpdateParamsDefaultsResponsibilities"
        ]
        """
        Default responsibilities held by either Stripe or the platform.
        """

    class UpdateParamsDefaultsResponsibilities(TypedDict):
        fees_collector: Literal["application", "stripe"]
        """
        A value indicating the party responsible for collecting fees from this account.
        """
        losses_collector: Literal["application", "stripe"]
        """
        A value indicating who is responsible for losses when this Account can't pay back negative balances from payments.
        """

    class UpdateParamsIdentity(TypedDict):
        attestations: NotRequired[
            "AccountService.UpdateParamsIdentityAttestations"
        ]
        """
        Attestations from the identity's key people, e.g. owners, executives, directors.
        """
        business_details: NotRequired[
            "AccountService.UpdateParamsIdentityBusinessDetails"
        ]
        """
        Information about the company or business.
        """
        country: NotRequired[
            Literal[
                "ad",
                "ae",
                "af",
                "ag",
                "ai",
                "al",
                "am",
                "ao",
                "aq",
                "ar",
                "as",
                "at",
                "au",
                "aw",
                "ax",
                "az",
                "ba",
                "bb",
                "bd",
                "be",
                "bf",
                "bg",
                "bh",
                "bi",
                "bj",
                "bl",
                "bm",
                "bn",
                "bo",
                "bq",
                "br",
                "bs",
                "bt",
                "bv",
                "bw",
                "by",
                "bz",
                "ca",
                "cc",
                "cd",
                "cf",
                "cg",
                "ch",
                "ci",
                "ck",
                "cl",
                "cm",
                "cn",
                "co",
                "cr",
                "cu",
                "cv",
                "cw",
                "cx",
                "cy",
                "cz",
                "de",
                "dj",
                "dk",
                "dm",
                "do",
                "dz",
                "ec",
                "ee",
                "eg",
                "eh",
                "er",
                "es",
                "et",
                "fi",
                "fj",
                "fk",
                "fm",
                "fo",
                "fr",
                "ga",
                "gb",
                "gd",
                "ge",
                "gf",
                "gg",
                "gh",
                "gi",
                "gl",
                "gm",
                "gn",
                "gp",
                "gq",
                "gr",
                "gs",
                "gt",
                "gu",
                "gw",
                "gy",
                "hk",
                "hm",
                "hn",
                "hr",
                "ht",
                "hu",
                "id",
                "ie",
                "il",
                "im",
                "in",
                "io",
                "iq",
                "ir",
                "is",
                "it",
                "je",
                "jm",
                "jo",
                "jp",
                "ke",
                "kg",
                "kh",
                "ki",
                "km",
                "kn",
                "kp",
                "kr",
                "kw",
                "ky",
                "kz",
                "la",
                "lb",
                "lc",
                "li",
                "lk",
                "lr",
                "ls",
                "lt",
                "lu",
                "lv",
                "ly",
                "ma",
                "mc",
                "md",
                "me",
                "mf",
                "mg",
                "mh",
                "mk",
                "ml",
                "mm",
                "mn",
                "mo",
                "mp",
                "mq",
                "mr",
                "ms",
                "mt",
                "mu",
                "mv",
                "mw",
                "mx",
                "my",
                "mz",
                "na",
                "nc",
                "ne",
                "nf",
                "ng",
                "ni",
                "nl",
                "no",
                "np",
                "nr",
                "nu",
                "nz",
                "om",
                "pa",
                "pe",
                "pf",
                "pg",
                "ph",
                "pk",
                "pl",
                "pm",
                "pn",
                "pr",
                "ps",
                "pt",
                "pw",
                "py",
                "qa",
                "qz",
                "re",
                "ro",
                "rs",
                "ru",
                "rw",
                "sa",
                "sb",
                "sc",
                "sd",
                "se",
                "sg",
                "sh",
                "si",
                "sj",
                "sk",
                "sl",
                "sm",
                "sn",
                "so",
                "sr",
                "ss",
                "st",
                "sv",
                "sx",
                "sy",
                "sz",
                "tc",
                "td",
                "tf",
                "tg",
                "th",
                "tj",
                "tk",
                "tl",
                "tm",
                "tn",
                "to",
                "tr",
                "tt",
                "tv",
                "tw",
                "tz",
                "ua",
                "ug",
                "um",
                "us",
                "uy",
                "uz",
                "va",
                "vc",
                "ve",
                "vg",
                "vi",
                "vn",
                "vu",
                "wf",
                "ws",
                "xx",
                "ye",
                "yt",
                "za",
                "zm",
                "zw",
            ]
        ]
        """
        The country in which the account holder resides, or in which the business is legally established. This should be an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.
        """
        entity_type: NotRequired[
            Literal["company", "government_entity", "individual", "non_profit"]
        ]
        """
        The entity type.
        """
        individual: NotRequired[
            "AccountService.UpdateParamsIdentityIndividual"
        ]
        """
        Information about the individual represented by the Account. This property is `null` unless `entity_type` is set to `individual`.
        """

    class UpdateParamsIdentityAttestations(TypedDict):
        directorship_declaration: NotRequired[
            "AccountService.UpdateParamsIdentityAttestationsDirectorshipDeclaration"
        ]
        """
        This hash is used to attest that the directors information provided to Stripe is both current and correct.
        """
        ownership_declaration: NotRequired[
            "AccountService.UpdateParamsIdentityAttestationsOwnershipDeclaration"
        ]
        """
        This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
        """
        persons_provided: NotRequired[
            "AccountService.UpdateParamsIdentityAttestationsPersonsProvided"
        ]
        """
        Attestation that all Persons with a specific Relationship value have been provided.
        """
        terms_of_service: NotRequired[
            "AccountService.UpdateParamsIdentityAttestationsTermsOfService"
        ]
        """
        Attestations of accepted terms of service agreements.
        """

    class UpdateParamsIdentityAttestationsDirectorshipDeclaration(TypedDict):
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

    class UpdateParamsIdentityAttestationsOwnershipDeclaration(TypedDict):
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

    class UpdateParamsIdentityAttestationsPersonsProvided(TypedDict):
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

    class UpdateParamsIdentityAttestationsTermsOfService(TypedDict):
        account: NotRequired[
            "AccountService.UpdateParamsIdentityAttestationsTermsOfServiceAccount"
        ]
        """
        Details on the Account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance).
        """

    class UpdateParamsIdentityAttestationsTermsOfServiceAccount(TypedDict):
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

    class UpdateParamsIdentityBusinessDetails(TypedDict):
        address: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsAddress"
            ]
        ]
        """
        The business registration address of the business entity.
        """
        annual_revenue: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsAnnualRevenue"
            ]
        ]
        """
        The business gross annual revenue for its preceding fiscal year.
        """
        documents: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocuments"
            ]
        ]
        """
        A document verifying the business.
        """
        doing_business_as: NotRequired[Optional[str]]
        """
        The name which is used by the business.
        """
        estimated_worker_count: NotRequired[Optional[int]]
        """
        An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
        """
        id_numbers: NotRequired[
            Optional[
                List[
                    "AccountService.UpdateParamsIdentityBusinessDetailsIdNumber"
                ]
            ]
        ]
        """
        The ID numbers of a business entity.
        """
        monthly_estimated_revenue: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue"
            ]
        ]
        """
        An estimate of the monthly revenue of the business.
        """
        phone: NotRequired[Optional[str]]
        """
        The phone number of the Business Entity.
        """
        product_description: NotRequired[Optional[str]]
        """
        Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
        """
        registered_name: NotRequired[Optional[str]]
        """
        The business legal name.
        """
        script_addresses: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptAddresses"
            ]
        ]
        """
        The business registration address of the business entity in non latin script.
        """
        script_names: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptNames"
            ]
        ]
        """
        The business legal name in non latin script.
        """
        structure: NotRequired[
            Optional[
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
        ]
        """
        The category identifying the legal structure of the business.
        """
        url: NotRequired[Optional[str]]
        """
        The business's publicly available website.
        """

    class UpdateParamsIdentityBusinessDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityBusinessDetailsAnnualRevenue(TypedDict):
        amount: NotRequired[AmountParam]
        """
        A non-negative integer representing the amount in the smallest currency unit.
        """
        fiscal_year_end: NotRequired[Optional[str]]
        """
        The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
        """

    class UpdateParamsIdentityBusinessDetailsDocuments(TypedDict):
        bank_account_ownership_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification"
            ]
        ]
        """
        One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
        """
        company_license: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsCompanyLicense"
            ]
        ]
        """
        One or more documents that demonstrate proof of a company's license to operate.
        """
        company_memorandum_of_association: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation"
            ]
        ]
        """
        One or more documents showing the company's Memorandum of Association.
        """
        company_ministerial_decree: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree"
            ]
        ]
        """
        Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
        """
        company_registration_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification"
            ]
        ]
        """
        One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
        """
        company_tax_id_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification"
            ]
        ]
        """
        One or more documents that demonstrate proof of a company's tax ID.
        """
        primary_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerification"
            ]
        ]
        """
        A document verifying the business.
        """
        proof_of_address: NotRequired[
            "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsProofOfAddress"
        ]
        """
        One or more documents that demonstrate proof of address.
        """
        proof_of_registration: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsProofOfRegistration"
            ]
        ]
        """
        One or more documents showing the company's proof of registration with the national business registry.
        """
        proof_of_ultimate_beneficial_ownership: NotRequired[
            "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership"
        ]
        """
        One or more documents that demonstrate proof of ultimate beneficial ownership.
        """

    class UpdateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsCompanyLicense(
        TypedDict
    ):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerification(
        TypedDict,
    ):
        front_back: "AccountService.UpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class UpdateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack(
        TypedDict,
    ):
        back: NotRequired[Optional[str]]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class UpdateParamsIdentityBusinessDetailsDocumentsProofOfAddress(
        TypedDict
    ):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsIdentityBusinessDetailsDocumentsProofOfRegistration(
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

    class UpdateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership(
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

    class UpdateParamsIdentityBusinessDetailsIdNumber(TypedDict):
        registrar: NotRequired[str]
        """
        The registrar of the ID number (Only valid for DE ID number types).
        """
        type: Literal[
            "ae_crn",
            "ae_vat",
            "at_fn",
            "au_abn",
            "au_acn",
            "au_in",
            "be_cbe",
            "bg_uic",
            "br_cnpj",
            "ca_cn",
            "ca_crarr",
            "ca_neq",
            "ca_rid",
            "ch_chid",
            "ch_uid",
            "cy_tic",
            "cz_ico",
            "de_hrn",
            "de_vat",
            "dk_cvr",
            "ee_rk",
            "es_cif",
            "fi_yt",
            "fr_siren",
            "fr_vat",
            "gb_crn",
            "gi_crn",
            "gr_gemi",
            "hk_br",
            "hk_cr",
            "hk_mbs",
            "hu_cjs",
            "ie_crn",
            "it_rea",
            "it_vat",
            "jp_cn",
            "li_uid",
            "lt_ccrn",
            "lu_rcs",
            "lv_urn",
            "mt_crn",
            "mx_rfc",
            "my_brn",
            "my_coid",
            "my_sst",
            "nl_kvk",
            "no_orgnr",
            "nz_bn",
            "pl_regon",
            "pt_vat",
            "ro_cui",
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

    class UpdateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue(
        TypedDict
    ):
        amount: NotRequired[AmountParam]
        """
        A non-negative integer representing the amount in the smallest currency unit.
        """

    class UpdateParamsIdentityBusinessDetailsScriptAddresses(TypedDict):
        kana: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptAddressesKana"
            ]
        ]
        """
        Kana Address.
        """
        kanji: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptAddressesKanji"
            ]
        ]
        """
        Kanji Address.
        """

    class UpdateParamsIdentityBusinessDetailsScriptAddressesKana(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityBusinessDetailsScriptAddressesKanji(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityBusinessDetailsScriptNames(TypedDict):
        kana: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptNamesKana"
            ]
        ]
        """
        Kana name.
        """
        kanji: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityBusinessDetailsScriptNamesKanji"
            ]
        ]
        """
        Kanji name.
        """

    class UpdateParamsIdentityBusinessDetailsScriptNamesKana(TypedDict):
        registered_name: NotRequired[Optional[str]]
        """
        Registered name of the business.
        """

    class UpdateParamsIdentityBusinessDetailsScriptNamesKanji(TypedDict):
        registered_name: NotRequired[Optional[str]]
        """
        Registered name of the business.
        """

    class UpdateParamsIdentityIndividual(TypedDict):
        additional_addresses: NotRequired[
            Optional[
                List[
                    "AccountService.UpdateParamsIdentityIndividualAdditionalAddress"
                ]
            ]
        ]
        """
        Additional addresses associated with the individual.
        """
        additional_names: NotRequired[
            Optional[
                List[
                    "AccountService.UpdateParamsIdentityIndividualAdditionalName"
                ]
            ]
        ]
        """
        Additional names (e.g. aliases) associated with the individual.
        """
        address: NotRequired[
            Optional["AccountService.UpdateParamsIdentityIndividualAddress"]
        ]
        """
        The individual's residential address.
        """
        date_of_birth: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualDateOfBirth"
            ]
        ]
        """
        The individual's date of birth.
        """
        documents: NotRequired[
            Optional["AccountService.UpdateParamsIdentityIndividualDocuments"]
        ]
        """
        Documents that may be submitted to satisfy various informational requests.
        """
        email: NotRequired[Optional[str]]
        """
        The individual's email address.
        """
        given_name: NotRequired[Optional[str]]
        """
        The individual's first name.
        """
        id_numbers: NotRequired[
            Optional[
                List["AccountService.UpdateParamsIdentityIndividualIdNumber"]
            ]
        ]
        """
        The identification numbers (e.g., SSN) associated with the individual.
        """
        legal_gender: NotRequired[Optional[Literal["female", "male"]]]
        """
        The individual's gender (International regulations require either "male" or "female").
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        nationalities: NotRequired[
            List[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        The countries where the individual is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        phone: NotRequired[Optional[str]]
        """
        The individual's phone number.
        """
        political_exposure: NotRequired[Optional[Literal["existing", "none"]]]
        """
        The individual's political exposure.
        """
        relationship: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualRelationship"
            ]
        ]
        """
        The relationship that this individual has with the account's identity.
        """
        script_addresses: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptAddresses"
            ]
        ]
        """
        The script addresses (e.g., non-Latin characters) associated with the individual.
        """
        script_names: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptNames"
            ]
        ]
        """
        The individuals primary name in non latin script.
        """
        surname: NotRequired[Optional[str]]
        """
        The individual's last name.
        """

    class UpdateParamsIdentityIndividualAdditionalAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        purpose: Literal["registered"]
        """
        Purpose of additional address.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityIndividualAdditionalName(TypedDict):
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

    class UpdateParamsIdentityIndividualAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityIndividualDateOfBirth(TypedDict):
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

    class UpdateParamsIdentityIndividualDocuments(TypedDict):
        company_authorization: NotRequired[
            "AccountService.UpdateParamsIdentityIndividualDocumentsCompanyAuthorization"
        ]
        """
        One or more documents that demonstrate proof that this person is authorized to represent the company.
        """
        passport: NotRequired[
            "AccountService.UpdateParamsIdentityIndividualDocumentsPassport"
        ]
        """
        One or more documents showing the person's passport page with photo and personal data.
        """
        primary_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualDocumentsPrimaryVerification"
            ]
        ]
        """
        An identifying document showing the person's name, either a passport or local ID card.
        """
        secondary_verification: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualDocumentsSecondaryVerification"
            ]
        ]
        """
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
        """
        visa: NotRequired[
            "AccountService.UpdateParamsIdentityIndividualDocumentsVisa"
        ]
        """
        One or more documents showing the person's visa required for living in the country where they are residing.
        """

    class UpdateParamsIdentityIndividualDocumentsCompanyAuthorization(
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

    class UpdateParamsIdentityIndividualDocumentsPassport(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsIdentityIndividualDocumentsPrimaryVerification(
        TypedDict
    ):
        front_back: "AccountService.UpdateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class UpdateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack(
        TypedDict,
    ):
        back: NotRequired[Optional[str]]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class UpdateParamsIdentityIndividualDocumentsSecondaryVerification(
        TypedDict,
    ):
        front_back: "AccountService.UpdateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack"
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class UpdateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack(
        TypedDict,
    ):
        back: NotRequired[Optional[str]]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class UpdateParamsIdentityIndividualDocumentsVisa(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsIdentityIndividualIdNumber(TypedDict):
        type: Literal[
            "ae_eid",
            "br_cpf",
            "de_stn",
            "hk_id",
            "mx_rfc",
            "my_nric",
            "nl_bsn",
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

    class UpdateParamsIdentityIndividualRelationship(TypedDict):
        director: NotRequired[Optional[bool]]
        """
        Whether the person is a director of the account's identity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
        """
        executive: NotRequired[Optional[bool]]
        """
        Whether the person has significant responsibility to control, manage, or direct the organization.
        """
        owner: NotRequired[Optional[bool]]
        """
        Whether the person is an owner of the account's identity.
        """
        percent_ownership: NotRequired[Optional[str]]
        """
        The percent owned by the person of the account's legal entity.
        """
        title: NotRequired[Optional[str]]
        """
        The person's title (e.g., CEO, Support Engineer).
        """

    class UpdateParamsIdentityIndividualScriptAddresses(TypedDict):
        kana: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptAddressesKana"
            ]
        ]
        """
        Kana Address.
        """
        kanji: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptAddressesKanji"
            ]
        ]
        """
        Kanji Address.
        """

    class UpdateParamsIdentityIndividualScriptAddressesKana(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityIndividualScriptAddressesKanji(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsIdentityIndividualScriptNames(TypedDict):
        kana: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptNamesKana"
            ]
        ]
        """
        Persons name in kana script.
        """
        kanji: NotRequired[
            Optional[
                "AccountService.UpdateParamsIdentityIndividualScriptNamesKanji"
            ]
        ]
        """
        Persons name in kanji script.
        """

    class UpdateParamsIdentityIndividualScriptNamesKana(TypedDict):
        given_name: NotRequired[Optional[str]]
        """
        The person's first or given name.
        """
        surname: NotRequired[Optional[str]]
        """
        The person's last or family name.
        """

    class UpdateParamsIdentityIndividualScriptNamesKanji(TypedDict):
        given_name: NotRequired[Optional[str]]
        """
        The person's first or given name.
        """
        surname: NotRequired[Optional[str]]
        """
        The person's last or family name.
        """

    def list(
        self,
        params: "AccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Account]:
        """
        Returns a list of Accounts.
        """
        return cast(
            ListObject[Account],
            self._request(
                "get",
                "/v2/core/accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "AccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Account]:
        """
        Returns a list of Accounts.
        """
        return cast(
            ListObject[Account],
            await self._request_async(
                "get",
                "/v2/core/accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "AccountService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        An Account is a representation of a company, individual or other entity that a user interacts with. Accounts contain identifying information about the entity, and configurations that store the features an account has access to. An account can be configured as any or all of the following configurations: Customer, Merchant and/or Recipient.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/core/accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        An Account is a representation of a company, individual or other entity that a user interacts with. Accounts contain identifying information about the entity, and configurations that store the features an account has access to. An account can be configured as any or all of the following configurations: Customer, Merchant and/or Recipient.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/core/accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "AccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Retrieves the details of an Account.
        """
        return cast(
            Account,
            self._request(
                "get",
                "/v2/core/accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "AccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Retrieves the details of an Account.
        """
        return cast(
            Account,
            await self._request_async(
                "get",
                "/v2/core/accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "AccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Updates the details of an Account.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/core/accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "AccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Updates the details of an Account.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/core/accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def close(
        self,
        id: str,
        params: "AccountService.CloseParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Removes access to the Account and its associated resources.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/core/accounts/{id}/close".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def close_async(
        self,
        id: str,
        params: "AccountService.CloseParams" = {},
        options: RequestOptions = {},
    ) -> Account:
        """
        Removes access to the Account and its associated resources.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/core/accounts/{id}/close".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
