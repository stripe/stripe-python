# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class TaxRate(
    CreateableAPIResource["TaxRate"],
    ListableAPIResource["TaxRate"],
    UpdateableAPIResource["TaxRate"],
):
    """
    Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

    Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
    """

    OBJECT_NAME: ClassVar[Literal["tax_rate"]] = "tax_rate"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            """
            Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
            """
            display_name: str
            """
            The display name of the tax rate, which will be shown to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            inclusive: bool
            """
            This specifies if the tax rate is inclusive or exclusive.
            """
            jurisdiction: NotRequired["str|None"]
            """
            The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer's invoice.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            percentage: float
            """
            This represents the tax rate percent out of 100.
            """
            state: NotRequired["str|None"]
            """
            [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States.
            """
            tax_type: NotRequired[
                "Literal['amusement_tax', 'communications_tax', 'gst', 'hst', 'igst', 'jct', 'lease_tax', 'pst', 'qst', 'rst', 'sales_tax', 'service_tax', 'vat']|None"
            ]
            """
            The high-level tax type, such as `vat` or `sales_tax`.
            """

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            """
            Optional flag to filter by tax rates that are either active or inactive (archived).
            """
            created: NotRequired["TaxRate.ListParamsCreated|int|None"]
            """
            Optional range for filtering created date.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            inclusive: NotRequired["bool|None"]
            """
            Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).
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
            Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
            """
            display_name: NotRequired["str|None"]
            """
            The display name of the tax rate, which will be shown to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            jurisdiction: NotRequired["str|None"]
            """
            The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer's invoice.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            state: NotRequired["str|None"]
            """
            [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States.
            """
            tax_type: NotRequired[
                "Literal['amusement_tax', 'communications_tax', 'gst', 'hst', 'igst', 'jct', 'lease_tax', 'pst', 'qst', 'rst', 'sales_tax', 'service_tax', 'vat']|None"
            ]
            """
            The high-level tax type, such as `vat` or `sales_tax`.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    active: bool
    """
    Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
    """
    country: Optional[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
    """
    display_name: str
    """
    The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.
    """
    effective_percentage: Optional[float]
    """
    Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
    this percentage reflects the rate actually used to calculate tax based on the product's taxability
    and whether the user is registered to collect taxes in the corresponding jurisdiction.
    """
    id: str
    """
    Unique identifier for the object.
    """
    inclusive: bool
    """
    This specifies if the tax rate is inclusive or exclusive.
    """
    jurisdiction: Optional[str]
    """
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer's invoice.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["tax_rate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percentage: float
    """
    Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.
    """
    state: Optional[str]
    """
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States.
    """
    tax_type: Optional[
        Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ]
    """
    The high-level tax type, such as `vat` or `sales_tax`.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["TaxRate.CreateParams"]
    ) -> "TaxRate":
        """
        Creates a new tax rate.
        """
        return cast(
            "TaxRate",
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
        **params: Unpack["TaxRate.ListParams"]
    ) -> ListObject["TaxRate"]:
        """
        Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.
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
        cls, id: str, **params: Unpack["TaxRate.ModifyParams"]
    ) -> "TaxRate":
        """
        Updates an existing tax rate.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "TaxRate",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["TaxRate.RetrieveParams"]
    ) -> "TaxRate":
        """
        Retrieves a tax rate with the given ID
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance
