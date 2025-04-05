# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class RedactionJobValidationError(
    ListableAPIResource["RedactionJobValidationError"],
):
    """
    Validation errors
    """

    OBJECT_NAME: ClassVar[
        Literal["privacy.redaction_job_validation_error"]
    ] = "privacy.redaction_job_validation_error"

    class ListParams(RequestOptions):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    code: str
    erroring_object: Optional[Dict[str, str]]
    id: str
    """
    Unique identifier for the object.
    """
    message: str
    object: Literal["privacy.redaction_job_validation_error"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def list(
        cls, **params: Unpack["RedactionJobValidationError.ListParams"]
    ) -> ListObject["RedactionJobValidationError"]:
        """
        List validation errors method
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["RedactionJobValidationError.ListParams"]
    ) -> ListObject["RedactionJobValidationError"]:
        """
        List validation errors method
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
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
        cls,
        id: str,
        **params: Unpack["RedactionJobValidationError.RetrieveParams"],
    ) -> "RedactionJobValidationError":
        """
        Retrieve validation error method
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["RedactionJobValidationError.RetrieveParams"],
    ) -> "RedactionJobValidationError":
        """
        Retrieve validation error method
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
