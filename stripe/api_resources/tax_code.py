# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class TaxCode(ListableAPIResource["TaxCode"]):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    OBJECT_NAME = "tax_code"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
