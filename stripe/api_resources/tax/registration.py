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
from typing import ClassVar, List, Optional, Union, cast
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

    OBJECT_NAME: ClassVar[Literal["tax.registration"]] = "tax.registration"

    class CountryOptions(StripeObject):
        class Ae(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class At(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Au(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Be(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Bg(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Ca(StripeObject):
            class ProvinceStandard(StripeObject):
                province: str
                """
                Two-letter CA province code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
                """

            province_standard: Optional[ProvinceStandard]
            type: Literal["province_standard", "simplified", "standard"]
            """
            Type of registration in Canada.
            """
            _inner_class_types = {"province_standard": ProvinceStandard}

        class Ch(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Cl(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Co(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Cy(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Cz(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class De(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Dk(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Ee(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Es(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Fi(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Fr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Gb(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Gr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Hr(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Hu(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Id(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Ie(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Is(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class It(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Jp(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Kr(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Lt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Lu(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Lv(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Mt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Mx(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class My(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Nl(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class No(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Nz(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Pl(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Pt(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Ro(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Sa(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Se(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Sg(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

        class Si(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Sk(StripeObject):
            class Standard(StripeObject):
                place_of_supply_scheme: Literal["small_seller", "standard"]
                """
                Place of supply scheme used in an EU standard registration.
                """

            standard: Optional[Standard]
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration in an EU country.
            """
            _inner_class_types = {"standard": Standard}

        class Th(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Tr(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Us(StripeObject):
            class LocalAmusementTax(StripeObject):
                jurisdiction: str
                """
                A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.
                """

            class LocalLeaseTax(StripeObject):
                jurisdiction: str
                """
                A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.
                """

            local_amusement_tax: Optional[LocalAmusementTax]
            local_lease_tax: Optional[LocalLeaseTax]
            state: str
            """
            Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
            """
            type: Literal[
                "local_amusement_tax",
                "local_lease_tax",
                "state_communications_tax",
                "state_sales_tax",
            ]
            """
            Type of registration in the US.
            """
            _inner_class_types = {
                "local_amusement_tax": LocalAmusementTax,
                "local_lease_tax": LocalLeaseTax,
            }

        class Vn(StripeObject):
            type: Literal["simplified"]
            """
            Type of registration in `country`.
            """

        class Za(StripeObject):
            type: Literal["standard"]
            """
            Type of registration in `country`.
            """

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
        is_: Optional[Is]
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
        _field_remappings = {"is_": "is"}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            active_from: Union[Literal["now"], int]
            """
            Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
            """
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            country_options: "Registration.CreateParamsCountryOptions"
            """
            Specific options for a registration in the specified `country`.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            expires_at: NotRequired["int|None"]
            """
            If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.
            """

        class CreateParamsCountryOptions(TypedDict):
            ae: NotRequired["Registration.CreateParamsCountryOptionsAe|None"]
            """
            Options for the registration in AE.
            """
            at: NotRequired["Registration.CreateParamsCountryOptionsAt|None"]
            """
            Options for the registration in AT.
            """
            au: NotRequired["Registration.CreateParamsCountryOptionsAu|None"]
            """
            Options for the registration in AU.
            """
            be: NotRequired["Registration.CreateParamsCountryOptionsBe|None"]
            """
            Options for the registration in BE.
            """
            bg: NotRequired["Registration.CreateParamsCountryOptionsBg|None"]
            """
            Options for the registration in BG.
            """
            ca: NotRequired["Registration.CreateParamsCountryOptionsCa|None"]
            """
            Options for the registration in CA.
            """
            ch: NotRequired["Registration.CreateParamsCountryOptionsCh|None"]
            """
            Options for the registration in CH.
            """
            cl: NotRequired["Registration.CreateParamsCountryOptionsCl|None"]
            """
            Options for the registration in CL.
            """
            co: NotRequired["Registration.CreateParamsCountryOptionsCo|None"]
            """
            Options for the registration in CO.
            """
            cy: NotRequired["Registration.CreateParamsCountryOptionsCy|None"]
            """
            Options for the registration in CY.
            """
            cz: NotRequired["Registration.CreateParamsCountryOptionsCz|None"]
            """
            Options for the registration in CZ.
            """
            de: NotRequired["Registration.CreateParamsCountryOptionsDe|None"]
            """
            Options for the registration in DE.
            """
            dk: NotRequired["Registration.CreateParamsCountryOptionsDk|None"]
            """
            Options for the registration in DK.
            """
            ee: NotRequired["Registration.CreateParamsCountryOptionsEe|None"]
            """
            Options for the registration in EE.
            """
            es: NotRequired["Registration.CreateParamsCountryOptionsEs|None"]
            """
            Options for the registration in ES.
            """
            fi: NotRequired["Registration.CreateParamsCountryOptionsFi|None"]
            """
            Options for the registration in FI.
            """
            fr: NotRequired["Registration.CreateParamsCountryOptionsFr|None"]
            """
            Options for the registration in FR.
            """
            gb: NotRequired["Registration.CreateParamsCountryOptionsGb|None"]
            """
            Options for the registration in GB.
            """
            gr: NotRequired["Registration.CreateParamsCountryOptionsGr|None"]
            """
            Options for the registration in GR.
            """
            hr: NotRequired["Registration.CreateParamsCountryOptionsHr|None"]
            """
            Options for the registration in HR.
            """
            hu: NotRequired["Registration.CreateParamsCountryOptionsHu|None"]
            """
            Options for the registration in HU.
            """
            id: NotRequired["Registration.CreateParamsCountryOptionsId|None"]
            """
            Options for the registration in ID.
            """
            ie: NotRequired["Registration.CreateParamsCountryOptionsIe|None"]
            """
            Options for the registration in IE.
            """
            it: NotRequired["Registration.CreateParamsCountryOptionsIt|None"]
            """
            Options for the registration in IT.
            """
            jp: NotRequired["Registration.CreateParamsCountryOptionsJp|None"]
            """
            Options for the registration in JP.
            """
            kr: NotRequired["Registration.CreateParamsCountryOptionsKr|None"]
            """
            Options for the registration in KR.
            """
            lt: NotRequired["Registration.CreateParamsCountryOptionsLt|None"]
            """
            Options for the registration in LT.
            """
            lu: NotRequired["Registration.CreateParamsCountryOptionsLu|None"]
            """
            Options for the registration in LU.
            """
            lv: NotRequired["Registration.CreateParamsCountryOptionsLv|None"]
            """
            Options for the registration in LV.
            """
            mt: NotRequired["Registration.CreateParamsCountryOptionsMt|None"]
            """
            Options for the registration in MT.
            """
            mx: NotRequired["Registration.CreateParamsCountryOptionsMx|None"]
            """
            Options for the registration in MX.
            """
            my: NotRequired["Registration.CreateParamsCountryOptionsMy|None"]
            """
            Options for the registration in MY.
            """
            nl: NotRequired["Registration.CreateParamsCountryOptionsNl|None"]
            """
            Options for the registration in NL.
            """
            no: NotRequired["Registration.CreateParamsCountryOptionsNo|None"]
            """
            Options for the registration in NO.
            """
            nz: NotRequired["Registration.CreateParamsCountryOptionsNz|None"]
            """
            Options for the registration in NZ.
            """
            pl: NotRequired["Registration.CreateParamsCountryOptionsPl|None"]
            """
            Options for the registration in PL.
            """
            pt: NotRequired["Registration.CreateParamsCountryOptionsPt|None"]
            """
            Options for the registration in PT.
            """
            ro: NotRequired["Registration.CreateParamsCountryOptionsRo|None"]
            """
            Options for the registration in RO.
            """
            sa: NotRequired["Registration.CreateParamsCountryOptionsSa|None"]
            """
            Options for the registration in SA.
            """
            se: NotRequired["Registration.CreateParamsCountryOptionsSe|None"]
            """
            Options for the registration in SE.
            """
            sg: NotRequired["Registration.CreateParamsCountryOptionsSg|None"]
            """
            Options for the registration in SG.
            """
            si: NotRequired["Registration.CreateParamsCountryOptionsSi|None"]
            """
            Options for the registration in SI.
            """
            sk: NotRequired["Registration.CreateParamsCountryOptionsSk|None"]
            """
            Options for the registration in SK.
            """
            th: NotRequired["Registration.CreateParamsCountryOptionsTh|None"]
            """
            Options for the registration in TH.
            """
            tr: NotRequired["Registration.CreateParamsCountryOptionsTr|None"]
            """
            Options for the registration in TR.
            """
            us: NotRequired["Registration.CreateParamsCountryOptionsUs|None"]
            """
            Options for the registration in US.
            """
            vn: NotRequired["Registration.CreateParamsCountryOptionsVn|None"]
            """
            Options for the registration in VN.
            """
            za: NotRequired["Registration.CreateParamsCountryOptionsZa|None"]
            """
            Options for the registration in ZA.
            """

        class CreateParamsCountryOptionsZa(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsVn(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsUs(TypedDict):
            local_amusement_tax: NotRequired[
                "Registration.CreateParamsCountryOptionsUsLocalAmusementTax|None"
            ]
            """
            Options for the local amusement tax registration.
            """
            local_lease_tax: NotRequired[
                "Registration.CreateParamsCountryOptionsUsLocalLeaseTax|None"
            ]
            """
            Options for the local lease tax registration.
            """
            state: str
            """
            Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
            """
            type: Literal[
                "local_amusement_tax",
                "local_lease_tax",
                "state_communications_tax",
                "state_sales_tax",
            ]
            """
            Type of registration to be created in the US.
            """

        class CreateParamsCountryOptionsUsLocalLeaseTax(TypedDict):
            jurisdiction: str
            """
            A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago).
            """

        class CreateParamsCountryOptionsUsLocalAmusementTax(TypedDict):
            jurisdiction: str
            """
            A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction. Supported FIPS codes are: `14000` (Chicago), `06613` (Bloomington), `21696` (East Dundee), `24582` (Evanston), and `68081` (Schiller Park).
            """

        class CreateParamsCountryOptionsTr(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsTh(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsSk(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSkStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsSkStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsSi(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSiStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsSiStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsSg(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsSe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsSeStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsSeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsSa(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsRo(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsRoStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsRoStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsPt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsPtStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsPtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsPl(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsPlStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsPlStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsNz(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsNo(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsNl(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsNlStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsNlStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsMy(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsMx(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsMt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsMtStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsMtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsLv(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLvStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsLvStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsLu(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLuStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsLuStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsLt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsLtStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsLtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsKr(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsJp(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsIt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsItStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsItStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsIs(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsIe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsIeStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsIeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsId(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsHu(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsHuStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsHuStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsHr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsHrStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsHrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsGr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsGrStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsGrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsGb(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsFr(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsFrStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsFrStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsFi(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsFiStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsFiStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsEs(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsEsStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsEsStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsEe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsEeStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsEeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsDk(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsDkStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsDkStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsDe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsDeStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsDeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsCz(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCzStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsCzStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsCy(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCyStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsCyStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsCo(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsCl(TypedDict):
            type: Literal["simplified"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsCh(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsCa(TypedDict):
            province_standard: NotRequired[
                "Registration.CreateParamsCountryOptionsCaProvinceStandard|None"
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

        class CreateParamsCountryOptionsBg(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsBgStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsBgStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsBe(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsBeStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsBeStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsAu(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class CreateParamsCountryOptionsAt(TypedDict):
            standard: NotRequired[
                "Registration.CreateParamsCountryOptionsAtStandard|None"
            ]
            """
            Options for the standard registration.
            """
            type: Literal["ioss", "oss_non_union", "oss_union", "standard"]
            """
            Type of registration to be created in an EU country.
            """

        class CreateParamsCountryOptionsAtStandard(TypedDict):
            place_of_supply_scheme: Literal["small_seller", "standard"]
            """
            Place of supply scheme used in an EU standard registration.
            """

        class CreateParamsCountryOptionsAe(TypedDict):
            type: Literal["standard"]
            """
            Type of registration to be created in `country`.
            """

        class ListParams(RequestOptions):
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
            status: NotRequired[
                "Literal['active', 'all', 'expired', 'scheduled']|None"
            ]
            """
            The status of the Tax Registration.
            """

        class ModifyParams(RequestOptions):
            active_from: NotRequired["Literal['now']|int|None"]
            """
            Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            expires_at: NotRequired["Literal['']|Literal['now']|int|None"]
            """
            If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
            """

    active_from: int
    """
    Time at which the registration becomes active. Measured in seconds since the Unix epoch.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    country_options: CountryOptions
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: Optional[int]
    """
    If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax.registration"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "expired", "scheduled"]
    """
    The status of the registration. This field is present for convenience and can be deduced from `active_from` and `expires_at`.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Registration.CreateParams"]
    ) -> "Registration":
        """
        Creates a new Tax Registration object.
        """
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
        """
        Returns a list of Tax Registration objects.
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
        cls, id: str, **params: Unpack["Registration.ModifyParams"]
    ) -> "Registration":
        """
        Updates an existing Tax Registration object.

        A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Registration",
            cls._static_request("post", url, params=params),
        )

    _inner_class_types = {"country_options": CountryOptions}
