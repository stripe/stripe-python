# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe.params.issuing._fraud_liability_debit_list_params import (
        FraudLiabilityDebitListParams,
    )
    from stripe.params.issuing._fraud_liability_debit_retrieve_params import (
        FraudLiabilityDebitRetrieveParams,
    )


class FraudLiabilityDebit(ListableAPIResource["FraudLiabilityDebit"]):
    """
    A fraud liability debit occurs when Stripe debits a platform's account for fraud losses on Issuing transactions.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.fraud_liability_debit"]] = (
        "issuing.fraud_liability_debit"
    )
    amount: int
    """
    Debited amount. This is equal to the disputed amount and is given in the card's currency and in the smallest currency unit.
    """
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    """
    ID of the [balance transaction](https://docs.stripe.com/api/balance_transactions) associated with this debit.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    The currency of the debit. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    dispute: str
    """
    The ID of the linked dispute.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["issuing.fraud_liability_debit"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def list(
        cls, **params: Unpack["FraudLiabilityDebitListParams"]
    ) -> ListObject["FraudLiabilityDebit"]:
        """
        Returns a list of Issuing FraudLiabilityDebit objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
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
        cls, **params: Unpack["FraudLiabilityDebitListParams"]
    ) -> ListObject["FraudLiabilityDebit"]:
        """
        Returns a list of Issuing FraudLiabilityDebit objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
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
        cls, id: str, **params: Unpack["FraudLiabilityDebitRetrieveParams"]
    ) -> "FraudLiabilityDebit":
        """
        Retrieves an Issuing FraudLiabilityDebit object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FraudLiabilityDebitRetrieveParams"]
    ) -> "FraudLiabilityDebit":
        """
        Retrieves an Issuing FraudLiabilityDebit object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
