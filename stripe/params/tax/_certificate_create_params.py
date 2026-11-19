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
    The ID of a [file](https://docs.stripe.com/api/files/object) uploaded with purpose `tax_certificate`. The file must belong to the same account and mode as the tax exemption. You can't use a deleted file or a file attached to another certificate that hasn't been deleted.
    """
    tax_exemption: str
    """
    The ID of an existing [customer tax exemption](https://docs.stripe.com/api/tax/exemptions/object) that hasn't been deleted.
    """
