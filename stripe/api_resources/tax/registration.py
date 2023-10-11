# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional, cast
from typing_extensions import Literal
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
        **params: Any
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "Registration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Registration",
            cls._static_request("post", url, params=params),
        )

    _inner_class_types = {"country_options": CountryOptions}
