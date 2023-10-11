# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class TaxCode(ListableAPIResource["TaxCode"]):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    OBJECT_NAME = "tax_code"

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    description: str
    id: str
    name: str
    object: Literal["tax_code"]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["TaxCode.ListParams"]
    ) -> ListObject["TaxCode"]:
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
    def retrieve(
        cls, id: str, **params: Unpack["TaxCode.RetrieveParams"]
    ) -> "TaxCode":
        instance = cls(id, **params)
        instance.refresh()
        return instance
