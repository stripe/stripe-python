# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        options: NotRequired[
            Optional["VerificationSession.CreateOptionsParams"]
        ]
        return_url: NotRequired[Optional[str]]
        type: Literal["document", "id_number"]

    class CreateOptionsParams(TypedDict):
        document: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "VerificationSession.CreateOptionsDocumentParams",
                ]
            ]
        ]

    class CreateOptionsDocumentParams(TypedDict):
        allowed_types: NotRequired[
            Optional[List[Literal["driving_license", "id_card", "passport"]]]
        ]
        require_id_number: NotRequired[Optional[bool]]
        require_live_capture: NotRequired[Optional[bool]]
        require_matching_selfie: NotRequired[Optional[bool]]

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["VerificationSession.ListCreatedParams", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[
                Literal["canceled", "processing", "requires_input", "verified"]
            ]
        ]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        options: NotRequired[
            Optional["VerificationSession.ModifyOptionsParams"]
        ]
        type: NotRequired[Optional[Literal["document", "id_number"]]]

    class ModifyOptionsParams(TypedDict):
        document: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "VerificationSession.ModifyOptionsDocumentParams",
                ]
            ]
        ]

    class ModifyOptionsDocumentParams(TypedDict):
        allowed_types: NotRequired[
            Optional[List[Literal["driving_license", "id_card", "passport"]]]
        ]
        require_id_number: NotRequired[Optional[bool]]
        require_live_capture: NotRequired[Optional[bool]]
        require_matching_selfie: NotRequired[Optional[bool]]

    class RedactParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
