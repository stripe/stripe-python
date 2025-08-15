# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._account import Account
from stripe.v2._list_object import ListObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class AccountService(StripeService):
    class CloseParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        configuration: NotRequired["AccountService.CreateParamsConfiguration"]
        """
        Configurations applied to this Account in order to allow it to be used in different product flows. Currently only supports the recipient configuration.
        """
        email: NotRequired[str]
        """
        The default contact email address for the Account. This field is optional, but must be supplied before the recipient configuration can be populated.
        """
        include: NotRequired[
            List[
                Literal[
                    "configuration.recipient_data",
                    "legal_entity_data",
                    "requirements",
                    "supportable_features.recipient_data",
                ]
            ]
        ]
        """
        Closed Enum. Additional fields to include in the response. Currently supports `configuration.recipient_data`, `legal_entity_data`, `requirements`, and `supportable_features.recipient_data`.
        """
        legal_entity_data: NotRequired[
            "AccountService.CreateParamsLegalEntityData"
        ]
        """
        Information about the company or individual that this Account represents. Stripe may require Legal Entity information in order to enable Features requested on the Account.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        name: NotRequired[str]
        """
        A descriptive name for the Account. This name will be surfaced in the Account directory in the dashboard.
        """

    class CreateParamsConfiguration(TypedDict):
        recipient_data: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientData"
        ]
        """
        Configuration to enable this Account to be used as a recipient of an OutboundPayment via the OutboundPayments API, or via the dashboard.
        """

    class CreateParamsConfigurationRecipientData(TypedDict):
        features: (
            "AccountService.CreateParamsConfigurationRecipientDataFeatures"
        )
        """
        Features representing the functionality that should be enabled for when this Account is used as a recipient. Features need to be explicitly requested, and the `status` field indicates if the Feature is `active`, `restricted` or `pending`. Once a Feature is `active`, the Account can be used with the product flow that the Feature enables.
        """

    class CreateParamsConfigurationRecipientDataFeatures(TypedDict):
        bank_accounts: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientDataFeaturesBankAccounts"
        ]
        """
        Features that enable OutboundPayments to a bank account linked to this Account.
        """
        cards: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientDataFeaturesCards"
        ]
        """
        Feature that enable OutboundPayments to a debit card linked to this Account.
        """

    class CreateParamsConfigurationRecipientDataFeaturesBankAccounts(
        TypedDict
    ):
        local: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientDataFeaturesBankAccountsLocal"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
        """
        wire: NotRequired[
            "AccountService.CreateParamsConfigurationRecipientDataFeaturesBankAccountsWire"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over wire.
        """

    class CreateParamsConfigurationRecipientDataFeaturesBankAccountsLocal(
        TypedDict,
    ):
        requested: bool
        """
        Whether or not to request the Feature.
        """

    class CreateParamsConfigurationRecipientDataFeaturesBankAccountsWire(
        TypedDict,
    ):
        requested: bool
        """
        Whether or not to request the Feature.
        """

    class CreateParamsConfigurationRecipientDataFeaturesCards(TypedDict):
        requested: bool
        """
        Whether or not to request the Feature.
        """

    class CreateParamsLegalEntityData(TypedDict):
        address: NotRequired[
            "AccountService.CreateParamsLegalEntityDataAddress"
        ]
        """
        The address of the Legal Entity.
        """
        business_type: NotRequired[Literal["company", "individual"]]
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
        name: NotRequired[str]
        """
        The legal name of this Legal Entity. Required unless the business type is `individual`.
        """
        representative: NotRequired[
            "AccountService.CreateParamsLegalEntityDataRepresentative"
        ]
        """
        The representative of the Legal Entity. This is the person nominated by the Legal Entity to provide information about themselves, and general information about the account. For legal entities with `individual` business type, this field is required and should contain the individual's information.
        """

    class CreateParamsLegalEntityDataAddress(TypedDict):
        city: NotRequired[str]
        """
        City.
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
        Open Enum. Two-letter country code.
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
        Town.
        """

    class CreateParamsLegalEntityDataRepresentative(TypedDict):
        address: NotRequired[
            "AccountService.CreateParamsLegalEntityDataRepresentativeAddress"
        ]
        """
        The address of the representative.
        """
        dob: NotRequired[
            "AccountService.CreateParamsLegalEntityDataRepresentativeDob"
        ]
        """
        The date of birth of the representative.
        """
        given_name: NotRequired[str]
        """
        The given name of the representative.
        """
        surname: NotRequired[str]
        """
        The surname of the representative.
        """

    class CreateParamsLegalEntityDataRepresentativeAddress(TypedDict):
        city: NotRequired[str]
        """
        City.
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
        Open Enum. Two-letter country code.
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
        Town.
        """

    class CreateParamsLegalEntityDataRepresentativeDob(TypedDict):
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

    class ListParams(TypedDict):
        applied_configurations: NotRequired[List[str]]
        """
        Filter by the configurations that have been applied to the account. If omitted, returns all Accounts regardless of which configurations they have. Currently only supports `recipient`, to filter by Accounts with the recipient configuration set.
        """
        limit: NotRequired[int]
        """
        The limit.
        """

    class RetrieveParams(TypedDict):
        include: NotRequired[
            List[
                Literal[
                    "configuration.recipient_data",
                    "legal_entity_data",
                    "requirements",
                    "supportable_features.recipient_data",
                ]
            ]
        ]
        """
        Closed Enum. Additional fields to include in the response. Currently supports `configuration.recipient_data`, `legal_entity_data`, `requirements`, and `supportable_features.recipient_data`.
        """

    class UpdateParams(TypedDict):
        configuration: NotRequired["AccountService.UpdateParamsConfiguration"]
        """
        Configurations applied to this Account in order to allow it to be used in different product flows. Currently only supports the recipient configuration.
        """
        email: NotRequired[str]
        """
        The default contact email address for the Account. This field is optional, but must be supplied before the recipient configuration can be populated.
        """
        include: NotRequired[
            List[
                Literal[
                    "configuration.recipient_data",
                    "legal_entity_data",
                    "requirements",
                    "supportable_features.recipient_data",
                ]
            ]
        ]
        """
        Closed Enum. Additional fields to include in the response. Currently supports `configuration.recipient_data`, `legal_entity_data`, `requirements`, and `supportable_features.recipient_data`.
        """
        legal_entity_data: NotRequired[
            "AccountService.UpdateParamsLegalEntityData"
        ]
        """
        Information about the company or individual that this Account represents. Stripe may require Legal Entity information in order to enable Features requested on the Account.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        name: NotRequired[str]
        """
        A descriptive name for the Account. This name will be surfaced in the Account directory in the dashboard.
        """

    class UpdateParamsConfiguration(TypedDict):
        recipient_data: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientData"
        ]
        """
        Configuration to enable this Account to be used as a recipient of an OutboundPayment via the OutboundPayments API, or via the dashboard.
        """

    class UpdateParamsConfigurationRecipientData(TypedDict):
        default_outbound_destination: NotRequired[Optional[str]]
        """
        The payout method id to be used as a default outbound destination. This will allow the PayoutMethod to be omitted on OutboundPayments made through API or sending payouts via dashboard. Can also be explicitly set to `null` to clear the existing default outbound destination.
        """
        features: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientDataFeatures"
        ]
        """
        Features representing the functionality that should be enabled for when this Account is used as a recipient. Features need to be explicitly requested, and the `status` field indicates if the Feature is `active`, `restricted` or `pending`. Once a Feature is `active`, the Account can be used with the product flow that the Feature enables.
        """

    class UpdateParamsConfigurationRecipientDataFeatures(TypedDict):
        bank_accounts: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientDataFeaturesBankAccounts"
        ]
        """
        Features that enable OutboundPayments to a bank account linked to this Account.
        """
        cards: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientDataFeaturesCards"
        ]
        """
        Feature that enable OutboundPayments to a debit card linked to this Account.
        """

    class UpdateParamsConfigurationRecipientDataFeaturesBankAccounts(
        TypedDict
    ):
        local: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientDataFeaturesBankAccountsLocal"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over local networks.
        """
        wire: NotRequired[
            "AccountService.UpdateParamsConfigurationRecipientDataFeaturesBankAccountsWire"
        ]
        """
        Enables this Account to receive OutboundPayments to linked bank accounts over wire.
        """

    class UpdateParamsConfigurationRecipientDataFeaturesBankAccountsLocal(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        Whether or not to request the Feature.
        """

    class UpdateParamsConfigurationRecipientDataFeaturesBankAccountsWire(
        TypedDict,
    ):
        requested: NotRequired[bool]
        """
        Whether or not to request the Feature.
        """

    class UpdateParamsConfigurationRecipientDataFeaturesCards(TypedDict):
        requested: NotRequired[bool]
        """
        Whether or not to request the Feature.
        """

    class UpdateParamsLegalEntityData(TypedDict):
        address: NotRequired[
            Optional["AccountService.UpdateParamsLegalEntityDataAddress"]
        ]
        """
        The address of the Legal Entity.
        """
        business_type: NotRequired[Optional[Literal["company", "individual"]]]
        """
        Closed Enum. The business type of the Legal Entity.
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
        Open Enum. Two-letter country code (ISO 3166-1 alpha-2) for where the company or individual is located.
        """
        name: NotRequired[Optional[str]]
        """
        The legal name of this Legal Entity. Required unless the business type is `individual`.
        """
        representative: NotRequired[
            Optional[
                "AccountService.UpdateParamsLegalEntityDataRepresentative"
            ]
        ]
        """
        The representative of the Legal Entity. This is the person nominated by the Legal Entity to provide information about themselves, and general information about the account. For legal entities with `individual` business type, this field is required and should contain the individual's information.
        """

    class UpdateParamsLegalEntityDataAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City.
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
        Open Enum. Two-letter country code.
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
        Town.
        """

    class UpdateParamsLegalEntityDataRepresentative(TypedDict):
        address: NotRequired[
            Optional[
                "AccountService.UpdateParamsLegalEntityDataRepresentativeAddress"
            ]
        ]
        """
        The address of the representative.
        """
        dob: NotRequired[
            Optional[
                "AccountService.UpdateParamsLegalEntityDataRepresentativeDob"
            ]
        ]
        """
        The date of birth of the representative.
        """
        given_name: NotRequired[Optional[str]]
        """
        The given name of the representative.
        """
        surname: NotRequired[Optional[str]]
        """
        The surname of the representative.
        """

    class UpdateParamsLegalEntityDataRepresentativeAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City.
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
        Open Enum. Two-letter country code.
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
        Town.
        """

    class UpdateParamsLegalEntityDataRepresentativeDob(TypedDict):
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

    def list(
        self,
        params: "AccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Account]:
        """
        Returns a list of Accounts. Note that the `include` parameter cannot be passed in on list requests.
        """
        return cast(
            ListObject[Account],
            self._request(
                "get",
                "/v2/accounts",
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
        Returns a list of Accounts. Note that the `include` parameter cannot be passed in on list requests.
        """
        return cast(
            ListObject[Account],
            await self._request_async(
                "get",
                "/v2/accounts",
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
        Creates an Account. You can optionally provide information about the associated Legal Entity, such as name and business type. The Account can also be configured as a recipient of OutboundPayments by requesting Features on the recipient configuration.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/accounts",
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
        Creates an Account. You can optionally provide information about the associated Legal Entity, such as name and business type. The Account can also be configured as a recipient of OutboundPayments by requesting Features on the recipient configuration.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/accounts",
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
                "/v2/accounts/{id}".format(id=sanitize_id(id)),
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
                "/v2/accounts/{id}".format(id=sanitize_id(id)),
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
        Updates the details of an Account. You can also optionally provide or update the details of the associated Legal Entity and recipient configuration.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/accounts/{id}".format(id=sanitize_id(id)),
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
        Updates the details of an Account. You can also optionally provide or update the details of the associated Legal Entity and recipient configuration.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/accounts/{id}".format(id=sanitize_id(id)),
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
        Closes and removes access to the Account and its associated resources.
        """
        return cast(
            Account,
            self._request(
                "post",
                "/v2/accounts/{id}/close".format(id=sanitize_id(id)),
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
        Closes and removes access to the Account and its associated resources.
        """
        return cast(
            Account,
            await self._request_async(
                "post",
                "/v2/accounts/{id}/close".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
