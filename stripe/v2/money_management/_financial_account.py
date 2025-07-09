# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class FinancialAccount(StripeObject):
    """
    The Financial Account is the container that allows for the configuration of money movement.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_account"]] = (
        "v2.money_management.financial_account"
    )

    class Balance(StripeObject):
        available: Dict[str, Amount]
        """
        Balance that can be used for money movement.
        """
        inbound_pending: Dict[str, Amount]
        """
        Balance of inbound funds that will later transition to the `available` balance.
        """
        outbound_pending: Dict[str, Amount]
        """
        Balance of funds that are being used for a pending outbound money movement.
        """

    class Other(StripeObject):
        type: str
        """
        The type of the FinancialAccount, represented as a string. Upgrade your API version to see the type reflected in `financial_account.type`.
        """

    class StatusDetails(StripeObject):
        class Closed(StripeObject):
            class ForwardingSettings(StripeObject):
                payment_method: Optional[str]
                """
                The address to send forwarded payments to.
                """
                payout_method: Optional[str]
                """
                The address to send forwarded payouts to.
                """

            forwarding_settings: Optional[ForwardingSettings]
            reason: Literal["account_closed", "closed_by_platform", "other"]
            _inner_class_types = {"forwarding_settings": ForwardingSettings}

        closed: Optional[Closed]
        _inner_class_types = {"closed": Closed}

    class Storage(StripeObject):
        holds_currencies: List[
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
        The currencies that this FinancialAccount can hold.
        """

    balance: Balance
    """
    Multi-currency balance of this FinancialAccount, split by availability state. Each balance is represented as a hash where the key is the three-letter ISO currency code, in lowercase, and the value is the amount for that currency.
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
    Open Enum. Two-letter country code that represents the country where the LegalEntity associated with the FinancialAccount is based in.
    """
    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Metadata associated with the FinancialAccount
    """
    object: Literal["v2.money_management.financial_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    other: Optional[Other]
    """
    If this is a `other` FinancialAccount, this hash indicates what the actual type is. Upgrade your API version to see it reflected in `type`.
    """
    status: Literal["closed", "open", "pending"]
    """
    Closed Enum. An enum representing the status of the FinancialAccount. This indicates whether or not the FinancialAccount can be used for any money movement flows.
    """
    status_details: Optional[StatusDetails]
    storage: Optional[Storage]
    """
    If this is a `storage` FinancialAccount, this hash includes details specific to `storage` FinancialAccounts.
    """
    type: Literal["other", "storage"]
    """
    Type of the FinancialAccount. An additional hash is included on the FinancialAccount with a name matching this value.
    It contains additional information specific to the FinancialAccount type.
    """
    _inner_class_types = {
        "balance": Balance,
        "other": Other,
        "status_details": StatusDetails,
        "storage": Storage,
    }
