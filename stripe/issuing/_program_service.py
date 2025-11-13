# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.issuing._program import Program
    from stripe.params.issuing._program_create_params import (
        ProgramCreateParams,
    )
    from stripe.params.issuing._program_list_params import ProgramListParams
    from stripe.params.issuing._program_retrieve_params import (
        ProgramRetrieveParams,
    )
    from stripe.params.issuing._program_update_params import (
        ProgramUpdateParams,
    )


class ProgramService(StripeService):
    def list(
        self,
        params: Optional["ProgramListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Program]":
        """
        List all of the programs the given Issuing user has access to.
        """
        return cast(
            "ListObject[Program]",
            self._request(
                "get",
                "/v1/issuing/programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ProgramListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Program]":
        """
        List all of the programs the given Issuing user has access to.
        """
        return cast(
            "ListObject[Program]",
            await self._request_async(
                "get",
                "/v1/issuing/programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ProgramCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Create a Program object.
        """
        return cast(
            "Program",
            self._request(
                "post",
                "/v1/issuing/programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ProgramCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Create a Program object.
        """
        return cast(
            "Program",
            await self._request_async(
                "post",
                "/v1/issuing/programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        program: str,
        params: Optional["ProgramRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Retrieves the program specified by the given id.
        """
        return cast(
            "Program",
            self._request(
                "get",
                "/v1/issuing/programs/{program}".format(
                    program=sanitize_id(program),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        program: str,
        params: Optional["ProgramRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Retrieves the program specified by the given id.
        """
        return cast(
            "Program",
            await self._request_async(
                "get",
                "/v1/issuing/programs/{program}".format(
                    program=sanitize_id(program),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        program: str,
        params: Optional["ProgramUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Updates a Program object.
        """
        return cast(
            "Program",
            self._request(
                "post",
                "/v1/issuing/programs/{program}".format(
                    program=sanitize_id(program),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        program: str,
        params: Optional["ProgramUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Program":
        """
        Updates a Program object.
        """
        return cast(
            "Program",
            await self._request_async(
                "post",
                "/v1/issuing/programs/{program}".format(
                    program=sanitize_id(program),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
