# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceRenderingTemplateModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    line_item_policy: NotRequired[
        "Literal['']|InvoiceRenderingTemplateModifyParamsLineItemPolicy"
    ]
    """
    Controls how individual line items are displayed on the invoice, visible to customers.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nickname: NotRequired[str]
    """
    Nickname for the template that is hidden from customers
    """
    summary_item_policies: NotRequired[
        "Literal['']|List[InvoiceRenderingTemplateModifyParamsSummaryItemPolicy]"
    ]
    """
    Controls the grouping of line items into summary items which are displayed on the invoice, visible to customers. The policies are applied in order - only ungrouped line items from the previous policy are considered by the following policies.
    """


class InvoiceRenderingTemplateModifyParamsLineItemPolicy(TypedDict):
    display: NotRequired[str]
    """
    A CEL expression that takes a line item and returns a boolean indicating whether to display it on the invoice.
    """


class InvoiceRenderingTemplateModifyParamsSummaryItemPolicy(TypedDict):
    display_items: NotRequired["Literal['all', 'none']|str"]
    """
    Controls how each summary group is rendered on the invoice. `all` displays the summary line item, its constituent line items, and a group subtotal. `none` displays only the summary line item. Defaults to `all`.
    """
    filter: NotRequired[str]
    """
    A CEL expression that takes a line item and returns a boolean indicating whether to include it in this grouping policy. If omitted, includes all ungrouped line items.
    """
    group_by: NotRequired[str]
    """
    A CEL expression that takes a line item and returns a string. Line items with the same result are grouped into a summary item, using that result as its group title.
    """
