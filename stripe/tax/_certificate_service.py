# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.tax._certificate_create_params import (
        CertificateCreateParams,
    )
    from stripe.params.tax._certificate_delete_params import (
        CertificateDeleteParams,
    )
    from stripe.params.tax._certificate_list_params import (
        CertificateListParams,
    )
    from stripe.params.tax._certificate_retrieve_params import (
        CertificateRetrieveParams,
    )
    from stripe.tax._certificate import Certificate


class CertificateService(StripeService):
    def delete(
        self,
        id: str,
        /,
        params: Optional["CertificateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            self._request(
                "delete",
                "/v1/tax/certificates/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        /,
        params: Optional["CertificateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            await self._request_async(
                "delete",
                "/v1/tax/certificates/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["CertificateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Retrieve a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            self._request(
                "get",
                "/v1/tax/certificates/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["CertificateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Retrieve a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            await self._request_async(
                "get",
                "/v1/tax/certificates/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "CertificateListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Certificate]":
        """
        List certificates for an existing tax exemption.
        """
        return cast(
            "ListObject[Certificate]",
            self._request(
                "get",
                "/v1/tax/certificates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CertificateListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Certificate]":
        """
        List certificates for an existing tax exemption.
        """
        return cast(
            "ListObject[Certificate]",
            await self._request_async(
                "get",
                "/v1/tax/certificates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CertificateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Create a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            self._request(
                "post",
                "/v1/tax/certificates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CertificateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Certificate":
        """
        Create a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            await self._request_async(
                "post",
                "/v1/tax/certificates",
                base_address="api",
                params=params,
                options=options,
            ),
        )
