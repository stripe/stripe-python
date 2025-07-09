# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class Account(StripeObject):
    """
    A V2 Account is a representation of a company or individual that a Stripe user does business with. Accounts contain the contact details, Legal Entity information, and configuration required to enable the Account for use across Stripe products.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.account"]] = "v2.core.account"

    class Configuration(StripeObject):
        class Customer(StripeObject):
            class AutomaticIndirectTax(StripeObject):
                class Location(StripeObject):
                    country: Optional[
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
                    The identified tax country of the customer.
                    """
                    state: Optional[str]
                    """
                    The identified tax state, county, province, or region of the customer.
                    """

                exempt: Optional[Literal["exempt", "none", "reverse"]]
                """
                Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to reverse, invoice and receipt PDFs include the following text: “Reverse charge”.
                """
                ip_address: Optional[str]
                """
                A recent IP address of the customer used for tax reporting and tax location inference.
                """
                location: Optional[Location]
                """
                The customer's identified tax location - uses `location_source`. Will only be rendered if the `automatic_indirect_tax` feature is requested and `active`.
                """
                location_source: Optional[
                    Literal[
                        "identity_address", "ip_address", "shipping_address"
                    ]
                ]
                """
                The data source used to identify the customer's tax location - defaults to 'identity_address'. Will only be used for automatic tax calculation on the customer's Invoices and Subscriptions.
                """
                _inner_class_types = {"location": Location}

            class Billing(StripeObject):
                class Invoice(StripeObject):
                    class CustomField(StripeObject):
                        name: str
                        """
                        The name of the custom field. This may be up to 40 characters.
                        """
                        value: str
                        """
                        The value of the custom field. This may be up to 140 characters. When updating, pass an empty string to remove previously-defined values.
                        """

                    class Rendering(StripeObject):
                        amount_tax_display: Optional[
                            Literal["exclude_tax", "include_inclusive_tax"]
                        ]
                        """
                        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of exclude_tax or include_inclusive_tax. include_inclusive_tax will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. exclude_tax will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
                        """
                        template: Optional[str]
                        """
                        ID of the invoice rendering template to use for future invoices.
                        """

                    custom_fields: List[CustomField]
                    """
                    The list of up to 4 default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.
                    """
                    footer: Optional[str]
                    """
                    Default footer to be displayed on invoices for this customer.
                    """
                    next_sequence: Optional[int]
                    """
                    The sequence to be used on the customer's next invoice. Defaults to 1.
                    """
                    prefix: Optional[str]
                    """
                    The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
                    """
                    rendering: Optional[Rendering]
                    """
                    Default options for invoice PDF rendering for this customer.
                    """
                    _inner_class_types = {
                        "custom_fields": CustomField,
                        "rendering": Rendering,
                    }

                default_payment_method: Optional[str]
                """
                ID of a payment method that's attached to the customer, to be used as the customer's default payment method for invoices and subscriptions.
                """
                invoice: Optional[Invoice]
                """
                Default settings used on invoices for this customer.
                """
                _inner_class_types = {"invoice": Invoice}

            class Capabilities(StripeObject):
                class AutomaticIndirectTax(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                automatic_indirect_tax: Optional[AutomaticIndirectTax]
                """
                Generates requirements for enabling automatic indirect tax calculation on this customer's invoices or subscriptions. Recommended to request this capability if planning to enable automatic tax calculation on this customer's invoices or subscriptions. Uses the `location_source` field.
                """
                _inner_class_types = {
                    "automatic_indirect_tax": AutomaticIndirectTax,
                }

            class Shipping(StripeObject):
                class Address(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """

                address: Optional[Address]
                """
                Customer shipping address.
                """
                name: Optional[str]
                """
                Customer name.
                """
                phone: Optional[str]
                """
                Customer phone (including extension).
                """
                _inner_class_types = {"address": Address}

            automatic_indirect_tax: Optional[AutomaticIndirectTax]
            """
            Automatic indirect tax settings to be used when automatic tax calculation is enabled on the customer's invoices, subscriptions, checkout sessions, or payment links. Surfaces if automatic tax calculation is possible given the current customer location information.
            """
            billing: Optional[Billing]
            """
            Billing settings - default settings used for this customer in Billing flows such as Invoices and Subscriptions.
            """
            capabilities: Optional[Capabilities]
            """
            Capabilities that have been requested on the Customer Configuration.
            """
            shipping: Optional[Shipping]
            """
            The customer's shipping information. Appears on invoices emailed to this customer.
            """
            test_clock: Optional[str]
            """
            ID of the test clock to attach to the customer. Can only be set on testmode Accounts, and when the Customer Configuration is first set on an Account.
            """
            _inner_class_types = {
                "automatic_indirect_tax": AutomaticIndirectTax,
                "billing": Billing,
                "capabilities": Capabilities,
                "shipping": Shipping,
            }

        class Merchant(StripeObject):
            class BacsDebitPayments(StripeObject):
                display_name: Optional[str]
                """
                Display name for Bacs debit payments.
                """
                service_user_number: Optional[str]
                """
                Service user number for Bacs debit payments.
                """

            class Branding(StripeObject):
                icon: Optional[str]
                """
                ID of a [file upload](https://docs.stripe.com/api/persons/update#create_file): An icon for the merchant. Must be square and at least 128px x 128px.
                """
                logo: Optional[str]
                """
                ID of a [file upload](https://docs.stripe.com/api/persons/update#create_file): A logo for the merchant that will be used in Checkout instead of the icon and without the merchant's name next to it if provided. Must be at least 128px x 128px.
                """
                primary_color: Optional[str]
                """
                A CSS hex color value representing the primary branding color for the merchant.
                """
                secondary_color: Optional[str]
                """
                A CSS hex color value representing the secondary branding color for the merchant.
                """

            class Capabilities(StripeObject):
                class AchDebitPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AcssDebitPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AffirmPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AfterpayClearpayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AlmaPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AmazonPayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class AuBecsDebitPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class BacsDebitPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class BancontactPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class BlikPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class BoletoPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class CardPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class CartesBancairesPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class CashappPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class EpsPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class FpxPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class GbBankTransferPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class GrabpayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class IdealPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class JcbPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class JpBankTransferPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class KakaoPayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class KlarnaPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class KonbiniPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class KrCardPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class LinkPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class MobilepayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class MultibancoPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class MxBankTransferPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class NaverPayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class OxxoPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class P24Payments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class PayByBankPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class PaycoPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class PaynowPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class PromptpayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class RevolutPayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class SamsungPayPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class SepaBankTransferPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class SepaDebitPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class StripeBalance(StripeObject):
                    class Payouts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    payouts: Optional[Payouts]
                    """
                    Allows the account to do payouts using their Stripe Balance (/v1/balance).
                    """
                    _inner_class_types = {"payouts": Payouts}

                class SwishPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class TwintPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class UsBankTransferPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class ZipPayments(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                ach_debit_payments: Optional[AchDebitPayments]
                """
                Allow the merchant to process ACH debit payments.
                """
                acss_debit_payments: Optional[AcssDebitPayments]
                """
                Allow the merchant to process ACSS debit payments.
                """
                affirm_payments: Optional[AffirmPayments]
                """
                Allow the merchant to process Affirm payments.
                """
                afterpay_clearpay_payments: Optional[AfterpayClearpayPayments]
                """
                Allow the merchant to process Afterpay/Clearpay payments.
                """
                alma_payments: Optional[AlmaPayments]
                """
                Allow the merchant to process Alma payments.
                """
                amazon_pay_payments: Optional[AmazonPayPayments]
                """
                Allow the merchant to process Amazon Pay payments.
                """
                au_becs_debit_payments: Optional[AuBecsDebitPayments]
                """
                Allow the merchant to process Australian BECS Direct Debit payments.
                """
                bacs_debit_payments: Optional[BacsDebitPayments]
                """
                Allow the merchant to process BACS Direct Debit payments.
                """
                bancontact_payments: Optional[BancontactPayments]
                """
                Allow the merchant to process Bancontact payments.
                """
                blik_payments: Optional[BlikPayments]
                """
                Allow the merchant to process BLIK payments.
                """
                boleto_payments: Optional[BoletoPayments]
                """
                Allow the merchant to process Boleto payments.
                """
                card_payments: Optional[CardPayments]
                """
                Allow the merchant to collect card payments.
                """
                cartes_bancaires_payments: Optional[CartesBancairesPayments]
                """
                Allow the merchant to process Cartes Bancaires payments.
                """
                cashapp_payments: Optional[CashappPayments]
                """
                Allow the merchant to process Cash App payments.
                """
                eps_payments: Optional[EpsPayments]
                """
                Allow the merchant to process EPS payments.
                """
                fpx_payments: Optional[FpxPayments]
                """
                Allow the merchant to process FPX payments.
                """
                gb_bank_transfer_payments: Optional[GbBankTransferPayments]
                """
                Allow the merchant to process UK bank transfer payments.
                """
                grabpay_payments: Optional[GrabpayPayments]
                """
                Allow the merchant to process GrabPay payments.
                """
                ideal_payments: Optional[IdealPayments]
                """
                Allow the merchant to process iDEAL payments.
                """
                jcb_payments: Optional[JcbPayments]
                """
                Allow the merchant to process JCB card payments.
                """
                jp_bank_transfer_payments: Optional[JpBankTransferPayments]
                """
                Allow the merchant to process Japanese bank transfer payments.
                """
                kakao_pay_payments: Optional[KakaoPayPayments]
                """
                Allow the merchant to process Kakao Pay payments.
                """
                klarna_payments: Optional[KlarnaPayments]
                """
                Allow the merchant to process Klarna payments.
                """
                konbini_payments: Optional[KonbiniPayments]
                """
                Allow the merchant to process Konbini convenience store payments.
                """
                kr_card_payments: Optional[KrCardPayments]
                """
                Allow the merchant to process Korean card payments.
                """
                link_payments: Optional[LinkPayments]
                """
                Allow the merchant to process Link payments.
                """
                mobilepay_payments: Optional[MobilepayPayments]
                """
                Allow the merchant to process MobilePay payments.
                """
                multibanco_payments: Optional[MultibancoPayments]
                """
                Allow the merchant to process Multibanco payments.
                """
                mx_bank_transfer_payments: Optional[MxBankTransferPayments]
                """
                Allow the merchant to process Mexican bank transfer payments.
                """
                naver_pay_payments: Optional[NaverPayPayments]
                """
                Allow the merchant to process Naver Pay payments.
                """
                oxxo_payments: Optional[OxxoPayments]
                """
                Allow the merchant to process OXXO payments.
                """
                p24_payments: Optional[P24Payments]
                """
                Allow the merchant to process Przelewy24 (P24) payments.
                """
                pay_by_bank_payments: Optional[PayByBankPayments]
                """
                Allow the merchant to process Pay by Bank payments.
                """
                payco_payments: Optional[PaycoPayments]
                """
                Allow the merchant to process PAYCO payments.
                """
                paynow_payments: Optional[PaynowPayments]
                """
                Allow the merchant to process PayNow payments.
                """
                promptpay_payments: Optional[PromptpayPayments]
                """
                Allow the merchant to process PromptPay payments.
                """
                revolut_pay_payments: Optional[RevolutPayPayments]
                """
                Allow the merchant to process Revolut Pay payments.
                """
                samsung_pay_payments: Optional[SamsungPayPayments]
                """
                Allow the merchant to process Samsung Pay payments.
                """
                sepa_bank_transfer_payments: Optional[SepaBankTransferPayments]
                """
                Allow the merchant to process SEPA bank transfer payments.
                """
                sepa_debit_payments: Optional[SepaDebitPayments]
                """
                Allow the merchant to process SEPA Direct Debit payments.
                """
                stripe_balance: Optional[StripeBalance]
                """
                Capabilities that enable the merchant to manage their Stripe Balance (/v1/balance).
                """
                swish_payments: Optional[SwishPayments]
                """
                Allow the merchant to process Swish payments.
                """
                twint_payments: Optional[TwintPayments]
                """
                Allow the merchant to process TWINT payments.
                """
                us_bank_transfer_payments: Optional[UsBankTransferPayments]
                """
                Allow the merchant to process US bank transfer payments.
                """
                zip_payments: Optional[ZipPayments]
                """
                Allow the merchant to process Zip payments.
                """
                _inner_class_types = {
                    "ach_debit_payments": AchDebitPayments,
                    "acss_debit_payments": AcssDebitPayments,
                    "affirm_payments": AffirmPayments,
                    "afterpay_clearpay_payments": AfterpayClearpayPayments,
                    "alma_payments": AlmaPayments,
                    "amazon_pay_payments": AmazonPayPayments,
                    "au_becs_debit_payments": AuBecsDebitPayments,
                    "bacs_debit_payments": BacsDebitPayments,
                    "bancontact_payments": BancontactPayments,
                    "blik_payments": BlikPayments,
                    "boleto_payments": BoletoPayments,
                    "card_payments": CardPayments,
                    "cartes_bancaires_payments": CartesBancairesPayments,
                    "cashapp_payments": CashappPayments,
                    "eps_payments": EpsPayments,
                    "fpx_payments": FpxPayments,
                    "gb_bank_transfer_payments": GbBankTransferPayments,
                    "grabpay_payments": GrabpayPayments,
                    "ideal_payments": IdealPayments,
                    "jcb_payments": JcbPayments,
                    "jp_bank_transfer_payments": JpBankTransferPayments,
                    "kakao_pay_payments": KakaoPayPayments,
                    "klarna_payments": KlarnaPayments,
                    "konbini_payments": KonbiniPayments,
                    "kr_card_payments": KrCardPayments,
                    "link_payments": LinkPayments,
                    "mobilepay_payments": MobilepayPayments,
                    "multibanco_payments": MultibancoPayments,
                    "mx_bank_transfer_payments": MxBankTransferPayments,
                    "naver_pay_payments": NaverPayPayments,
                    "oxxo_payments": OxxoPayments,
                    "p24_payments": P24Payments,
                    "pay_by_bank_payments": PayByBankPayments,
                    "payco_payments": PaycoPayments,
                    "paynow_payments": PaynowPayments,
                    "promptpay_payments": PromptpayPayments,
                    "revolut_pay_payments": RevolutPayPayments,
                    "samsung_pay_payments": SamsungPayPayments,
                    "sepa_bank_transfer_payments": SepaBankTransferPayments,
                    "sepa_debit_payments": SepaDebitPayments,
                    "stripe_balance": StripeBalance,
                    "swish_payments": SwishPayments,
                    "twint_payments": TwintPayments,
                    "us_bank_transfer_payments": UsBankTransferPayments,
                    "zip_payments": ZipPayments,
                }

            class CardPayments(StripeObject):
                class DeclineOn(StripeObject):
                    avs_failure: Optional[bool]
                    """
                    Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
                    """
                    cvc_failure: Optional[bool]
                    """
                    Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
                    """

                decline_on: Optional[DeclineOn]
                """
                Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
                """
                _inner_class_types = {"decline_on": DeclineOn}

            class SepaDebitPayments(StripeObject):
                creditor_id: Optional[str]
                """
                Creditor ID for SEPA debit payments.
                """

            class StatementDescriptor(StripeObject):
                descriptor: Optional[str]
                """
                The default text that appears on statements for non-card charges outside of Japan. For card charges, if you don't set a statement_descriptor_prefix, this text is also used as the statement descriptor prefix. In that case, if concatenating the statement descriptor suffix causes the combined statement descriptor to exceed 22 characters, we truncate the statement_descriptor text to limit the full descriptor to 22 characters. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
                """
                prefix: Optional[str]
                """
                Default text that appears on statements for card charges outside of Japan, prefixing any dynamic statement_descriptor_suffix specified on the charge. To maximize space for the dynamic part of the descriptor, keep this text short. If you don't specify this value, statement_descriptor is used as the prefix. For more information about statement descriptors and their requirements, see the Merchant Configuration settings documentation.
                """

            class Support(StripeObject):
                class Address(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """
                    town: Optional[str]
                    """
                    Town or cho-me.
                    """

                address: Optional[Address]
                """
                A publicly available mailing address for sending support issues to.
                """
                email: Optional[str]
                """
                A publicly available email address for sending support issues to.
                """
                phone: Optional[str]
                """
                A publicly available phone number to call with support issues.
                """
                url: Optional[str]
                """
                A publicly available website for handling support issues.
                """
                _inner_class_types = {"address": Address}

            bacs_debit_payments: Optional[BacsDebitPayments]
            """
            Settings used for Bacs debit payments.
            """
            branding: Optional[Branding]
            """
            Settings used to apply the merchant's branding to email receipts, invoices, Checkout, and other products.
            """
            capabilities: Optional[Capabilities]
            """
            Capabilities that have been requested on the Merchant Configuration.
            """
            card_payments: Optional[CardPayments]
            """
            Card payments settings.
            """
            mcc: Optional[str]
            """
            The merchant category code for the merchant. MCCs are used to classify businesses based on the goods or services they provide.
            """
            sepa_debit_payments: Optional[SepaDebitPayments]
            """
            Settings used for SEPA debit payments.
            """
            statement_descriptor: Optional[StatementDescriptor]
            """
            Statement descriptor.
            """
            support: Optional[Support]
            """
            Publicly available contact information for sending support issues to.
            """
            _inner_class_types = {
                "bacs_debit_payments": BacsDebitPayments,
                "branding": Branding,
                "capabilities": Capabilities,
                "card_payments": CardPayments,
                "sepa_debit_payments": SepaDebitPayments,
                "statement_descriptor": StatementDescriptor,
                "support": Support,
            }

        class Recipient(StripeObject):
            class Capabilities(StripeObject):
                class BankAccounts(StripeObject):
                    class Local(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class Wire(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    local: Optional[Local]
                    """
                    Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
                    """
                    wire: Optional[Wire]
                    """
                    Enables this Account to receive OutboundPayments to linked bank accounts over wire.
                    """
                    _inner_class_types = {"local": Local, "wire": Wire}

                class Cards(StripeObject):
                    class StatusDetail(StripeObject):
                        code: Literal[
                            "determining_status",
                            "requirements_past_due",
                            "requirements_pending_verification",
                            "restricted_other",
                            "unsupported_business",
                            "unsupported_country",
                            "unsupported_entity_type",
                        ]
                        """
                        Machine-readable code explaining the reason for the Capability to be in its current status.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Machine-readable code explaining how to make the Capability active.
                        """

                    requested: bool
                    """
                    Whether the Capability has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    The status of the Capability.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                class StripeBalance(StripeObject):
                    class Payouts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class StripeTransfers(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    payouts: Optional[Payouts]
                    """
                    Allows the account to do payouts using their Stripe Balance (/v1/balance).
                    """
                    stripe_transfers: Optional[StripeTransfers]
                    """
                    Allows the account to receive /v1/transfers into their Stripe Balance (/v1/balance).
                    """
                    _inner_class_types = {
                        "payouts": Payouts,
                        "stripe_transfers": StripeTransfers,
                    }

                bank_accounts: Optional[BankAccounts]
                """
                Capabilities that enable OutboundPayments to a bank account linked to this Account.
                """
                cards: Optional[Cards]
                """
                Capability that enable OutboundPayments to a debit card linked to this Account.
                """
                stripe_balance: Optional[StripeBalance]
                """
                Capabilities that enable the recipient to manage their Stripe Balance (/v1/balance).
                """
                _inner_class_types = {
                    "bank_accounts": BankAccounts,
                    "cards": Cards,
                    "stripe_balance": StripeBalance,
                }

            class DefaultOutboundDestination(StripeObject):
                id: str
                """
                The payout method ID of the default outbound destination.
                """
                type: Literal[
                    "at_bank_account",
                    "au_bank_account",
                    "ba_bank_account",
                    "be_bank_account",
                    "bg_bank_account",
                    "bj_bank_account",
                    "bs_bank_account",
                    "card",
                    "ca_bank_account",
                    "ch_bank_account",
                    "ci_bank_account",
                    "cy_bank_account",
                    "cz_bank_account",
                    "de_bank_account",
                    "dk_bank_account",
                    "ec_bank_account",
                    "ee_bank_account",
                    "es_bank_account",
                    "et_bank_account",
                    "fi_bank_account",
                    "fr_bank_account",
                    "gb_bank_account",
                    "gr_bank_account",
                    "hr_bank_account",
                    "hu_bank_account",
                    "id_bank_account",
                    "ie_bank_account",
                    "il_bank_account",
                    "in_bank_account",
                    "is_bank_account",
                    "it_bank_account",
                    "ke_bank_account",
                    "li_bank_account",
                    "lt_bank_account",
                    "lu_bank_account",
                    "lv_bank_account",
                    "mn_bank_account",
                    "mt_bank_account",
                    "mu_bank_account",
                    "mx_bank_account",
                    "na_bank_account",
                    "nl_bank_account",
                    "no_bank_account",
                    "nz_bank_account",
                    "pa_bank_account",
                    "ph_bank_account",
                    "pl_bank_account",
                    "pt_bank_account",
                    "ro_bank_account",
                    "rs_bank_account",
                    "se_bank_account",
                    "sg_bank_account",
                    "si_bank_account",
                    "sk_bank_account",
                    "sn_bank_account",
                    "sv_bank_account",
                    "tn_bank_account",
                    "tr_bank_account",
                    "us_bank_account",
                    "za_bank_account",
                ]
                """
                Closed Enum. The payout method type of the default outbound destination.
                """

            capabilities: Optional[Capabilities]
            """
            Capabilities that have been requested on the Recipient Configuration.
            """
            default_outbound_destination: Optional[DefaultOutboundDestination]
            """
            The payout method to be used as a default outbound destination. This will allow the PayoutMethod to be omitted on OutboundPayments made through the dashboard.
            """
            _inner_class_types = {
                "capabilities": Capabilities,
                "default_outbound_destination": DefaultOutboundDestination,
            }

        class Storer(StripeObject):
            class Capabilities(StripeObject):
                class FinancialAddresses(StripeObject):
                    class BankAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    bank_accounts: Optional[BankAccounts]
                    """
                    Can provision a bank-account like financial address (VBAN) to credit/debit a FinancialAccount.
                    """
                    _inner_class_types = {"bank_accounts": BankAccounts}

                class HoldsCurrencies(StripeObject):
                    class Gbp(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    gbp: Optional[Gbp]
                    """
                    Can hold storage-type funds on Stripe in GBP.
                    """
                    _inner_class_types = {"gbp": Gbp}

                class InboundTransfers(StripeObject):
                    class BankAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    bank_accounts: Optional[BankAccounts]
                    """
                    Can pull funds from an external bank account, owned by yourself, to a FinancialAccount.
                    """
                    _inner_class_types = {"bank_accounts": BankAccounts}

                class OutboundPayments(StripeObject):
                    class BankAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class Cards(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class FinancialAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    bank_accounts: Optional[BankAccounts]
                    """
                    Can send funds from a FinancialAccount to a bank account, owned by someone else.
                    """
                    cards: Optional[Cards]
                    """
                    Can send funds from a FinancialAccount to a debit card, owned by someone else.
                    """
                    financial_accounts: Optional[FinancialAccounts]
                    """
                    Can send funds from a FinancialAccount to another FinancialAccount, owned by someone else.
                    """
                    _inner_class_types = {
                        "bank_accounts": BankAccounts,
                        "cards": Cards,
                        "financial_accounts": FinancialAccounts,
                    }

                class OutboundTransfers(StripeObject):
                    class BankAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class FinancialAccounts(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_business",
                                "unsupported_country",
                                "unsupported_entity_type",
                            ]
                            """
                            Machine-readable code explaining the reason for the Capability to be in its current status.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Machine-readable code explaining how to make the Capability active.
                            """

                        requested: bool
                        """
                        Whether the Capability has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        The status of the Capability.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Capability. `status_details` will be empty if the Capability's status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    bank_accounts: Optional[BankAccounts]
                    """
                    Can send funds from a FinancialAccount, to a bank account, owned by yourself.
                    """
                    financial_accounts: Optional[FinancialAccounts]
                    """
                    Can send funds from a FinancialAccount to another FinancialAccount, owned by yourself.
                    """
                    _inner_class_types = {
                        "bank_accounts": BankAccounts,
                        "financial_accounts": FinancialAccounts,
                    }

                financial_addresses: Optional[FinancialAddresses]
                """
                Can provision a financial address to credit/debit a FinancialAccount.
                """
                holds_currencies: Optional[HoldsCurrencies]
                """
                Can hold storage-type funds on Stripe.
                """
                inbound_transfers: Optional[InboundTransfers]
                """
                Can pull funds from an external source, owned by yourself, to a FinancialAccount.
                """
                outbound_payments: Optional[OutboundPayments]
                """
                Can send funds from a FinancialAccount to a destination owned by someone else.
                """
                outbound_transfers: Optional[OutboundTransfers]
                """
                Can send funds from a FinancialAccount to a destination owned by yourself.
                """
                _inner_class_types = {
                    "financial_addresses": FinancialAddresses,
                    "holds_currencies": HoldsCurrencies,
                    "inbound_transfers": InboundTransfers,
                    "outbound_payments": OutboundPayments,
                    "outbound_transfers": OutboundTransfers,
                }

            capabilities: Optional[Capabilities]
            """
            Capabilities that have been requested on the Storer Configuration.
            """
            _inner_class_types = {"capabilities": Capabilities}

        customer: Optional[Customer]
        """
        The Customer Configuration allows the Account to be used in inbound payment flows.
        """
        merchant: Optional[Merchant]
        """
        The Merchant configuration allows the Account to act as a connected account and collect payments facilitated by a Connect platform. You can add this configuration to your connected accounts only if you've completed onboarding as a Connect platform.
        """
        recipient: Optional[Recipient]
        """
        The Recipient Configuration allows the Account to receive funds.
        """
        storer: Optional[Storer]
        """
        The Storer Configuration allows the Account to store and move funds using stored-value FinancialAccounts.
        """
        _inner_class_types = {
            "customer": Customer,
            "merchant": Merchant,
            "recipient": Recipient,
            "storer": Storer,
        }

    class Defaults(StripeObject):
        class Responsibilities(StripeObject):
            fees_collector: Literal["application", "stripe"]
            """
            A value indicating the responsible payer of a bundle of Stripe fees for pricing-control eligible products on this Account.
            """
            losses_collector: Literal["application", "stripe"]
            """
            A value indicating who is responsible for losses when this Account can't pay back negative balances from payments.
            """

        currency: Optional[
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
        locales: Optional[
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
        responsibilities: Optional[Responsibilities]
        """
        Default responsibilities held by either Stripe or the platform.
        """
        _inner_class_types = {"responsibilities": Responsibilities}

    class Identity(StripeObject):
        class Attestations(StripeObject):
            class DirectorshipDeclaration(StripeObject):
                date: Optional[str]
                """
                The time marking when the director attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
                """
                ip: Optional[str]
                """
                The IP address from which the director attestation was made.
                """
                user_agent: Optional[str]
                """
                The user agent of the browser from which the director attestation was made.
                """

            class OwnershipDeclaration(StripeObject):
                date: Optional[str]
                """
                The time marking when the beneficial owner attestation was made. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
                """
                ip: Optional[str]
                """
                The IP address from which the beneficial owner attestation was made.
                """
                user_agent: Optional[str]
                """
                The user agent of the browser from which the beneficial owner attestation was made.
                """

            class PersonsProvided(StripeObject):
                directors: Optional[bool]
                """
                Whether the company's directors have been provided. Set this Boolean to true after creating all the company's directors with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
                """
                executives: Optional[bool]
                """
                Whether the company's executives have been provided. Set this Boolean to true after creating all the company's executives with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
                """
                owners: Optional[bool]
                """
                Whether the company's owners have been provided. Set this Boolean to true after creating all the company's owners with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
                """
                ownership_exemption_reason: Optional[
                    Literal[
                        "qualified_entity_exceeds_ownership_threshold",
                        "qualifies_as_financial_institution",
                    ]
                ]
                """
                Reason for why the company is exempt from providing ownership information.
                """

            class TermsOfService(StripeObject):
                class Account(StripeObject):
                    date: Optional[str]
                    """
                    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
                    """
                    ip: Optional[str]
                    """
                    The IP address from which the Account's representative accepted the terms of service.
                    """
                    user_agent: Optional[str]
                    """
                    The user agent of the browser from which the Account's representative accepted the terms of service.
                    """

                account: Optional[Account]
                """
                Details on the Account's acceptance of the [Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance).
                """
                _inner_class_types = {"account": Account}

            directorship_declaration: Optional[DirectorshipDeclaration]
            """
            This hash is used to attest that the directors information provided to Stripe is both current and correct.
            """
            ownership_declaration: Optional[OwnershipDeclaration]
            """
            This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
            """
            persons_provided: Optional[PersonsProvided]
            """
            Attestation that all Persons with a specific Relationship value have been provided.
            """
            terms_of_service: Optional[TermsOfService]
            """
            Attestations of accepted terms of service agreements.
            """
            _inner_class_types = {
                "directorship_declaration": DirectorshipDeclaration,
                "ownership_declaration": OwnershipDeclaration,
                "persons_provided": PersonsProvided,
                "terms_of_service": TermsOfService,
            }

        class BusinessDetails(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[
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
                line1: Optional[str]
                """
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """
                town: Optional[str]
                """
                Town or cho-me.
                """

            class AnnualRevenue(StripeObject):
                amount: Optional[Amount]
                """
                A non-negative integer representing the amount in the smallest currency unit.
                """
                fiscal_year_end: Optional[str]
                """
                The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
                """

            class Documents(StripeObject):
                class BankAccountOwnershipVerification(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class CompanyLicense(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class CompanyMemorandumOfAssociation(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class CompanyMinisterialDecree(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class CompanyRegistrationVerification(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class CompanyTaxIdVerification(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class PrimaryVerification(StripeObject):
                    class FrontBack(StripeObject):
                        back: Optional[str]
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """
                        front: str
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """

                    front_back: FrontBack
                    """
                    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens for the front and back of the verification document.
                    """
                    type: Literal["front_back"]
                    """
                    The format of the verification document. Currently supports `front_back` only.
                    """
                    _inner_class_types = {"front_back": FrontBack}

                class ProofOfAddress(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class ProofOfRegistration(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class ProofOfUltimateBeneficialOwnership(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                bank_account_ownership_verification: Optional[
                    BankAccountOwnershipVerification
                ]
                """
                One or more documents that support the Bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
                """
                company_license: Optional[CompanyLicense]
                """
                One or more documents that demonstrate proof of a company's license to operate.
                """
                company_memorandum_of_association: Optional[
                    CompanyMemorandumOfAssociation
                ]
                """
                One or more documents showing the company's Memorandum of Association.
                """
                company_ministerial_decree: Optional[CompanyMinisterialDecree]
                """
                Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
                """
                company_registration_verification: Optional[
                    CompanyRegistrationVerification
                ]
                """
                One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
                """
                company_tax_id_verification: Optional[CompanyTaxIdVerification]
                """
                One or more documents that demonstrate proof of a company's tax ID.
                """
                primary_verification: Optional[PrimaryVerification]
                """
                A document verifying the business.
                """
                proof_of_address: Optional[ProofOfAddress]
                """
                One or more documents that demonstrate proof of address.
                """
                proof_of_registration: Optional[ProofOfRegistration]
                """
                One or more documents showing the company's proof of registration with the national business registry.
                """
                proof_of_ultimate_beneficial_ownership: Optional[
                    ProofOfUltimateBeneficialOwnership
                ]
                """
                One or more documents that demonstrate proof of ultimate beneficial ownership.
                """
                _inner_class_types = {
                    "bank_account_ownership_verification": BankAccountOwnershipVerification,
                    "company_license": CompanyLicense,
                    "company_memorandum_of_association": CompanyMemorandumOfAssociation,
                    "company_ministerial_decree": CompanyMinisterialDecree,
                    "company_registration_verification": CompanyRegistrationVerification,
                    "company_tax_id_verification": CompanyTaxIdVerification,
                    "primary_verification": PrimaryVerification,
                    "proof_of_address": ProofOfAddress,
                    "proof_of_registration": ProofOfRegistration,
                    "proof_of_ultimate_beneficial_ownership": ProofOfUltimateBeneficialOwnership,
                }

            class IdNumber(StripeObject):
                registrar: Optional[str]
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

            class MonthlyEstimatedRevenue(StripeObject):
                amount: Optional[Amount]
                """
                A non-negative integer representing the amount in the smallest currency unit.
                """

            class ScriptAddresses(StripeObject):
                class Kana(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """
                    town: Optional[str]
                    """
                    Town or cho-me.
                    """

                class Kanji(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """
                    town: Optional[str]
                    """
                    Town or cho-me.
                    """

                kana: Optional[Kana]
                """
                Kana Address.
                """
                kanji: Optional[Kanji]
                """
                Kanji Address.
                """
                _inner_class_types = {"kana": Kana, "kanji": Kanji}

            class ScriptNames(StripeObject):
                class Kana(StripeObject):
                    registered_name: Optional[str]
                    """
                    Registered name of the business.
                    """

                class Kanji(StripeObject):
                    registered_name: Optional[str]
                    """
                    Registered name of the business.
                    """

                kana: Optional[Kana]
                """
                Kana name.
                """
                kanji: Optional[Kanji]
                """
                Kanji name.
                """
                _inner_class_types = {"kana": Kana, "kanji": Kanji}

            address: Optional[Address]
            """
            The company's primary address.
            """
            annual_revenue: Optional[AnnualRevenue]
            """
            The business gross annual revenue for its preceding fiscal year.
            """
            documents: Optional[Documents]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            doing_business_as: Optional[str]
            """
            The company's legal name.
            """
            estimated_worker_count: Optional[int]
            """
            An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
            """
            id_numbers: Optional[List[IdNumber]]
            """
            The provided ID numbers of a business entity.
            """
            monthly_estimated_revenue: Optional[MonthlyEstimatedRevenue]
            """
            An estimate of the monthly revenue of the business.
            """
            phone: Optional[str]
            """
            The company's phone number (used for verification).
            """
            product_description: Optional[str]
            """
            Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
            """
            registered_name: Optional[str]
            """
            The business legal name.
            """
            script_addresses: Optional[ScriptAddresses]
            """
            The business registration address of the business entity in non latin script.
            """
            script_names: Optional[ScriptNames]
            """
            The business legal name in non latin script.
            """
            structure: Optional[
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
            url: Optional[str]
            """
            The business's publicly available website.
            """
            _inner_class_types = {
                "address": Address,
                "annual_revenue": AnnualRevenue,
                "documents": Documents,
                "id_numbers": IdNumber,
                "monthly_estimated_revenue": MonthlyEstimatedRevenue,
                "script_addresses": ScriptAddresses,
                "script_names": ScriptNames,
            }

        class Individual(StripeObject):
            class AdditionalAddress(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[
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
                line1: Optional[str]
                """
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                purpose: Literal["registered"]
                """
                Purpose of additional address.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """
                town: Optional[str]
                """
                Town or cho-me.
                """

            class AdditionalName(StripeObject):
                full_name: Optional[str]
                """
                The individual's full name.
                """
                given_name: Optional[str]
                """
                The individual's first or given name.
                """
                purpose: Literal["alias", "maiden"]
                """
                The purpose or type of the additional name.
                """
                surname: Optional[str]
                """
                The individual's last or family name.
                """

            class AdditionalTermsOfService(StripeObject):
                class Account(StripeObject):
                    date: Optional[str]
                    """
                    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
                    """
                    ip: Optional[str]
                    """
                    The IP address from which the Account's representative accepted the terms of service.
                    """
                    user_agent: Optional[str]
                    """
                    The user agent of the browser from which the Account's representative accepted the terms of service.
                    """

                account: Optional[Account]
                """
                Stripe terms of service agreement.
                """
                _inner_class_types = {"account": Account}

            class Address(StripeObject):
                city: Optional[str]
                """
                City, district, suburb, town, or village.
                """
                country: Optional[
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
                line1: Optional[str]
                """
                Address line 1 (e.g., street, PO Box, or company name).
                """
                line2: Optional[str]
                """
                Address line 2 (e.g., apartment, suite, unit, or building).
                """
                postal_code: Optional[str]
                """
                ZIP or postal code.
                """
                state: Optional[str]
                """
                State, county, province, or region.
                """
                town: Optional[str]
                """
                Town or cho-me.
                """

            class DateOfBirth(StripeObject):
                day: int
                """
                The day of birth, between 1 and 31.
                """
                month: int
                """
                The month of birth, between 1 and 12.
                """
                year: int
                """
                The four-digit year of birth.
                """

            class Documents(StripeObject):
                class CompanyAuthorization(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class Passport(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                class PrimaryVerification(StripeObject):
                    class FrontBack(StripeObject):
                        back: Optional[str]
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """
                        front: str
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """

                    front_back: FrontBack
                    """
                    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens for the front and back of the verification document.
                    """
                    type: Literal["front_back"]
                    """
                    The format of the verification document. Currently supports `front_back` only.
                    """
                    _inner_class_types = {"front_back": FrontBack}

                class SecondaryVerification(StripeObject):
                    class FrontBack(StripeObject):
                        back: Optional[str]
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """
                        front: str
                        """
                        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                        """

                    front_back: FrontBack
                    """
                    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens for the front and back of the verification document.
                    """
                    type: Literal["front_back"]
                    """
                    The format of the verification document. Currently supports `front_back` only.
                    """
                    _inner_class_types = {"front_back": FrontBack}

                class Visa(StripeObject):
                    files: List[str]
                    """
                    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
                    """
                    type: Literal["files"]
                    """
                    The format of the document. Currently supports `files` only.
                    """

                company_authorization: Optional[CompanyAuthorization]
                """
                One or more documents that demonstrate proof that this person is authorized to represent the company.
                """
                passport: Optional[Passport]
                """
                One or more documents showing the person's passport page with photo and personal data.
                """
                primary_verification: Optional[PrimaryVerification]
                """
                An identifying document showing the person's name, either a passport or local ID card.
                """
                secondary_verification: Optional[SecondaryVerification]
                """
                A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
                """
                visa: Optional[Visa]
                """
                One or more documents showing the person's visa required for living in the country where they are residing.
                """
                _inner_class_types = {
                    "company_authorization": CompanyAuthorization,
                    "passport": Passport,
                    "primary_verification": PrimaryVerification,
                    "secondary_verification": SecondaryVerification,
                    "visa": Visa,
                }

            class IdNumber(StripeObject):
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

            class Relationship(StripeObject):
                authorizer: Optional[bool]
                """
                Whether the individual is an authorizer of the Account's legal entity.
                """
                director: Optional[bool]
                """
                Whether the individual is a director of the Account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
                """
                executive: Optional[bool]
                """
                Whether the individual has significant responsibility to control, manage, or direct the organization.
                """
                legal_guardian: Optional[bool]
                """
                Whether the individual is the legal guardian of the Account's representative.
                """
                owner: Optional[bool]
                """
                Whether the individual is an owner of the Account's legal entity.
                """
                percent_ownership: Optional[str]
                """
                The percent owned by the individual of the Account's legal entity.
                """
                representative: Optional[bool]
                """
                Whether the individual is authorized as the primary representative of the Account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
                """
                title: Optional[str]
                """
                The individual's title (e.g., CEO, Support Engineer).
                """

            class ScriptAddresses(StripeObject):
                class Kana(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """
                    town: Optional[str]
                    """
                    Town or cho-me.
                    """

                class Kanji(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: Optional[
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
                    line1: Optional[str]
                    """
                    Address line 1 (e.g., street, PO Box, or company name).
                    """
                    line2: Optional[str]
                    """
                    Address line 2 (e.g., apartment, suite, unit, or building).
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """
                    town: Optional[str]
                    """
                    Town or cho-me.
                    """

                kana: Optional[Kana]
                """
                Kana Address.
                """
                kanji: Optional[Kanji]
                """
                Kanji Address.
                """
                _inner_class_types = {"kana": Kana, "kanji": Kanji}

            class ScriptNames(StripeObject):
                class Kana(StripeObject):
                    given_name: Optional[str]
                    """
                    The person's first or given name.
                    """
                    surname: Optional[str]
                    """
                    The person's last or family name.
                    """

                class Kanji(StripeObject):
                    given_name: Optional[str]
                    """
                    The person's first or given name.
                    """
                    surname: Optional[str]
                    """
                    The person's last or family name.
                    """

                kana: Optional[Kana]
                """
                Persons name in kana script.
                """
                kanji: Optional[Kanji]
                """
                Persons name in kanji script.
                """
                _inner_class_types = {"kana": Kana, "kanji": Kanji}

            account: str
            """
            The account ID which the individual belongs to.
            """
            additional_addresses: Optional[List[AdditionalAddress]]
            """
            Additional addresses associated with the individual.
            """
            additional_names: Optional[List[AdditionalName]]
            """
            Additional names (e.g. aliases) associated with the individual.
            """
            additional_terms_of_service: Optional[AdditionalTermsOfService]
            """
            Terms of service acceptances.
            """
            address: Optional[Address]
            """
            The individual's residential address.
            """
            created: str
            """
            Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
            """
            date_of_birth: Optional[DateOfBirth]
            """
            The individual's date of birth.
            """
            documents: Optional[Documents]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            email: Optional[str]
            """
            The individual's email address.
            """
            given_name: Optional[str]
            """
            The individual's first name.
            """
            id: str
            """
            Unique identifier for the object.
            """
            id_numbers: Optional[List[IdNumber]]
            """
            The identification numbers (e.g., SSN) associated with the individual.
            """
            legal_gender: Optional[Literal["female", "male"]]
            """
            The individual's gender (International regulations require either "male” or "female").
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            nationalities: Optional[
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
            object: str
            """
            String representing the object's type. Objects of the same type share the same value.
            """
            phone: Optional[str]
            """
            The individual's phone number.
            """
            political_exposure: Optional[Literal["existing", "none"]]
            """
            Indicates if the individual or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
            """
            relationship: Optional[Relationship]
            """
            The relationship that this individual has with the Account's identity.
            """
            script_addresses: Optional[ScriptAddresses]
            """
            The script addresses (e.g., non-Latin characters) associated with the individual.
            """
            script_names: Optional[ScriptNames]
            """
            The script names (e.g. non-Latin characters) associated with the individual.
            """
            surname: Optional[str]
            """
            The individual's last name.
            """
            updated: str
            """
            Time at which the object was last updated.
            """
            _inner_class_types = {
                "additional_addresses": AdditionalAddress,
                "additional_names": AdditionalName,
                "additional_terms_of_service": AdditionalTermsOfService,
                "address": Address,
                "date_of_birth": DateOfBirth,
                "documents": Documents,
                "id_numbers": IdNumber,
                "relationship": Relationship,
                "script_addresses": ScriptAddresses,
                "script_names": ScriptNames,
            }

        attestations: Optional[Attestations]
        """
        Attestations from the identity's key people, e.g. owners, executives, directors.
        """
        business_details: Optional[BusinessDetails]
        """
        Information about the company or business.
        """
        country: Optional[
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
        entity_type: Optional[
            Literal["company", "government_entity", "individual", "non_profit"]
        ]
        """
        The entity type.
        """
        individual: Optional[Individual]
        """
        Information about the individual represented by the Account. This property is `null` unless `entity_type` is set to `individual`.
        """
        _inner_class_types = {
            "attestations": Attestations,
            "business_details": BusinessDetails,
            "individual": Individual,
        }

    class Requirements(StripeObject):
        class Entry(StripeObject):
            class Error(StripeObject):
                code: Literal[
                    "invalid_address_city_state_postal_code",
                    "invalid_address_highway_contract_box",
                    "invalid_address_private_mailbox",
                    "invalid_business_profile_name",
                    "invalid_business_profile_name_denylisted",
                    "invalid_company_name_denylisted",
                    "invalid_dob_age_over_maximum",
                    "invalid_dob_age_under_18",
                    "invalid_dob_age_under_minimum",
                    "invalid_product_description_length",
                    "invalid_product_description_url_match",
                    "invalid_representative_country",
                    "invalid_statement_descriptor_business_mismatch",
                    "invalid_statement_descriptor_denylisted",
                    "invalid_statement_descriptor_length",
                    "invalid_statement_descriptor_prefix_denylisted",
                    "invalid_statement_descriptor_prefix_mismatch",
                    "invalid_street_address",
                    "invalid_tax_id",
                    "invalid_tax_id_format",
                    "invalid_tos_acceptance",
                    "invalid_url_denylisted",
                    "invalid_url_format",
                    "invalid_url_website_business_information_mismatch",
                    "invalid_url_website_empty",
                    "invalid_url_website_inaccessible",
                    "invalid_url_website_inaccessible_geoblocked",
                    "invalid_url_website_inaccessible_password_protected",
                    "invalid_url_website_incomplete",
                    "invalid_url_website_incomplete_cancellation_policy",
                    "invalid_url_website_incomplete_customer_service_details",
                    "invalid_url_website_incomplete_legal_restrictions",
                    "invalid_url_website_incomplete_refund_policy",
                    "invalid_url_website_incomplete_return_policy",
                    "invalid_url_website_incomplete_terms_and_conditions",
                    "invalid_url_website_incomplete_under_construction",
                    "invalid_url_website_other",
                    "invalid_url_web_presence_detected",
                    "invalid_value_other",
                    "unresolvable_ip_address",
                    "unresolvable_postal_code",
                    "verification_directors_mismatch",
                    "verification_document_address_mismatch",
                    "verification_document_address_missing",
                    "verification_document_corrupt",
                    "verification_document_country_not_supported",
                    "verification_document_directors_mismatch",
                    "verification_document_dob_mismatch",
                    "verification_document_duplicate_type",
                    "verification_document_expired",
                    "verification_document_failed_copy",
                    "verification_document_failed_greyscale",
                    "verification_document_failed_other",
                    "verification_document_failed_test_mode",
                    "verification_document_fraudulent",
                    "verification_document_id_number_mismatch",
                    "verification_document_id_number_missing",
                    "verification_document_incomplete",
                    "verification_document_invalid",
                    "verification_document_issue_or_expiry_date_missing",
                    "verification_document_manipulated",
                    "verification_document_missing_back",
                    "verification_document_missing_front",
                    "verification_document_name_mismatch",
                    "verification_document_name_missing",
                    "verification_document_nationality_mismatch",
                    "verification_document_not_readable",
                    "verification_document_not_signed",
                    "verification_document_not_uploaded",
                    "verification_document_photo_mismatch",
                    "verification_document_too_large",
                    "verification_document_type_not_supported",
                    "verification_extraneous_directors",
                    "verification_failed_address_match",
                    "verification_failed_business_iec_number",
                    "verification_failed_document_match",
                    "verification_failed_id_number_match",
                    "verification_failed_keyed_identity",
                    "verification_failed_keyed_match",
                    "verification_failed_name_match",
                    "verification_failed_other",
                    "verification_failed_representative_authority",
                    "verification_failed_residential_address",
                    "verification_failed_tax_id_match",
                    "verification_failed_tax_id_not_issued",
                    "verification_missing_directors",
                    "verification_missing_executives",
                    "verification_missing_owners",
                    "verification_requires_additional_memorandum_of_associations",
                    "verification_requires_additional_proof_of_registration",
                    "verification_selfie_document_missing_photo",
                    "verification_selfie_face_mismatch",
                    "verification_selfie_manipulated",
                    "verification_selfie_unverified_other",
                    "verification_supportability",
                    "verification_token_stale",
                ]
                """
                Machine-readable code describing the error.
                """
                description: str
                """
                Human-readable description of the error.
                """

            class Impact(StripeObject):
                class RestrictsCapability(StripeObject):
                    class Deadline(StripeObject):
                        status: Literal[
                            "currently_due", "eventually_due", "past_due"
                        ]
                        """
                        The current status of the requirement's impact.
                        """

                    capability: Literal[
                        "ach_debit_payments",
                        "acss_debit_payments",
                        "affirm_payments",
                        "afterpay_clearpay_payments",
                        "alma_payments",
                        "amazon_pay_payments",
                        "automatic_indirect_tax",
                        "au_becs_debit_payments",
                        "bacs_debit_payments",
                        "bancontact_payments",
                        "bank_accounts.local",
                        "bank_accounts.wire",
                        "blik_payments",
                        "boleto_payments",
                        "cards",
                        "card_payments",
                        "cartes_bancaires_payments",
                        "cashapp_payments",
                        "eps_payments",
                        "financial_addresses.bank_accounts",
                        "fpx_payments",
                        "gb_bank_transfer_payments",
                        "grabpay_payments",
                        "holds_currencies.gbp",
                        "ideal_payments",
                        "inbound_transfers.financial_accounts",
                        "jcb_payments",
                        "jp_bank_transfer_payments",
                        "kakao_pay_payments",
                        "klarna_payments",
                        "konbini_payments",
                        "kr_card_payments",
                        "link_payments",
                        "mobilepay_payments",
                        "multibanco_payments",
                        "mx_bank_transfer_payments",
                        "naver_pay_payments",
                        "outbound_payments.bank_accounts",
                        "outbound_payments.cards",
                        "outbound_payments.financial_accounts",
                        "outbound_transfers.bank_accounts",
                        "outbound_transfers.financial_accounts",
                        "oxxo_payments",
                        "p24_payments",
                        "payco_payments",
                        "paynow_payments",
                        "pay_by_bank_payments",
                        "promptpay_payments",
                        "revolut_pay_payments",
                        "samsung_pay_payments",
                        "sepa_bank_transfer_payments",
                        "sepa_debit_payments",
                        "stripe_balance.payouts",
                        "stripe_balance.stripe_transfers",
                        "swish_payments",
                        "twint_payments",
                        "us_bank_transfer_payments",
                        "zip_payments",
                    ]
                    """
                    The name of the Capability which will be restricted.
                    """
                    configuration: Literal[
                        "customer", "merchant", "recipient", "storer"
                    ]
                    """
                    The configuration which specifies the Capability which will be restricted.
                    """
                    deadline: Deadline
                    """
                    Details about when in the account lifecycle the requirement must be collected by the avoid the Capability restriction.
                    """
                    _inner_class_types = {"deadline": Deadline}

                restricts_capabilities: Optional[List[RestrictsCapability]]
                """
                The Capabilities that will be restricted if the requirement is not collected and satisfactory to Stripe.
                """
                _inner_class_types = {
                    "restricts_capabilities": RestrictsCapability,
                }

            class MinimumDeadline(StripeObject):
                status: Literal["currently_due", "eventually_due", "past_due"]
                """
                The current status of the requirement's impact.
                """

            class Reference(StripeObject):
                inquiry: Optional[str]
                """
                If `inquiry` is the type, the inquiry token.
                """
                resource: Optional[str]
                """
                If `resource` is the type, the resource token.
                """
                type: Literal["inquiry", "resource"]
                """
                The type of the reference. An additional hash is included with a name matching the type. It contains additional information specific to the type.
                """

            class RequestedReason(StripeObject):
                code: Literal[
                    "future_requirements",
                    "routine_onboarding",
                    "routine_verification",
                ]
                """
                Machine-readable description of Stripe's reason for collecting the requirement.
                """

            awaiting_action_from: Literal["stripe", "user"]
            """
            Whether the responsibility is with the integrator or with Stripe (to review info, to wait for some condition, etc.) to action the requirement.
            """
            description: str
            """
            Machine-readable string describing the requirement.
            """
            errors: List[Error]
            """
            Descriptions of why the requirement must be collected, or why the collected information isn't satisfactory to Stripe.
            """
            impact: Impact
            """
            A hash describing the impact of not collecting the requirement, or Stripe not being able to verify the collected information.
            """
            minimum_deadline: MinimumDeadline
            """
            The soonest point when the account will be impacted by not providing the requirement.
            """
            reference: Optional[Reference]
            """
            A reference to the location of the requirement.
            """
            requested_reasons: List[RequestedReason]
            """
            A list of reasons why Stripe is collecting the requirement.
            """
            _inner_class_types = {
                "errors": Error,
                "impact": Impact,
                "minimum_deadline": MinimumDeadline,
                "reference": Reference,
                "requested_reasons": RequestedReason,
            }

        class Summary(StripeObject):
            class MinimumDeadline(StripeObject):
                status: Literal["currently_due", "eventually_due", "past_due"]
                """
                The current strictest status of all requirements on the Account.
                """
                time: Optional[str]
                """
                The soonest RFC3339 date & time UTC value a requirement can impact the Account.
                """

            minimum_deadline: Optional[MinimumDeadline]
            """
            The soonest date and time a requirement on the Account will become `past due`. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
            """
            _inner_class_types = {"minimum_deadline": MinimumDeadline}

        collector: Literal["application", "stripe"]
        """
        A value indicating responsibility for collecting requirements on this account.
        """
        entries: Optional[List[Entry]]
        """
        A list of requirements for the Account.
        """
        summary: Optional[Summary]
        """
        An object containing an overview of requirements for the Account.
        """
        _inner_class_types = {"entries": Entry, "summary": Summary}

    applied_configurations: List[
        Literal["customer", "merchant", "recipient", "storer"]
    ]
    """
    Filter only accounts that have all of the configurations specified. If omitted, returns all accounts regardless of which configurations they have.
    """
    configuration: Optional[Configuration]
    """
    An Account Configuration which allows the Account to take on a key persona across Stripe products.
    """
    contact_email: Optional[str]
    """
    The default contact email address for the Account. Required when configuring the account as a merchant or recipient.
    """
    created: str
    """
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    dashboard: Optional[Literal["express", "full", "none"]]
    """
    A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.
    """
    defaults: Optional[Defaults]
    """
    Default values to be used on Account Configurations.
    """
    display_name: Optional[str]
    """
    A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
    """
    id: str
    """
    Unique identifier for the Account.
    """
    identity: Optional[Identity]
    """
    Information about the company, individual, and business represented by the Account.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.core.account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    requirements: Optional[Requirements]
    """
    Information about the requirements for the Account, including what information needs to be collected, and by when.
    """
    _inner_class_types = {
        "configuration": Configuration,
        "defaults": Defaults,
        "identity": Identity,
        "requirements": Requirements,
    }
