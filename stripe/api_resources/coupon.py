# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Coupon(
    CreateableAPIResource["Coupon"],
    DeletableAPIResource["Coupon"],
    ListableAPIResource["Coupon"],
    UpdateableAPIResource["Coupon"],
):
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).
    """

    OBJECT_NAME = "coupon"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount_off: NotRequired["int|None"]
            applies_to: NotRequired["Coupon.CreateParamsAppliesTo|None"]
            currency: NotRequired["str|None"]
            currency_options: NotRequired[
                "Dict[str, Coupon.CreateParamsCurrencyOptions]|None"
            ]
            duration: NotRequired[
                "Literal['forever', 'once', 'repeating']|None"
            ]
            duration_in_months: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            id: NotRequired["str|None"]
            max_redemptions: NotRequired["int|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: NotRequired["str|None"]
            percent_off: NotRequired["float|None"]
            redeem_by: NotRequired["int|None"]

        class CreateParamsCurrencyOptions(TypedDict):
            amount_off: int

        class CreateParamsAppliesTo(TypedDict):
            products: NotRequired["List[str]|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["Coupon.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            currency_options: NotRequired[
                "Dict[str, Coupon.ModifyParamsCurrencyOptions]|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: NotRequired["str|None"]

        class ModifyParamsCurrencyOptions(TypedDict):
            amount_off: int

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount_off: Optional[int]
    applies_to: Optional[StripeObject]
    created: int
    currency: Optional[str]
    currency_options: Optional[Dict[str, StripeObject]]
    duration: Literal["forever", "once", "repeating"]
    duration_in_months: Optional[int]
    id: str
    livemode: bool
    max_redemptions: Optional[int]
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["coupon"]
    percent_off: Optional[float]
    redeem_by: Optional[int]
    times_redeemed: int
    valid: bool
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Coupon.CreateParams"]
    ) -> "Coupon":
        return cast(
            "Coupon",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Coupon.DeleteParams"]
    ) -> "Coupon":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Coupon",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Coupon.DeleteParams"]) -> "Coupon":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Coupon.ListParams"]
    ) -> ListObject["Coupon"]:
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
    def modify(cls, id, **params: Unpack["Coupon.ModifyParams"]) -> "Coupon":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Coupon",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Coupon.RetrieveParams"]
    ) -> "Coupon":
        instance = cls(id, **params)
        instance.refresh()
        return instance
