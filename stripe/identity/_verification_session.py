# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.identity._verification_report import VerificationReport


class VerificationSession(
    CreateableAPIResource["VerificationSession"],
    ListableAPIResource["VerificationSession"],
    UpdateableAPIResource["VerificationSession"],
):
    """
    A VerificationSession guides you through the process of collecting and verifying the identities
    of your users. It contains details about the type of verification, such as what [verification
    check](https://stripe.com/docs/identity/verification-checks) to perform. Only create one VerificationSession for
    each verification in your system.

    A VerificationSession transitions through [multiple
    statuses](https://stripe.com/docs/identity/how-sessions-work) throughout its lifetime as it progresses through
    the verification flow. The VerificationSession contains the user's verified data after
    verification checks are complete.

    Related guide: [The Verification Sessions API](https://stripe.com/docs/identity/verification-sessions)
    """

    OBJECT_NAME: ClassVar[
        Literal["identity.verification_session"]
    ] = "identity.verification_session"

    class LastError(StripeObject):
        code: Optional[
            Literal[
                "abandoned",
                "consent_declined",
                "country_not_supported",
                "device_not_supported",
                "document_expired",
                "document_type_not_supported",
                "document_unverified_other",
                "id_number_insufficient_document_data",
                "id_number_mismatch",
                "id_number_unverified_other",
                "selfie_document_missing_photo",
                "selfie_face_mismatch",
                "selfie_manipulated",
                "selfie_unverified_other",
                "under_supported_age",
            ]
        ]
        """
        A short machine-readable string giving the reason for the verification or user-session failure.
        """
        reason: Optional[str]
        """
        A message that explains the reason for verification or user-session failure.
        """

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

    class Redaction(StripeObject):
        status: Literal["processing", "redacted"]
        """
        Indicates whether this object and its related objects have been redacted or not.
        """

    class VerifiedOutputs(StripeObject):
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

        address: Optional[Address]
        """
        The user's verified address.
        """
        dob: Optional[Dob]
        """
        The user's verified date of birth.
        """
        first_name: Optional[str]
        """
        The user's verified first name.
        """
        id_number: Optional[str]
        """
        The user's verified id number.
        """
        id_number_type: Optional[Literal["br_cpf", "sg_nric", "us_ssn"]]
        """
        The user's verified id number type.
        """
        last_name: Optional[str]
        """
        The user's verified last name.
        """
        _inner_class_types = {"address": Address, "dob": Dob}

    class CancelParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        options: NotRequired["VerificationSession.CreateParamsOptions"]
        """
        A set of options for the session's verification checks.
        """
        return_url: NotRequired["str"]
        """
        The URL that the user will be redirected to upon completing the verification flow.
        """
        type: Literal["document", "id_number"]
        """
        The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
        """

    class CreateParamsOptions(TypedDict):
        document: NotRequired[
            "Literal['']|VerificationSession.CreateParamsOptionsDocument"
        ]
        """
        Options that apply to the [document check](https://stripe.com/docs/identity/verification-checks?type=document).
        """

    class CreateParamsOptionsDocument(TypedDict):
        allowed_types: NotRequired[
            "List[Literal['driving_license', 'id_card', 'passport']]"
        ]
        """
        Array of strings of allowed identity document types. If the provided identity document isn't one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
        """
        require_id_number: NotRequired["bool"]
        """
        Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document's extracted name and date of birth.
        """
        require_live_capture: NotRequired["bool"]
        """
        Disable image uploads, identity document images have to be captured using the device's camera.
        """
        require_matching_selfie: NotRequired["bool"]
        """
        Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user's face. [Learn more](https://stripe.com/docs/identity/selfie).
        """

    class ListParams(RequestOptions):
        created: NotRequired["VerificationSession.ListParamsCreated|int"]
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
        status: NotRequired[
            "Literal['canceled', 'processing', 'requires_input', 'verified']"
        ]
        """
        Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).
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

    class ModifyParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        options: NotRequired["VerificationSession.ModifyParamsOptions"]
        """
        A set of options for the session's verification checks.
        """
        type: NotRequired["Literal['document', 'id_number']"]
        """
        The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
        """

    class ModifyParamsOptions(TypedDict):
        document: NotRequired[
            "Literal['']|VerificationSession.ModifyParamsOptionsDocument"
        ]
        """
        Options that apply to the [document check](https://stripe.com/docs/identity/verification-checks?type=document).
        """

    class ModifyParamsOptionsDocument(TypedDict):
        allowed_types: NotRequired[
            "List[Literal['driving_license', 'id_card', 'passport']]"
        ]
        """
        Array of strings of allowed identity document types. If the provided identity document isn't one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
        """
        require_id_number: NotRequired["bool"]
        """
        Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document's extracted name and date of birth.
        """
        require_live_capture: NotRequired["bool"]
        """
        Disable image uploads, identity document images have to be captured using the device's camera.
        """
        require_matching_selfie: NotRequired["bool"]
        """
        Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user's face. [Learn more](https://stripe.com/docs/identity/selfie).
        """

    class RedactParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    client_secret: Optional[str]
    """
    The short-lived client secret used by Stripe.js to [show a verification modal](https://stripe.com/docs/js/identity/modal) inside your app. This client secret expires after 24 hours and can only be used once. Don't store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on [passing the client secret to the frontend](https://stripe.com/docs/identity/verification-sessions#client-secret) to learn more.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last_error: Optional[LastError]
    """
    If present, this property tells you the last error encountered when processing the verification.
    """
    last_verification_report: Optional[ExpandableField["VerificationReport"]]
    """
    ID of the most recent VerificationReport. [Learn more about accessing detailed verification results.](https://stripe.com/docs/identity/verification-sessions#results)
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["identity.verification_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    options: Optional[Options]
    """
    A set of options for the session's verification checks.
    """
    redaction: Optional[Redaction]
    """
    Redaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.
    """
    status: Literal["canceled", "processing", "requires_input", "verified"]
    """
    Status of this VerificationSession. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).
    """
    type: Optional[Literal["document", "id_number"]]
    """
    The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
    """
    url: Optional[str]
    """
    The short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don't store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on [verifying identity documents](https://stripe.com/docs/identity/verify-identity-documents?platform=web&type=redirect) to learn how to redirect users to Stripe.
    """
    verified_outputs: Optional[VerifiedOutputs]
    """
    The user's verified data.
    """

    @classmethod
    def _cls_cancel(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        A VerificationSession object can be canceled when it is in requires_input [status](https://stripe.com/docs/identity/how-sessions-work).

        Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://stripe.com/docs/identity/verification-sessions#cancel).
        """
        return cast(
            "VerificationSession",
            cls._static_request(
                "post",
                "/v1/identity/verification_sessions/{session}/cancel".format(
                    session=_util.sanitize_id(session)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        A VerificationSession object can be canceled when it is in requires_input [status](https://stripe.com/docs/identity/how-sessions-work).

        Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://stripe.com/docs/identity/verification-sessions#cancel).
        """
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        A VerificationSession object can be canceled when it is in requires_input [status](https://stripe.com/docs/identity/how-sessions-work).

        Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://stripe.com/docs/identity/verification-sessions#cancel).
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        A VerificationSession object can be canceled when it is in requires_input [status](https://stripe.com/docs/identity/how-sessions-work).

        Once canceled, future submission attempts are disabled. This cannot be undone. [Learn more](https://stripe.com/docs/identity/verification-sessions#cancel).
        """
        return cast(
            "VerificationSession",
            self._request(
                "post",
                "/v1/identity/verification_sessions/{session}/cancel".format(
                    session=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        Creates a VerificationSession object.

        After the VerificationSession is created, display a verification modal using the session client_secret or send your users to the session's url.

        If your API key is in test mode, verification checks won't actually process, though everything else will occur as if in live mode.

        Related guide: [Verify your users' identity documents](https://stripe.com/docs/identity/verify-identity-documents)
        """
        return cast(
            "VerificationSession",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["VerificationSession"]:
        """
        Returns a list of VerificationSessions
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
    def modify(
        cls, id: str, **params: Unpack["VerificationSession.ModifyParams"]
    ) -> "VerificationSession":
        """
        Updates a VerificationSession object.

        When the session status is requires_input, you can use this method to update the
        verification check and options.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "VerificationSession",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_redact(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.RedactParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.

        A VerificationSession object can be redacted when it is in requires_input or verified
        [status](https://stripe.com/docs/identity/how-sessions-work). Redacting a VerificationSession in requires_action
        state will automatically cancel it.

        The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession's redaction.status field will be set to processing; when the process is
        finished, it will change to redacted and an identity.verification_session.redacted event
        will be emitted.

        Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string [redacted] or a similar
        placeholder. The metadata field will also be erased. Redacted objects cannot be updated or
        used for any purpose.

        [Learn more](https://stripe.com/docs/identity/verification-sessions#redact).
        """
        return cast(
            "VerificationSession",
            cls._static_request(
                "post",
                "/v1/identity/verification_sessions/{session}/redact".format(
                    session=_util.sanitize_id(session)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def redact(
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.RedactParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.

        A VerificationSession object can be redacted when it is in requires_input or verified
        [status](https://stripe.com/docs/identity/how-sessions-work). Redacting a VerificationSession in requires_action
        state will automatically cancel it.

        The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession's redaction.status field will be set to processing; when the process is
        finished, it will change to redacted and an identity.verification_session.redacted event
        will be emitted.

        Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string [redacted] or a similar
        placeholder. The metadata field will also be erased. Redacted objects cannot be updated or
        used for any purpose.

        [Learn more](https://stripe.com/docs/identity/verification-sessions#redact).
        """
        ...

    @overload
    def redact(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.RedactParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.

        A VerificationSession object can be redacted when it is in requires_input or verified
        [status](https://stripe.com/docs/identity/how-sessions-work). Redacting a VerificationSession in requires_action
        state will automatically cancel it.

        The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession's redaction.status field will be set to processing; when the process is
        finished, it will change to redacted and an identity.verification_session.redacted event
        will be emitted.

        Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string [redacted] or a similar
        placeholder. The metadata field will also be erased. Redacted objects cannot be updated or
        used for any purpose.

        [Learn more](https://stripe.com/docs/identity/verification-sessions#redact).
        """
        ...

    @class_method_variant("_cls_redact")
    def redact(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "VerificationSession.RedactParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "VerificationSession":
        """
        Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.

        A VerificationSession object can be redacted when it is in requires_input or verified
        [status](https://stripe.com/docs/identity/how-sessions-work). Redacting a VerificationSession in requires_action
        state will automatically cancel it.

        The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession's redaction.status field will be set to processing; when the process is
        finished, it will change to redacted and an identity.verification_session.redacted event
        will be emitted.

        Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string [redacted] or a similar
        placeholder. The metadata field will also be erased. Redacted objects cannot be updated or
        used for any purpose.

        [Learn more](https://stripe.com/docs/identity/verification-sessions#redact).
        """
        return cast(
            "VerificationSession",
            self._request(
                "post",
                "/v1/identity/verification_sessions/{session}/redact".format(
                    session=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["VerificationSession.RetrieveParams"]
    ) -> "VerificationSession":
        """
        Retrieves the details of a VerificationSession that was previously created.

        When the session status is requires_input, you can use this method to retrieve a valid
        client_secret or url to allow re-submission.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "last_error": LastError,
        "options": Options,
        "redaction": Redaction,
        "verified_outputs": VerifiedOutputs,
    }
