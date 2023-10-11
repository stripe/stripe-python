# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        country: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        display_name: str
        expand: NotRequired[Optional[List[str]]]
        inclusive: bool
        jurisdiction: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        percentage: float
        state: NotRequired[Optional[str]]
        tax_type: NotRequired[
            Optional[
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
        ]

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        created: NotRequired[Optional[Union["TaxRate.ListCreatedParams", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        inclusive: NotRequired[Optional[bool]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        country: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        display_name: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        jurisdiction: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        state: NotRequired[Optional[str]]
        tax_type: NotRequired[
            Optional[
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
        ]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
