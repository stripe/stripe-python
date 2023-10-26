# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


class FinancingOffer(ListableAPIResource["FinancingOffer"]):
    """
    This is an object representing an offer of financing from
    Stripe Capital to a Connect subaccount.
    """

    OBJECT_NAME: ClassVar[
        Literal["capital.financing_offer"]
    ] = "capital.financing_offer"

    class AcceptedTerms(StripeObject):
        advance_amount: int
        """
        Amount of financing offered, in minor units.
        """
        currency: str
        """
        Currency that the financing offer is transacted in. For example, `usd`.
        """
        fee_amount: int
        """
        Fixed fee amount, in minor units.
        """
        previous_financing_fee_discount_amount: Optional[int]
        """
        Populated when the `product_type` of the `financingoffer` is `refill`.
        Represents the discount amount on remaining premium for the existing loan at payout time.
        """
        withhold_rate: float
        """
        Per-transaction rate at which Stripe will withhold funds to repay the financing.
        """

    class OfferedTerms(StripeObject):
        advance_amount: int
        """
        Amount of financing offered, in minor units.
        """
        campaign_type: Literal[
            "newly_eligible_user", "previously_eligible_user", "repeat_user"
        ]
        """
        Describes the type of user the offer is being extended to.
        """
        currency: str
        """
        Currency that the financing offer is transacted in. For example, `usd`.
        """
        fee_amount: int
        """
        Fixed fee amount, in minor units.
        """
        previous_financing_fee_discount_rate: Optional[float]
        """
        Populated when the `product_type` of the `financingoffer` is `refill`.
        Represents the discount rate percentage on remaining fee on the existing loan. When the `financing_offer`
        is paid out, the `previous_financing_fee_discount_amount` will be computed as the multiple of this rate
        and the remaining fee.
        """
        withhold_rate: float
        """
        Per-transaction rate at which Stripe will withhold funds to repay the financing.
        """

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            connected_account: NotRequired["str|None"]
            """
            limit list to offers belonging to given connected account
            """
            created: NotRequired["FinancingOffer.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['accepted', 'canceled', 'completed', 'delivered', 'expired', 'fully_repaid', 'paid_out', 'rejected', 'revoked', 'undelivered']|None"
            ]
            """
            limit list to offers with given status
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class MarkDeliveredParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    accepted_terms: Optional[AcceptedTerms]
    """
    This is an object representing the terms of an offer of financing from
    Stripe Capital to a Connected account. This resource represents
    the terms accepted by the Connected account, which may differ from those
    offered.
    """
    account: str
    """
    The ID of the merchant associated with this financing object.
    """
    created: int
    """
    Time at which the offer was created. Given in seconds since unix epoch.
    """
    expires_after: float
    """
    Time at which the offer expires. Given in seconds since unix epoch.
    """
    financing_type: Optional[Literal["cash_advance", "flex_loan"]]
    """
    The type of financing being offered.
    """
    id: str
    """
    A unique identifier for the financing object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["capital.financing_offer"]
    """
    The object type: financing_offer.
    """
    offered_terms: Optional[OfferedTerms]
    """
    This is an object representing the terms of an offer of financing from
    Stripe Capital to a Connected account. This resource represents
    both the terms offered to the Connected account.
    """
    product_type: Optional[Literal["refill", "standard"]]
    """
    Financing product identifier.
    """
    replacement: Optional[str]
    """
    The ID of the financing offer that replaced this offer.
    """
    replacement_for: Optional[str]
    """
    The ID of the financing offer that this offer is a replacement for.
    """
    status: Literal[
        "accepted",
        "canceled",
        "completed",
        "delivered",
        "expired",
        "fully_repaid",
        "paid_out",
        "rejected",
        "replaced",
        "undelivered",
    ]
    """
    The current status of the offer.
    """
    type: Optional[Literal["cash_advance", "flex_loan"]]
    """
    See [financing_type](https://stripe.com/docs/api/capital/connect_financing_object#financing_offer_object-financing_type).
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancingOffer.ListParams"]
    ) -> ListObject["FinancingOffer"]:
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
    def _cls_mark_delivered(
        cls,
        financing_offer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        return cast(
            "FinancingOffer",
            cls._static_request(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=util.sanitize_id(financing_offer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def mark_delivered(
        cls,
        financing_offer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        ...

    @overload
    def mark_delivered(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        ...

    @class_method_variant("_cls_mark_delivered")
    def mark_delivered(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        return cast(
            "FinancingOffer",
            self._request(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FinancingOffer.RetrieveParams"]
    ) -> "FinancingOffer":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "accepted_terms": AcceptedTerms,
        "offered_terms": OfferedTerms,
    }
