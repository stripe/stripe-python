# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._project_create_params import (
        ProjectCreateParams,
    )
    from stripe.v2.provisioning._project import Project


class ProjectService(StripeService):
    def create(
        self,
        params: "ProjectCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Project":
        """
        Creates a new project.
        """
        return cast(
            "Project",
            self._request(
                "post",
                "/v2/provisioning/projects",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ProjectCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Project":
        """
        Creates a new project.
        """
        return cast(
            "Project",
            await self._request_async(
                "post",
                "/v2/provisioning/projects",
                base_address="api",
                params=params,
                options=options,
            ),
        )
