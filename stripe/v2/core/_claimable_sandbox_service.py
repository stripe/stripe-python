# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.core._claimable_sandbox import ClaimableSandbox
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class ClaimableSandboxService(StripeService):
    class CreateParams(TypedDict):
        enable_mcp_access: bool
        """
        If true, returns a key that can be used with [Stripe's MCP server](https://docs.stripe.com/mcp).
        """
        prefill: "ClaimableSandboxService.CreateParamsPrefill"
        """
        Values that are prefilled when a user claims the sandbox.
        """

    class CreateParamsPrefill(TypedDict):
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
        notify this email address before the sandbox expires.
        """
        name: NotRequired[str]
        """
        Name for the sandbox. If not provided, this will be generated.
        """

    class RetrieveParams(TypedDict):
        pass

    def create(
        self,
        params: "ClaimableSandboxService.CreateParams",
        options: RequestOptions = {},
    ) -> ClaimableSandbox:
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            ClaimableSandbox,
            self._request(
                "post",
                "/v2/core/claimable_sandboxes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ClaimableSandboxService.CreateParams",
        options: RequestOptions = {},
    ) -> ClaimableSandbox:
        """
        Create an anonymous, claimable sandbox. This sandbox can be prefilled with data. The response will include
        a claim URL that allow a user to claim the account.
        """
        return cast(
            ClaimableSandbox,
            await self._request_async(
                "post",
                "/v2/core/claimable_sandboxes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ClaimableSandboxService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ClaimableSandbox:
        """
        Retrieves the details of a claimable sandbox that was previously been created.
        Supply the unique claimable sandbox ID that was returned from your creation request,
        and Stripe will return the corresponding sandbox information.
        """
        return cast(
            ClaimableSandbox,
            self._request(
                "get",
                "/v2/core/claimable_sandboxes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "ClaimableSandboxService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ClaimableSandbox:
        """
        Retrieves the details of a claimable sandbox that was previously been created.
        Supply the unique claimable sandbox ID that was returned from your creation request,
        and Stripe will return the corresponding sandbox information.
        """
        return cast(
            ClaimableSandbox,
            await self._request_async(
                "get",
                "/v2/core/claimable_sandboxes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
