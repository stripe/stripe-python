# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class Schema(ListableAPIResource["Schema"]):
    """
    Contains information about the tables in a reporting Schema.
    """

    OBJECT_NAME: ClassVar[Literal["sigma.schema"]] = "sigma.schema"

    class Table(StripeObject):
        class Column(StripeObject):
            comment: str
            foreign_key: Optional[str]
            name: str
            primary_key: bool
            type: str

        columns: List[Column]
        comment: str
        name: str
        section: str
        _inner_class_types = {"columns": Column}

    class ListParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        product: NotRequired[Literal["sigma", "stripe_data_pipeline"]]

    name: str
    object: Literal["sigma.schema"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    tables: List[Table]

    @classmethod
    def list(
        cls, **params: Unpack["Schema.ListParams"]
    ) -> ListObject["Schema"]:
        """
        Lists the schemas available to the authorized merchant in Stripe's data products
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Schema.ListParams"]
    ) -> ListObject["Schema"]:
        """
        Lists the schemas available to the authorized merchant in Stripe's data products
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    _inner_class_types = {"tables": Table}
