# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.issuing._program_create_params import (
        ProgramCreateParams,
    )
    from stripe.params.issuing._program_list_params import ProgramListParams
    from stripe.params.issuing._program_modify_params import (
        ProgramModifyParams,
    )
    from stripe.params.issuing._program_retrieve_params import (
        ProgramRetrieveParams,
    )


class Program(
    CreateableAPIResource["Program"],
    ListableAPIResource["Program"],
    UpdateableAPIResource["Program"],
):
    """
    An Issuing `Program` represents a card program that the user has access to.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.program"]] = "issuing.program"
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    is_default: bool
    """
    Whether or not this is the "default" issuing program new cards are created on. Only one active `is_default` program at the same time.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["issuing.program"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    platform_program: Optional[str]
    """
    The platform's Issuing Program for which this program is associated.
    """

    @classmethod
    def create(cls, **params: Unpack["ProgramCreateParams"]) -> "Program":
        """
        Create a Program object.
        """
        return cast(
            "Program",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["ProgramCreateParams"]
    ) -> "Program":
        """
        Create a Program object.
        """
        return cast(
            "Program",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["ProgramListParams"]
    ) -> ListObject["Program"]:
        """
        List all of the programs the given Issuing user has access to.
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
        cls, **params: Unpack["ProgramListParams"]
    ) -> ListObject["Program"]:
        """
        List all of the programs the given Issuing user has access to.
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
    def modify(
        cls, id: str, **params: Unpack["ProgramModifyParams"]
    ) -> "Program":
        """
        Updates a Program object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Program",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["ProgramModifyParams"]
    ) -> "Program":
        """
        Updates a Program object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Program",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ProgramRetrieveParams"]
    ) -> "Program":
        """
        Retrieves the program specified by the given id.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["ProgramRetrieveParams"]
    ) -> "Program":
        """
        Retrieves the program specified by the given id.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
