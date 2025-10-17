# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._license_fee_create_params import (
        LicenseFeeCreateParams,
    )
    from stripe.params.v2.billing._license_fee_list_params import (
        LicenseFeeListParams,
    )
    from stripe.params.v2.billing._license_fee_retrieve_params import (
        LicenseFeeRetrieveParams,
    )
    from stripe.params.v2.billing._license_fee_update_params import (
        LicenseFeeUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._license_fee import LicenseFee
    from stripe.v2.billing.license_fees._version_service import VersionService

_subservices = {
    "versions": [
        "stripe.v2.billing.license_fees._version_service",
        "VersionService",
    ],
}


class LicenseFeeService(StripeService):
    versions: "VersionService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: "LicenseFeeListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicenseFee]":
        """
        List all License Fee objects.
        """
        return cast(
            "ListObject[LicenseFee]",
            self._request(
                "get",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "LicenseFeeListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[LicenseFee]":
        """
        List all License Fee objects.
        """
        return cast(
            "ListObject[LicenseFee]",
            await self._request_async(
                "get",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "LicenseFeeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Create a License Fee object.
        """
        return cast(
            "LicenseFee",
            self._request(
                "post",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "LicenseFeeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Create a License Fee object.
        """
        return cast(
            "LicenseFee",
            await self._request_async(
                "post",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["LicenseFeeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Retrieve a License Fee object.
        """
        return cast(
            "LicenseFee",
            self._request(
                "get",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["LicenseFeeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Retrieve a License Fee object.
        """
        return cast(
            "LicenseFee",
            await self._request_async(
                "get",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["LicenseFeeUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Update a License Fee object.
        """
        return cast(
            "LicenseFee",
            self._request(
                "post",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["LicenseFeeUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "LicenseFee":
        """
        Update a License Fee object.
        """
        return cast(
            "LicenseFee",
            await self._request_async(
                "post",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
