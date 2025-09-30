# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.financial_connections._institution_list_params import (
        InstitutionListParams,
    )
    from stripe.params.financial_connections._institution_retrieve_params import (
        InstitutionRetrieveParams,
    )


class Institution(ListableAPIResource["Institution"]):
    """
    An institution represents a financial institution to which an end user can connect using the Financial Connections authentication flow.
    """

    OBJECT_NAME: ClassVar[Literal["financial_connections.institution"]] = (
        "financial_connections.institution"
    )

    class Features(StripeObject):
        class Balances(StripeObject):
            supported: bool
            """
            Whether the given feature is supported by this institution.
            """

        class Ownership(StripeObject):
            supported: bool
            """
            Whether the given feature is supported by this institution.
            """

        class PaymentMethod(StripeObject):
            supported: bool
            """
            Whether the given feature is supported by this institution.
            """

        class Transactions(StripeObject):
            supported: bool
            """
            Whether the given feature is supported by this institution.
            """

        balances: Balances
        ownership: Ownership
        payment_method: PaymentMethod
        transactions: Transactions
        _inner_class_types = {
            "balances": Balances,
            "ownership": Ownership,
            "payment_method": PaymentMethod,
            "transactions": Transactions,
        }

    countries: List[str]
    """
    The list of countries supported by this institution, formatted as ISO country codes.
    """
    features: Features
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str
    """
    The name of this institution.
    """
    object: Literal["financial_connections.institution"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    routing_numbers: List[str]
    """
    A list of routing numbers which are known to correspond to this institution. Due to the many to many relationship between institutions and routing numbers, this list may not be comprehensive and routing numbers may also be shared between institutions.
    """
    status: Literal["active", "degraded", "inactive"]
    """
    The status of this institution in the Financial Connections authentication flow.
    """
    url: Optional[str]
    """
    A URL corresponding to this institution. This URL is also displayed in the authentication flow to help end users confirm that they are authenticating with the right institution.
    """

    @classmethod
    def list(
        cls, **params: Unpack["InstitutionListParams"]
    ) -> ListObject["Institution"]:
        """
        Returns a list of Financial Connections Institution objects.
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
        cls, **params: Unpack["InstitutionListParams"]
    ) -> ListObject["Institution"]:
        """
        Returns a list of Financial Connections Institution objects.
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
        cls, id: str, **params: Unpack["InstitutionRetrieveParams"]
    ) -> "Institution":
        """
        Retrieves the details of a Financial Connections Institution.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["InstitutionRetrieveParams"]
    ) -> "Institution":
        """
        Retrieves the details of a Financial Connections Institution.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"features": Features}
