# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class TaxRate(
    CreateableAPIResource["TaxRate"],
    ListableAPIResource["TaxRate"],
    UpdateableAPIResource["TaxRate"],
):
    """
    Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

    Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
    """

    OBJECT_NAME = "tax_rate"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            country: NotRequired["str|None"]
            description: NotRequired["str|None"]
            display_name: str
            expand: NotRequired["List[str]|None"]
            inclusive: bool
            jurisdiction: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            percentage: float
            state: NotRequired["str|None"]
            tax_type: NotRequired[
                "Literal['amusement_tax', 'communications_tax', 'gst', 'hst', 'igst', 'jct', 'lease_tax', 'pst', 'qst', 'rst', 'sales_tax', 'service_tax', 'vat']|None"
            ]

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            created: NotRequired["TaxRate.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            inclusive: NotRequired["bool|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            country: NotRequired["str|None"]
            description: NotRequired["str|None"]
            display_name: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            jurisdiction: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            state: NotRequired["str|None"]
            tax_type: NotRequired[
                "Literal['amusement_tax', 'communications_tax', 'gst', 'hst', 'igst', 'jct', 'lease_tax', 'pst', 'qst', 'rst', 'sales_tax', 'service_tax', 'vat']|None"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    active: bool
    country: Optional[str]
    created: int
    description: Optional[str]
    display_name: str
    effective_percentage: Optional[float]
    id: str
    inclusive: bool
    jurisdiction: Optional[str]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax_rate"]
    percentage: float
    state: Optional[str]
    tax_type: Optional[
        Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["TaxRate.CreateParams"]
    ) -> "TaxRate":
        return cast(
            "TaxRate",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["TaxRate.ListParams"]
    ) -> ListObject["TaxRate"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Unpack["TaxRate.ModifyParams"]) -> "TaxRate":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "TaxRate",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["TaxRate.RetrieveParams"]
    ) -> "TaxRate":
        instance = cls(id, **params)
        instance.refresh()
        return instance
