# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import NotRequired, TypedDict


class AccountNoticeModifyParams(RequestOptions):
    email: "AccountNoticeModifyParamsEmail"
    """
    Information about the email you sent.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    sent_at: int
    """
    Date when you sent the notice.
    """


class AccountNoticeModifyParamsEmail(TypedDict):
    plain_text: str
    """
    Content of the email in plain text. The copy must match exactly the language that Stripe Compliance has approved for use.
    """
    recipient: str
    """
    Email address of the recipient.
    """
    subject: str
    """
    Subject of the email.
    """
