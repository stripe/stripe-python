# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.tax_code import TaxCode


class ShippingRate(
    CreateableAPIResource["ShippingRate"],
    ListableAPIResource["ShippingRate"],
    UpdateableAPIResource["ShippingRate"],
):
    """
    Shipping rates describe the price of shipping presented to your customers and
    applied to a purchase. For more information, see [Charge for shipping](https://stripe.com/docs/payments/during-payment/charge-shipping).
    """

    OBJECT_NAME: ClassVar[Literal["shipping_rate"]] = "shipping_rate"

    class DeliveryEstimate(StripeObject):
        class Maximum(StripeObject):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            """
            A unit of time.
            """
            value: int
            """
            Must be greater than 0.
            """

        class Minimum(StripeObject):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            """
            A unit of time.
            """
            value: int
            """
            Must be greater than 0.
            """

        maximum: Optional[Maximum]
        """
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
        """
        minimum: Optional[Minimum]
        """
        The lower bound of the estimated range. If empty, represents no lower bound.
        """
        _inner_class_types = {"maximum": Maximum, "minimum": Minimum}

    class FixedAmount(StripeObject):
        class CurrencyOptions(StripeObject):
            amount: int
            """
            A non-negative integer in cents representing how much to charge.
            """
            tax_behavior: Literal["exclusive", "inclusive", "unspecified"]
            """
            Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            """

        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        currency_options: Optional[Dict[str, CurrencyOptions]]
        """
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """
        _inner_class_types = {"currency_options": CurrencyOptions}
        _inner_class_dicts = ["currency_options"]

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            delivery_estimate: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimate|None"
            ]
            """
            The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
            """
            display_name: str
            """
            The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fixed_amount: NotRequired[
                "ShippingRate.CreateParamsFixedAmount|None"
            ]
            """
            Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            """
            tax_code: NotRequired["str|None"]
            """
            A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
            """
            type: NotRequired["Literal['fixed_amount']|None"]
            """
            The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now.
            """

        class CreateParamsFixedAmount(TypedDict):
            amount: int
            """
            A non-negative integer in cents representing how much to charge.
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            currency_options: NotRequired[
                "Dict[str, ShippingRate.CreateParamsFixedAmountCurrencyOptions]|None"
            ]
            """
            Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
            """

        class CreateParamsFixedAmountCurrencyOptions(TypedDict):
            amount: int
            """
            A non-negative integer in cents representing how much to charge.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            """

        class CreateParamsDeliveryEstimate(TypedDict):
            maximum: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimateMaximum|None"
            ]
            """
            The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
            """
            minimum: NotRequired[
                "ShippingRate.CreateParamsDeliveryEstimateMinimum|None"
            ]
            """
            The lower bound of the estimated range. If empty, represents no lower bound.
            """

        class CreateParamsDeliveryEstimateMinimum(TypedDict):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            """
            A unit of time.
            """
            value: int
            """
            Must be greater than 0.
            """

        class CreateParamsDeliveryEstimateMaximum(TypedDict):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            """
            A unit of time.
            """
            value: int
            """
            Must be greater than 0.
            """

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            """
            Only return shipping rates that are active or inactive.
            """
            created: NotRequired["ShippingRate.ListParamsCreated|int|None"]
            """
            A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            """
            currency: NotRequired["str|None"]
            """
            Only return shipping rates for the given currency.
            """
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

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            """
            Whether the shipping rate can be used for new purchases. Defaults to `true`.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fixed_amount: NotRequired[
                "ShippingRate.ModifyParamsFixedAmount|None"
            ]
            """
            Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            """

        class ModifyParamsFixedAmount(TypedDict):
            currency_options: NotRequired[
                "Dict[str, ShippingRate.ModifyParamsFixedAmountCurrencyOptions]|None"
            ]
            """
            Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
            """

        class ModifyParamsFixedAmountCurrencyOptions(TypedDict):
            amount: NotRequired["int|None"]
            """
            A non-negative integer in cents representing how much to charge.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    active: bool
    """
    Whether the shipping rate can be used for new purchases. Defaults to `true`.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    delivery_estimate: Optional[DeliveryEstimate]
    """
    The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    display_name: Optional[str]
    """
    The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    fixed_amount: Optional[FixedAmount]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["shipping_rate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """
    tax_code: Optional[ExpandableField["TaxCode"]]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    """
    type: Literal["fixed_amount"]
    """
    The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ShippingRate.CreateParams"]
    ) -> "ShippingRate":
        """
        Creates a new shipping rate object.
        """
        return cast(
            "ShippingRate",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ShippingRate.ListParams"]
    ) -> ListObject["ShippingRate"]:
        """
        Returns a list of your shipping rates.
        """
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
    def modify(
        cls, id: str, **params: Unpack["ShippingRate.ModifyParams"]
    ) -> "ShippingRate":
        """
        Updates an existing shipping rate object.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "ShippingRate",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ShippingRate.RetrieveParams"]
    ) -> "ShippingRate":
        """
        Returns the shipping rate object with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "delivery_estimate": DeliveryEstimate,
        "fixed_amount": FixedAmount,
    }
