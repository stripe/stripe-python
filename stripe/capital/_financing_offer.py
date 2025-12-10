# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, Optional, cast, overload
from typing_extensions import Literal, Type, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.capital._financing_offer_create_params import (
        FinancingOfferCreateParams,
    )
    from stripe.params.capital._financing_offer_list_params import (
        FinancingOfferListParams,
    )
    from stripe.params.capital._financing_offer_mark_delivered_params import (
        FinancingOfferMarkDeliveredParams,
    )
    from stripe.params.capital._financing_offer_refill_params import (
        FinancingOfferRefillParams,
    )
    from stripe.params.capital._financing_offer_retrieve_params import (
        FinancingOfferRetrieveParams,
    )


class FinancingOffer(ListableAPIResource["FinancingOffer"]):
    """
    This is an object representing an offer of financing from
    Stripe Capital to a Connect subaccount.
    """

    OBJECT_NAME: ClassVar[Literal["capital.financing_offer"]] = (
        "capital.financing_offer"
    )

    class AcceptedTerms(StripeObject):
        advance_amount: int
        """
        Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.
        """
        currency: str
        """
        Currency that the financing offer is transacted in. For example, `usd`.
        """
        fee_amount: int
        """
        Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.
        """
        previous_financing_fee_discount_amount: Optional[int]
        """
        Populated when the `product_type` of the `financingoffer` is `refill`.
        Represents the discount amount on remaining premium for the existing loan at payout time.
        """
        withhold_rate: float
        """
        Per-transaction rate at which Stripe withholds funds to repay the financing.
        """

    class OfferedTerms(StripeObject):
        advance_amount: int
        """
        Amount of financing offered, in minor units. For example, 1,000 USD is represented as 100000.
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
        Fixed fee amount, in minor units. For example, 100 USD is represented as 10000.
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
        Per-transaction rate at which Stripe withholds funds to repay the financing.
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
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
    type: Optional[Literal["cash_advance", "fixed_term_loan", "flex_loan"]]
    """
    See [financing_type](https://docs.stripe.com/api/capital/connect_financing_object#financing_offer_object-financing_type).
    """

    @classmethod
    def list(
        cls, **params: Unpack["FinancingOfferListParams"]
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
        cls, **params: Unpack["FinancingOfferListParams"]
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
        **params: Unpack["FinancingOfferMarkDeliveredParams"],
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
        **params: Unpack["FinancingOfferMarkDeliveredParams"],
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @overload
    def mark_delivered(
        self, **params: Unpack["FinancingOfferMarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @class_method_variant("_cls_mark_delivered")
    def mark_delivered(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FinancingOfferMarkDeliveredParams"]
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
        **params: Unpack["FinancingOfferMarkDeliveredParams"],
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
        **params: Unpack["FinancingOfferMarkDeliveredParams"],
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @overload
    async def mark_delivered_async(
        self, **params: Unpack["FinancingOfferMarkDeliveredParams"]
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        ...

    @class_method_variant("_cls_mark_delivered_async")
    async def mark_delivered_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FinancingOfferMarkDeliveredParams"]
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
        cls, id: str, **params: Unpack["FinancingOfferRetrieveParams"]
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FinancingOfferRetrieveParams"]
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    class TestHelpers(APIResourceTestHelpers["FinancingOffer"]):
        _resource_cls: Type["FinancingOffer"]

        @classmethod
        def create(
            cls, **params: Unpack["FinancingOfferCreateParams"]
        ) -> "FinancingOffer":
            """
            Creates a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/capital/financing_offers",
                    params=params,
                ),
            )

        @classmethod
        async def create_async(
            cls, **params: Unpack["FinancingOfferCreateParams"]
        ) -> "FinancingOffer":
            """
            Creates a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/capital/financing_offers",
                    params=params,
                ),
            )

        @classmethod
        def _cls_refill(
            cls,
            financing_offer: str,
            **params: Unpack["FinancingOfferRefillParams"],
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                        financing_offer=sanitize_id(financing_offer)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def refill(
            financing_offer: str,
            **params: Unpack["FinancingOfferRefillParams"],
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            ...

        @overload
        def refill(
            self, **params: Unpack["FinancingOfferRefillParams"]
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            ...

        @class_method_variant("_cls_refill")
        def refill(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["FinancingOfferRefillParams"]
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                        financing_offer=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_refill_async(
            cls,
            financing_offer: str,
            **params: Unpack["FinancingOfferRefillParams"],
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                        financing_offer=sanitize_id(financing_offer)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def refill_async(
            financing_offer: str,
            **params: Unpack["FinancingOfferRefillParams"],
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            ...

        @overload
        async def refill_async(
            self, **params: Unpack["FinancingOfferRefillParams"]
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            ...

        @class_method_variant("_cls_refill_async")
        async def refill_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["FinancingOfferRefillParams"]
        ) -> "FinancingOffer":
            """
            Refills a test financing offer for a connected account.
            """
            return cast(
                "FinancingOffer",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                        financing_offer=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "accepted_terms": AcceptedTerms,
        "offered_terms": OfferedTerms,
    }


FinancingOffer.TestHelpers._resource_cls = FinancingOffer
