# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer_tax_exemption import CustomerTaxExemption
    from stripe._file import File
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


class Certificate(
    CreateableAPIResource["Certificate"],
    DeletableAPIResource["Certificate"],
    ListableAPIResource["Certificate"],
):
    """
    Tax exemption and resale certificates associated with tax exemptions.
    """

    OBJECT_NAME: ClassVar[Literal["tax.certificate"]] = "tax.certificate"
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deleted: bool
    """
    Whether the certificate has been deleted.
    """
    file: ExpandableField["File"]
    """
    The uploaded certificate file.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["tax.certificate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    tax_exemption: Optional[ExpandableField["CustomerTaxExemption"]]
    """
    The tax exemption associated with this certificate.
    """

    @classmethod
    def create(
        cls, **params: Unpack["CertificateCreateParams"]
    ) -> "Certificate":
        """
        Create a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["CertificateCreateParams"]
    ) -> "Certificate":
        """
        Create a tax certificate associated with a tax exemption.
        """
        return cast(
            "Certificate",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, /, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Certificate",
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, /, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, /, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Certificate",
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, /, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Delete a tax certificate associated with a tax exemption.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls, **params: Unpack["CertificateListParams"]
    ) -> ListObject["Certificate"]:
        """
        List certificates for an existing tax exemption.
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
        cls, **params: Unpack["CertificateListParams"]
    ) -> ListObject["Certificate"]:
        """
        List certificates for an existing tax exemption.
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
        cls, id: str, **params: Unpack["CertificateRetrieveParams"]
    ) -> "Certificate":
        """
        Retrieve a tax certificate associated with a tax exemption.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["CertificateRetrieveParams"]
    ) -> "Certificate":
        """
        Retrieve a tax certificate associated with a tax exemption.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
