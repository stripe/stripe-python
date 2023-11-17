# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


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

    OBJECT_NAME: ClassVar[
        Literal["identity.verification_report"]
    ] = "identity.verification_report"

    class Document(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        class Dob(StripeObject):
            day: Optional[int]
            """
            Numerical day between 1 and 31.
            """
            month: Optional[int]
            """
            Numerical month between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year.
            """

        class Error(StripeObject):
            code: Optional[
                Literal[
                    "document_expired",
                    "document_type_not_supported",
                    "document_unverified_other",
                ]
            ]
            """
            A short machine-readable string giving the reason for the verification failure.
            """
            reason: Optional[str]
            """
            A human-readable message giving the reason for the failure. These messages can be shown to your users.
            """

        class ExpirationDate(StripeObject):
            day: Optional[int]
            """
            Numerical day between 1 and 31.
            """
            month: Optional[int]
            """
            Numerical month between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year.
            """

        class IssuedDate(StripeObject):
            day: Optional[int]
            """
            Numerical day between 1 and 31.
            """
            month: Optional[int]
            """
            Numerical month between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year.
            """

        address: Optional[Address]
        """
        Address as it appears in the document.
        """
        dob: Optional[Dob]
        """
        Date of birth as it appears in the document.
        """
        error: Optional[Error]
        """
        Details on the verification error. Present when status is `unverified`.
        """
        expiration_date: Optional[ExpirationDate]
        """
        Expiration date of the document.
        """
        files: Optional[List[str]]
        """
        Array of [File](https://stripe.com/docs/api/files) ids containing images for this document.
        """
        first_name: Optional[str]
        """
        First name as it appears in the document.
        """
        issued_date: Optional[IssuedDate]
        """
        Issued date of the document.
        """
        issuing_country: Optional[str]
        """
        Issuing country of the document.
        """
        last_name: Optional[str]
        """
        Last name as it appears in the document.
        """
        number: Optional[str]
        """
        Document ID number.
        """
        status: Literal["unverified", "verified"]
        """
        Status of this `document` check.
        """
        type: Optional[Literal["driving_license", "id_card", "passport"]]
        """
        Type of the document.
        """
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
            """
            Numerical day between 1 and 31.
            """
            month: Optional[int]
            """
            Numerical month between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year.
            """

        class Error(StripeObject):
            code: Optional[
                Literal[
                    "id_number_insufficient_document_data",
                    "id_number_mismatch",
                    "id_number_unverified_other",
                ]
            ]
            """
            A short machine-readable string giving the reason for the verification failure.
            """
            reason: Optional[str]
            """
            A human-readable message giving the reason for the failure. These messages can be shown to your users.
            """

        dob: Optional[Dob]
        """
        Date of birth.
        """
        error: Optional[Error]
        """
        Details on the verification error. Present when status is `unverified`.
        """
        first_name: Optional[str]
        """
        First name.
        """
        id_number: Optional[str]
        """
        ID number.
        """
        id_number_type: Optional[Literal["br_cpf", "sg_nric", "us_ssn"]]
        """
        Type of ID number.
        """
        last_name: Optional[str]
        """
        Last name.
        """
        status: Literal["unverified", "verified"]
        """
        Status of this `id_number` check.
        """
        _inner_class_types = {"dob": Dob, "error": Error}

    class Options(StripeObject):
        class Document(StripeObject):
            allowed_types: Optional[
                List[Literal["driving_license", "id_card", "passport"]]
            ]
            """
            Array of strings of allowed identity document types. If the provided identity document isn't one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
            """
            require_id_number: Optional[bool]
            """
            Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document's extracted name and date of birth.
            """
            require_live_capture: Optional[bool]
            """
            Disable image uploads, identity document images have to be captured using the device's camera.
            """
            require_matching_selfie: Optional[bool]
            """
            Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user's face. [Learn more](https://stripe.com/docs/identity/selfie).
            """

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
            """
            A short machine-readable string giving the reason for the verification failure.
            """
            reason: Optional[str]
            """
            A human-readable message giving the reason for the failure. These messages can be shown to your users.
            """

        document: Optional[str]
        """
        ID of the [File](https://stripe.com/docs/api/files) holding the image of the identity document used in this check.
        """
        error: Optional[Error]
        """
        Details on the verification error. Present when status is `unverified`.
        """
        selfie: Optional[str]
        """
        ID of the [File](https://stripe.com/docs/api/files) holding the image of the selfie used in this check.
        """
        status: Literal["unverified", "verified"]
        """
        Status of this `selfie` check.
        """
        _inner_class_types = {"error": Error}

    class ListParams(RequestOptions):
        created: NotRequired["VerificationReport.ListParamsCreated|int"]
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        type: NotRequired["Literal['document', 'id_number']"]
        """
        Only return VerificationReports of this type
        """
        verification_session: NotRequired["str"]
        """
        Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    document: Optional[Document]
    """
    Result from a document check
    """
    id: str
    """
    Unique identifier for the object.
    """
    id_number: Optional[IdNumber]
    """
    Result from an id_number check
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["identity.verification_report"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    options: Optional[Options]
    selfie: Optional[Selfie]
    """
    Result from a selfie check
    """
    type: Optional[Literal["document", "id_number"]]
    """
    Type of report.
    """
    verification_session: Optional[str]
    """
    ID of the VerificationSession that created this report.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationReport.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["VerificationReport"]:
        """
        List all verification reports.
        """
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
        cls, id: str, **params: Unpack["VerificationReport.RetrieveParams"]
    ) -> "VerificationReport":
        """
        Retrieves an existing VerificationReport
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "document": Document,
        "id_number": IdNumber,
        "options": Options,
        "selfie": Selfie,
    }
