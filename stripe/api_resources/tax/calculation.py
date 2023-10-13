# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
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

    OBJECT_NAME = "tax.calculation"

    class CustomerDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: str
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

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
            value: str

        address: Optional[Address]
        address_source: Optional[Literal["billing", "shipping"]]
        ip_address: Optional[str]
        tax_ids: List[TaxId]
        taxability_override: Literal[
            "customer_exempt", "none", "reverse_charge"
        ]
        _inner_class_types = {"address": Address, "tax_ids": TaxId}

    class ShippingCost(StripeObject):
        class TaxBreakdown(StripeObject):
            class Jurisdiction(StripeObject):
                country: str
                display_name: str
                level: Literal[
                    "city", "country", "county", "district", "state"
                ]
                state: Optional[str]

            class TaxRateDetails(StripeObject):
                display_name: str
                percentage_decimal: str
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

            amount: int
            jurisdiction: Jurisdiction
            sourcing: Literal["destination", "origin"]
            tax_rate_details: Optional[TaxRateDetails]
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
            taxable_amount: int
            _inner_class_types = {
                "jurisdiction": Jurisdiction,
                "tax_rate_details": TaxRateDetails,
            }

        amount: int
        amount_tax: int
        shipping_rate: Optional[str]
        tax_behavior: Literal["exclusive", "inclusive"]
        tax_breakdown: Optional[List[TaxBreakdown]]
        tax_code: str
        _inner_class_types = {"tax_breakdown": TaxBreakdown}

    class TaxBreakdown(StripeObject):
        class TaxRateDetails(StripeObject):
            country: Optional[str]
            percentage_decimal: str
            state: Optional[str]
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

        amount: int
        inclusive: bool
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
        taxable_amount: int
        _inner_class_types = {"tax_rate_details": TaxRateDetails}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            currency: str
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Calculation.CreateParamsCustomerDetails|None"
            ]
            expand: NotRequired["List[str]|None"]
            line_items: List["Calculation.CreateParamsLineItem"]
            shipping_cost: NotRequired[
                "Calculation.CreateParamsShippingCost|None"
            ]
            tax_date: NotRequired["int|None"]

        class CreateParamsShippingCost(TypedDict):
            amount: NotRequired["int|None"]
            shipping_rate: NotRequired["str|None"]
            tax_behavior: NotRequired["Literal['exclusive', 'inclusive']|None"]
            tax_code: NotRequired["str|None"]

        class CreateParamsLineItem(TypedDict):
            amount: int
            product: NotRequired["str|None"]
            quantity: NotRequired["int|None"]
            reference: NotRequired["str|None"]
            tax_behavior: NotRequired["Literal['exclusive', 'inclusive']|None"]
            tax_code: NotRequired["str|None"]

        class CreateParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Calculation.CreateParamsCustomerDetailsAddress|None"
            ]
            address_source: NotRequired["Literal['billing', 'shipping']|None"]
            ip_address: NotRequired["str|None"]
            tax_ids: NotRequired[
                "List[Calculation.CreateParamsCustomerDetailsTaxId]|None"
            ]
            taxability_override: NotRequired[
                "Literal['customer_exempt', 'none', 'reverse_charge']|None"
            ]

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
            value: str

        class CreateParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["Literal['']|str|None"]
            country: str
            line1: NotRequired["Literal['']|str|None"]
            line2: NotRequired["Literal['']|str|None"]
            postal_code: NotRequired["Literal['']|str|None"]
            state: NotRequired["Literal['']|str|None"]

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

    amount_total: int
    currency: str
    customer: Optional[str]
    customer_details: CustomerDetails
    expires_at: Optional[int]
    id: Optional[str]
    line_items: Optional[ListObject["CalculationLineItem"]]
    livemode: bool
    object: Literal["tax.calculation"]
    shipping_cost: Optional[ShippingCost]
    tax_amount_exclusive: int
    tax_amount_inclusive: int
    tax_breakdown: List[TaxBreakdown]
    tax_date: int

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
    ):
        return cls._static_request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(calculation)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Calculation.ListLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    _inner_class_types = {
        "customer_details": CustomerDetails,
        "shipping_cost": ShippingCost,
        "tax_breakdown": TaxBreakdown,
    }
