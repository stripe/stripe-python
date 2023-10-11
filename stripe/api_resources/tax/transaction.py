# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax.transaction_line_item import (
        TransactionLineItem,
    )


class Transaction(APIResource["Transaction"]):
    """
    A Tax Transaction records the tax collected from or refunded to your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom#tax-transaction)
    """

    OBJECT_NAME = "tax.transaction"

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

    class Reversal(StripeObject):
        original_transaction: Optional[str]

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

    created: int
    currency: str
    customer: Optional[str]
    customer_details: CustomerDetails
    id: str
    line_items: Optional[ListObject["TransactionLineItem"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax.transaction"]
    reference: str
    reversal: Optional[Reversal]
    shipping_cost: Optional[ShippingCost]
    tax_date: int
    type: Literal["reversal", "transaction"]

    @classmethod
    def create_from_calculation(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_from_calculation",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_reversal(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/tax/transactions/create_reversal",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(transaction)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/tax/transactions/{transaction}/line_items".format(
                transaction=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Transaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "customer_details": CustomerDetails,
        "reversal": Reversal,
        "shipping_cost": ShippingCost,
    }
