# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceRenderingTemplateCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    line_item_policy: NotRequired[
        "InvoiceRenderingTemplateCreateParamsLineItemPolicy"
    ]
    """
    Controls how individual line items are displayed on the invoice, visible to customers.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nickname: NotRequired[str]
    """
    Nickname for the template that is hidden from customers
    """
    rendering_settings: NotRequired[
        "InvoiceRenderingTemplateCreateParamsRenderingSettings"
    ]
    """
    Rendering settings for invoices using this template.
    """
    summary_item_policies: NotRequired[
        List["InvoiceRenderingTemplateCreateParamsSummaryItemPolicy"]
    ]
    """
    Controls the grouping of line items into summary items which are displayed on the invoice, visible to customers. The policies are applied in order - only ungrouped line items from the previous policy are considered by the following policies.
    """


class InvoiceRenderingTemplateCreateParamsLineItemPolicy(TypedDict):
    display: NotRequired[str]
    """
    A CEL expression that takes a line item and returns a boolean indicating whether to display it on the invoice.
    """


class InvoiceRenderingTemplateCreateParamsRenderingSettings(TypedDict):
    invoice_pdf: NotRequired[
        "InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdf"
    ]
    """
    Rendering settings for the invoice PDF.
    """


class InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdf(
    TypedDict,
):
    blocks: NotRequired[
        "Literal['']|List[InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdfBlock]"
    ]
    """
    Ordered invoice PDF blocks. A maximum of 20 blocks is allowed.
    """


class InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdfBlock(
    TypedDict,
):
    custom_plain_text_cel: NotRequired[
        "InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdfBlockCustomPlainTextCel"
    ]
    """
    Configuration for a custom CEL text block.
    """
    key: NotRequired[str]
    """
    A unique key within this template's blocks. Generated when omitted.
    """
    type: Union[
        Literal[
            "custom_plain_text_cel",
            "footer_content",
            "invoice_details",
            "line_items",
            "parties",
            "payment_remittance_instructions",
            "status_and_memo",
            "tax_footnotes",
            "title_and_logo",
        ],
        str,
    ]
    """
    The type of content block.
    """


class InvoiceRenderingTemplateCreateParamsRenderingSettingsInvoicePdfBlockCustomPlainTextCel(
    TypedDict,
):
    cel_expression: str
    """
    A CEL expression that returns text using the invoice context.
    """


class InvoiceRenderingTemplateCreateParamsSummaryItemPolicy(TypedDict):
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
