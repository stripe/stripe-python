# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._customer import Customer
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class TaxId(APIResource["TaxId"]):
    """
    You can add one or multiple tax IDs to a [customer](https://stripe.com/docs/api/customers) or account.
    Customer and account tax IDs get displayed on related invoices and credit notes.

    Related guides: [Customer tax identification numbers](https://stripe.com/docs/billing/taxes/tax-ids), [Account tax IDs](https://stripe.com/docs/invoicing/connect#account-tax-ids)
    """

    OBJECT_NAME: ClassVar[Literal["tax_id"]] = "tax_id"

    class Verification(StripeObject):
        status: Literal["pending", "unavailable", "unverified", "verified"]
        """
        Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`.
        """
        verified_address: Optional[str]
        """
        Verified address.
        """
        verified_name: Optional[str]
        """
        Verified name.
        """

    country: Optional[str]
    """
    Two-letter ISO code representing the country of the tax ID.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    ID of the customer.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax_id"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
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
    Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`. Note that some legacy tax IDs have type `unknown`
    """
    value: str
    """
    Value of the tax ID.
    """
    verification: Optional[Verification]
    """
    Tax ID verification information.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    def instance_url(self):
        token = self.id
        customer = self.customer
        base = Customer.class_url()
        assert customer is not None
        if isinstance(customer, Customer):
            customer = customer.id
        cust_extn = quote_plus(customer)
        extn = quote_plus(token)
        return "%s/%s/tax_ids/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a tax id without a customer ID. Use customer.retrieve_tax_id('tax_id')"
        )

    _inner_class_types = {"verification": Verification}
