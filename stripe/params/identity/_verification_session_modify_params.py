# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class VerificationSessionModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    options: NotRequired["VerificationSessionModifyParamsOptions"]
    """
    A set of options for the session's verification checks.
    """
    provided_details: NotRequired[
        "VerificationSessionModifyParamsProvidedDetails"
    ]
    """
    Details provided about the user being verified. These details may be shown to the user.
    """
    type: NotRequired[Literal["document", "id_number"]]
    """
    The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
    """


class VerificationSessionModifyParamsOptions(TypedDict):
    document: NotRequired[
        "Literal['']|VerificationSessionModifyParamsOptionsDocument"
    ]
    """
    Options that apply to the [document check](https://stripe.com/docs/identity/verification-checks?type=document).
    """


class VerificationSessionModifyParamsOptionsDocument(TypedDict):
    allowed_types: NotRequired[
        List[Literal["driving_license", "id_card", "passport"]]
    ]
    """
    Array of strings of allowed identity document types. If the provided identity document isn't one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
    """
    require_id_number: NotRequired[bool]
    """
    Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document's extracted name and date of birth.
    """
    require_live_capture: NotRequired[bool]
    """
    Disable image uploads, identity document images have to be captured using the device's camera.
    """
    require_matching_selfie: NotRequired[bool]
    """
    Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user's face. [Learn more](https://stripe.com/docs/identity/selfie).
    """


class VerificationSessionModifyParamsProvidedDetails(TypedDict):
    email: NotRequired[str]
    """
    Email of user being verified
    """
    phone: NotRequired[str]
    """
    Phone number of user being verified
    """
