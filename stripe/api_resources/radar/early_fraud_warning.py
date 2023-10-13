# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class EarlyFraudWarning(ListableAPIResource["EarlyFraudWarning"]):
    """
    An early fraud warning indicates that the card issuer has notified us that a
    charge may be fraudulent.

    Related guide: [Early fraud warnings](https://stripe.com/docs/disputes/measuring#early-fraud-warnings)
    """

    OBJECT_NAME = "radar.early_fraud_warning"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            charge: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payment_intent: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    actionable: bool
    charge: ExpandableField["Charge"]
    created: int
    fraud_type: str
    id: str
    livemode: bool
    object: Literal["radar.early_fraud_warning"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["EarlyFraudWarning.ListParams"]
    ) -> ListObject["EarlyFraudWarning"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
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
        cls, id: str, **params: Unpack["EarlyFraudWarning.RetrieveParams"]
    ) -> "EarlyFraudWarning":
        instance = cls(id, **params)
        instance.refresh()
        return instance
