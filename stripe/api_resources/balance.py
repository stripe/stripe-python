# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import SingletonAPIResource
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class Balance(SingletonAPIResource["Balance"]):
    """
    This is an object representing your Stripe balance. You can retrieve it to see
    the balance currently on your Stripe account.

    You can also retrieve the balance history, which contains a list of
    [transactions](https://stripe.com/docs/reporting/balance-transaction-types) that contributed to the balance
    (charges, payouts, and so forth).

    The available and pending amounts for each currency are broken down further by
    payment source types.

    Related guide: [Understanding Connect account balances](https://stripe.com/docs/connect/account-balances)
    """

    OBJECT_NAME: ClassVar[Literal["balance"]] = "balance"
    if TYPE_CHECKING:

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    available: List[StripeObject]
    """
    Available funds that you can transfer or pay out automatically by Stripe or explicitly through the [Transfers API](https://stripe.com/docs/api#transfers) or [Payouts API](https://stripe.com/docs/api#payouts). You can find the available balance for each currency and payment type in the `source_types` property.
    """
    connect_reserved: Optional[List[StripeObject]]
    """
    Funds held due to negative balances on connected Custom accounts. You can find the connect reserve balance for each currency and payment type in the `source_types` property.
    """
    instant_available: Optional[List[StripeObject]]
    """
    Funds that you can pay out using Instant Payouts.
    """
    issuing: Optional[StripeObject]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending: List[StripeObject]
    """
    Funds that aren't available in the balance yet. You can find the pending balance for each currency and each payment type in the `source_types` property.
    """

    @classmethod
    def retrieve(cls, **params: Unpack["Balance.RetrieveParams"]) -> "Balance":
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/balance"
