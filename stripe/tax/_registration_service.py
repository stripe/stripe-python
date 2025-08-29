# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.tax._registration import Registration
from typing import List, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict


class RegistrationService(StripeService):
    class CreateParams(TypedDict):
        active_from: Union[Literal["now"], int]
        """
        Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
        """
        country: str
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        country_options: "RegistrationService.CreateParamsCountryOptions"
        """
        Specific options for a registration in the specified `country`.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.
        """

    _CreateParamsCountryOptionsBase = TypedDict(
        "CreateParamsCountryOptions",
        {
            "in": NotRequired[
                "RegistrationService.CreateParamsCountryOptionsIn"
            ],
            "is": NotRequired[
                "RegistrationService.CreateParamsCountryOptionsIs"
            ],
        },
    )

    class CreateParamsCountryOptions(_CreateParamsCountryOptionsBase):
        ae: NotRequired["RegistrationService.CreateParamsCountryOptionsAe"]
        """
        Options for the registration in AE.
        """
        al: NotRequired["RegistrationService.CreateParamsCountryOptionsAl"]
        """
        Options for the registration in AL.
        """
        am: NotRequired["RegistrationService.CreateParamsCountryOptionsAm"]
        """
        Options for the registration in AM.
        """
        ao: NotRequired["RegistrationService.CreateParamsCountryOptionsAo"]
        """
        Options for the registration in AO.
        """
        at: NotRequired["RegistrationService.CreateParamsCountryOptionsAt"]
        """
        Options for the registration in AT.
        """
        au: NotRequired["RegistrationService.CreateParamsCountryOptionsAu"]
        """
        Options for the registration in AU.
        """
        aw: NotRequired["RegistrationService.CreateParamsCountryOptionsAw"]
        """
        Options for the registration in AW.
        """
        az: NotRequired["RegistrationService.CreateParamsCountryOptionsAz"]
        """
        Options for the registration in AZ.
        """
        ba: NotRequired["RegistrationService.CreateParamsCountryOptionsBa"]
        """
        Options for the registration in BA.
        """
        bb: NotRequired["RegistrationService.CreateParamsCountryOptionsBb"]
        """
        Options for the registration in BB.
        """
        bd: NotRequired["RegistrationService.CreateParamsCountryOptionsBd"]
        """
        Options for the registration in BD.
        """
        be: NotRequired["RegistrationService.CreateParamsCountryOptionsBe"]
        """
        Options for the registration in BE.
        """
        bf: NotRequired["RegistrationService.CreateParamsCountryOptionsBf"]
        """
        Options for the registration in BF.
        """
        bg: NotRequired["RegistrationService.CreateParamsCountryOptionsBg"]
        """
        Options for the registration in BG.
        """
        bh: NotRequired["RegistrationService.CreateParamsCountryOptionsBh"]
        """
        Options for the registration in BH.
        """
        bj: NotRequired["RegistrationService.CreateParamsCountryOptionsBj"]
        """
        Options for the registration in BJ.
        """
        bs: NotRequired["RegistrationService.CreateParamsCountryOptionsBs"]
        """
        Options for the registration in BS.
        """
        by: NotRequired["RegistrationService.CreateParamsCountryOptionsBy"]
        """
        Options for the registration in BY.
        """
        ca: NotRequired["RegistrationService.CreateParamsCountryOptionsCa"]
        """
        Options for the registration in CA.
        """
        cd: NotRequired["RegistrationService.CreateParamsCountryOptionsCd"]
        """
        Options for the registration in CD.
        """
        ch: NotRequired["RegistrationService.CreateParamsCountryOptionsCh"]
        """
        Options for the registration in CH.
        """
        cl: NotRequired["RegistrationService.CreateParamsCountryOptionsCl"]
        """
        Options for the registration in CL.
        """
        cm: NotRequired["RegistrationService.CreateParamsCountryOptionsCm"]
        """
        Options for the registration in CM.
        """
        co: NotRequired["RegistrationService.CreateParamsCountryOptionsCo"]
        """
        Options for the registration in CO.
        """
        cr: NotRequired["RegistrationService.CreateParamsCountryOptionsCr"]
        """
        Options for the registration in CR.
        """
        cv: NotRequired["RegistrationService.CreateParamsCountryOptionsCv"]
        """
        Options for the registration in CV.
        """
        cy: NotRequired["RegistrationService.CreateParamsCountryOptionsCy"]
        """
        Options for the registration in CY.
        """
        cz: NotRequired["RegistrationService.CreateParamsCountryOptionsCz"]
        """
        Options for the registration in CZ.
        """
        de: NotRequired["RegistrationService.CreateParamsCountryOptionsDe"]
        """
        Options for the registration in DE.
        """
        dk: NotRequired["RegistrationService.CreateParamsCountryOptionsDk"]
        """
        Options for the registration in DK.
        """
        ec: NotRequired["RegistrationService.CreateParamsCountryOptionsEc"]
        """
        Options for the registration in EC.
        """
        ee: NotRequired["RegistrationService.CreateParamsCountryOptionsEe"]
        """
        Options for the registration in EE.
        """
        eg: NotRequired["RegistrationService.CreateParamsCountryOptionsEg"]
        """
        Options for the registration in EG.
        """
        es: NotRequired["RegistrationService.CreateParamsCountryOptionsEs"]
        """
        Options for the registration in ES.
        """
        et: NotRequired["RegistrationService.CreateParamsCountryOptionsEt"]
        """
        Options for the registration in ET.
        """
        fi: NotRequired["RegistrationService.CreateParamsCountryOptionsFi"]
        """
        Options for the registration in FI.
        """
        fr: NotRequired["RegistrationService.CreateParamsCountryOptionsFr"]
        """
        Options for the registration in FR.
        """
        gb: NotRequired["RegistrationService.CreateParamsCountryOptionsGb"]
        """
        Options for the registration in GB.
        """
        ge: NotRequired["RegistrationService.CreateParamsCountryOptionsGe"]
        """
        Options for the registration in GE.
        """
        gn: NotRequired["RegistrationService.CreateParamsCountryOptionsGn"]
        """
        Options for the registration in GN.
        """
        gr: NotRequired["RegistrationService.CreateParamsCountryOptionsGr"]
        """
        Options for the registration in GR.
        """
        hr: NotRequired["RegistrationService.CreateParamsCountryOptionsHr"]
        """
        Options for the registration in HR.
        """
        hu: NotRequired["RegistrationService.CreateParamsCountryOptionsHu"]
        """
        Options for the registration in HU.
        """
        id: NotRequired["RegistrationService.CreateParamsCountryOptionsId"]
        """
        Options for the registration in ID.
        """
        ie: NotRequired["RegistrationService.CreateParamsCountryOptionsIe"]
        """
        Options for the registration in IE.
        """
        it: NotRequired["RegistrationService.CreateParamsCountryOptionsIt"]
        """
        Options for the registration in IT.
        """
        jp: NotRequired["RegistrationService.CreateParamsCountryOptionsJp"]
        """
        Options for the registration in JP.
        """
        ke: NotRequired["RegistrationService.CreateParamsCountryOptionsKe"]
        """
        Options for the registration in KE.
        """
        kg: NotRequired["RegistrationService.CreateParamsCountryOptionsKg"]
        """
        Options for the registration in KG.
        """
        kh: NotRequired["RegistrationService.CreateParamsCountryOptionsKh"]
        """
        Options for the registration in KH.
        """
        kr: NotRequired["RegistrationService.CreateParamsCountryOptionsKr"]
        """
        Options for the registration in KR.
        """
        kz: NotRequired["RegistrationService.CreateParamsCountryOptionsKz"]
        """
        Options for the registration in KZ.
        """
        la: NotRequired["RegistrationService.CreateParamsCountryOptionsLa"]
        """
        Options for the registration in LA.
        """
        lt: NotRequired["RegistrationService.CreateParamsCountryOptionsLt"]
        """
        Options for the registration in LT.
        """
        lu: NotRequired["RegistrationService.CreateParamsCountryOptionsLu"]
        """
        Options for the registration in LU.
        """
        lv: NotRequired["RegistrationService.CreateParamsCountryOptionsLv"]
        """
        Options for the registration in LV.
        """
        ma: NotRequired["RegistrationService.CreateParamsCountryOptionsMa"]
        """
        Options for the registration in MA.
        """
        md: NotRequired["RegistrationService.CreateParamsCountryOptionsMd"]
        """
        Options for the registration in MD.
        """
        me: NotRequired["RegistrationService.CreateParamsCountryOptionsMe"]
        """
        Options for the registration in ME.
        """
        mk: NotRequired["RegistrationService.CreateParamsCountryOptionsMk"]
        """
        Options for the registration in MK.
        """
        mr: NotRequired["RegistrationService.CreateParamsCountryOptionsMr"]
        """
        Options for the registration in MR.
        """
        mt: NotRequired["RegistrationService.CreateParamsCountryOptionsMt"]
        """
        Options for the registration in MT.
        """
        mx: NotRequired["RegistrationService.CreateParamsCountryOptionsMx"]
        """
        Options for the registration in MX.
        """
        my: NotRequired["RegistrationService.CreateParamsCountryOptionsMy"]
        """
        Options for the registration in MY.
        """
        ng: NotRequired["RegistrationService.CreateParamsCountryOptionsNg"]
        """
        Options for the registration in NG.
        """
        nl: NotRequired["RegistrationService.CreateParamsCountryOptionsNl"]
        """
        Options for the registration in NL.
        """
        no: NotRequired["RegistrationService.CreateParamsCountryOptionsNo"]
        """
        Options for the registration in NO.
        """
        np: NotRequired["RegistrationService.CreateParamsCountryOptionsNp"]
        """
        Options for the registration in NP.
        """
        nz: NotRequired["RegistrationService.CreateParamsCountryOptionsNz"]
        """
        Options for the registration in NZ.
        """
        om: NotRequired["RegistrationService.CreateParamsCountryOptionsOm"]
        """
        Options for the registration in OM.
        """
        pe: NotRequired["RegistrationService.CreateParamsCountryOptionsPe"]
        """
        Options for the registration in PE.
        """
        ph: NotRequired["RegistrationService.CreateParamsCountryOptionsPh"]
        """
        Options for the registration in PH.
        """
        pl: NotRequired["RegistrationService.CreateParamsCountryOptionsPl"]
        """
        Options for the registration in PL.
        """
        pt: NotRequired["RegistrationService.CreateParamsCountryOptionsPt"]
        """
        Options for the registration in PT.
        """
        ro: NotRequired["RegistrationService.CreateParamsCountryOptionsRo"]
        """
        Options for the registration in RO.
        """
        rs: NotRequired["RegistrationService.CreateParamsCountryOptionsRs"]
        """
        Options for the registration in RS.
        """
        ru: NotRequired["RegistrationService.CreateParamsCountryOptionsRu"]
        """
        Options for the registration in RU.
        """
        sa: NotRequired["RegistrationService.CreateParamsCountryOptionsSa"]
        """
        Options for the registration in SA.
        """
        se: NotRequired["RegistrationService.CreateParamsCountryOptionsSe"]
        """
        Options for the registration in SE.
        """
        sg: NotRequired["RegistrationService.CreateParamsCountryOptionsSg"]
        """
        Options for the registration in SG.
        """
        si: NotRequired["RegistrationService.CreateParamsCountryOptionsSi"]
        """
        Options for the registration in SI.
        """
        sk: NotRequired["RegistrationService.CreateParamsCountryOptionsSk"]
        """
        Options for the registration in SK.
        """
        sn: NotRequired["RegistrationService.CreateParamsCountryOptionsSn"]
        """
        Options for the registration in SN.
        """
        sr: NotRequired["RegistrationService.CreateParamsCountryOptionsSr"]
        """
        Options for the registration in SR.
        """
        th: NotRequired["RegistrationService.CreateParamsCountryOptionsTh"]
        """
        Options for the registration in TH.
        """
        tj: NotRequired["RegistrationService.CreateParamsCountryOptionsTj"]
        """
        Options for the registration in TJ.
        """
        tr: NotRequired["RegistrationService.CreateParamsCountryOptionsTr"]
        """
        Options for the registration in TR.
        """
        tz: NotRequired["RegistrationService.CreateParamsCountryOptionsTz"]
        """
        Options for the registration in TZ.
        """
        ua: NotRequired["RegistrationService.CreateParamsCountryOptionsUa"]
        """
        Options for the registration in UA.
        """
        ug: NotRequired["RegistrationService.CreateParamsCountryOptionsUg"]
        """
        Options for the registration in UG.
        """
        us: NotRequired["RegistrationService.CreateParamsCountryOptionsUs"]
        """
        Options for the registration in US.
        """
        uy: NotRequired["RegistrationService.CreateParamsCountryOptionsUy"]
        """
        Options for the registration in UY.
        """
        uz: NotRequired["RegistrationService.CreateParamsCountryOptionsUz"]
        """
        Options for the registration in UZ.
        """
        vn: NotRequired["RegistrationService.CreateParamsCountryOptionsVn"]
        """
        Options for the registration in VN.
        """
        za: NotRequired["RegistrationService.CreateParamsCountryOptionsZa"]
        """
        Options for the registration in ZA.
        """
        zm: NotRequired["RegistrationService.CreateParamsCountryOptionsZm"]
        """
        Options for the registration in ZM.
        """
        zw: NotRequired["RegistrationService.CreateParamsCountryOptionsZw"]
        """
        Options for the registration in ZW.
        """

    class CreateParamsCountryOptionsAe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAeStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsAl(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAlStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAlStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsAm(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAo(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAoStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAoStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsAt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAtStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsAtStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsAu(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAuStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAuStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsAw(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsAwStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsAwStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsAz(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBa(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBaStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBaStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBb(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBbStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBbStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBd(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBdStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBdStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsBeStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsBf(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBfStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBfStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBg(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBgStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsBgStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsBh(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBhStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBhStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBj(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBs(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsBsStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsBsStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsBy(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCa(TypedDict):
        province_standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsCaProvinceStandard"
        ]
        """
        Options for the provincial tax registration.
        """
        type: Literal["province_standard", "simplified", "standard"]
        """
        Type of registration to be created in Canada.
        """

    class CreateParamsCountryOptionsCaProvinceStandard(TypedDict):
        province: str
        """
        Two-letter CA province code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
        """

    class CreateParamsCountryOptionsCd(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsCdStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCdStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsCh(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsChStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsChStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsCl(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCm(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCo(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCr(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCv(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsCy(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsCyStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsCyStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsCz(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsCzStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsCzStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsDe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsDeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsDeStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsDk(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsDkStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsDkStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsEc(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsEe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsEeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsEeStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsEg(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsEs(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsEsStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsEsStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsEt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsEtStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsEtStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsFi(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsFiStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsFiStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsFr(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsFrStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsFrStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsGb(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsGbStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsGbStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsGe(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsGn(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsGnStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsGnStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsGr(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsGrStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsGrStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsHr(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsHrStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsHrStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsHu(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsHuStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsHuStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsId(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsIe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsIeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsIeStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsIn(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsIs(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsIsStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsIsStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsIt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsItStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsItStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsJp(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsJpStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsJpStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsKe(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsKg(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsKh(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsKr(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsKz(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsLa(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsLt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsLtStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsLtStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsLu(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsLuStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsLuStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsLv(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsLvStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsLvStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsMa(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMd(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsMeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMeStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsMk(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsMkStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMkStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsMr(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsMrStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMrStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsMt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsMtStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsMtStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsMx(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsMy(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsNg(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsNl(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsNlStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsNlStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsNo(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsNoStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsNoStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsNp(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsNz(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsNzStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsNzStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsOm(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsOmStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsOmStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsPe(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsPh(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsPl(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsPlStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsPlStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsPt(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsPtStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsPtStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsRo(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsRoStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsRoStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsRs(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsRsStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsRsStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsRu(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsSa(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsSe(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsSeStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsSeStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsSg(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsSgStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsSgStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsSi(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsSiStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsSiStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsSk(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsSkStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
        """
        Type of registration to be created in an EU country.
        """

    class CreateParamsCountryOptionsSkStandard(TypedDict):
        place_of_supply_scheme: Literal[
            "inbound_goods", "small_seller", "standard"
        ]
        """
        Place of supply scheme used in an EU standard registration.
        """

    class CreateParamsCountryOptionsSn(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsSr(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsSrStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsSrStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsTh(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsTj(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsTr(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsTz(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsUa(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsUg(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsUs(TypedDict):
        local_amusement_tax: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsUsLocalAmusementTax"
        ]
        """
        Options for the local amusement tax registration.
        """
        local_lease_tax: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsUsLocalLeaseTax"
        ]
        """
        Options for the local lease tax registration.
        """
        state: str
        """
        Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
        """
        state_sales_tax: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsUsStateSalesTax"
        ]
        """
        Options for the state sales tax registration.
        """
        type: Literal[
            "local_amusement_tax",
            "local_lease_tax",
            "state_communications_tax",
            "state_retail_delivery_fee",
            "state_sales_tax",
        ]
        """
        Type of registration to be created in the US.
        """

    class CreateParamsCountryOptionsUsLocalAmusementTax(TypedDict):
        jurisdiction: str
        """
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago), `06613` (Bloomington), `21696` (East Dundee), `24582` (Evanston), `45421` (Lynwood), `48892` (Midlothian), `64343` (River Grove), and `68081` (Schiller Park).
        """

    class CreateParamsCountryOptionsUsLocalLeaseTax(TypedDict):
        jurisdiction: str
        """
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago).
        """

    class CreateParamsCountryOptionsUsStateSalesTax(TypedDict):
        elections: List[
            "RegistrationService.CreateParamsCountryOptionsUsStateSalesTaxElection"
        ]
        """
        Elections for the state sales tax registration.
        """

    class CreateParamsCountryOptionsUsStateSalesTaxElection(TypedDict):
        jurisdiction: NotRequired[str]
        """
        A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `003` (Allegheny County) and `60000` (Philadelphia City).
        """
        type: Literal[
            "local_use_tax",
            "simplified_sellers_use_tax",
            "single_local_use_tax",
        ]
        """
        The type of the election for the state sales tax registration.
        """

    class CreateParamsCountryOptionsUy(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsUyStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsUyStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsUz(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsVn(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsZa(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsZaStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsZaStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

    class CreateParamsCountryOptionsZm(TypedDict):
        type: Literal["simplified"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsZw(TypedDict):
        standard: NotRequired[
            "RegistrationService.CreateParamsCountryOptionsZwStandard"
        ]
        """
        Options for the standard registration.
        """
        type: Literal["standard"]
        """
        Type of registration to be created in `country`.
        """

    class CreateParamsCountryOptionsZwStandard(TypedDict):
        place_of_supply_scheme: NotRequired[
            Literal["inbound_goods", "standard"]
        ]
        """
        Place of supply scheme used in an standard registration.
        """

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
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[Literal["active", "all", "expired", "scheduled"]]
        """
        The status of the Tax Registration.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        active_from: NotRequired["Literal['now']|int"]
        """
        Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired["Literal['']|Literal['now']|int"]
        """
        If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
        """

    def list(
        self,
        params: "RegistrationService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Registration]:
        """
        Returns a list of Tax Registration objects.
        """
        return cast(
            ListObject[Registration],
            self._request(
                "get",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "RegistrationService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Registration]:
        """
        Returns a list of Tax Registration objects.
        """
        return cast(
            ListObject[Registration],
            await self._request_async(
                "get",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RegistrationService.CreateParams",
        options: RequestOptions = {},
    ) -> Registration:
        """
        Creates a new Tax Registration object.
        """
        return cast(
            Registration,
            self._request(
                "post",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RegistrationService.CreateParams",
        options: RequestOptions = {},
    ) -> Registration:
        """
        Creates a new Tax Registration object.
        """
        return cast(
            Registration,
            await self._request_async(
                "post",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "RegistrationService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Registration:
        """
        Returns a Tax Registration object.
        """
        return cast(
            Registration,
            self._request(
                "get",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "RegistrationService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Registration:
        """
        Returns a Tax Registration object.
        """
        return cast(
            Registration,
            await self._request_async(
                "get",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "RegistrationService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Registration:
        """
        Updates an existing Tax Registration object.

        A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.
        """
        return cast(
            Registration,
            self._request(
                "post",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "RegistrationService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Registration:
        """
        Updates an existing Tax Registration object.

        A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.
        """
        return cast(
            Registration,
            await self._request_async(
                "post",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
