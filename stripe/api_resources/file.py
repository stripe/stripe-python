# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.file_link import FileLink


class File(ListableAPIResource["File"]):
    """
    This object represents files hosted on Stripe's servers. You can upload
    files with the [create file](https://stripe.com/docs/api#create_file) request
    (for example, when uploading dispute evidence). Stripe also
    creates files independetly (for example, the results of a [Sigma scheduled
    query](https://stripe.com/docs/api#scheduled_queries)).

    Related guide: [File upload guide](https://stripe.com/docs/file-upload)
    """

    OBJECT_NAME = "file"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired["File.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            purpose: NotRequired[
                "Literal['account_requirement', 'additional_verification', 'business_icon', 'business_logo', 'customer_signature', 'dispute_evidence', 'document_provider_identity_document', 'finance_report_run', 'identity_document', 'identity_document_downloadable', 'pci_document', 'selfie', 'sigma_scheduled_query', 'tax_document_user_upload', 'terminal_reader_splashscreen']|None"
            ]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    created: int
    expires_at: Optional[int]
    filename: Optional[str]
    id: str
    links: Optional[ListObject["FileLink"]]
    object: Literal["file"]
    purpose: Literal[
        "account_requirement",
        "additional_verification",
        "business_icon",
        "business_logo",
        "customer_signature",
        "dispute_evidence",
        "document_provider_identity_document",
        "finance_report_run",
        "identity_document",
        "identity_document_downloadable",
        "pci_document",
        "selfie",
        "sigma_scheduled_query",
        "tax_document_user_upload",
        "terminal_reader_splashscreen",
    ]
    size: int
    title: Optional[str]
    type: Optional[str]
    url: Optional[str]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["File.ListParams"]
    ) -> ListObject["File"]:
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
        cls, id: str, **params: Unpack["File.RetrieveParams"]
    ) -> "File":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    # This resource can have two different object names. In latter API
    # versions, only `file` is used, but since stripe-python may be used with
    # any API version, we need to support deserializing the older
    # `file_upload` object into the same class.
    OBJECT_NAME_ALT = "file_upload"

    @classmethod
    def class_url(cls):
        return "/v1/files"

    @classmethod
    def create(
        # 'api_version' is deprecated, please use 'stripe_version'
        cls,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = cls.class_url()
        supplied_headers = {"Content-Type": "multipart/form-data"}
        response, api_key = requestor.request(
            "post", url, params=params, headers=supplied_headers
        )
        return util.convert_to_stripe_object(
            response, api_key, version, stripe_account
        )


# For backwards compatibility, the `File` class is aliased to `FileUpload`.
FileUpload = File
