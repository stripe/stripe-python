# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.identity.verification_report import (
        VerificationReport,
    )


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

    OBJECT_NAME = "identity.verification_session"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            options: NotRequired[
                "VerificationSession.CreateParamsOptions|None"
            ]
            return_url: NotRequired["str|None"]
            type: Literal["document", "id_number"]

        class CreateParamsOptions(TypedDict):
            document: NotRequired[
                "Literal['']|VerificationSession.CreateParamsOptionsDocument|None"
            ]

        class CreateParamsOptionsDocument(TypedDict):
            allowed_types: NotRequired[
                "List[Literal['driving_license', 'id_card', 'passport']]|None"
            ]
            require_id_number: NotRequired["bool|None"]
            require_live_capture: NotRequired["bool|None"]
            require_matching_selfie: NotRequired["bool|None"]

        class ListParams(RequestOptions):
            created: NotRequired[
                "VerificationSession.ListParamsCreated|int|None"
            ]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['canceled', 'processing', 'requires_input', 'verified']|None"
            ]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            options: NotRequired[
                "VerificationSession.ModifyParamsOptions|None"
            ]
            type: NotRequired["Literal['document', 'id_number']|None"]

        class ModifyParamsOptions(TypedDict):
            document: NotRequired[
                "Literal['']|VerificationSession.ModifyParamsOptionsDocument|None"
            ]

        class ModifyParamsOptionsDocument(TypedDict):
            allowed_types: NotRequired[
                "List[Literal['driving_license', 'id_card', 'passport']]|None"
            ]
            require_id_number: NotRequired["bool|None"]
            require_live_capture: NotRequired["bool|None"]
            require_matching_selfie: NotRequired["bool|None"]

        class RedactParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    client_secret: Optional[str]
    created: int
    id: str
    last_error: Optional[StripeObject]
    last_verification_report: Optional[ExpandableField["VerificationReport"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["identity.verification_session"]
    options: Optional[StripeObject]
    redaction: Optional[StripeObject]
    status: Literal["canceled", "processing", "requires_input", "verified"]
    type: Optional[Literal["document", "id_number"]]
    url: Optional[str]
    verified_outputs: Optional[StripeObject]

    @classmethod
    def _cls_cancel(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["VerificationSession.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/identity/verification_sessions/{session}/cancel".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["VerificationSession.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/identity/verification_sessions/{session}/cancel".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["VerificationSession.CreateParams"]
    ) -> "VerificationSession":
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
        **params: Unpack["VerificationSession.ListParams"]
    ) -> ListObject["VerificationSession"]:
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
        cls, id, **params: Unpack["VerificationSession.ModifyParams"]
    ) -> "VerificationSession":
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
        **params: Unpack["VerificationSession.RedactParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/identity/verification_sessions/{session}/redact".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_redact")
    def redact(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["VerificationSession.RedactParams"]
    ):
        return self._request(
            "post",
            "/v1/identity/verification_sessions/{session}/redact".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["VerificationSession.RetrieveParams"]
    ) -> "VerificationSession":
        instance = cls(id, **params)
        instance.refresh()
        return instance
