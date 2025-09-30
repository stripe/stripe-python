# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class FormListParams(RequestOptions):
    ending_before: NotRequired[str]
    """
    A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    limit: NotRequired[int]
    """
    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    """
    payee: "FormListParamsPayee"
    """
    The payee whose volume is represented on the tax form.
    """
    starting_after: NotRequired[str]
    """
    A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    """
    type: NotRequired[
        Literal[
            "au_serr",
            "ca_mrdp",
            "eu_dac7",
            "gb_mrdp",
            "nz_mrdp",
            "us_1099_k",
            "us_1099_misc",
            "us_1099_nec",
        ]
    ]
    """
    An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future tax form types. If your integration expects only one type of tax form in the response, make sure to provide a type value in the request.
    """


class FormListParamsPayee(TypedDict):
    account: NotRequired[str]
    """
    The ID of the Stripe account whose forms will be retrieved.
    """
    external_reference: NotRequired[str]
    """
    The external reference to the payee whose forms will be retrieved.
    """
    type: NotRequired[Literal["account", "external_reference"]]
    """
    Specifies the payee type. Either `account` or `external_reference`.
    """
