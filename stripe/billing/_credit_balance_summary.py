# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._request_options import RequestOptions
from stripe._singleton_api_resource import SingletonAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._customer import Customer


class CreditBalanceSummary(SingletonAPIResource["CreditBalanceSummary"]):
    """
    Indicates the billing credit balance for billing credits granted to a customer.
    """

    OBJECT_NAME: ClassVar[Literal["billing.credit_balance_summary"]] = (
        "billing.credit_balance_summary"
    )

    class Balance(StripeObject):
        class AvailableBalance(StripeObject):
            class CustomPricingUnit(StripeObject):
                class CustomPricingUnitDetails(StripeObject):
                    created: int
                    """
                    Time at which the object was created. Measured in seconds since the Unix epoch.
                    """
                    display_name: str
                    """
                    The name of the custom pricing unit.
                    """
                    id: str
                    """
                    Unique identifier for the object.
                    """
                    lookup_key: Optional[str]
                    """
                    A lookup key for the custom pricing unit.
                    """
                    metadata: Dict[str, str]
                    """
                    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
                    """
                    status: str
                    """
                    The status of the custom pricing unit.
                    """

                custom_pricing_unit_details: Optional[CustomPricingUnitDetails]
                """
                The custom pricing unit object.
                """
                id: str
                """
                Unique identifier for the object.
                """
                value: str
                """
                A positive integer representing the amount.
                """
                _inner_class_types = {
                    "custom_pricing_unit_details": CustomPricingUnitDetails,
                }

            class Monetary(StripeObject):
                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: int
                """
                A positive integer representing the amount.
                """

            custom_pricing_unit: Optional[CustomPricingUnit]
            """
            The custom pricing unit amount.
            """
            monetary: Optional[Monetary]
            """
            The monetary amount.
            """
            type: Literal["custom_pricing_unit", "monetary"]
            """
            The type of this amount. We currently only support `monetary` billing credits.
            """
            _inner_class_types = {
                "custom_pricing_unit": CustomPricingUnit,
                "monetary": Monetary,
            }

        class LedgerBalance(StripeObject):
            class CustomPricingUnit(StripeObject):
                class CustomPricingUnitDetails(StripeObject):
                    created: int
                    """
                    Time at which the object was created. Measured in seconds since the Unix epoch.
                    """
                    display_name: str
                    """
                    The name of the custom pricing unit.
                    """
                    id: str
                    """
                    Unique identifier for the object.
                    """
                    lookup_key: Optional[str]
                    """
                    A lookup key for the custom pricing unit.
                    """
                    metadata: Dict[str, str]
                    """
                    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
                    """
                    status: str
                    """
                    The status of the custom pricing unit.
                    """

                custom_pricing_unit_details: Optional[CustomPricingUnitDetails]
                """
                The custom pricing unit object.
                """
                id: str
                """
                Unique identifier for the object.
                """
                value: str
                """
                A positive integer representing the amount.
                """
                _inner_class_types = {
                    "custom_pricing_unit_details": CustomPricingUnitDetails,
                }

            class Monetary(StripeObject):
                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: int
                """
                A positive integer representing the amount.
                """

            custom_pricing_unit: Optional[CustomPricingUnit]
            """
            The custom pricing unit amount.
            """
            monetary: Optional[Monetary]
            """
            The monetary amount.
            """
            type: Literal["custom_pricing_unit", "monetary"]
            """
            The type of this amount. We currently only support `monetary` billing credits.
            """
            _inner_class_types = {
                "custom_pricing_unit": CustomPricingUnit,
                "monetary": Monetary,
            }

        available_balance: AvailableBalance
        ledger_balance: LedgerBalance
        _inner_class_types = {
            "available_balance": AvailableBalance,
            "ledger_balance": LedgerBalance,
        }

    class RetrieveParams(RequestOptions):
        customer: NotRequired[str]
        """
        The customer for which to fetch credit balance summary.
        """
        customer_account: NotRequired[str]
        """
        The account for which to fetch credit balance summary.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        filter: "CreditBalanceSummary.RetrieveParamsFilter"
        """
        The filter criteria for the credit balance summary.
        """

    class RetrieveParamsFilter(TypedDict):
        applicability_scope: NotRequired[
            "CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope"
        ]
        """
        The billing credit applicability scope for which to fetch credit balance summary.
        """
        credit_grant: NotRequired[str]
        """
        The credit grant for which to fetch credit balance summary.
        """
        type: Literal["applicability_scope", "credit_grant"]
        """
        Specify the type of this filter.
        """

    class RetrieveParamsFilterApplicabilityScope(TypedDict):
        billable_items: NotRequired[
            List[
                "CreditBalanceSummary.RetrieveParamsFilterApplicabilityScopeBillableItem"
            ]
        ]
        """
        A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.
        """
        price_type: NotRequired[Literal["metered"]]
        """
        The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
        """
        prices: NotRequired[
            List[
                "CreditBalanceSummary.RetrieveParamsFilterApplicabilityScopePrice"
            ]
        ]
        """
        A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.
        """

    class RetrieveParamsFilterApplicabilityScopeBillableItem(TypedDict):
        id: str
        """
        The billable item ID this credit grant should apply to.
        """

    class RetrieveParamsFilterApplicabilityScopePrice(TypedDict):
        id: str
        """
        The price ID this credit grant should apply to.
        """

    balances: List[Balance]
    """
    The billing credit balances. One entry per credit grant currency. If a customer only has credit grants in a single currency, then this will have a single balance entry.
    """
    customer: ExpandableField["Customer"]
    """
    The customer the balance is for.
    """
    customer_account: Optional[str]
    """
    The account the balance is for.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.credit_balance_summary"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def retrieve(
        cls, **params: Unpack["CreditBalanceSummary.RetrieveParams"]
    ) -> "CreditBalanceSummary":
        """
        Retrieves the credit balance summary for a customer.
        """
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, **params: Unpack["CreditBalanceSummary.RetrieveParams"]
    ) -> "CreditBalanceSummary":
        """
        Retrieves the credit balance summary for a customer.
        """
        instance = cls(None, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/billing/credit_balance_summary"

    _inner_class_types = {"balances": Balance}
