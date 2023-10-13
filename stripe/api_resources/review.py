# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class Review(ListableAPIResource["Review"]):
    """
    Reviews can be used to supplement automated fraud detection with human expertise.

    Learn more about [Radar](https://stripe.com/radar) and reviewing payments
    [here](https://stripe.com/docs/radar/reviews).
    """

    OBJECT_NAME = "review"
    if TYPE_CHECKING:

        class ApproveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            created: NotRequired["Review.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    billing_zip: Optional[str]
    charge: Optional[ExpandableField["Charge"]]
    closed_reason: Optional[
        Literal[
            "approved", "disputed", "redacted", "refunded", "refunded_as_fraud"
        ]
    ]
    created: int
    id: str
    ip_address: Optional[str]
    ip_address_location: Optional[StripeObject]
    livemode: bool
    object: Literal["review"]
    open: bool
    opened_reason: Literal["manual", "rule"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    reason: str
    session: Optional[StripeObject]

    @classmethod
    def _cls_approve(
        cls,
        review: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Review.ApproveParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/reviews/{review}/approve".format(
                review=util.sanitize_id(review)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_approve")
    def approve(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Review.ApproveParams"]
    ):
        return self._request(
            "post",
            "/v1/reviews/{review}/approve".format(
                review=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Review.ListParams"]
    ) -> ListObject["Review"]:
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
        cls, id: str, **params: Unpack["Review.RetrieveParams"]
    ) -> "Review":
        instance = cls(id, **params)
        instance.refresh()
        return instance
