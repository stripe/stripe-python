# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.money_management._financial_account import FinancialAccount
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAccountService(StripeService):
    class CloseParams(TypedDict):
        forwarding_settings: NotRequired[
            "FinancialAccountService.CloseParamsForwardingSettings"
        ]
        """
        The addresses to forward any incoming transactions to.
        """

    class CloseParamsForwardingSettings(TypedDict):
        payment_method: NotRequired[str]
        """
        The address to send forwarded payments to.
        """
        payout_method: NotRequired[str]
        """
        The address to send forwarded payouts to.
        """

    class CreateParams(TypedDict):
        metadata: NotRequired[Dict[str, str]]
        """
        Metadata associated with the FinancialAccount.
        """
        storage: NotRequired["FinancialAccountService.CreateParamsStorage"]
        """
        Parameters specific to creating `storage` type FinancialAccounts.
        """
        type: Literal["storage"]
        """
        The type of FinancialAccount to create.
        """

    class CreateParamsStorage(TypedDict):
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

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page limit.
        """
        status: NotRequired[Literal["closed", "open", "pending"]]
        """
        The status of the FinancialAccount to filter by. By default, closed FinancialAccounts are not returned.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "FinancialAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAccount]:
        """
        Lists FinancialAccounts in this compartment.
        """
        return cast(
            ListObject[FinancialAccount],
            self._request(
                "get",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "FinancialAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancialAccount]:
        """
        Lists FinancialAccounts in this compartment.
        """
        return cast(
            ListObject[FinancialAccount],
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FinancialAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Creates a new FinancialAccount.
        """
        return cast(
            FinancialAccount,
            self._request(
                "post",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FinancialAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Creates a new FinancialAccount.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "FinancialAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            FinancialAccount,
            self._request(
                "get",
                "/v2/money_management/financial_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "FinancialAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Retrieves the details of an existing FinancialAccount.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def close(
        self,
        id: str,
        params: "FinancialAccountService.CloseParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Closes a FinancialAccount with or without forwarding settings.
        """
        return cast(
            FinancialAccount,
            self._request(
                "post",
                "/v2/money_management/financial_accounts/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def close_async(
        self,
        id: str,
        params: "FinancialAccountService.CloseParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccount:
        """
        Closes a FinancialAccount with or without forwarding settings.
        """
        return cast(
            FinancialAccount,
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts/{id}/close".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
