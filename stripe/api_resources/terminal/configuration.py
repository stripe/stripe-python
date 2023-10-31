# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
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
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.file import File


class Configuration(
    CreateableAPIResource["Configuration"],
    DeletableAPIResource["Configuration"],
    ListableAPIResource["Configuration"],
    UpdateableAPIResource["Configuration"],
):
    """
    A Configurations object represents how features should be configured for terminal readers.
    """

    OBJECT_NAME: ClassVar[
        Literal["terminal.configuration"]
    ] = "terminal.configuration"

    class BbposWiseposE(StripeObject):
        splashscreen: Optional[ExpandableField["File"]]
        """
        A File ID representing an image you would like displayed on the reader.
        """

    class Offline(StripeObject):
        enabled: Optional[bool]
        """
        Determines whether to allow transactions to be collected while reader is offline. Defaults to false.
        """

    class Tipping(StripeObject):
        class Aud(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Cad(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Chf(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Czk(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Dkk(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Eur(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Gbp(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Hkd(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Myr(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Nok(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Nzd(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Sek(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Sgd(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class Usd(StripeObject):
            fixed_amounts: Optional[List[int]]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: Optional[List[int]]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: Optional[int]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        aud: Optional[Aud]
        cad: Optional[Cad]
        chf: Optional[Chf]
        czk: Optional[Czk]
        dkk: Optional[Dkk]
        eur: Optional[Eur]
        gbp: Optional[Gbp]
        hkd: Optional[Hkd]
        myr: Optional[Myr]
        nok: Optional[Nok]
        nzd: Optional[Nzd]
        sek: Optional[Sek]
        sgd: Optional[Sgd]
        usd: Optional[Usd]
        _inner_class_types = {
            "aud": Aud,
            "cad": Cad,
            "chf": Chf,
            "czk": Czk,
            "dkk": Dkk,
            "eur": Eur,
            "gbp": Gbp,
            "hkd": Hkd,
            "myr": Myr,
            "nok": Nok,
            "nzd": Nzd,
            "sek": Sek,
            "sgd": Sgd,
            "usd": Usd,
        }

    class VerifoneP400(StripeObject):
        splashscreen: Optional[ExpandableField["File"]]
        """
        A File ID representing an image you would like displayed on the reader.
        """

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            bbpos_wisepos_e: NotRequired[
                "Configuration.CreateParamsBbposWiseposE|None"
            ]
            """
            An object containing device type specific settings for BBPOS WisePOS E readers
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            offline: NotRequired[
                "Literal['']|Configuration.CreateParamsOffline|None"
            ]
            """
            Configurations for collecting transactions offline.
            """
            tipping: NotRequired[
                "Literal['']|Configuration.CreateParamsTipping|None"
            ]
            """
            Tipping configurations for readers supporting on-reader tips
            """
            verifone_p400: NotRequired[
                "Configuration.CreateParamsVerifoneP400|None"
            ]
            """
            An object containing device type specific settings for Verifone P400 readers
            """

        class CreateParamsVerifoneP400(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]
            """
            A File ID representing an image you would like displayed on the reader.
            """

        class CreateParamsTipping(TypedDict):
            aud: NotRequired["Configuration.CreateParamsTippingAud|None"]
            """
            Tipping configuration for AUD
            """
            cad: NotRequired["Configuration.CreateParamsTippingCad|None"]
            """
            Tipping configuration for CAD
            """
            chf: NotRequired["Configuration.CreateParamsTippingChf|None"]
            """
            Tipping configuration for CHF
            """
            czk: NotRequired["Configuration.CreateParamsTippingCzk|None"]
            """
            Tipping configuration for CZK
            """
            dkk: NotRequired["Configuration.CreateParamsTippingDkk|None"]
            """
            Tipping configuration for DKK
            """
            eur: NotRequired["Configuration.CreateParamsTippingEur|None"]
            """
            Tipping configuration for EUR
            """
            gbp: NotRequired["Configuration.CreateParamsTippingGbp|None"]
            """
            Tipping configuration for GBP
            """
            hkd: NotRequired["Configuration.CreateParamsTippingHkd|None"]
            """
            Tipping configuration for HKD
            """
            myr: NotRequired["Configuration.CreateParamsTippingMyr|None"]
            """
            Tipping configuration for MYR
            """
            nok: NotRequired["Configuration.CreateParamsTippingNok|None"]
            """
            Tipping configuration for NOK
            """
            nzd: NotRequired["Configuration.CreateParamsTippingNzd|None"]
            """
            Tipping configuration for NZD
            """
            sek: NotRequired["Configuration.CreateParamsTippingSek|None"]
            """
            Tipping configuration for SEK
            """
            sgd: NotRequired["Configuration.CreateParamsTippingSgd|None"]
            """
            Tipping configuration for SGD
            """
            usd: NotRequired["Configuration.CreateParamsTippingUsd|None"]
            """
            Tipping configuration for USD
            """

        class CreateParamsTippingUsd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingSgd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingSek(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingNzd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingNok(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingMyr(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingHkd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingGbp(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingEur(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingDkk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingCzk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingChf(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingCad(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsTippingAud(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class CreateParamsOffline(TypedDict):
            enabled: bool
            """
            Determines whether to allow transactions to be collected while reader is offline. Defaults to false.
            """

        class CreateParamsBbposWiseposE(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]
            """
            A File ID representing an image you would like displayed on the reader.
            """

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            is_account_default: NotRequired["bool|None"]
            """
            if present, only return the account default or non-default configurations.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ModifyParams(RequestOptions):
            bbpos_wisepos_e: NotRequired[
                "Literal['']|Configuration.ModifyParamsBbposWiseposE|None"
            ]
            """
            An object containing device type specific settings for BBPOS WisePOS E readers
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            offline: NotRequired[
                "Literal['']|Configuration.ModifyParamsOffline|None"
            ]
            """
            Configurations for collecting transactions offline.
            """
            tipping: NotRequired[
                "Literal['']|Configuration.ModifyParamsTipping|None"
            ]
            """
            Tipping configurations for readers supporting on-reader tips
            """
            verifone_p400: NotRequired[
                "Literal['']|Configuration.ModifyParamsVerifoneP400|None"
            ]
            """
            An object containing device type specific settings for Verifone P400 readers
            """

        class ModifyParamsVerifoneP400(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]
            """
            A File ID representing an image you would like displayed on the reader.
            """

        class ModifyParamsTipping(TypedDict):
            aud: NotRequired["Configuration.ModifyParamsTippingAud|None"]
            """
            Tipping configuration for AUD
            """
            cad: NotRequired["Configuration.ModifyParamsTippingCad|None"]
            """
            Tipping configuration for CAD
            """
            chf: NotRequired["Configuration.ModifyParamsTippingChf|None"]
            """
            Tipping configuration for CHF
            """
            czk: NotRequired["Configuration.ModifyParamsTippingCzk|None"]
            """
            Tipping configuration for CZK
            """
            dkk: NotRequired["Configuration.ModifyParamsTippingDkk|None"]
            """
            Tipping configuration for DKK
            """
            eur: NotRequired["Configuration.ModifyParamsTippingEur|None"]
            """
            Tipping configuration for EUR
            """
            gbp: NotRequired["Configuration.ModifyParamsTippingGbp|None"]
            """
            Tipping configuration for GBP
            """
            hkd: NotRequired["Configuration.ModifyParamsTippingHkd|None"]
            """
            Tipping configuration for HKD
            """
            myr: NotRequired["Configuration.ModifyParamsTippingMyr|None"]
            """
            Tipping configuration for MYR
            """
            nok: NotRequired["Configuration.ModifyParamsTippingNok|None"]
            """
            Tipping configuration for NOK
            """
            nzd: NotRequired["Configuration.ModifyParamsTippingNzd|None"]
            """
            Tipping configuration for NZD
            """
            sek: NotRequired["Configuration.ModifyParamsTippingSek|None"]
            """
            Tipping configuration for SEK
            """
            sgd: NotRequired["Configuration.ModifyParamsTippingSgd|None"]
            """
            Tipping configuration for SGD
            """
            usd: NotRequired["Configuration.ModifyParamsTippingUsd|None"]
            """
            Tipping configuration for USD
            """

        class ModifyParamsTippingUsd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingSgd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingSek(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingNzd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingNok(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingMyr(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingHkd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingGbp(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingEur(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingDkk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingCzk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingChf(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingCad(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsTippingAud(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            """
            Fixed amounts displayed when collecting a tip
            """
            percentages: NotRequired["List[int]|None"]
            """
            Percentages displayed when collecting a tip
            """
            smart_tip_threshold: NotRequired["int|None"]
            """
            Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
            """

        class ModifyParamsOffline(TypedDict):
            enabled: bool
            """
            Determines whether to allow transactions to be collected while reader is offline. Defaults to false.
            """

        class ModifyParamsBbposWiseposE(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]
            """
            A File ID representing an image you would like displayed on the reader.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    bbpos_wisepos_e: Optional[BbposWiseposE]
    id: str
    """
    Unique identifier for the object.
    """
    is_account_default: Optional[bool]
    """
    Whether this Configuration is the default for your account
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["terminal.configuration"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    offline: Optional[Offline]
    tipping: Optional[Tipping]
    verifone_p400: Optional[VerifoneP400]
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Configuration.CreateParams"]
    ) -> "Configuration":
        """
        Creates a new Configuration object.
        """
        return cast(
            "Configuration",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        """
        Deletes a Configuration object.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Configuration",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        """
        Deletes a Configuration object.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        """
        Deletes a Configuration object.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        """
        Deletes a Configuration object.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Configuration.ListParams"]
    ) -> ListObject["Configuration"]:
        """
        Returns a list of Configuration objects.
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
        cls, id: str, **params: Unpack["Configuration.ModifyParams"]
    ) -> "Configuration":
        """
        Updates a new Configuration object.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Configuration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Configuration.RetrieveParams"]
    ) -> "Configuration":
        """
        Retrieves a Configuration object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "bbpos_wisepos_e": BbposWiseposE,
        "offline": Offline,
        "tipping": Tipping,
        "verifone_p400": VerifoneP400,
    }
