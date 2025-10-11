# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class BlocklistEntryCreateParams(RequestOptions):
    check_existing_verifications: NotRequired[bool]
    """
    When true, the created BlocklistEntry will be used to retroactively unverify matching verifications.
    """
    entry_type: Literal["document", "selfie"]
    """
    The type of blocklist entry to be created.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    verification_report: str
    """
    The identifier of the VerificationReport to create the BlocklistEntry from.
    """
