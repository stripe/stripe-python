# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


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

    class ListParams(RequestOptions):
        connected_account: NotRequired["str"]
        """
        limit list to offers belonging to given connected account
        """
        created: NotRequired["FinancingOffer.ListParamsCreated|int"]
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            "Literal['accepted', 'canceled', 'completed', 'delivered', 'expired', 'fully_repaid', 'paid_out', 'rejected', 'revoked', 'undelivered']"
        ]
        """
        limit list to offers with given status
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class MarkDeliveredParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
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
    charged_off_at: Optional[int]
    """
    The time at which this financing offer was charged off, if applicable. Given in seconds since unix epoch.
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
        cls, **params: Unpack["FinancingOffer.ListParams"]
    ) -> ListObject["FinancingOffer"]:
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
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
        cls, **params: Unpack["FinancingOffer.ListParams"]
    ) -> ListObject["FinancingOffer"]:
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
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
    def _cls_mark_delivered(
        cls,
        financing_offer: str,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            cls._static_request(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(financing_offer)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def mark_delivered(
        financing_offer: str,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @overload
    def mark_delivered(
        self, **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @class_method_variant("_cls_mark_delivered")
    def mark_delivered(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            self._request(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_mark_delivered_async(
        cls,
        financing_offer: str,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            await cls._static_request_async(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(financing_offer)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def mark_delivered_async(
        financing_offer: str,
        **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @overload
    async def mark_delivered_async(
        self, **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @class_method_variant("_cls_mark_delivered_async")
    async def mark_delivered_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FinancingOffer.MarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            await self._request_async(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FinancingOffer.RetrieveParams"]
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FinancingOffer.RetrieveParams"]
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "accepted_terms": AcceptedTerms,
        "offered_terms": OfferedTerms,
    }
