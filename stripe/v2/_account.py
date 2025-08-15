# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class Account(StripeObject):
    """
    A V2 Account is a representation of a company or individual that a Stripe user does business with. Accounts contain the contact details, Legal Entity information, and configuration required to enable the Account for use across Stripe products.
    """

    OBJECT_NAME: ClassVar[Literal["account"]] = "account"

    class Configuration(StripeObject):
        class RecipientData(StripeObject):
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

            class Features(StripeObject):
                class BankAccounts(StripeObject):
                    class Local(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_country",
                            ]
                            """
                            Closed Enum. Status code, explaining why the Feature has a given status, if it is not `active`.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Closed Enum. Additional information about how to resolve the Feature status, if it is not `active`.
                            """

                        requested: bool
                        """
                        Whether or not the Feature has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        Closed Enum. The current status of the Feature. Once the status is `active`, the Account is ready to be used in the product flow that the Feature represents.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Feature - will be empty if status is `active`.
                        """
                        _inner_class_types = {"status_details": StatusDetail}

                    class Wire(StripeObject):
                        class StatusDetail(StripeObject):
                            code: Literal[
                                "determining_status",
                                "requirements_past_due",
                                "requirements_pending_verification",
                                "restricted_other",
                                "unsupported_country",
                            ]
                            """
                            Closed Enum. Status code, explaining why the Feature has a given status, if it is not `active`.
                            """
                            resolution: Literal[
                                "contact_stripe",
                                "no_resolution",
                                "provide_info",
                            ]
                            """
                            Closed Enum. Additional information about how to resolve the Feature status, if it is not `active`.
                            """

                        requested: bool
                        """
                        Whether or not the Feature has been requested.
                        """
                        status: Literal[
                            "active", "pending", "restricted", "unsupported"
                        ]
                        """
                        Closed Enum. The current status of the Feature. Once the status is `active`, the Account is ready to be used in the product flow that the Feature represents.
                        """
                        status_details: List[StatusDetail]
                        """
                        Additional details regarding the status of the Feature - will be empty if status is `active`.
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
                            "unsupported_country",
                        ]
                        """
                        Closed Enum. Status code, explaining why the Feature has a given status, if it is not `active`.
                        """
                        resolution: Literal[
                            "contact_stripe", "no_resolution", "provide_info"
                        ]
                        """
                        Closed Enum. Additional information about how to resolve the Feature status, if it is not `active`.
                        """

                    requested: bool
                    """
                    Whether or not the Feature has been requested.
                    """
                    status: Literal[
                        "active", "pending", "restricted", "unsupported"
                    ]
                    """
                    Closed Enum. The current status of the Feature. Once the status is `active`, the Account is ready to be used in the product flow that the Feature represents.
                    """
                    status_details: List[StatusDetail]
                    """
                    Additional details regarding the status of the Feature - will be empty if status is `active`.
                    """
                    _inner_class_types = {"status_details": StatusDetail}

                bank_accounts: BankAccounts
                """
                Features that enable OutboundPayments to a bank account linked to this Account.
                """
                cards: Optional[Cards]
                """
                Features that enable OutboundPayments to a card linked to this Account.
                """
                _inner_class_types = {
                    "bank_accounts": BankAccounts,
                    "cards": Cards,
                }

            default_outbound_destination: Optional[DefaultOutboundDestination]
            """
            The payout method id to be used as a default outbound destination. This will allow the PayoutMethod to be omitted on OutboundPayments made through API or sending payouts via dashboard.
            """
            features: Features
            """
            Features representing the functionality that should be enabled for when this Account is used as a recipient. Features need to be explicitly requested, and the `status` field indicates if the Feature is `active`, `restricted` or `pending`. Once a Feature is `active`, the Account can be used with the product flow that the Feature enables.
            """
            _inner_class_types = {
                "default_outbound_destination": DefaultOutboundDestination,
                "features": Features,
            }

        class SupportableFeatures(StripeObject):
            recipient_data: Optional[
                List[
                    Literal[
                        "bank_accounts.local", "bank_accounts.wire", "cards"
                    ]
                ]
            ]
            """
            Closed Enum. A list of supported features that can be requested when the Account is configured as a recipient. Will be unset unless Legal Entity country has been provided for this Account.
            """

        recipient_data: Optional[RecipientData]
        """
        Configuration to enable this Account to be used as a recipient of an OutboundPayment via the OutboundPayments API, or via the dashboard. This field will only be returned if `configuration.recipient_data` is passed in the `include` parameter. Note that you cannot pass the `include` parameter on list requests so this field cannot be populated for lists.
        """
        supportable_features: Optional[SupportableFeatures]
        """
        Supported features that can be requested for the Account's configurations. This field will only be returned if `supportable_features.recipient_data` is passed in the `include` parameter. Note that you cannot pass the `include` parameter on list requests so this field cannot be populated for lists.
        """
        _inner_class_types = {
            "recipient_data": RecipientData,
            "supportable_features": SupportableFeatures,
        }

    class LegalEntityData(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City.
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
            Open Enum. Two-letter country code.
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
            Town.
            """

        class Representative(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                """
                City.
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
                Open Enum. Two-letter country code.
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
                Town.
                """

            class Dob(StripeObject):
                day: int
                """
                The day of birth of the representative.
                """
                month: int
                """
                The month of birth of the representative.
                """
                year: int
                """
                The year of birth of the representative.
                """

            address: Optional[Address]
            """
            The address of the representative.
            """
            dob: Optional[Dob]
            """
            The date of birth of the representative.
            """
            given_name: Optional[str]
            """
            The given name of the representative.
            """
            surname: Optional[str]
            """
            The surname of the representative.
            """
            _inner_class_types = {"address": Address, "dob": Dob}

        address: Optional[Address]
        """
        The address of the Legal Entity.
        """
        business_type: Optional[Literal["company", "individual"]]
        """
        Closed Enum. The business type of the Legal Entity.
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
        Open Enum. Two-letter country code (ISO 3166-1 alpha-2) for where the company or individual is located.
        """
        name: Optional[str]
        """
        The legal name of this Legal Entity. Required unless the business type is `individual`.
        """
        representative: Optional[Representative]
        """
        The representative of the Legal Entity. This is the person nominated by the Legal Entity to provide information about themselves, and general information about the account. For legal entities with `individual` business type, this field is required and should contain the individual's information.
        """
        _inner_class_types = {
            "address": Address,
            "representative": Representative,
        }

    class Requirement(StripeObject):
        class Deadline(StripeObject):
            due_at: Optional[str]
            """
            Machine-readable version of the deadline.
            """
            status: Literal[
                "conditionally_due", "currently_due", "deadline_past_due"
            ]
            """
            Closed Enum. Human-readable description of the deadline.
            """

        class Error(StripeObject):
            code: Literal["po_box_address_not_allowed"]
            """
            Open Enum. Machine-readable error codes.
            """
            message: str
            """
            Human-readable error messages.
            """

        class Impact(StripeObject):
            required_for_features: List[
                Literal["bank_accounts.local", "bank_accounts.wire", "cards"]
            ]
            """
            Open Enum. The set of Features that are restricted by this requirement.
            """

        awaiting_action_from: Literal["stripe", "user"]
        """
        Closed Enum. Whether the responsibility is with the integrator to action, or with Stripe (to review info, to wait for some condition, etc.).
        """
        deadline: Deadline
        """
        When the requirement is due.
        """
        description: Literal[
            "legal_entity.addresses.business_registration.city",
            "legal_entity.addresses.business_registration.country",
            "legal_entity.addresses.business_registration.line1",
            "legal_entity.addresses.business_registration.postal_code",
            "legal_entity.addresses.business_registration.state",
            "legal_entity.business_type",
            "legal_entity.documents.primary_identification",
            "legal_entity.name",
            "recipient_config.recipient_verification",
            "representative.addresses.residential.city",
            "representative.addresses.residential.country",
            "representative.addresses.residential.line1",
            "representative.addresses.residential.postal_code",
            "representative.addresses.residential.state",
            "representative.dob",
            "representative.documents.primary_identification",
            "representative.given_name",
            "representative.surname",
        ]
        """
        Open Enum. The unique identifier describing the data to be collected for this requirement.
        """
        errors: List[Error]
        """
        Communicate remediation steps with users if data previously submitted by user is not acceptable by Stripe.
        """
        impact: Impact
        """
        Consequence of not completing this entry on time and in a Stripe-accepted manner.
        """
        requested_reasons: List[
            Literal["routine_onboarding", "routine_verification"]
        ]
        """
        Open Enum. Why Stripe wants this information.
        """
        _inner_class_types = {
            "deadline": Deadline,
            "errors": Error,
            "impact": Impact,
        }

    applied_configurations: List[Literal["recipient", "storer"]]
    """
    Closed Enum. A list of the configurations which have been applied to the Account to allow Accounts to be filtered by the products they have been configured for. Currently can only contain `recipient`, which will be present if a recipient configuration is set.
    """
    configuration: Optional[Configuration]
    """
    Configuration to enable this Account to be used as a recipient of an OutboundPayment via the OutboundPayments API, or via the dashboard.
    """
    created: str
    """
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    email: Optional[str]
    """
    The default contact email address for the Account. This field is optional, but must be supplied before the recipient configuration can be populated.
    """
    id: str
    """
    Unique identifier for the Account.
    """
    legal_entity_data: Optional[LegalEntityData]
    """
    The default set of verification information for the Account. Currently, this only includes a single Legal Entity which must be set as the default.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    A descriptive name for the Account. This name will be surfaced in the Account directory in the dashboard.
    """
    object: Literal["account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    requirements: Optional[List[Requirement]]
    """
    A list of outstanding tasks users must complete before Stripe allows the Account's Features to be activated.
    """
    _inner_class_types = {
        "configuration": Configuration,
        "legal_entity_data": LegalEntityData,
        "requirements": Requirement,
    }
