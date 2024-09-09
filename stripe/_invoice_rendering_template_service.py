# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._invoice_rendering_template import InvoiceRenderingTemplate
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceRenderingTemplateService(StripeService):
    class ArchiveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(TypedDict):
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
        status: NotRequired[Literal["active", "archived"]]

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        version: NotRequired[int]

    class UnarchiveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "InvoiceRenderingTemplateService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceRenderingTemplate]:
        """
        List all templates, ordered by creation date, with the most recently created template appearing first.
        """
        return cast(
            ListObject[InvoiceRenderingTemplate],
            self._request(
                "get",
                "/v1/invoice_rendering_templates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InvoiceRenderingTemplateService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceRenderingTemplate]:
        """
        List all templates, ordered by creation date, with the most recently created template appearing first.
        """
        return cast(
            ListObject[InvoiceRenderingTemplate],
            await self._request_async(
                "get",
                "/v1/invoice_rendering_templates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.
        """
        return cast(
            InvoiceRenderingTemplate,
            self._request(
                "get",
                "/v1/invoice_rendering_templates/{template}".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.
        """
        return cast(
            InvoiceRenderingTemplate,
            await self._request_async(
                "get",
                "/v1/invoice_rendering_templates/{template}".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def archive(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Updates the status of an invoice rendering template to ‘archived' so no new Stripe objects (customers, invoices, etc.) can reference it. The template can also no longer be updated. However, if the template is already set on a Stripe object, it will continue to be applied on invoices generated by it.
        """
        return cast(
            InvoiceRenderingTemplate,
            self._request(
                "post",
                "/v1/invoice_rendering_templates/{template}/archive".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def archive_async(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.ArchiveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Updates the status of an invoice rendering template to ‘archived' so no new Stripe objects (customers, invoices, etc.) can reference it. The template can also no longer be updated. However, if the template is already set on a Stripe object, it will continue to be applied on invoices generated by it.
        """
        return cast(
            InvoiceRenderingTemplate,
            await self._request_async(
                "post",
                "/v1/invoice_rendering_templates/{template}/archive".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def unarchive(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.UnarchiveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Unarchive an invoice rendering template so it can be used on new Stripe objects again.
        """
        return cast(
            InvoiceRenderingTemplate,
            self._request(
                "post",
                "/v1/invoice_rendering_templates/{template}/unarchive".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def unarchive_async(
        self,
        template: str,
        params: "InvoiceRenderingTemplateService.UnarchiveParams" = {},
        options: RequestOptions = {},
    ) -> InvoiceRenderingTemplate:
        """
        Unarchive an invoice rendering template so it can be used on new Stripe objects again.
        """
        return cast(
            InvoiceRenderingTemplate,
            await self._request_async(
                "post",
                "/v1/invoice_rendering_templates/{template}/unarchive".format(
                    template=sanitize_id(template),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
