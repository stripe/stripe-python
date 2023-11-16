# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import ClassVar, List, Optional, cast
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

    OBJECT_NAME: ClassVar[Literal["file"]] = "file"

    class ListParams(RequestOptions):
        created: NotRequired["File.ListParamsCreated|int"]
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
        purpose: NotRequired[
            "Literal['account_requirement', 'additional_verification', 'business_icon', 'business_logo', 'customer_signature', 'dispute_evidence', 'document_provider_identity_document', 'finance_report_run', 'identity_document', 'identity_document_downloadable', 'pci_document', 'selfie', 'sigma_scheduled_query', 'tax_document_user_upload', 'terminal_reader_splashscreen']"
        ]
        """
        Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
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
    expires_at: Optional[int]
    """
    The file expires and isn't available at this time in epoch seconds.
    """
    filename: Optional[str]
    """
    The suitable name for saving the file to a filesystem.
    """
    id: str
    """
    Unique identifier for the object.
    """
    links: Optional[ListObject["FileLink"]]
    """
    A list of [file links](https://stripe.com/docs/api#file_links) that point at this file.
    """
    object: Literal["file"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
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
    """
    The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file.
    """
    size: int
    """
    The size of the file object in bytes.
    """
    title: Optional[str]
    """
    A suitable title for the document.
    """
    type: Optional[str]
    """
    The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`).
    """
    url: Optional[str]
    """
    Use your live secret API key to download the file from this URL.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "File.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["File"]:
        """
        Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.
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
        cls, id: str, **params: Unpack["File.RetrieveParams"]
    ) -> "File":
        """
        Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to [access file contents](https://stripe.com/docs/file-upload#download-file-contents).
        """
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
    ) -> "File":
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
        return cast(
            "File",
            util.convert_to_stripe_object(
                response, api_key, version, stripe_account
            ),
        )


# For backwards compatibility, the `File` class is aliased to `FileUpload`.
FileUpload = File
