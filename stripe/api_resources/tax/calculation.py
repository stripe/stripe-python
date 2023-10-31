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

    class CustomerDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
            """

        class TaxId(StripeObject):
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
                "unknown",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            """
            The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, or `unknown`
            """
            value: str
            """
            The value of the tax ID.
            """

        address: Optional[Address]
        """
        The customer's postal address (for example, home or business location).
        """
        address_source: Optional[Literal["billing", "shipping"]]
        """
        The type of customer address provided.
        """
        ip_address: Optional[str]
        """
        The customer's IP address (IPv4 or IPv6).
        """
        tax_ids: List[TaxId]
        """
        The customer's tax IDs (for example, EU VAT numbers).
        """
        taxability_override: Literal[
            "customer_exempt", "none", "reverse_charge"
        ]
        """
        The taxability override used for taxation.
        """
        _inner_class_types = {"address": Address, "tax_ids": TaxId}

    class ShippingCost(StripeObject):
        class TaxBreakdown(StripeObject):
            class Jurisdiction(StripeObject):
                country: str
                """
                Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
                """
                display_name: str
                """
                A human-readable name for the jurisdiction imposing the tax.
                """
                level: Literal[
                    "city", "country", "county", "district", "state"
                ]
                """
                Indicates the level of the jurisdiction imposing the tax.
                """
                state: Optional[str]
                """
                [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix. For example, "NY" for New York, United States.
                """

            class TaxRateDetails(StripeObject):
                display_name: str
                """
                A localized display name for tax type, intended to be human-readable. For example, "Local Sales and Use Tax", "Value-added tax (VAT)", or "Umsatzsteuer (USt.)".
                """
                percentage_decimal: str
                """
                The tax rate percentage as a string. For example, 8.5% is represented as "8.5".
                """
                tax_type: Literal[
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
                    "vat",
                ]
                """
                The tax type, such as `vat` or `sales_tax`.
                """

            amount: int
            """
            The amount of tax, in integer cents.
            """
            jurisdiction: Jurisdiction
            sourcing: Literal["destination", "origin"]
            """
            Indicates whether the jurisdiction was determined by the origin (merchant's address) or destination (customer's address).
            """
            tax_rate_details: Optional[TaxRateDetails]
            """
            Details regarding the rate for this tax. This field will be `null` when the tax is not imposed, for example if the product is exempt from tax.
            """
            taxability_reason: Literal[
                "customer_exempt",
                "not_collecting",
                "not_subject_to_tax",
                "not_supported",
                "portion_product_exempt",
                "portion_reduced_rated",
                "portion_standard_rated",
                "product_exempt",
                "product_exempt_holiday",
                "proportionally_rated",
                "reduced_rated",
                "reverse_charge",
                "standard_rated",
                "taxable_basis_reduced",
                "zero_rated",
            ]
            """
            The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
            """
            taxable_amount: int
            """
            The amount on which tax is calculated, in integer cents.
            """
            _inner_class_types = {
                "jurisdiction": Jurisdiction,
                "tax_rate_details": TaxRateDetails,
            }

        amount: int
        """
        The shipping amount in integer cents. If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
        """
        amount_tax: int
        """
        The amount of tax calculated for shipping, in integer cents.
        """
        shipping_rate: Optional[str]
        """
        The ID of an existing [ShippingRate](https://stripe.com/docs/api/shipping_rates/object).
        """
        tax_behavior: Literal["exclusive", "inclusive"]
        """
        Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
        """
        tax_breakdown: Optional[List[TaxBreakdown]]
        """
        Detailed account of taxes relevant to shipping cost.
        """
        tax_code: str
        """
        The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for shipping.
        """
        _inner_class_types = {"tax_breakdown": TaxBreakdown}

    class TaxBreakdown(StripeObject):
        class TaxRateDetails(StripeObject):
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            percentage_decimal: str
            """
            The tax rate percentage as a string. For example, 8.5% is represented as `"8.5"`.
            """
            state: Optional[str]
            """
            State, county, province, or region.
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
                    "vat",
                ]
            ]
            """
            The tax type, such as `vat` or `sales_tax`.
            """

        amount: int
        """
        The amount of tax, in integer cents.
        """
        inclusive: bool
        """
        Specifies whether the tax amount is included in the line item amount.
        """
        tax_rate_details: TaxRateDetails
        taxability_reason: Literal[
            "customer_exempt",
            "not_collecting",
            "not_subject_to_tax",
            "not_supported",
            "portion_product_exempt",
            "portion_reduced_rated",
            "portion_standard_rated",
            "product_exempt",
            "product_exempt_holiday",
            "proportionally_rated",
            "reduced_rated",
            "reverse_charge",
            "standard_rated",
            "taxable_basis_reduced",
            "zero_rated",
        ]
        """
        The reasoning behind this tax, for example, if the product is tax exempt. We might extend the possible values for this field to support new tax rules.
        """
        taxable_amount: int
        """
        The amount on which tax is calculated, in integer cents.
        """
        _inner_class_types = {"tax_rate_details": TaxRateDetails}

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
    customer_details: CustomerDetails
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
    shipping_cost: Optional[ShippingCost]
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
    tax_breakdown: List[TaxBreakdown]
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
        """
        Calculates tax based on input and returns a Tax Calculation object.
        """
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
        """
        Retrieves the line items of a persisted tax calculation as a collection.
        """
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
    @staticmethod
    def list_line_items(
        calculation: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        """
        Retrieves the line items of a persisted tax calculation as a collection.
        """
        ...

    @overload
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        """
        Retrieves the line items of a persisted tax calculation as a collection.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ) -> ListObject["CalculationLineItem"]:
        """
        Retrieves the line items of a persisted tax calculation as a collection.
        """
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

    _inner_class_types = {
        "customer_details": CustomerDetails,
        "shipping_cost": ShippingCost,
        "tax_breakdown": TaxBreakdown,
    }
