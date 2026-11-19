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
    A Tax Certificate associates an uploaded exemption or resale certificate file with a customer's tax exemption. A tax exemption can have multiple certificates. Deleting a tax exemption also deletes its certificates, but retains their uploaded files.
    """

    OBJECT_NAME: ClassVar[Literal["tax.certificate"]] = "tax.certificate"
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deleted: bool
    """
    If `true`, the certificate has been deleted. If `false`, it hasn't been deleted.
    """
    file: ExpandableField["File"]
    """
    The ID of the uploaded certificate [file](https://docs.stripe.com/api/files/object).
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
    The ID of the [customer tax exemption](https://docs.stripe.com/api/tax/exemptions/object) associated with this certificate.
    """

    @classmethod
    def create(
        cls, **params: Unpack["CertificateCreateParams"]
    ) -> "Certificate":
        """
        Creates a Tax Certificate associated with a tax exemption. Before creating the certificate, [upload a file](https://docs.stripe.com/api/files/create) with purpose tax_certificate.
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
        Creates a Tax Certificate associated with a tax exemption. Before creating the certificate, [upload a file](https://docs.stripe.com/api/files/create) with purpose tax_certificate.
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
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
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
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
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
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
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
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(
        self, **params: Unpack["CertificateDeleteParams"]
    ) -> "Certificate":
        """
        Deletes a Tax Certificate without deleting its uploaded file. You can reuse the file to create another certificate, and you can still retrieve the deleted certificate.
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
        Lists a tax exemption's certificates, ordered from newest to oldest. The list excludes deleted certificates.
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
        Lists a tax exemption's certificates, ordered from newest to oldest. The list excludes deleted certificates.
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
        Retrieves a Tax Certificate. Deleted certificates remain retrievable with all their fields and deleted set to true.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["CertificateRetrieveParams"]
    ) -> "Certificate":
        """
        Retrieves a Tax Certificate. Deleted certificates remain retrievable with all their fields and deleted set to true.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
