# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class CertificateCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    file: str
    """
    The ID of a file uploaded with purpose `tax_certificate`.
    """
    tax_exemption: str
    """
    The ID of an existing tax exemption.
    """
