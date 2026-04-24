# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ProductCatalogImport(StripeObject):
    """
    The product catalog import object tracks the long-running background process that handles uploading, processing and validation.
    """

    OBJECT_NAME: ClassVar[Literal["v2.commerce.product_catalog_import"]] = (
        "v2.commerce.product_catalog_import"
    )

    class StatusDetails(StripeObject):
        class AwaitingUpload(StripeObject):
            class UploadUrl(StripeObject):
                expires_at: str
                """
                The timestamp when the upload URL expires.
                """
                url: str
                """
                The pre-signed URL for uploading the catalog file.
                """

            upload_url: UploadUrl
            """
            The pre-signed URL information for uploading the catalog file.
            """
            _inner_class_types = {"upload_url": UploadUrl}

        class Failed(StripeObject):
            code: Literal["file_not_found", "internal_error", "invalid_file"]
            """
            The error code for this product catalog processing failure.
            """
            failure_message: str
            """
            A message explaining why the import failed.
            """
            type: Literal["cannot_proceed", "transient_failure"]
            """
            The error type for this product catalog processing failure.
            """

        class Processing(StripeObject):
            error_count: int
            """
            The number of records that failed to process so far.
            """
            success_count: int
            """
            The number of records processed so far.
            """
            _field_encodings = {
                "error_count": "int64_string",
                "success_count": "int64_string",
            }

        class Succeeded(StripeObject):
            success_count: int
            """
            The total number of records processed.
            """
            _field_encodings = {"success_count": "int64_string"}

        class SucceededWithErrors(StripeObject):
            class ErrorFile(StripeObject):
                class DownloadUrl(StripeObject):
                    expires_at: str
                    """
                    The timestamp when the download URL expires.
                    """
                    url: str
                    """
                    The pre-signed URL for downloading the error file.
                    """

                content_type: str
                """
                The MIME type of the error file.
                """
                download_url: DownloadUrl
                """
                The pre-signed URL information for downloading the error file.
                """
                size: int
                """
                The size of the error file in bytes.
                """
                _inner_class_types = {"download_url": DownloadUrl}
                _field_encodings = {"size": "int64_string"}

            class Sample(StripeObject):
                error_message: str
                """
                A description of what went wrong with this record.
                """
                field: str
                """
                The name of the field that caused the error.
                """
                id: str
                """
                The identifier of the record that failed to process.
                """
                row: int
                """
                The row number in the import file where the error occurred.
                """
                _field_encodings = {"row": "int64_string"}

            error_count: int
            """
            The total number of records that failed to process.
            """
            error_file: ErrorFile
            """
            A file containing details about all errors that occurred.
            """
            samples: List[Sample]
            """
            A sample of errors that occurred during processing.
            """
            success_count: int
            """
            The total number of records processed.
            """
            _inner_class_types = {"error_file": ErrorFile, "samples": Sample}
            _field_encodings = {
                "error_count": "int64_string",
                "success_count": "int64_string",
            }

        awaiting_upload: Optional[AwaitingUpload]
        """
        Details when the import is awaiting file upload.
        """
        failed: Optional[Failed]
        """
        Details when the import didn't complete.
        """
        processing: Optional[Processing]
        """
        Details when the import is processing.
        """
        succeeded: Optional[Succeeded]
        """
        Details when the import has succeeded.
        """
        succeeded_with_errors: Optional[SucceededWithErrors]
        """
        Details when the import completed but some records failed to process.
        """
        _inner_class_types = {
            "awaiting_upload": AwaitingUpload,
            "failed": Failed,
            "processing": Processing,
            "succeeded": Succeeded,
            "succeeded_with_errors": SucceededWithErrors,
        }

    created: str
    """
    The time this ProductCatalogImport was created.
    """
    feed_type: Literal["inventory", "pricing", "product"]
    """
    The type of feed data being imported into the product catalog.
    """
    id: str
    """
    The unique identifier for this ProductCatalogImport.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: UntypedStripeObject[str]
    """
    Additional information about the object in a structured format.
    """
    object: Literal["v2.commerce.product_catalog_import"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal[
        "awaiting_upload",
        "failed",
        "processing",
        "succeeded",
        "succeeded_with_errors",
    ]
    """
    The current status of this ProductCatalogImport.
    """
    status_details: Optional[StatusDetails]
    """
    Details about the current import status.
    """
    _inner_class_types = {"status_details": StatusDetails}
