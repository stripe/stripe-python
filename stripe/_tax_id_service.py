# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._tax_id import TaxId
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class TaxIdService(StripeService):
    class CreateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        owner: NotRequired["TaxIdService.CreateParamsOwner"]
        """
        The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.
        """
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "al_tin",
            "am_tin",
            "ao_tin",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "aw_tin",
            "az_tin",
            "ba_tin",
            "bb_tin",
            "bd_bin",
            "bf_ifu",
            "bg_uic",
            "bh_vat",
            "bj_ifu",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "bs_tin",
            "by_tin",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "cd_nif",
            "ch_uid",
            "ch_vat",
            "cl_tin",
            "cm_niu",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "cv_nif",
            "de_stn",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "et_tin",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "gn_nif",
            "hk_br",
            "hr_oib",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kg_tin",
            "kh_tin",
            "kr_brn",
            "kz_bin",
            "la_tin",
            "li_uid",
            "li_vat",
            "ma_vat",
            "md_vat",
            "me_pib",
            "mk_vat",
            "mr_nif",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "ng_tin",
            "no_vat",
            "no_voec",
            "np_pan",
            "nz_gst",
            "om_vat",
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
            "sn_ninea",
            "sr_fin",
            "sv_nit",
            "th_vat",
            "tj_tin",
            "tr_tin",
            "tw_vat",
            "tz_vat",
            "ua_vat",
            "ug_tin",
            "us_ein",
            "uy_ruc",
            "uz_tin",
            "uz_vat",
            "ve_rif",
            "vn_tin",
            "za_vat",
            "zm_tin",
            "zw_tin",
        ]
        """
        Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`
        """
        value: str
        """
        Value of the tax ID.
        """

    class CreateParamsOwner(TypedDict):
        account: NotRequired[str]
        """
        Account the tax ID belongs to. Required when `type=account`
        """
        customer: NotRequired[str]
        """
        Customer the tax ID belongs to. Required when `type=customer`
        """
        type: Literal["account", "application", "customer", "self"]
        """
        Type of owner referenced.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
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
        owner: NotRequired["TaxIdService.ListParamsOwner"]
        """
        The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParamsOwner(TypedDict):
        account: NotRequired[str]
        """
        Account the tax ID belongs to. Required when `type=account`
        """
        customer: NotRequired[str]
        """
        Customer the tax ID belongs to. Required when `type=customer`
        """
        type: Literal["account", "application", "customer", "self"]
        """
        Type of owner referenced.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def delete(
        self,
        id: str,
        params: "TaxIdService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> TaxId:
        """
        Deletes an existing account or customer tax_id object.
        """
        return cast(
            TaxId,
            self._request(
                "delete",
                "/v1/tax_ids/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: "TaxIdService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> TaxId:
        """
        Deletes an existing account or customer tax_id object.
        """
        return cast(
            TaxId,
            await self._request_async(
                "delete",
                "/v1/tax_ids/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "TaxIdService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> TaxId:
        """
        Retrieves an account or customer tax_id object.
        """
        return cast(
            TaxId,
            self._request(
                "get",
                "/v1/tax_ids/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "TaxIdService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> TaxId:
        """
        Retrieves an account or customer tax_id object.
        """
        return cast(
            TaxId,
            await self._request_async(
                "get",
                "/v1/tax_ids/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "TaxIdService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[TaxId]:
        """
        Returns a list of tax IDs.
        """
        return cast(
            ListObject[TaxId],
            self._request(
                "get",
                "/v1/tax_ids",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "TaxIdService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[TaxId]:
        """
        Returns a list of tax IDs.
        """
        return cast(
            ListObject[TaxId],
            await self._request_async(
                "get",
                "/v1/tax_ids",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self, params: "TaxIdService.CreateParams", options: RequestOptions = {}
    ) -> TaxId:
        """
        Creates a new account or customer tax_id object.
        """
        return cast(
            TaxId,
            self._request(
                "post",
                "/v1/tax_ids",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self, params: "TaxIdService.CreateParams", options: RequestOptions = {}
    ) -> TaxId:
        """
        Creates a new account or customer tax_id object.
        """
        return cast(
            TaxId,
            await self._request_async(
                "post",
                "/v1/tax_ids",
                base_address="api",
                params=params,
                options=options,
            ),
        )
