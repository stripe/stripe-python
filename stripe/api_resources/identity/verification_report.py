# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal


class VerificationReport(ListableAPIResource["VerificationReport"]):
    """
    A VerificationReport is the result of an attempt to collect and verify data from a user.
    The collection of verification checks performed is determined from the `type` and `options`
    parameters used. You can find the result of each verification check performed in the
    appropriate sub-resource: `document`, `id_number`, `selfie`.

    Each VerificationReport contains a copy of any data collected by the user as well as
    reference IDs which can be used to access collected images through the [FileUpload](https://stripe.com/docs/api/files)
    API. To configure and create VerificationReports, use the
    [VerificationSession](https://stripe.com/docs/api/identity/verification_sessions) API.

    Related guides: [Accessing verification results](https://stripe.com/docs/identity/verification-sessions#results).
    """

    OBJECT_NAME = "identity.verification_report"

    class Document(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        class Dob(StripeObject):
            day: Optional[int]
            month: Optional[int]
            year: Optional[int]

        class Error(StripeObject):
            code: Optional[
                Literal[
                    "document_expired",
                    "document_type_not_supported",
                    "document_unverified_other",
                ]
            ]
            reason: Optional[str]

        class ExpirationDate(StripeObject):
            day: Optional[int]
            month: Optional[int]
            year: Optional[int]

        class IssuedDate(StripeObject):
            day: Optional[int]
            month: Optional[int]
            year: Optional[int]

        address: Optional[Address]
        dob: Optional[Dob]
        error: Optional[Error]
        expiration_date: Optional[ExpirationDate]
        files: Optional[List[str]]
        first_name: Optional[str]
        issued_date: Optional[IssuedDate]
        issuing_country: Optional[str]
        last_name: Optional[str]
        number: Optional[str]
        status: Literal["unverified", "verified"]
        type: Optional[Literal["driving_license", "id_card", "passport"]]
        _inner_class_types = {
            "address": Address,
            "dob": Dob,
            "error": Error,
            "expiration_date": ExpirationDate,
            "issued_date": IssuedDate,
        }

    class IdNumber(StripeObject):
        class Dob(StripeObject):
            day: Optional[int]
            month: Optional[int]
            year: Optional[int]

        class Error(StripeObject):
            code: Optional[
                Literal[
                    "id_number_insufficient_document_data",
                    "id_number_mismatch",
                    "id_number_unverified_other",
                ]
            ]
            reason: Optional[str]

        dob: Optional[Dob]
        error: Optional[Error]
        first_name: Optional[str]
        id_number: Optional[str]
        id_number_type: Optional[Literal["br_cpf", "sg_nric", "us_ssn"]]
        last_name: Optional[str]
        status: Literal["unverified", "verified"]
        _inner_class_types = {"dob": Dob, "error": Error}

    class Options(StripeObject):
        class Document(StripeObject):
            allowed_types: Optional[
                List[Literal["driving_license", "id_card", "passport"]]
            ]
            require_id_number: Optional[bool]
            require_live_capture: Optional[bool]
            require_matching_selfie: Optional[bool]

        class IdNumber(StripeObject):
            pass

        document: Optional[Document]
        id_number: Optional[IdNumber]
        _inner_class_types = {"document": Document, "id_number": IdNumber}

    class Selfie(StripeObject):
        class Error(StripeObject):
            code: Optional[
                Literal[
                    "selfie_document_missing_photo",
                    "selfie_face_mismatch",
                    "selfie_manipulated",
                    "selfie_unverified_other",
                ]
            ]
            reason: Optional[str]

        document: Optional[str]
        error: Optional[Error]
        selfie: Optional[str]
        status: Literal["unverified", "verified"]
        _inner_class_types = {"error": Error}

    created: int
    document: Optional[Document]
    id: str
    id_number: Optional[IdNumber]
    livemode: bool
    object: Literal["identity.verification_report"]
    options: Optional[Options]
    selfie: Optional[Selfie]
    type: Optional[Literal["document", "id_number"]]
    verification_session: Optional[str]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["VerificationReport"]:
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "VerificationReport":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "document": Document,
        "id_number": IdNumber,
        "options": Options,
        "selfie": Selfie,
    }
