# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ClaimableSandbox(StripeObject):
    """
    A claimable sandbox represents a Stripe sandbox that is anonymous.
    When it is created, it can be prefilled with specific metadata, such as email, name, or country.
    Claimable sandboxes can be claimed through a URL. When a user claims a sandbox through this URL,
    it will prompt them to create a new Stripe account. Or, it will allow them to claim this sandbox in their
    existing Stripe account.
    Claimable sandboxes have 60 days to be claimed. After this expiration time has passed,
    if the sandbox is not claimed, it will be deleted.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.claimable_sandbox"]] = (
        "v2.core.claimable_sandbox"
    )

    class ApiKeys(StripeObject):
        mcp: Optional[str]
        """
        Used to communicate with [Stripe's MCP server](https://docs.stripe.com/mcp).
        This allows LLM agents to securely operate on a Stripe account.
        """
        publishable: str
        """
        Publicly accessible in a web or mobile app client-side code.
        """
        secret: str
        """
        Should be stored securely in server-side code (such as an environment variable).
        """

    class Prefill(StripeObject):
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
        Country in which the account holder resides, or in which the business is legally established.
        Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        email: str
        """
        Email that this sandbox is meant to be claimed by. Stripe will
        send an email to this email address before the sandbox expires.
        """
        name: str
        """
        Name for the sandbox.
        """

    api_keys: ApiKeys
    """
    Keys that can be used to set up an integration for this sandbox and operate on the account.
    """
    claim_url: str
    """
    URL for user to claim sandbox into their existing Stripe account.
    """
    created: str
    """
    When the sandbox is created.
    """
    id: str
    """
    Unique identifier for the Claimable sandbox.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.claimable_sandbox"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    prefill: Prefill
    """
    Values prefilled during the creation of the sandbox.
    """
    _inner_class_types = {"api_keys": ApiKeys, "prefill": Prefill}
