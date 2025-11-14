# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._fx_quote_create_params import FxQuoteCreateParams
    from stripe.params._fx_quote_list_params import FxQuoteListParams
    from stripe.params._fx_quote_retrieve_params import FxQuoteRetrieveParams


class FxQuote(
    CreateableAPIResource["FxQuote"], ListableAPIResource["FxQuote"]
):
    """
    The FX Quotes API provides three functions:
    - View Stripe's current exchange rate for any given currency pair.
    - Extend quoted rates for a 1-hour period or a 24-hour period, minimizing uncertainty from FX fluctuations.
    - Preview the FX fees Stripe will charge on your FX transaction, allowing you to anticipate specific settlement amounts before payment costs.

    [View the docs](https://docs.stripe.com/payments/currencies/localize-prices/fx-quotes-api)
    """

    OBJECT_NAME: ClassVar[Literal["fx_quote"]] = "fx_quote"

    class Rates(StripeObject):
        class RateDetails(StripeObject):
            base_rate: float
            """
            The rate for the currency pair.
            """
            duration_premium: float
            """
            The fee for locking the conversion rates.
            """
            fx_fee_rate: float
            """
            The FX fee for the currency pair.
            """
            reference_rate: Optional[float]
            """
            A reference rate for the currency pair provided by the reference rate provider.
            """
            reference_rate_provider: Optional[Literal["ecb"]]
            """
            The reference rate provider.
            """

        exchange_rate: float
        """
        The rate that includes the FX fee rate.
        """
        rate_details: RateDetails
        _inner_class_types = {"rate_details": RateDetails}

    class Usage(StripeObject):
        class Payment(StripeObject):
            destination: Optional[str]
            """
            The Stripe account ID that the funds will be transferred to.

            This field should match the account ID that would be used in the PaymentIntent's transfer_data[destination] field.
            """
            on_behalf_of: Optional[str]
            """
            The Stripe account ID that these funds are intended for.

            This field must match the account ID that would be used in the PaymentIntent's on_behalf_of field.
            """

        class Transfer(StripeObject):
            destination: str
            """
            The Stripe account ID that the funds will be transferred to.

            This field should match the account ID that would be used in the Transfer's destination field.
            """

        payment: Optional[Payment]
        """
        The details required to use an FX Quote for a payment
        """
        transfer: Optional[Transfer]
        """
        The details required to use an FX Quote for a transfer
        """
        type: Literal["payment", "transfer"]
        """
        The transaction type for which the FX Quote will be used.

        Can be 'payment' or 'transfer'.
        """
        _inner_class_types = {"payment": Payment, "transfer": Transfer}

    created: int
    """
    Time at which the quote was created, measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    lock_duration: Literal["day", "five_minutes", "hour", "none"]
    """
    The duration the exchange rate quote remains valid from creation time. Allowed values are none, hour, and day. Note that for the test mode API available in alpha, you can request an extended quote, but it won't be usable for any transactions.
    """
    lock_expires_at: Optional[int]
    """
    Time at which the quote will expire, measured in seconds since the Unix epoch.

    If lock_duration is set to ‘none' this field will be set to null.
    """
    lock_status: Literal["active", "expired", "none"]
    """
    Lock status of the quote. Transitions from active to expired once past the lock_expires_at timestamp.

    Can return value none, active, or expired.
    """
    object: Literal["fx_quote"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    rates: Dict[str, Rates]
    """
    Information about the rates.
    """
    to_currency: str
    """
    The currency to convert into, typically this is the currency that you want to settle to your Stripe balance. Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    usage: Usage

    @classmethod
    def create(cls, **params: Unpack["FxQuoteCreateParams"]) -> "FxQuote":
        """
        Creates an FX Quote object
        """
        return cast(
            "FxQuote",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["FxQuoteCreateParams"]
    ) -> "FxQuote":
        """
        Creates an FX Quote object
        """
        return cast(
            "FxQuote",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["FxQuoteListParams"]
    ) -> ListObject["FxQuote"]:
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
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
        cls, **params: Unpack["FxQuoteListParams"]
    ) -> ListObject["FxQuote"]:
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
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
        cls, id: str, **params: Unpack["FxQuoteRetrieveParams"]
    ) -> "FxQuote":
        """
        Retrieve an FX Quote object
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FxQuoteRetrieveParams"]
    ) -> "FxQuote":
        """
        Retrieve an FX Quote object
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"rates": Rates, "usage": Usage}
