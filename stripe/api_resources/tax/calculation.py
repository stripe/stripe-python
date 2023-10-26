# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.tax.calculation_line_item import (
        CalculationLineItem,
    )


class Calculation(CreateableAPIResource["Calculation"]):
    """
    A Tax Calculation allows you to calculate the tax to collect from your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom)
    """

    OBJECT_NAME: ClassVar[Literal["tax.calculation"]] = "tax.calculation"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            customer: NotRequired["str|None"]
            """
            The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`.
            """
            customer_details: NotRequired[
                "Calculation.CreateParamsCustomerDetails|None"
            ]
            """
            Details about the customer, including address and tax IDs.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            line_items: List["Calculation.CreateParamsLineItem"]
            """
            A list of items the customer is purchasing.
            """
            shipping_cost: NotRequired[
                "Calculation.CreateParamsShippingCost|None"
            ]
            """
            Shipping cost details to be used for the calculation.
            """
            tax_date: NotRequired["int|None"]
            """
            Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future.
            """

        class CreateParamsShippingCost(TypedDict):
            amount: NotRequired["int|None"]
            """
            A positive integer in cents representing the shipping charge. If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes are calculated on top of this amount.
            """
            shipping_rate: NotRequired["str|None"]
            """
            If provided, the [shipping rate](https://stripe.com/docs/api/shipping_rates/object)'s `amount`, `tax_code` and `tax_behavior` are used. If you provide a shipping rate, then you cannot pass the `amount`, `tax_code`, or `tax_behavior` parameters.
            """
            tax_behavior: NotRequired["Literal['exclusive', 'inclusive']|None"]
            """
            Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes. Defaults to `exclusive`.
            """
            tax_code: NotRequired["str|None"]
            """
            The [tax code](https://stripe.com/docs/tax/tax-categories) used to calculate tax on shipping. If not provided, the default shipping tax code from your [Tax Settings](https://stripe.com/settings/tax) is used.
            """

        class CreateParamsLineItem(TypedDict):
            amount: int
            """
            A positive integer in cents representing the line item's total price. If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes are calculated on top of this amount.
            """
            product: NotRequired["str|None"]
            """
            If provided, the product's `tax_code` will be used as the line item's `tax_code`.
            """
            quantity: NotRequired["int|None"]
            """
            The number of units of the item being purchased. Used to calculate the per-unit price from the total `amount` for the line. For example, if `amount=100` and `quantity=4`, the calculated unit price is 25.
            """
            reference: NotRequired["str|None"]
            """
            A custom identifier for this line item, which must be unique across the line items in the calculation. The reference helps identify each line item in exported [tax reports](https://stripe.com/docs/tax/reports).
            """
            tax_behavior: NotRequired["Literal['exclusive', 'inclusive']|None"]
            """
            Specifies whether the `amount` includes taxes. Defaults to `exclusive`.
            """
            tax_code: NotRequired["str|None"]
            """
            A [tax code](https://stripe.com/docs/tax/tax-categories) ID to use for this line item. If not provided, we will use the tax code from the provided `product` param. If neither `tax_code` nor `product` is provided, we will use the default tax code from your Tax Settings.
            """

        class CreateParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Calculation.CreateParamsCustomerDetailsAddress|None"
            ]
            """
            The customer's postal address (for example, home or business location).
            """
            address_source: NotRequired["Literal['billing', 'shipping']|None"]
            """
            The type of customer address provided.
            """
            ip_address: NotRequired["str|None"]
            """
            The customer's IP address (IPv4 or IPv6).
            """
            tax_ids: NotRequired[
                "List[Calculation.CreateParamsCustomerDetailsTaxId]|None"
            ]
            """
            The customer's tax IDs.
            """
            taxability_override: NotRequired[
                "Literal['customer_exempt', 'none', 'reverse_charge']|None"
            ]
            """
            Overrides the tax calculation result to allow you to not collect tax from your customer. Use this if you've manually checked your customer's tax exemptions. Prefer providing the customer's `tax_ids` where possible, which automatically determines whether `reverse_charge` applies.
            """

        class CreateParamsCustomerDetailsTaxId(TypedDict):
            type: Literal[
                "ad_nrt",
                "ae_trn",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "bg_uic",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "ch_vat",
                "cl_tin",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "hk_br",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kr_brn",
                "li_uid",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "no_vat",
                "nz_gst",
                "pe_ruc",
                "ph_tin",
                "ro_tin",
                "rs_pib",
                "ru_inn",
                "ru_kpp",
                "sa_vat",
                "sg_gst",
                "sg_uen",
                "si_tin",
                "sv_nit",
                "th_vat",
                "tr_tin",
                "tw_vat",
                "ua_vat",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            """
            Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
            """
            value: str
            """
            Value of the tax ID.
            """

        class CreateParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["Literal['']|str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["Literal['']|str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["Literal['']|str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["Literal['']|str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["Literal['']|str|None"]
            """
            State, county, province, or region. We recommend sending [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code value when possible.
            """

        class ListLineItemsParams(RequestOptions):
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

    amount_total: int
    """
    Total after taxes.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[str]
    """
    The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource.
    """
    customer_details: StripeObject
    expires_at: Optional[int]
    """
    Timestamp of date at which the tax calculation will expire.
    """
    id: Optional[str]
    """
    Unique identifier for the calculation.
    """
    line_items: Optional[ListObject["CalculationLineItem"]]
    """
    The list of items the customer is purchasing.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax.calculation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    shipping_cost: Optional[StripeObject]
    """
    The shipping cost details for the calculation.
    """
    tax_amount_exclusive: int
    """
    The amount of tax to be collected on top of the line item prices.
    """
    tax_amount_inclusive: int
    """
    The amount of tax already included in the line item prices.
    """
    tax_breakdown: List[StripeObject]
    """
    Breakdown of individual tax amounts that add up to the total.
    """
    tax_date: int
    """
    Timestamp of date at which the tax rules and rates in effect applies for the calculation.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Calculation.CreateParams"]
    ) -> "Calculation":
        return cast(
            "Calculation",
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
    def _cls_list_line_items(
        cls,
        calculation: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        return cast(
            ListObject["CalculationLineItem"],
            cls._static_request(
                "get",
                "/v1/tax/calculations/{calculation}/line_items".format(
                    calculation=util.sanitize_id(calculation)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_line_items(
        cls,
        calculation: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        ...

    @overload
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        return cast(
            ListObject["CalculationLineItem"],
            self._request(
                "get",
                "/v1/tax/calculations/{calculation}/line_items".format(
                    calculation=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )
