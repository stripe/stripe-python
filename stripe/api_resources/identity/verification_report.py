# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


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
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired[
                "VerificationReport.ListParamsCreated|int|None"
            ]
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            type: NotRequired["Literal['document', 'id_number']|None"]
            """
            Only return VerificationReports of this type
            """
            verification_session: NotRequired["str|None"]
            """
            Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    document: Optional[StripeObject]
    """
    Result from a document check
    """
    id: str
    """
    Unique identifier for the object.
    """
    id_number: Optional[StripeObject]
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
    options: Optional[StripeObject]
    selfie: Optional[StripeObject]
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
        **params: Unpack["VerificationReport.ListParams"]
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
        cls, id: str, **params: Unpack["VerificationReport.RetrieveParams"]
    ) -> "VerificationReport":
        instance = cls(id, **params)
        instance.refresh()
        return instance
