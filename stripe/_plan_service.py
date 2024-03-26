# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._plan import Plan
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict


class PlanService(StripeService):
    class CreateParams(TypedDict):
        active: NotRequired[bool]
        """
        Whether the plan is currently available for new subscriptions. Defaults to `true`.
        """
        aggregate_usage: NotRequired[
            Literal["last_during_period", "last_ever", "max", "sum"]
        ]
        """
        Specifies a usage aggregation strategy for plans of `usage_type=metered`. Allowed values are `sum` for summing up all usage during a period, `last_during_period` for using the last usage record reported within a period, `last_ever` for using the last usage record ever (across period bounds) or `max` which uses the usage record with the maximum reported usage during a period. Defaults to `sum`.
        """
        amount: NotRequired[int]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free plan) representing how much to charge on a recurring basis.
        """
        amount_decimal: NotRequired[str]
        """
        Same as `amount`, but accepts a decimal value with at most 12 decimal places. Only one of `amount` and `amount_decimal` can be set.
        """
        billing_scheme: NotRequired[Literal["per_unit", "tiered"]]
        """
        Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        id: NotRequired[str]
        """
        An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes.
        """
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired[int]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        nickname: NotRequired[str]
        """
        A brief description of the plan, hidden from customers.
        """
        product: NotRequired["PlanService.CreateParamsProduct|str"]
        tiers: NotRequired[List["PlanService.CreateParamsTier"]]
        """
        Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
        """
        tiers_mode: NotRequired[Literal["graduated", "volume"]]
        """
        Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
        """
        transform_usage: NotRequired["PlanService.CreateParamsTransformUsage"]
        """
        Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
        """
        trial_period_days: NotRequired[int]
        """
        Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
        """
        usage_type: NotRequired[Literal["licensed", "metered"]]
        """
        Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
        """

    class CreateParamsProduct(TypedDict):
        active: NotRequired[bool]
        """
        Whether the product is currently available for purchase. Defaults to `true`.
        """
        id: NotRequired[str]
        """
        The identifier for the product. Must be unique. If not provided, an identifier will be randomly generated.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: str
        """
        The product's name, meant to be displayable to the customer.
        """
        statement_descriptor: NotRequired[str]
        """
        An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

        This may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
        """
        tax_code: NotRequired[str]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        unit_label: NotRequired[str]
        """
        A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
        """

    class CreateParamsTier(TypedDict):
        flat_amount: NotRequired[int]
        """
        The flat billing amount for an entire tier, regardless of the number of units in the tier.
        """
        flat_amount_decimal: NotRequired[str]
        """
        Same as `flat_amount`, but accepts a decimal value representing an integer in the minor units of the currency. Only one of `flat_amount` and `flat_amount_decimal` can be set.
        """
        unit_amount: NotRequired[int]
        """
        The per unit billing amount for each individual unit for which this tier applies.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """
        up_to: Union[Literal["inf"], int]
        """
        Specifies the upper bound of this tier. The lower bound of a tier is the upper bound of the previous tier adding one. Use `inf` to define a fallback tier.
        """

    class CreateParamsTransformUsage(TypedDict):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, either round the result `up` or `down`.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        active: NotRequired[bool]
        """
        Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).
        """
        created: NotRequired["PlanService.ListParamsCreated|int"]
        """
        A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        product: NotRequired[str]
        """
        Only return plans for the given product.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired[int]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired[int]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired[int]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired[int]
        """
        Maximum value to filter by (inclusive)
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        active: NotRequired[bool]
        """
        Whether the plan is currently available for new subscriptions.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        nickname: NotRequired[str]
        """
        A brief description of the plan, hidden from customers.
        """
        product: NotRequired[str]
        """
        The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.
        """
        trial_period_days: NotRequired[int]
        """
        Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
        """

    def delete(
        self,
        plan: str,
        params: "PlanService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Plan:
        """
        Deleting plans means new subscribers can't be added. Existing subscribers aren't affected.
        """
        return cast(
            Plan,
            self._request(
                "delete",
                "/v1/plans/{plan}".format(plan=sanitize_id(plan)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        plan: str,
        params: "PlanService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Plan:
        """
        Retrieves the plan with the given ID.
        """
        return cast(
            Plan,
            self._request(
                "get",
                "/v1/plans/{plan}".format(plan=sanitize_id(plan)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        plan: str,
        params: "PlanService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Plan:
        """
        Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan's ID, amount, currency, or billing cycle.
        """
        return cast(
            Plan,
            self._request(
                "post",
                "/v1/plans/{plan}".format(plan=sanitize_id(plan)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "PlanService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Plan]:
        """
        Returns a list of your plans.
        """
        return cast(
            ListObject[Plan],
            self._request(
                "get",
                "/v1/plans",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self, params: "PlanService.CreateParams", options: RequestOptions = {}
    ) -> Plan:
        """
        You can now model subscriptions more flexibly using the [Prices API](https://stripe.com/docs/api#prices). It replaces the Plans API and is backwards compatible to simplify your migration.
        """
        return cast(
            Plan,
            self._request(
                "post",
                "/v1/plans",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
