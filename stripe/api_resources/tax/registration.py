# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Registration(
    CreateableAPIResource["Registration"],
    ListableAPIResource["Registration"],
    UpdateableAPIResource["Registration"],
):
    """
    A Tax `Registration` lets us know that your business is registered to collect tax on payments within a region, enabling you to [automatically collect tax](https://stripe.com/docs/tax).

    Stripe doesn't register on your behalf with the relevant authorities when you create a Tax `Registration` object. For more information on how to register to collect tax, see [our guide](https://stripe.com/docs/tax/registering).

    Related guide: [Using the Registrations API](https://stripe.com/docs/tax/registrations-api)
    """

    OBJECT_NAME = "tax.registration"

    class CountryOptions(StripeObject):
        class Ae(StripeObject):
            type: Literal["standard"]

        class At(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Au(StripeObject):
            type: Literal["standard"]

        class Be(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Bg(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Ca(StripeObject):
            class ProvinceStandard(StripeObject):
                province: str

            province_standard: Optional[ProvinceStandard]
            type: Literal["province_standard", "simplified", "standard"]
            _inner_class_types = {"province_standard": ProvinceStandard}

        class Ch(StripeObject):
            type: Literal["standard"]

        class Cl(StripeObject):
            type: Literal["simplified"]

        class Co(StripeObject):
            type: Literal["simplified"]

        class Cy(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Cz(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class De(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Dk(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Ee(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Es(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Fi(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Fr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Gb(StripeObject):
            type: Literal["standard"]

        class Gr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Hr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Hu(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Id(StripeObject):
            type: Literal["simplified"]

        class Ie(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Is(StripeObject):
            type: Literal["standard"]

        class It(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Jp(StripeObject):
            type: Literal["standard"]

        class Kr(StripeObject):
            type: Literal["simplified"]

        class Lt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Lu(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Lv(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Mt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Mx(StripeObject):
            type: Literal["simplified"]

        class My(StripeObject):
            type: Literal["simplified"]

        class Nl(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class No(StripeObject):
            type: Literal["standard"]

        class Nz(StripeObject):
            type: Literal["standard"]

        class Pl(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Pt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Ro(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Sa(StripeObject):
            type: Literal["simplified"]

        class Se(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Sg(StripeObject):
            type: Literal["standard"]

        class Si(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Sk(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            _inner_class_types = {"standard": Standard}

        class Th(StripeObject):
            type: Literal["simplified"]

        class Tr(StripeObject):
            type: Literal["simplified"]

        class Us(StripeObject):
            class LocalAmusementTax(StripeObject):
                jurisdiction: str

            class LocalLeaseTax(StripeObject):
                jurisdiction: str

            local_amusement_tax: Optional[LocalAmusementTax]
            local_lease_tax: Optional[LocalLeaseTax]
            state: str
            type: Literal[
                "local_amusement_tax",
                "local_lease_tax",
                "state_communications_tax",
                "state_sales_tax",
            ]
            _inner_class_types = {
                "local_amusement_tax": LocalAmusementTax,
                "local_lease_tax": LocalLeaseTax,
            }

        class Vn(StripeObject):
            type: Literal["simplified"]

        class Za(StripeObject):
            type: Literal["standard"]

        ae: Optional[Ae]
        at: Optional[At]
        au: Optional[Au]
        be: Optional[Be]
        bg: Optional[Bg]
        ca: Optional[Ca]
        ch: Optional[Ch]
        cl: Optional[Cl]
        co: Optional[Co]
        cy: Optional[Cy]
        cz: Optional[Cz]
        de: Optional[De]
        dk: Optional[Dk]
        ee: Optional[Ee]
        es: Optional[Es]
        fi: Optional[Fi]
        fr: Optional[Fr]
        gb: Optional[Gb]
        gr: Optional[Gr]
        hr: Optional[Hr]
        hu: Optional[Hu]
        id: Optional[Id]
        ie: Optional[Ie]
        # TODO: Cannot include a type definition for is as it is a python reserved word
        it: Optional[It]
        jp: Optional[Jp]
        kr: Optional[Kr]
        lt: Optional[Lt]
        lu: Optional[Lu]
        lv: Optional[Lv]
        mt: Optional[Mt]
        mx: Optional[Mx]
        my: Optional[My]
        nl: Optional[Nl]
        no: Optional[No]
        nz: Optional[Nz]
        pl: Optional[Pl]
        pt: Optional[Pt]
        ro: Optional[Ro]
        sa: Optional[Sa]
        se: Optional[Se]
        sg: Optional[Sg]
        si: Optional[Si]
        sk: Optional[Sk]
        th: Optional[Th]
        tr: Optional[Tr]
        us: Optional[Us]
        vn: Optional[Vn]
        za: Optional[Za]
        _inner_class_types = {
            "ae": Ae,
            "at": At,
            "au": Au,
            "be": Be,
            "bg": Bg,
            "ca": Ca,
            "ch": Ch,
            "cl": Cl,
            "co": Co,
            "cy": Cy,
            "cz": Cz,
            "de": De,
            "dk": Dk,
            "ee": Ee,
            "es": Es,
            "fi": Fi,
            "fr": Fr,
            "gb": Gb,
            "gr": Gr,
            "hr": Hr,
            "hu": Hu,
            "id": Id,
            "ie": Ie,
            "is": Is,
            "it": It,
            "jp": Jp,
            "kr": Kr,
            "lt": Lt,
            "lu": Lu,
            "lv": Lv,
            "mt": Mt,
            "mx": Mx,
            "my": My,
            "nl": Nl,
            "no": No,
            "nz": Nz,
            "pl": Pl,
            "pt": Pt,
            "ro": Ro,
            "sa": Sa,
            "se": Se,
            "sg": Sg,
            "si": Si,
            "sk": Sk,
            "th": Th,
            "tr": Tr,
            "us": Us,
            "vn": Vn,
            "za": Za,
        }

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active_from: Union[int, Literal["now"]]
            country: str
            country_options: "Registration.CreateParamsCountryOptions"
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]

        class CreateParamsCountryOptions(TypedDict):
            ae: NotRequired["Registration.CreateParamsCountryOptionsAe|None"]
            at: NotRequired["Registration.CreateParamsCountryOptionsAt|None"]
            au: NotRequired["Registration.CreateParamsCountryOptionsAu|None"]
            be: NotRequired["Registration.CreateParamsCountryOptionsBe|None"]
            bg: NotRequired["Registration.CreateParamsCountryOptionsBg|None"]
            ca: NotRequired["Registration.CreateParamsCountryOptionsCa|None"]
            ch: NotRequired["Registration.CreateParamsCountryOptionsCh|None"]
            cl: NotRequired["Registration.CreateParamsCountryOptionsCl|None"]
            co: NotRequired["Registration.CreateParamsCountryOptionsCo|None"]
            cy: NotRequired["Registration.CreateParamsCountryOptionsCy|None"]
            cz: NotRequired["Registration.CreateParamsCountryOptionsCz|None"]
            de: NotRequired["Registration.CreateParamsCountryOptionsDe|None"]
            dk: NotRequired["Registration.CreateParamsCountryOptionsDk|None"]
            ee: NotRequired["Registration.CreateParamsCountryOptionsEe|None"]
            es: NotRequired["Registration.CreateParamsCountryOptionsEs|None"]
            fi: NotRequired["Registration.CreateParamsCountryOptionsFi|None"]
            fr: NotRequired["Registration.CreateParamsCountryOptionsFr|None"]
            gb: NotRequired["Registration.CreateParamsCountryOptionsGb|None"]
            gr: NotRequired["Registration.CreateParamsCountryOptionsGr|None"]
            hr: NotRequired["Registration.CreateParamsCountryOptionsHr|None"]
            hu: NotRequired["Registration.CreateParamsCountryOptionsHu|None"]
            id: NotRequired["Registration.CreateParamsCountryOptionsId|None"]
            ie: NotRequired["Registration.CreateParamsCountryOptionsIe|None"]
            # TODO: Cannot include a type definition for is as it is a python reserved word
            it: NotRequired["Registration.CreateParamsCountryOptionsIt|None"]
            jp: NotRequired["Registration.CreateParamsCountryOptionsJp|None"]
            kr: NotRequired["Registration.CreateParamsCountryOptionsKr|None"]
            lt: NotRequired["Registration.CreateParamsCountryOptionsLt|None"]
            lu: NotRequired["Registration.CreateParamsCountryOptionsLu|None"]
            lv: NotRequired["Registration.CreateParamsCountryOptionsLv|None"]
            mt: NotRequired["Registration.CreateParamsCountryOptionsMt|None"]
            mx: NotRequired["Registration.CreateParamsCountryOptionsMx|None"]
            my: NotRequired["Registration.CreateParamsCountryOptionsMy|None"]
            nl: NotRequired["Registration.CreateParamsCountryOptionsNl|None"]
            no: NotRequired["Registration.CreateParamsCountryOptionsNo|None"]
            nz: NotRequired["Registration.CreateParamsCountryOptionsNz|None"]
            pl: NotRequired["Registration.CreateParamsCountryOptionsPl|None"]
            pt: NotRequired["Registration.CreateParamsCountryOptionsPt|None"]
            ro: NotRequired["Registration.CreateParamsCountryOptionsRo|None"]
            sa: NotRequired["Registration.CreateParamsCountryOptionsSa|None"]
            se: NotRequired["Registration.CreateParamsCountryOptionsSe|None"]
            sg: NotRequired["Registration.CreateParamsCountryOptionsSg|None"]
            si: NotRequired["Registration.CreateParamsCountryOptionsSi|None"]
            sk: NotRequired["Registration.CreateParamsCountryOptionsSk|None"]
            th: NotRequired["Registration.CreateParamsCountryOptionsTh|None"]
            tr: NotRequired["Registration.CreateParamsCountryOptionsTr|None"]
            us: NotRequired["Registration.CreateParamsCountryOptionsUs|None"]
            vn: NotRequired["Registration.CreateParamsCountryOptionsVn|None"]
            za: NotRequired["Registration.CreateParamsCountryOptionsZa|None"]

        class CreateParamsCountryOptionsZa(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsVn(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsUs(TypedDict):
            local_amusement_tax: NotRequired[
                "Registration.CreateParamsCountryOptionsUsLocalAmusementTax|None"
            ]
            local_lease_tax: NotRequired[
                "Registration.CreateParamsCountryOptionsUsLocalLeaseTax|None"
            ]
            state: str
            type: Literal[
                "local_amusement_tax",
                "local_lease_tax",
                "state_communications_tax",
                "state_sales_tax",
            ]

        class CreateParamsCountryOptionsUsLocalLeaseTax(TypedDict):
            jurisdiction: str

        class CreateParamsCountryOptionsUsLocalAmusementTax(TypedDict):
            jurisdiction: str

        class CreateParamsCountryOptionsTr(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsTh(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsSk(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSkStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsSkStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsSi(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSiStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsSiStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsSg(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsSe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSeStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsSeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsSa(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsRo(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsRoStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsRoStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsPt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsPtStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsPtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsPl(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsPlStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsPlStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsNz(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsNo(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsNl(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsNlStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsNlStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsMy(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsMx(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsMt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsMtStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsMtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsLv(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLvStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsLvStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsLu(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLuStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsLuStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsLt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLtStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsLtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsKr(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsJp(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsIt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsItStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsItStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsIs(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsIe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsIeStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsIeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsId(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsHu(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsHuStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsHuStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsHr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsHrStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsHrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsGr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsGrStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsGrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsGb(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsFr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsFrStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsFrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsFi(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsFiStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsFiStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsEs(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsEsStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsEsStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsEe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsEeStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsEeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsDk(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsDkStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsDkStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsDe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsDeStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsDeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsCz(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCzStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsCzStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsCy(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCyStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsCyStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsCo(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsCl(TypedDict):
            type: Literal["simplified"]

        class CreateParamsCountryOptionsCh(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsCa(TypedDict):
            province_standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCaProvinceStandard|None"
            ]
            type: Literal["province_standard", "simplified", "standard"]

        class CreateParamsCountryOptionsCaProvinceStandard(TypedDict):
            province: str

        class CreateParamsCountryOptionsBg(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsBgStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsBgStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsBe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsBeStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsBeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsAu(TypedDict):
            type: Literal["standard"]

        class CreateParamsCountryOptionsAt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsAtStandard|None"
            ]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]

        class CreateParamsCountryOptionsAtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]

        class CreateParamsCountryOptionsAe(TypedDict):
            type: Literal["standard"]

        class ListParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            status: NotRequired[
                "Literal['active', 'all', 'expired', 'scheduled']|None"
            ]

        class ModifyParams(RequestOptions):
            active_from: NotRequired["int|Literal['now']|None"]
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["Literal['']|int|Literal['now']|None"]

    active_from: int
    country: str
    country_options: CountryOptions
    created: int
    expires_at: Optional[int]
    id: str
    livemode: bool
    object: Literal["tax.registration"]
    status: Literal["active", "expired", "scheduled"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Registration.CreateParams"]
    ) -> "Registration":
        return cast(
            "Registration",
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
        **params: Unpack["Registration.ListParams"]
    ) -> ListObject["Registration"]:
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
        cls, id, **params: Unpack["Registration.ModifyParams"]
    ) -> "Registration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Registration",
            cls._static_request("post", url, params=params),
        )

    _inner_class_types = {"country_options": CountryOptions}
