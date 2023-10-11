# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

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

    class CreateParams(RequestOptions):
        currency: str
        customer: NotRequired[Optional[str]]
        customer_details: NotRequired[
            Optional["Calculation.CreateCustomerDetailsParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        line_items: List["Calculation.CreateLineItemParams"]
        shipping_cost: NotRequired[
            Optional["Calculation.CreateShippingCostParams"]
        ]
        tax_date: NotRequired[Optional[int]]

    class CreateShippingCostParams(TypedDict):
        amount: NotRequired[Optional[int]]
        shipping_rate: NotRequired[Optional[str]]
        tax_behavior: NotRequired[Optional[Literal["exclusive", "inclusive"]]]
        tax_code: NotRequired[Optional[str]]

    class CreateLineItemParams(TypedDict):
        amount: int
        product: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]
        reference: NotRequired[Optional[str]]
        tax_behavior: NotRequired[Optional[Literal["exclusive", "inclusive"]]]
        tax_code: NotRequired[Optional[str]]

    class CreateCustomerDetailsParams(TypedDict):
        address: NotRequired[
            Optional["Calculation.CreateCustomerDetailsAddressParams"]
        ]
        address_source: NotRequired[Optional[Literal["billing", "shipping"]]]
        ip_address: NotRequired[Optional[str]]
        tax_ids: NotRequired[
            Optional[List["Calculation.CreateCustomerDetailsTaxIdParams"]]
        ]
        taxability_override: NotRequired[
            Optional[Literal["customer_exempt", "none", "reverse_charge"]]
        ]

    class CreateCustomerDetailsTaxIdParams(TypedDict):
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

    class CreateCustomerDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[Union[Literal[""], str]]]
        country: str
        line1: NotRequired[Optional[Union[Literal[""], str]]]
        line2: NotRequired[Optional[Union[Literal[""], str]]]
        postal_code: NotRequired[Optional[Union[Literal[""], str]]]
        state: NotRequired[Optional[Union[Literal[""], str]]]

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    amount_total: int
    currency: str
    customer: Optional[str]
    customer_details: StripeObject
    expires_at: Optional[int]
    id: Optional[str]
    line_items: Optional[ListObject["CalculationLineItem"]]
    livemode: bool
    object: Literal["tax.calculation"]
    shipping_cost: Optional[StripeObject]
    tax_amount_exclusive: int
    tax_amount_inclusive: int
    tax_breakdown: List[StripeObject]
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
