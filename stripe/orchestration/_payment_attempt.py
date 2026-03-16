# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.orchestration._payment_attempt_retrieve_params import (
        PaymentAttemptRetrieveParams,
    )


class PaymentAttempt(APIResource["PaymentAttempt"]):
    """
    Represents orchestration information for a payment attempt record (e.g. return url).
    """

    OBJECT_NAME: ClassVar[Literal["orchestration.payment_attempt"]] = (
        "orchestration.payment_attempt"
    )
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["orchestration.payment_attempt"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    return_url: Optional[str]
    """
    If present, the return URL for this payment attempt.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentAttemptRetrieveParams"]
    ) -> "PaymentAttempt":
        """
        Retrieves orchestration information for the given payment attempt record (e.g. return url).
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentAttemptRetrieveParams"]
    ) -> "PaymentAttempt":
        """
        Retrieves orchestration information for the given payment attempt record (e.g. return url).
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance
